## Session 8: Database in Flask — CRUD operations

*Phase 8 — Flask · Session 8 of 13*

### What we're learning today

You know Flask. You know SQLite. Today they
combine. Routes read from the database, forms
write to it. By the end your guestbook from Session
5 will store messages in a real database — they
**survive server restarts.** You'll also learn the
**four CRUD operations** (Create, Read, Update,
Delete) tied to URL routes — the shape of every
real web app.

### You'll need to remember from last time

- **SQLite basics** — `connect`, `cursor`,
  `execute`, `commit`.
- **SQL** — CREATE, INSERT, SELECT, UPDATE, DELETE.
- **Parameterized queries** — `?` placeholders.
- **Flask** — routes, templates, forms,
  POST-Redirect-GET.

---

### Part A: Connecting Flask to SQLite

#### A helper function

Talking to the database from every route gets
repetitive. Let's make a helper:

```python
import sqlite3

def get_db():
    conn = sqlite3.connect("guestbook.db")
    conn.row_factory = sqlite3.Row    # rows behave like dicts
    return conn
```

Two things new:

- **`conn.row_factory = sqlite3.Row`** — instead
  of plain tuples, rows behave like dicts. So
  `row["name"]` works, not just `row[0]`. Way
  more readable.
- **The function** keeps connection setup in one
  place.

Now any route can call `get_db()` to get a working
connection.

#### Create the table on startup

Run the `CREATE TABLE` once when the app starts.
Add to `app.py`:

```python
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()    # runs when the app starts
```

The `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`
column auto-fills with the current time when a row
is inserted. Free metadata.

#### Refactor the guestbook

Take the Session 5 guestbook. Replace the in-memory
`messages = []` with database calls.

Full `app.py`:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "dev-secret"

