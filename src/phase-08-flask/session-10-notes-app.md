## Session 10: Build a notes app together

*Phase 8 — Flask · Session 10 of 13*

### What we're learning today

You have all the pieces. Today they combine into a
**complete multi-user notes app.** Each user has
their own private notes — create, view, edit,
delete. Login required. Built as a class. By the
end you'll have **the most ambitious project of
the curriculum** — a full-stack Flask app you
could host and use for real.

This is the **integration moment.**

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

#### What we're building

- **Signup / login / logout** (from Session 9).
- **Notes table** with user ownership.
- **List your notes** (only yours).
- **Create a note** (title + content).
- **View a single note.**
- **Edit a note.**
- **Delete a note.**
- **Login required** for everything except
  signup/login.

The shape of countless real apps — Trello, Notion,
journals, blogs — all start here.

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
│   ├── note_form.html
│   └── note_view.html
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
`WHERE user_id = ?`.

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
created and auth working.* **This is the natural
stop point if class is cut short.**

---

### Part B: The notes routes

#### List notes

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
        <a href="{{ url_for('note_view', note_id=note.id) }}">
            <h3>{{ note.title }}</h3>
            <p>{{ note.content[:100] }}{% if note.content|length > 100 %}…{% endif %}</p>
            <small>{{ note.updated_at }}</small>
        </a>
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

`templates/note_form.html` (used for both create
and edit — pass `note=None` for create, the row
for edit):

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
`note`).

#### View a single note

```python
@app.route("/notes/<int:note_id>")
@login_required
def note_view(note_id):
    user = current_user()
    conn = get_db()
    note = conn.execute(
        "SELECT * FROM notes WHERE id = ? AND user_id = ?",
        (note_id, user["id"])
    ).fetchone()
    conn.close()
    
    if not note:
        abort(404)
    
    return render_template("note_view.html", note=note)
```

**The crucial query:** `WHERE id = ? AND user_id = ?`.
We check both the note ID AND that it belongs to
the current user. **Without the user_id check, any
logged-in user could view *any* note** — security
hole.

`templates/note_view.html`:

```html
{% extends "base.html" %}
{% block title %}{{ note.title }}{% endblock %}
{% block content %}
<article>
    <h1>{{ note.title }}</h1>
    <p>{{ note.content }}</p>
    <small>Created {{ note.created_at }} · Updated {{ note.updated_at }}</small>
</article>

<div class="actions">
    <a href="{{ url_for('note_edit', note_id=note.id) }}" class="btn">Edit</a>
    <form method="post" action="{{ url_for('note_delete', note_id=note.id) }}"
          onsubmit="return confirm('Delete this note?');"
          style="display: inline;">
        <button type="submit" class="btn btn-danger">Delete</button>
    </form>
    <a href="{{ url_for('notes_list') }}">Back to list</a>
</div>
{% endblock %}
```

The `onsubmit="return confirm(...)"` is JS from
Phase 7 — confirmation before destructive action.

#### Edit a note

```python
@app.route("/notes/<int:note_id>/edit", methods=["GET", "POST"])
@login_required
def note_edit(note_id):
    user = current_user()
    conn = get_db()
    note = conn.execute(
        "SELECT * FROM notes WHERE id = ? AND user_id = ?",
        (note_id, user["id"])
    ).fetchone()
    
    if not note:
        conn.close()
        abort(404)
    
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        
        if not title or not content:
            flash("Both fields required.", "error")
        else:
            conn.execute(
                """UPDATE notes
                   SET title = ?, content = ?, updated_at = CURRENT_TIMESTAMP
                   WHERE id = ? AND user_id = ?""",
                (title, content, note_id, user["id"])
            )
            conn.commit()
            conn.close()
            flash("Note updated.", "success")
            return redirect(url_for("note_view", note_id=note_id))
    
    conn.close()
    return render_template("note_form.html", note=note)
```

Same pattern as Session 8's edit — GET shows
form, POST saves changes. **Same
`AND user_id = ?` check** to prevent editing
others' notes.

The `updated_at = CURRENT_TIMESTAMP` updates the
last-modified time.

#### Delete a note

```python
@app.route("/notes/<int:note_id>/delete", methods=["POST"])
@login_required
def note_delete(note_id):
    user = current_user()
    conn = get_db()
    conn.execute(
        "DELETE FROM notes WHERE id = ? AND user_id = ?",
        (note_id, user["id"])
    )
    conn.commit()
    conn.close()
    flash("Note deleted.", "success")
    return redirect(url_for("notes_list"))
```

