## Session 8 — Teacher Notes

*Phase 8, Flask · Session 8 of 13 · Title: Database
in Flask — CRUD operations*

### Purpose of this session

Tie everything together. Five jobs, in priority
order:

1. **Land Flask + SQLite integration.** A helper
   function for connections, init on startup.
2. **Land the four CRUD operations as routes.**
   Create (POST), Read (GET), Update (POST),
   Delete (POST).
3. **Drill parameterized queries.** Every external
   data goes through `?` placeholders.
4. **Land `row_factory = sqlite3.Row`** for
   dict-like access in templates.
5. **Set up Session 9 (accounts).** Today's
   patterns generalize to a `users` table.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built persistent guestbook (Part A
  end-state).
- Pre-built guestbook with full CRUD (Part B
  end-state).
- Pre-built guestbook with search (stretch).

**Prep time:** ~25 minutes.

### Timing and flow

Total: ~90 min — possibly tight.

- **Welcome and recap** (~5 min). Recap Session 7
  (SQLite).
- **Part A: get_db + init_db + persistent
  guestbook** (~40 min).
- **Break** (~5 min).
- **Part B: edit and delete** (~30 min).
- **Stretches** (~5 min).
- **Wrap-up** (~5 min).

If running short, **drop edit (keep delete only)**.
The persistent guestbook is the priority.

### Teaching Part A

#### "Last week + this week = real app"

Frame:

> "Last week: SQLite in plain Python. This week:
> SQLite in Flask. The two combine into *real
> persistent web apps*. By end of session your
> guestbook from Session 5 has a database — data
> survives restarts."

#### `get_db()` helper

```python
def get_db():
    conn = sqlite3.connect("guestbook.db")
    conn.row_factory = sqlite3.Row
    return conn
```

Frame:

> "Three lines repeated everywhere is annoying.
> One function, called from each route. *Real
> production apps* have similar helpers (often
> with connection pooling, error handling,
> etc.)."

The `row_factory = sqlite3.Row` is the key
upgrade:

> "Without `row_factory`, rows come back as plain
> tuples — `row[0]`, `row[1]`. With it, they
> behave like dicts — `row['name']`, `row['id']`.
> *Way* more readable, especially in templates."

#### `init_db()` and call at startup

```python
def init_db():
    # CREATE TABLE IF NOT EXISTS ...
    
init_db()
```

Frame:

> "Run `CREATE TABLE` once when the app starts.
> `IF NOT EXISTS` makes it safe to run repeatedly.
>
> Real production apps use *migrations* — versioned
> schema changes. Beyond our scope. For class:
> just init on startup."

#### Walk through the refactor

Live, with the Session 5 code on screen alongside:

- Replace `messages = []` with the database.
- Replace `messages.append(...)` with `INSERT`.
- Replace `for m in messages:` with `SELECT`.

Show side-by-side:

```python
# Session 5
messages.append({"name": name, "message": message})

# Session 8
conn.execute(
    "INSERT INTO messages (name, message) VALUES (?, ?)",
    (name, message)
)
conn.commit()
```

Frame:

> "Same shape. Same data. Different storage.
> Database is more code per operation, but the
> data *survives*."

#### `?` parameterized queries — drill it

Every value from `request.form` or URL params
goes through `?`. Show the unsafe vs safe:

```python
# UNSAFE — never do this
conn.execute(f"INSERT INTO messages (name) VALUES ('{name}')")

# SAFE — always do this
conn.execute("INSERT INTO messages (name) VALUES (?)", (name,))
```

Reinforce from Session 7:

> "SQL injection is real. Always parameterize.
> *Always.*"

#### Reload-after-restart demo

The big moment:

1. Submit messages.
2. Stop the server (Ctrl+C).
3. Start it again.
4. Reload the page.
5. **Messages still there.**

Pause for it:

> "*That's* the database. Compared to last week's
> in-memory list — completely different. Real
> persistence. The guestbook now works the way
> guestbooks should."

### Teaching Part B

#### CRUD as routes

Diagram on the board:

```
CRUD Operation        URL                  Method
─────────────────────────────────────────────────
Create (insert)       /                    POST
Read all              /                    GET
Read one              /messages/<id>       GET
Update                /edit/<id>           POST
Delete                /delete/<id>         POST
```

Frame:

> "Every web app does these. CMS, blog, social
> network, todo app, e-commerce — all CRUD on
> top of a database. *Today you learn all four.*"

#### Delete first (simpler)

Walk through:

