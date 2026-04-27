## Session 11: Build a notes app together — polish

*Phase 8 — Flask · Session 11 of 14*

### What we're learning today

Last session we built the notes app foundation:
auth, schema, list, create. Today we **finish
the app** — view a note, edit it, delete it —
and then **try to break it** (in the good way)
to prove our per-user filter actually holds.

This session is the **integration moment.** By
the end you have a working full-stack
multi-user app. The shape of every modern web
app: Trello, Notion, journals, blogs.

### You'll need to remember from last time

- **Your notes app from Session 10** — auth,
  schema, list, create.
- **The `WHERE user_id = ?` filter.** Every
  notes query has it. We add it to three more
  routes today.
- **`abort()` from Flask** — return a 404 from
  inside a route.

---

### Part A: View, edit, and delete

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
We check both the note ID *and* that it belongs
to the current user. **Without the user_id
check, any logged-in user could view *any* note
by changing the number in the URL** — security
hole.

We'll demo this in Part B.

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
Phase 7 — confirmation before destructive
action.

Now **link the list to the view.** Open
`notes_list.html` and wrap each note's title in
an anchor:

```html
<li>
    <a href="{{ url_for('note_view', note_id=note.id) }}">
        <h3>{{ note.title }}</h3>
        <p>{{ note.content[:100] }}{% if note.content|length > 100 %}…{% endif %}</p>
        <small>{{ note.updated_at }}</small>
    </a>
</li>
```

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
the form pre-filled, POST saves changes. **Same
`AND user_id = ?` check** to prevent editing
others' notes — and notice it appears *twice*
in this route (once on the SELECT, once on the
UPDATE). Both matter.

`updated_at = CURRENT_TIMESTAMP` updates the
last-modified time. The template (`note_form.html`)
is the **same template** you wrote last week —
it already pre-fills when `note` is passed.

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

POST only (Session 8 rule — destructive actions
are POST, not GET). Same user-check.

#### Test it

1. Log in. Open the notes list.
2. **Click a note.** View page loads.
3. **Click Edit.** Form pre-fills. Change the
   title. Save. **Updated time changes.**
4. **Click Delete.** Confirmation appears.
   Confirm. **Returns to list, note is gone.**

**Checkpoint:** *Your notes app has list,
create, view, edit, and delete — all filtering
by user.* **This is the natural stop point if
class is cut short.**

---

### Part B: Multi-user demo + try to break it

#### The multi-user demo

This is the moment the app feels real. Try it
with the kid next to you:

1. **You sign up as User A. Your buddy as User
   B.** (Same app, two accounts — different
   browsers, or one browser plus an incognito
   window.)
2. **Each create some notes.**
3. **Log out as A. Log in as B.** Look at "Your
   notes" — only B's notes show. **A's notes
   don't appear.** Same for the reverse.

**Two users. Different data. Same app.** This
is the magic. Per-user state, real persistence,
real isolation.

#### Now try to break it

Real engineers test their security by trying to
get past it. Let's do that to your app:

1. **Log in as User B.**
2. **Create a note.** Click into it. Look at
   the URL — something like
   `http://127.0.0.1:5000/notes/3`. Note the
   number.
3. **Now visit a smaller number** — say,
   `/notes/1`. (User A's notes have ID 1 and
   2; you're guessing.)
4. **You get a 404 page.** Even though note 1
   *exists* in the database, the
   `AND user_id = ?` filter excludes it. The
   query returns no rows → `abort(404)`.

Try the same trick on `/notes/1/edit`. **Same
404.** The check holds on edit too.

**That's the security demo.** *Even if a user
guesses the right ID, the per-user filter
protects.* This is real, and it's the same
pattern that protects your bank account from
showing other people's data.

What if you *forgot* the filter? Try this for
real (then put it back!):

```python
note = conn.execute(
    "SELECT * FROM notes WHERE id = ?",  # NO user_id check
    (note_id,)
).fetchone()
```

Now log in as B. Visit `/notes/1`. **You see
A's note.** That's the security hole the filter
prevents.

**Put the filter back when you're done
testing.**

#### What you have now

- Auth (signup, login, logout)
- Per-user data with `WHERE user_id = ?` on
  every query
- Full CRUD: list, create, view, edit, delete
- Templates with extends/block
- Forms with POST-Redirect-GET
- Flash messages
- A real multi-user web app

This is **the entire shape of every modern web
app.** Whatever you build next — bigger,
fancier, in different languages — the
*patterns* are the same.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show the multi-user demo with
  your buddy. Two accounts, isolated data.
- For the kids who tried the URL-tampering
  break — was the protection satisfying? It
  should be. Real apps survive on this.
- Did the integration feel powerful? *All the
  pieces working together.*

Next week: **deployment.** Get your notes app
on a real public URL. Anyone can sign up.

### If you missed this session

Open Thonny. Start with your Session 10 notes
app foundation.

1. Add the view, edit, and delete routes from
   Part A.

2. Update `notes_list.html` to link to the view
   page.

3. Test the full flow: list, create, view,
   edit, delete.

4. Try the URL-tampering test with two
   accounts.

About 60-90 minutes.

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
    notes = conn.execute(
        "SELECT * FROM notes WHERE user_id = ? ORDER BY updated_at DESC",
        (user["id"],)
    ).fetchall()
```

Add a search box to `notes_list.html`:

```html
<form method="get" action="{{ url_for('notes_list') }}">
    <input type="search" name="q" placeholder="Search notes..."
           value="{{ request.args.get('q', '') }}">
    <button type="submit">Search</button>
</form>
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

#### Public notes

A `is_public` column. Public notes are readable
without login. URL: `/public/<note_id>`. **No
user_id check** for public notes — but only on
that one route. The user's *own* views still
filter by user_id.

#### Pagination

`LIMIT 20 OFFSET ?` for big lists. Add page
controls to the template.

#### Rich text (Markdown)

Replace plain `<textarea>` with Markdown. Save
Markdown, render with a Markdown library:

```python
import markdown
note["html"] = markdown.markdown(note["content"])
```

In template:

```html
<div class="content">{{ note.html|safe }}</div>
```

(`|safe` is needed because Jinja escapes by
default. Markdown output is intended HTML.)

#### Export

A "Download all my notes" button. Generates a
JSON file:

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

#### Sharing (advanced)

A `shared_notes` table:

```sql
CREATE TABLE shared_notes (
    note_id INTEGER,
    shared_with_user_id INTEGER,
    PRIMARY KEY (note_id, shared_with_user_id)
);
```

User A shares a note with User B. User B sees
it in a "Shared with me" view. Real
collaboration.

#### Other directions

- **Categories / folders** for notes.
- **Star / favorite** notes.
- **Most recent N** on home page.
- **Stats** — how many notes, words, etc.
- **Export individual note as text or PDF.**
- **API endpoint** that returns notes as JSON
  (Phase 7 fetch could call this).

### What's next

Next week: **deployment.** PythonAnywhere — free
Python hosting designed for educators and
students. Walk through signup, upload code,
configure, hit the public URL. Your notes app
becomes a *real internet thing* — anyone can
sign up.