POST only (Session 8 rule). Same user-check.

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
4. Click the note. **View page loads.**
5. Edit. Save. **Updated time changes.**
6. Delete. **Confirms, deletes, returns to list.**

**Logout. Sign up as a different user.** Log in.
Click "Your notes." **Empty** — your notes are
*yours*. Each user has their own.

**You built a real multi-user app.** Auth +
database + per-user data + full CRUD.

**Checkpoint:** *Your notes app has signup, login,
create, list, view, edit, and delete — all
filtering by user.* **This is the natural stop
point if class is cut short.**

---

### Stretch and extension ideas

#### Search

Add `?q=word` to filter notes:

```python
search = request.args.get("q", "").strip()
if search:
    notes = conn.execute(
        """SELECT * FROM notes
           WHERE user_id = ? AND (title LIKE ? OR content LIKE ?)
           ORDER BY updated_at DESC""",
        (user["id"], f"%{search}%", f"%{search}%")
    ).fetchall()
else:
    notes = conn.execute(...).fetchall()
```

#### Tags

Add a `tags` table and a `note_tags` join table.
Real database design:

```sql
CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE note_tags (
    note_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (note_id, tag_id)
);
```

Query notes with their tags via JOIN.

#### Sharing (advanced)

A `shared_notes` table:

```sql
CREATE TABLE shared_notes (
    note_id INTEGER,
    shared_with_user_id INTEGER,
    PRIMARY KEY (note_id, shared_with_user_id)
);
```

User A shares a note with User B. User B sees it
in a "Shared with me" view. Real collaboration.

#### Public notes

A `is_public` column. Public notes are readable
without login. URL: `/public/<note_id>`. **No
user_id check** for public notes.

#### Pagination

`LIMIT 20 OFFSET ?` for big lists. Add page
controls.

#### Rich text

Replace plain `<textarea>` with a Markdown editor
(or a simple WYSIWYG). Save Markdown, render with
a Markdown library:

```python
import markdown
note["html"] = markdown.markdown(note["content"])
```

In template:

```html
<div class="content">{{ note.html|safe }}</div>
```

(The `|safe` is needed because `markdown.markdown`
already produces safe HTML — but only if the
input was Markdown, which is user-controlled.
Safer: sanitize with `bleach`.)

#### Export

A "Download all my notes" button. Generates a
text or JSON file with all the user's notes:

```python
from flask import send_file
import json
import io

@app.route("/notes/export")
@login_required
def export_notes():
    user = current_user()
    conn = get_db()
    notes = conn.execute(
        "SELECT * FROM notes WHERE user_id = ?", (user["id"],)
    ).fetchall()
    conn.close()
    
    data = [dict(note) for note in notes]
    json_str = json.dumps(data, indent=2)
    
    return send_file(
        io.BytesIO(json_str.encode()),
        as_attachment=True,
        download_name="notes.json",
        mimetype="application/json"
    )
```

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your notes app working.
  Create a note. View it.
- For multi-user pairs — sign up as different
  people, verify your notes don't show up in
  someone else's list.
- For the kids who tried search or tags — show
  off.
- Did the integration feel powerful? *All the
  pieces working together.*

Today you built **a real full-stack app:**

- HTML + CSS templates with extends/block
- Database schema with foreign keys
- Multi-table queries with user-filter
- Auth with hashed passwords + sessions
- Full CRUD via routes
- Forms with POST-Redirect-GET
- Flash messages for feedback
- Per-user data isolation

This is **the entire shape of every modern web
app.** Whatever you build next — bigger, fancier,
in different languages — the *patterns* are the
same.

Next week: **deployment.** Get your notes app on
a real public URL. Anyone can sign up.

### If you missed this session

Open Thonny.

1. Build the foundation from Part A — both
   tables, auth.

2. Build each notes route from Part B — list,
   create, view, edit, delete.

3. Build the templates.

4. Test the full flow.

About 90-120 minutes — this is the longest
session yet.

### Stretch and extension ideas

- **All the stretches above.**
- **Categories / folders** for notes.
- **Star / favorite** notes.
- **Most recent N** on home page.
- **Stats** — how many notes, words, etc.
- **Export individual note as text or PDF.**
- **Markdown rendering.**
- **Public notes** with shareable URLs.
- **API endpoint** that returns notes as JSON
  (Phase 7 fetch could call this).

### What's next

Next week: **deployment.** PythonAnywhere — free
Python hosting designed for educators and
students. Walk through signup, upload code,
configure, hit the public URL. Your notes app
becomes a *real internet thing*.