```python
@app.route("/delete/<int:message_id>", methods=["POST"])
def delete(message_id):
    conn = get_db()
    conn.execute("DELETE FROM messages WHERE id = ?", (message_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))
```

In the template, each message gets a delete *form*
(not link):

```html
<form method="post" action="{{ url_for('delete', message_id=m.id) }}">
    <button>Delete</button>
</form>
```

Frame:

> "Delete is a *change* — POST, not GET. So we
> use a form with a button, not a link. The form
> submits to `/delete/N` where N is the message
> ID."

The "delete must be POST" rule is real:

> "If delete were GET, search engine crawlers
> following links would *delete things by
> accident.* Always use POST for changes."

#### Edit — two-route pattern (or single route)

Walk through:

```python
@app.route("/edit/<int:message_id>", methods=["GET", "POST"])
def edit(message_id):
    conn = get_db()
    
    if request.method == "POST":
        # save changes
        return redirect(...)
    
    # show edit form
    row = conn.execute(...).fetchone()
    return render_template("edit.html", message=row)
```

> "GET shows the edit form *with the existing
> values pre-filled.* POST saves the changes and
> redirects.
>
> Same single-route pattern as Session 5's form."

The template uses `value="{{ message.name }}"` to
pre-fill — preserving existing data so user can
modify, not retype.

### Common stumbles

- **`OperationalError: no such table`.** Forgot
  `init_db()` or wrong DB filename.
- **Forgot `commit()`.** Insert/update/delete
  silently doesn't persist.
- **Forgot `?` parameterization.** SQL injection
  vulnerability. Drill.
- **`fetchall()` vs `fetchone()`.** All rows vs
  first row. Different return types.
- **Trying to access tuple columns by name** when
  not using `row_factory`. Walk through.
- **Connection not closed.** Cursor errors,
  resource leaks. Add `conn.close()`.
- **Multiple `init_db()` calls.** Slow startup,
  but `IF NOT EXISTS` makes it safe.
- **Thread issues** with `sqlite3.connect`.
  SQLite by default has restrictions on
  cross-thread connections. Flask dev server
  can hit this; production use Flask app
  context. Out of scope; mention if encountered.
- **Delete uses GET link.** Easy to do
  accidentally; works but is wrong. Use POST
  form.
- **Edit form not pre-filled.** Forgot
  `value="..."` on inputs.
- **Edit submit goes to wrong route.** `action=`
  missing or wrong.

### Differentiation

- **Younger kids (9-10):** Goal is the
  persistent guestbook (Part A). Skip edit and
  delete.
- **Older kids (12+):** Push for delete and edit
  (full CRUD).
- **Advanced (any age):** Suggest:
  - Search with LIKE
  - Sort options
  - Pagination with LIMIT/OFFSET
  - Counts and stats
  - Confirm dialogs with JS
  - Multiple tables
- **Struggling:** A kid who can't get the table
  populated is the kid you focus on. Most
  common cause: forgot init_db, forgot commit,
  or wrong file.

### What to watch for

- **The "messages survived restart!" reaction.**
  Real moment. Pause for it.
- **Buddies tampering with each other's
  messages.** Encourage as testing; address as
  community management if it gets mean.
- **Excitement about edit/delete.** Real
  empowerment.
- **Kids skipping `?`** — string format the SQL.
  Catch immediately, walk through SQL injection
  again.
- **Forgot to close connection.** Usually fine
  for class scale; mention as good habit.
- **Database file accidentally deleted/renamed.**
  Easy fix: re-init, lose data. Real-world: don't
  do this.
- **Multiple kids hitting the same DB file** —
  not an issue if each kid has their own
  guestbook.db locally.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 9 (accounts).** `users` table with
  hashed passwords. Same CRUD pattern.
- **Session 10 (notes app).** Multi-table app:
  users + notes, with auth. Real production
  shape.
- **Session 11 (deployment).** Deploy a real
  database-backed app to the public.
- **Phase 5/7 callback:** todo apps in
  customtkinter and browser. Now upgrade to
  multi-user with a real database.
- **Career-long callback:** every backend dev
  works with CRUD daily. The patterns are
  universal.
- **Peanut butter callback opportunity:** the
  forgot-`?` → SQL injection moment. Code does
  what you wrote; if you wrote it unsafely,
  it's exploitable.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built persistent guestbook
- [ ] Pre-built guestbook with full CRUD
- [ ] Pre-built guestbook with search
- [ ] Projector
- [ ] Class roster
