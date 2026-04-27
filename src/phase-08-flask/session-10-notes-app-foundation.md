## Session 10: Build a notes app together — foundation

*Phase 8 — Flask · Session 10 of 14*

### What we're learning today

You have all the pieces. Today they start to
combine into a **multi-user notes app** — each
user has their own private notes. Built as a
class.

This session builds the **foundation:**
two-table database, auth from Session 9 wired
in, list notes, create notes. The crucial
**per-user data pattern** (`WHERE user_id = ?`)
gets its own dedicated time today.

Next session: view, edit, delete, and the
multi-user demo.

### You'll need to remember from last time

- **Auth flow** — signup, login, session,
  password hashing (Session 9).
- **Database CRUD** — get_db, parameterized
  queries (Session 8).
- **Templates with extends/block** (Session 4).
- **Forms with POST-Redirect-GET** (Session 5).
- **Flash messages** (Session 6).
- **`@login_required` decorator** (Session 9
  stretch).

---

### Part A: Set up the foundation

#### What we're building today

- **Signup / login / logout** (from Session 9).
- **Notes table** with user ownership.
- **List your notes** (only yours).
- **Create a note** (title + content).
- **Login required** for everything except
  signup/login.

The shape of countless real apps — Trello,
Notion, journals, blogs — all start here.
**View, edit, and delete come next session.**

#### Project structure

```
notes_app/
├── app.py
├── notes.db
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── signup.html
│   ├── login.html
│   ├── notes_list.html
│   └── note_form.html
└── static/
    └── style.css
```

#### Database schema

Two tables. The `users` table from Session 9, plus
a `notes` table with a foreign key:

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

The **`user_id`** column links each note to a
user. The `FOREIGN KEY` says "this column points
to the `id` column of the `users` table."

When listing a user's notes, we filter by
`WHERE user_id = ?`. **This filter is the most
important line of code in this whole app.** We'll
come back to it.

#### `app.py` — foundation

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3

app = Flask(__name__)
app.secret_key = "dev-secret"

def get_db():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    conn.commit()
    conn.close()

init_db()

def current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return user

@app.context_processor
def inject_user():
    return {"current_user": current_user()}

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user():
            flash("Please log in.", "error")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated
```

What's new:

- **`conn.executescript(...)`** — run multiple
  SQL statements at once. Used here to create
  both tables in one call.

#### Auth routes (from Session 9)

Add the same signup, login, logout routes as
Session 9. (Skipping repetition here — copy from
Session 9.)

**Checkpoint:** *Your foundation has both tables
created and auth working. You can sign up, log
in, and log out, but there are no notes routes
yet.* **This is the natural stop point if class
is cut short.**

---

### Part B: List and create notes

#### List notes — the per-user query

```python
@app.route("/notes")
@login_required
def notes_list():
    user = current_user()
    conn = get_db()
    notes = conn.execute(
        "SELECT * FROM notes WHERE user_id = ? ORDER BY updated_at DESC",
        (user["id"],)
    ).fetchall()
    conn.close()
    return render_template("notes_list.html", notes=notes)
```

Two crucial pieces:

- **`@login_required`** — must be logged in.
- **`WHERE user_id = ?`** — only *this user's*
  notes.

**Stop and read that filter again.** *This* query
is the entire pattern of per-user data. Same
`notes` table for every user — but the filter
narrows it to this user's rows. Without the
filter, *every* user would see *everyone's*
notes. That's a security catastrophe. The
`WHERE user_id = ?` is non-negotiable on every
notes query you write.

`templates/notes_list.html`:

```html
{% extends "base.html" %}
{% block title %}Your notes{% endblock %}
{% block content %}
<h1>Your notes</h1>
<a href="{{ url_for('note_create') }}" class="btn">+ New note</a>

{% if notes %}
<ul class="notes">
    {% for note in notes %}
    <li>
        <h3>{{ note.title }}</h3>
        <p>{{ note.content[:100] }}{% if note.content|length > 100 %}…{% endif %}</p>
        <small>{{ note.updated_at }}</small>
    </li>
    {% endfor %}