def get_db():
    conn = sqlite3.connect("guestbook.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db()
    
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        
        if not name or not message:
            flash("Both fields required.", "error")
        else:
            conn.execute(
                "INSERT INTO messages (name, message) VALUES (?, ?)",
                (name, message)
            )
            conn.commit()
            flash("Message posted!", "success")
        
        conn.close()
        return redirect(url_for("home"))
    
    rows = conn.execute(
        "SELECT * FROM messages ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    
    return render_template("guestbook.html", messages=rows)

if __name__ == "__main__":
    app.run(debug=True)
```

Update `templates/guestbook.html`:

```html
{% extends "base.html" %}
{% block title %}Guestbook{% endblock %}
{% block content %}
<h1>Guestbook</h1>

<form method="post">
    <label>Your name: <input type="text" name="name" required></label>
    <label>Message: <textarea name="message" rows="3" required></textarea></label>
    <button type="submit">Post</button>
</form>

<h2>Messages</h2>
{% if messages %}
    {% for m in messages %}
    <article class="message">
        <header><strong>{{ m.name }}</strong> · <time>{{ m.created_at }}</time></header>
        <p>{{ m.message }}</p>
    </article>
    {% endfor %}
{% else %}
    <p>No messages yet.</p>
{% endif %}
{% endblock %}
```

Save. Run. Submit a few messages. **They appear,
in newest-first order, with timestamps.** Stop
the server. Start it again. **Messages still there.**

**The database is doing its job.**

#### What changed from Session 5

| Session 5 | Session 8 |
|-----------|-----------|
| `messages = []` (in-memory) | `messages` table in SQLite |
| `messages.append(...)` | `INSERT INTO messages` |
| `for m in messages:` | `SELECT * FROM messages` |
| Lost on restart | **Persists** |
| One server only | **Shared across processes** |

Same UX, infinitely better backend.

**Checkpoint:** *Your guestbook stores messages in
SQLite — they survive server restarts.* **This is
the natural stop point if class is cut short.**

---

### Part B: Full CRUD

The guestbook only does **C**reate (insert) and
**R**ead (select). Real apps also need **U**pdate
(edit) and **D**elete. That's CRUD.

#### Add a delete button

Update `templates/guestbook.html` — each message
gets a delete button:

```html
{% for m in messages %}
<article class="message">
    <header><strong>{{ m.name }}</strong> · <time>{{ m.created_at }}</time></header>
    <p>{{ m.message }}</p>
    <form method="post" action="{{ url_for('delete', message_id=m.id) }}" style="display: inline;">
        <button type="submit" class="delete-btn">Delete</button>
    </form>
</article>
{% endfor %}
```

Add the route in `app.py`:

```python
@app.route("/delete/<int:message_id>", methods=["POST"])
def delete(message_id):
    conn = get_db()
    conn.execute("DELETE FROM messages WHERE id = ?", (message_id,))
    conn.commit()
    conn.close()
    flash("Message deleted.", "success")
    return redirect(url_for("home"))
```

Save. Reload. Each message has a delete button.
Click → message gone, flash confirms.

What's new:

- **`<int:message_id>`** — URL parameter (Session
  2). The integer ID of the message to delete.
- **Form with action**, not just a link, because
  delete is a *change* (POST) not a *read* (GET).
- **Parameterized DELETE** — `?` for the ID.

#### Edit a message

Two routes:

- **GET `/edit/<id>`** — show the edit form.
- **POST `/edit/<id>`** — save the changes.

```python
@app.route("/edit/<int:message_id>", methods=["GET", "POST"])
def edit(message_id):
    conn = get_db()
    
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        
        if not name or not message:
            flash("Both fields required.", "error")
            conn.close()
            return redirect(url_for("edit", message_id=message_id))
        
        conn.execute(
            "UPDATE messages SET name = ?, message = ? WHERE id = ?",
            (name, message, message_id)
        )
        conn.commit()
        conn.close()
        flash("Message updated.", "success")
        return redirect(url_for("home"))
    
    row = conn.execute(
        "SELECT * FROM messages WHERE id = ?",
        (message_id,)
    ).fetchone()
    conn.close()
    
    if not row:
        flash("Message not found.", "error")
        return redirect(url_for("home"))
    
    return render_template("edit.html", message=row)
```

`templates/edit.html`:

```html
{% extends "base.html" %}
{% block title %}Edit message{% endblock %}
{% block content %}
<h1>Edit message</h1>

<form method="post">
    <label>Name: <input type="text" name="name" value="{{ message.name }}" required></label>
    <label>Message: <textarea name="message" rows="3" required>{{ message.message }}</textarea></label>
    <button type="submit">Save</button>
    <a href="{{ url_for('home') }}">Cancel</a>
</form>
{% endblock %}
```

Update the guestbook to add an edit link per
message:

```html
<a href="{{ url_for('edit', message_id=m.id) }}">Edit</a>
```

Save. Click "Edit" on any message → edit form
loaded with current values. Change. Submit.
**Message updated.**

You now have full CRUD: **C**reate, **R**ead,
**U**pdate, **D**elete. The shape of every CMS,
every blog, every social network.

#### Stretch — sort and filter

Add a search:

```python
search = request.args.get("q", "").strip()

if search:
    rows = conn.execute(
        "SELECT * FROM messages WHERE message LIKE ? ORDER BY created_at DESC",
        (f"%{search}%",)
    ).fetchall()
else:
    rows = conn.execute(
        "SELECT * FROM messages ORDER BY created_at DESC"
    ).fetchall()
```

Add a search box in the template:

```html
<form method="get" action="{{ url_for('home') }}">
    <input type="text" name="q" value="{{ request.args.get('q', '') }}" placeholder="Search">
    <button type="submit">Search</button>
</form>
```

The `LIKE` operator with `%` wildcards = substring
match. `%pizza%` matches anywhere "pizza" appears.

Visit `/?q=pizza` — only matching messages show.

#### Stretch — counts

```python
total = conn.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
```

Show "{{ total }} messages" in the template.

#### Stretch — pagination

For long lists:

```python
PAGE_SIZE = 10
page = int(request.args.get("page", 1))
offset = (page - 1) * PAGE_SIZE

rows = conn.execute(
    "SELECT * FROM messages ORDER BY created_at DESC LIMIT ? OFFSET ?",
    (PAGE_SIZE, offset)
).fetchall()
```

Add "Next page" / "Previous page" links.
`LIMIT N OFFSET M` = "give me N rows, skipping the
first M."

#### Extension — confirm dialog

Use Phase 7 JS for delete confirmation:

```html
<form ...
      onsubmit="return confirm('Are you sure?');">
```

`return confirm(...)` cancels the submit if user
clicks Cancel.

#### Extension — schema migrations

When you add a column to an existing table, you
need:

```sql
ALTER TABLE messages ADD COLUMN topic TEXT
```

Or for class: delete `guestbook.db` and let
`init_db()` recreate. (For real production: real
migration tools.)

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your persistent guestbook.
  Did messages survive a restart?
- For the kids who added edit/delete — full CRUD!
- For the kids who added search — useful?
- Did the database feel powerful compared to
  in-memory `messages = []`?

Today you learned:

- **Tie Flask routes to database operations.**
- **`get_db()` helper** for connection setup.
- **`row_factory = sqlite3.Row`** for dict-like
  rows.
- **`init_db()` on startup** to ensure schema.
- **`INSERT` in routes for creating data.**
- **`SELECT` in routes for reading.**
- **`UPDATE` for editing.**
- **`DELETE` for removing.**
- **The four CRUD operations** mapped to routes.
- **`<int:id>` URL params** for targeting specific
  records.
- **POST for changes**, GET for reads.

You can now build **real persistent web apps.**
The guestbook is the simplest version, but the
shape is universal.

Next week: **user accounts** — signup, login,
password hashing. Multiple users, each with their
own data. The web's most-used pattern.

### If you missed this session

Open Thonny.

1. Take the Session 5 guestbook.

2. Add `get_db()` and `init_db()`.

3. Replace `messages = []` with SQL operations.

4. Run, post messages, restart, verify they
   persist.

5. (Stretch) Add edit and delete routes.

About 60-90 minutes — this is a substantial
session.

### Stretch and extension ideas

- **Edit and delete** routes (above).
- **Search** with LIKE.
- **Counts** with COUNT(*).
- **Pagination** with LIMIT/OFFSET.
- **Sort options** — by name, by date, by length.
- **Confirm dialog** with JS.
- **Mark messages as "favorite"** — extra column,
  toggle button.
- **Different SQL dialects** — read about how
  PostgreSQL or MySQL differ. (Mostly compatible
  with SQLite.)

### What's next

Next week: **user accounts.** A `users` table
with hashed passwords. Signup, login, logout. The
session stores who's logged in. Each user has
their own data (next session — the notes app).
