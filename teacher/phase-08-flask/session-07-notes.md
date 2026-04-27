## Session 7 — Teacher Notes

*Phase 8, Flask · Session 7 of 13 · Title: SQLite —
your first database*

### Purpose of this session

The "real persistence" session. Five jobs, in
priority order:

1. **Land "what a database is."** Tables, rows,
   columns. Spreadsheet analogy works for kids.
2. **Land basic SQL** — `CREATE`, `INSERT`,
   `SELECT`, `WHERE`, `UPDATE`, `DELETE`.
3. **Land `sqlite3` module.** Built in. No install.
4. **Land `conn.commit()`** as required-after-write.
5. **Set up parameterized queries** for Session 8.
   Drill the SQL injection danger.

**Note:** No Flask today. Just plain Python. SQL is
its own thing — separating it from Flask makes
both easier.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Python + Thonny + DB Browser
  for SQLite (optional but recommended).
- Pre-built `pets.py` script.
- A pre-existing `pets.db` to inspect with DB
  Browser.
- Optional: SQL Murder Mystery URL bookmarked
  for stretch.

**Prep time:** ~20 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 6
  (sessions/flash).
- **Part A: what's a database** (~15 min). Whiteboard
  table diagram.
- **Part A: REPL exploration** (~25 min). Type
  commands in Thonny shell.
- **Break** (~5 min).
- **Part B: complete script** (~25 min).
- **Part B: parameterized queries** (~10 min).
- **Wrap-up** (~5 min).

If running short, **drop the multiple-tables
preview and DB Browser stretch.** The base CRUD +
parameterized queries is the priority.

### Teaching the framing

#### "Why a database?"

Open with a comparison:

> "Phase 5 had JSON file save/load. Phase 7 had
> localStorage. Both work for *one user, one
> machine, simple data*.
>
> Real apps need:
> - **Multi-user** — many people hitting the same
>   server, sharing data.
> - **Queries** — 'give me all users older than
>   12.' One line in SQL; a loop and filter in
>   Python.
> - **Speed** — even with a million rows.
> - **Reliability** — atomic transactions, no
>   half-saves.
>
> *Databases* solve all of that."

### Teaching Part A

#### Spreadsheet analogy

On the board, draw a table:

```
pets
─────────────────────────
id │ name     │ species │ age
───┼──────────┼─────────┼────
 1 │ Whiskers │ cat     │ 3
 2 │ Rex      │ dog     │ 5
 3 │ Tweety   │ bird    │ 1
```

Frame:

> "Like a spreadsheet. Each *row* is one item.
> Each *column* is a property. The whole thing is
> a *table*. A *database* is a collection of
> tables.
>
> Two big differences from a spreadsheet:
>
> 1. *Schema enforced* — you declared the
>    columns and types up front. Can't sneak in a
>    'shoe size' column without rewriting.
> 2. *Queries* — 'give me all dogs' is one
>    line, not a manual filter."

#### REPL is the safest learning surface

Type SQL commands in the Thonny shell on the
projector. Each one runs immediately. Kids see
results.

Walk through:

```python
import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
```

> "Three lines to start. Open the database file,
> get a cursor for running SQL."

#### `CREATE TABLE` — the schema

```sql
CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age INTEGER
)
```

Walk through each column:

- `id INTEGER PRIMARY KEY` — auto-incrementing
  unique ID.
- `name TEXT NOT NULL` — text, required.
- `species TEXT NOT NULL` — text, required.
- `age INTEGER` — number, optional.

Frame:

> "PRIMARY KEY = unique identifier for each row.
> NOT NULL = required field. INTEGER, TEXT, REAL
> (decimal), BLOB (binary) are common types."

#### `INSERT` and `SELECT`

```sql
INSERT INTO pets (name, species, age) VALUES ('Whiskers', 'cat', 3)
SELECT * FROM pets
```

> "Insert specifies columns and values. SELECT *
> means 'all columns.' WHERE filters."

#### `conn.commit()` is mandatory

```python
conn.commit()
```

> "Without commit, your changes vanish when the
> program exits. *Always commit after writes.*
> Like saving a file."

Demo: insert, *don't commit*, close connection,
reopen. **Data gone.** Insert, *commit*, close,
reopen. **Data there.**

Real lesson.

### Teaching Part B

#### Build `pets.py`

Type live. Walk through:

- `IF NOT EXISTS` — safe re-run.
- `SELECT COUNT(*)` — checking if table is
  populated.
- `for row in cursor.execute(...)` — execute and
  iterate in one.

Run twice. Show:

- First run: "Added 4 pets."
- Second run: "Already have 4 pets."