</ul>
{% else %}
<p>No notes yet. <a href="{{ url_for('note_create') }}">Create your first one</a>.</p>
{% endif %}
{% endblock %}
```

Note `note.content[:100]` — first 100 characters
as a preview. Jinja supports Python slicing.

(We're not linking to a "view" page yet — that's
next session. For now, the list shows previews.)

#### Create a note

```python
@app.route("/notes/new", methods=["GET", "POST"])
@login_required
def note_create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        
        if not title or not content:
            flash("Both title and content required.", "error")
        else:
            user = current_user()
            conn = get_db()
            conn.execute(
                "INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
                (user["id"], title, content)
            )
            conn.commit()
            conn.close()
            flash("Note created!", "success")
            return redirect(url_for("notes_list"))
    
    return render_template("note_form.html", note=None)
```

Look at the INSERT carefully:

```python
"INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
(user["id"], title, content)
```

We **hardcode** `user_id = current user's id`.
The user *cannot* set this to someone else's id
by tampering — it's not in the form. If `user_id`
came from a hidden form field, users could edit
their browser's HTML and assign notes to other
people. **Always set user_id from
`current_user()`, never from form data.** Real
apps have been compromised this way.

`templates/note_form.html` (the same template
will get reused next session for editing — pass
`note=None` for create, the row for edit):

```html
{% extends "base.html" %}
{% block title %}{% if note %}Edit{% else %}New{% endif %} note{% endblock %}
{% block content %}
<h1>{% if note %}Edit{% else %}New{% endif %} note</h1>

<form method="post">
    <label>Title:
        <input type="text" name="title"
               value="{{ note.title if note else '' }}" required>
    </label>
    <label>Content:
        <textarea name="content" rows="10" required>{{ note.content if note else '' }}</textarea>
    </label>
    <button type="submit">Save</button>
    <a href="{{ url_for('notes_list') }}">Cancel</a>
</form>
{% endblock %}
```

The `value="{{ note.title if note else '' }}"`
handles both new (no `note`) and edit (with
`note`) — Jinja short-circuits.

#### Update the home page

`templates/home.html`:

```html
{% extends "base.html" %}
{% block content %}
{% if current_user %}
    <h1>Welcome, {{ current_user.username }}!</h1>
    <a href="{{ url_for('notes_list') }}" class="btn">Your notes</a>
{% else %}
    <h1>Welcome!</h1>
    <p>A simple note-taking app. Sign up or log in to start.</p>
{% endif %}
{% endblock %}
```

#### Test it

1. Sign up. Log in.
2. Click "Your notes." Empty list.
3. Click "+ New note." Type a title and content.
   Save. **Note appears in the list.**
4. Create a few more.

**Now log out. Sign up as a different user.**
Log in. Click "Your notes." **Empty** — your
notes are *yours*. The first user's notes don't
appear here. **The `WHERE user_id = ?` filter is
working.**

You just built the core of every multi-user app
ever written. **That filter is the difference
between a journal app and a journal-app-shaped
security incident.**

**Checkpoint:** *Your notes app has signup,
login, list, and create — all filtering by
user.* **This is the natural stop point if
class is cut short.**

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your notes app working.
  Create a note. List it.
- For the kids who tested with two users — show
  off the per-user isolation.
- Did the per-user filter feel important? *It
  should.* Every multi-user app you ever build
  rests on it.

Today you built **the foundation** of a real
full-stack app:

- Two tables with a foreign key
- Auth wired in (from Session 9)
- The per-user data pattern (`WHERE user_id = ?`)
- List and create routes

Next week we add **view, edit, delete**, do the
multi-user security demo, and explore the
stretches (search, tags, public notes).

### If you missed this session

Open Thonny.

1. Build the foundation from Part A — both
   tables, auth (copy from Session 9).

2. Build the list and create routes from Part B.

3. Build the templates.

4. Test the full flow: signup, login, list,
   create. Try with two users.

About 60-90 minutes.

### Stretch and extension ideas

- **Sort options** — newest first vs alphabetical.
- **Empty-state styling** — make the "no notes
  yet" page friendlier.
- **Character counter** in the new-note form
  (Phase 7 JS).
- **Note count** in the page heading: "Your 5
  notes."
- **Read ahead** — peek at the spec for next
  session and try edit / delete on your own.

### What's next

Next week: **view, edit, delete, and the
multi-user security demo.** We finish the notes
app and try to break it (in the good way) to
prove the per-user filter holds.