> "*That's* persistence. Database survives the
> program ending. Re-run anytime — same data."

#### Parameterized queries — the security drill

Show the bad version:

```python
name = "user input"
cursor.execute(f"SELECT * FROM pets WHERE name = '{name}'")
```

Frame:

> "If `name` came from a form, what if a malicious
> user types `'; DROP TABLE pets; --`?
>
> Your query becomes:
> `SELECT * FROM pets WHERE name = ''; DROP TABLE pets; --'`
>
> *That deletes your entire pets table.* This is
> SQL injection — the most common database attack
> in history. Real attack. Happens daily."

Show the fix:

```python
cursor.execute("SELECT * FROM pets WHERE name = ?", (name,))
```

> "Question marks are *placeholders*. The database
> engine substitutes safely — no injection
> possible.
>
> *Always use parameterized queries* when data
> comes from outside (forms, URLs, files). Drill
> this. Production code that violates this gets
> attacked."

This is foundational security. Worth its own time.

#### DB Browser for SQLite (stretch)

If you have it installed:

1. Open `pets.db` in DB Browser.
2. **Show the table** — visual rows and columns.
3. Run a query in the SQL tab.

> "Useful for inspection and debugging. Not
> required, but nice."

### Common stumbles

- **Forgot `conn.commit()`.** Inserts vanish.
  Walk through.
- **`OperationalError: no such table`.** Forgot
  `CREATE TABLE` or wrong DB file.
- **`OperationalError: table already exists`.**
  Tried to recreate. Use `IF NOT EXISTS`.
- **SELECT result confusion.** `cursor.fetchall()`
  returns a list of tuples. Iterating yields
  tuples. Index columns by position.
- **Single-row tuple.** `cursor.fetchone()[0]`
  gets the first column of the first row.
- **String formatting in SQL.** Don't! Use
  parameterized queries.
- **Quotes mismatch.** SQL uses single quotes for
  strings; Python f-strings use them too;
  mismatch causes errors. Parameterized queries
  avoid this entirely.
- **Different file each run.** `sqlite3.connect("test.db")`
  uses relative path. Run from different folder
  → different file. Use absolute path or
  consistent working directory.
- **Lost data.** Maybe didn't commit. Maybe wrong
  file. Maybe in-memory mode (`":memory:"` —
  intentional for tests, surprising in production).

### Differentiation

- **Younger kids (9-10):** Goal is the basic REPL
  exploration — create table, insert, select.
  The Python script is a stretch.
- **Older kids (12+):** Push for the full script
  + parameterized queries.
- **Advanced (any age):** Suggest:
  - DB Browser for SQLite
  - More SQL: ORDER BY, LIMIT, LIKE, IN
  - Aggregate functions (COUNT, AVG, etc.)
  - Multiple tables + JOIN
  - SQLBolt / SQL Murder Mystery
- **Struggling:** A kid who can't get the table
  created is the kid you focus on. Most common
  cause: typo in SQL, forgot to import, or
  cursor confusion.

### What to watch for

- **The "data survived restart!" reaction.** Real.
  Bigger than they expected.
- **Buddies querying each other's data.** Encourage.
- **SQL injection demo lands.** Some kids will be
  visibly impressed by the attack scenario. Real
  security awareness.
- **DB Browser excitement.** Visual data is
  satisfying.
- **Kids trying complex queries.** Encourage.
- **The "this is just like a dict, but better"
  reaction.** Yes — affirm.
- **Frustration with SQL syntax.** New language.
  Reassure: 4 commands cover 90% of needs.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 8 (DB in Flask).** Tie SQLite to
  Flask. Routes do CRUD. Persistent guestbook.
- **Session 9 (accounts).** `users` table with
  hashed passwords.
- **Session 10 (notes app).** `users` + `notes`
  tables, JOINs, real multi-user app.
- **Phase 5 callback:** customtkinter Session 6's
  JSON save was the simpler version. Now upgrade
  to a real database.
- **Career-long callback:** SQL is *the* universal
  data query language. Every backend dev uses it.
  PostgreSQL, MySQL, SQLite, even cloud
  databases — same SQL.
- **Peanut butter callback opportunity:** the
  string-format-into-SQL → injection bug is *the*
  classic precision moment. Code does what you
  wrote; what you wrote was unsafe.

### Materials checklist

- [ ] Demo machine with Python + Thonny
- [ ] DB Browser for SQLite (optional)
- [ ] Pre-built `pets.py`
- [ ] Pre-existing `pets.db` for visual demo
- [ ] Optional: SQL Murder Mystery URL
- [ ] Projector
- [ ] Class roster
