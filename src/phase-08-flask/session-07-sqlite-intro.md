## Session 7: SQLite — your first database

*Phase 8 — Flask · Session 7 of 13*

### What we're learning today

In Phase 5 you saved data to JSON files. In Phase 7
you used localStorage. Both work for one user, one
machine, simple cases. **Real apps use a
database** — structured storage with powerful
queries, multi-user, designed for it. Today you meet
**SQLite** — Python's built-in database — and the
SQL language for talking to it. By the end you'll
have a database file, a table, and you'll be running
queries against it.

This is a **plain Python session.** No Flask. We
focus on SQL first, then tie it to Flask in
Session 8.

### You'll need to remember from last time

- **Python lists and dictionaries.**
- **`with open(...) as f:`** pattern — similar
  shape for `with sqlite3.connect(...)`.
- **`for row in result:`** — iterating.
- **Phase 3 Session 11** (file I/O) — same need
  for persistence, much less powerful tool.

---

### Part A: What's a database?

#### The model

A **database** is structured storage for data.
Think of it like a *spreadsheet* with strict rules:

- **Tables** (like worksheets) — each table holds
  one *kind* of thing. A `users` table, a `posts`
  table.
- **Rows** (like spreadsheet rows) — each row is
  one *item* in the table. One user. One post.
- **Columns** (like spreadsheet columns) — each
  column is a *property* of the items. Name,
  age, email.
- **Schema** — the rules: which tables exist,
  what columns they have, what types those
  columns hold.

Example `users` table:

| id | name  | age |
|----|-------|-----|
| 1  | Alex  | 12  |
| 2  | Sam   | 10  |
| 3  | Pat   | 14  |

Three rows, three columns.

#### Why a database?

vs. JSON file:
- **Queries** — "give me users older than 11"
  takes one line; with JSON you'd loop and filter.
- **Speed** — databases are *fast* even with
  thousands of rows.
- **Multi-user** — multiple Flask requests can
  read/write at once safely.
- **Integrity** — schemas reject bad data.
- **Real apps use them.**

vs. localStorage:
- localStorage is per-browser. Database is *for
  everyone*.

#### What's SQLite?

**SQLite** is a database that:

- Stores everything in a **single file** (no
  separate server program).
- **Built into Python** — no install needed (it's
  the `sqlite3` module).
- Used by *millions* of apps — Firefox, Chrome,
  iOS, Android, countless tools.
- Perfect for small-to-medium apps.

Other databases (PostgreSQL, MySQL) are more
powerful for huge apps but require running a
separate server. SQLite is a great starting point.

#### What's SQL?

**SQL** (Structured Query Language) is the
language for talking to databases. Mostly the same
across all SQL databases (PostgreSQL, MySQL,
SQLite, etc.).

Four main commands:

- **`SELECT`** — read data.
- **`INSERT`** — add new row.
- **`UPDATE`** — change existing row.
- **`DELETE`** — remove row.

Plus:

- **`CREATE TABLE`** — define a table.

That's most of what you need.

#### Try it — Python REPL

Open Thonny. Open the **Shell** (View → Shell, or
just type at the bottom). We'll work in Python's
interactive mode.

```python
>>> import sqlite3
>>> conn = sqlite3.connect("test.db")
>>> cursor = conn.cursor()
```

Three lines. Walk through:

- **`import sqlite3`** — Python's built-in module.
- **`sqlite3.connect("test.db")`** — open (or
  create) a database file. After this line, a
  file called `test.db` exists in your folder.
- **`conn.cursor()`** — get a cursor for running
  SQL.

#### Create a table

```python
>>> cursor.execute("""
...     CREATE TABLE pets (
...         id INTEGER PRIMARY KEY,
...         name TEXT NOT NULL,
...         species TEXT NOT NULL,
...         age INTEGER
...     )
... """)
```

The triple-quoted string is multi-line SQL. Walk
through:

- **`CREATE TABLE pets`** — make a table named
  `pets`.
- **`id INTEGER PRIMARY KEY`** — id is an
  integer, automatically unique and
  auto-incrementing.
- **`name TEXT NOT NULL`** — name is text,
  required.
- **`species TEXT NOT NULL`** — species is text,
  required.
- **`age INTEGER`** — age is an integer
  (optional — no `NOT NULL`).

After this, the table exists. **Try the line
again** — you'll get an error: "table pets
already exists." Tables are persistent.

#### Insert rows

```python
>>> cursor.execute("INSERT INTO pets (name, species, age) VALUES ('Whiskers', 'cat', 3)")
>>> cursor.execute("INSERT INTO pets (name, species, age) VALUES ('Rex', 'dog', 5)")
>>> cursor.execute("INSERT INTO pets (name, species, age) VALUES ('Buddy', 'dog', 2)")
>>> conn.commit()
```

Walk through:

- **`INSERT INTO pets (name, species, age) VALUES (...)`**
  — add a new row.
- **`conn.commit()`** — save the changes to disk.
  Without it, your inserts vanish if the program
  ends.

`commit()` is like saving a file. Required after
any change.

#### Read rows

```python
>>> cursor.execute("SELECT * FROM pets")
>>> for row in cursor.fetchall():
...     print(row)
```

You see:

```
(1, 'Whiskers', 'cat', 3)
(2, 'Rex', 'dog', 5)
(3, 'Buddy', 'dog', 2)
```

Each row comes back as a **tuple** — the columns
in order.

The `*` in `SELECT *` means "all columns." Or
specify:

```python
>>> cursor.execute("SELECT name, age FROM pets")
>>> for row in cursor.fetchall():
...     print(row)
(Whiskers, 3)
(Rex, 5)
(Buddy, 2)
```

#### Filter with WHERE

```python
>>> cursor.execute("SELECT name FROM pets WHERE species = 'dog'")
>>> for row in cursor.fetchall():
...     print(row)
(Rex,)
(Buddy,)
```

The `WHERE` clause filters rows.

```python
>>> cursor.execute("SELECT name FROM pets WHERE age > 2")
>>> for row in cursor.fetchall():
...     print(row)
(Whiskers,)
(Rex,)
```

Operators: `=`, `<`, `>`, `<=`, `>=`, `!=` (or
`<>`), `LIKE 'pattern%'` (substring match).

#### Update and delete

```python
>>> cursor.execute("UPDATE pets SET age = 4 WHERE name = 'Whiskers'")
>>> conn.commit()

>>> cursor.execute("DELETE FROM pets WHERE name = 'Buddy'")
>>> conn.commit()
```

`UPDATE` changes rows. `DELETE` removes rows. Both
need `conn.commit()`.

**WARNING:** A `DELETE` or `UPDATE` without
`WHERE` affects *every row*. `DELETE FROM pets`
empties the table. **Always include `WHERE`** for
targeted changes.

#### Close the connection

```python
>>> conn.close()
```

Always close when done. (Real apps do this in
Flask via context managers — Session 8.)

**Checkpoint:** *You created a table, inserted at
least 2 rows, queried with SELECT and WHERE,
updated and deleted at least once.* **This is the
natural stop point if class is cut short.**

---

### Part B: A complete Python script

Time to put it all in a runnable file (not REPL).

#### Build it

Save as `pets.py`:

```python
import sqlite3

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Create the table (if it doesn't exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        species TEXT NOT NULL,
        age INTEGER
    )
""")

# Add some pets (only if the table is empty)
cursor.execute("SELECT COUNT(*) FROM pets")
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute("INSERT INTO pets (name, species, age) VALUES ('Whiskers', 'cat', 3)")
    cursor.execute("INSERT INTO pets (name, species, age) VALUES ('Rex', 'dog', 5)")
    cursor.execute("INSERT INTO pets (name, species, age) VALUES ('Tweety', 'bird', 1)")
    cursor.execute("INSERT INTO pets (name, species, age) VALUES ('Goldie', 'fish', 2)")
    conn.commit()
    print(f"Added 4 pets.")
else:
    print(f"Already have {count} pets.")

# List all pets
print("\nAll pets:")
for row in cursor.execute("SELECT * FROM pets"):
    print(f"  {row[1]} ({row[2]}, age {row[3]})")

# Filter
print("\nDogs only:")
for row in cursor.execute("SELECT name, age FROM pets WHERE species = 'dog'"):
    print(f"  {row[0]} (age {row[1]})")

conn.close()
```

Save. Run.

```
Added 4 pets.

All pets:
  Whiskers (cat, age 3)
  Rex (dog, age 5)
  Tweety (bird, age 1)
  Goldie (fish, age 2)

Dogs only:
  Rex (age 5)
```

Run *again*. The first message changes to "Already
have 4 pets" because the table now has data.
**Survives between runs** — that's the database.

What's new:

- **`CREATE TABLE IF NOT EXISTS`** — only create
  if missing. Safe to run repeatedly.
- **`SELECT COUNT(*)`** — count rows. Returns one
  row with one column.
- **`cursor.fetchone()[0]`** — get the first
  (only) row, then the first (only) column.
- **`for row in cursor.execute(...)`** —
  shortcut: execute and iterate in one step.

#### Stretch — parameterized queries (SQL injection)

**Never** string-format user input into SQL:

```python
# DON'T DO THIS
name = "user input"
cursor.execute(f"SELECT * FROM pets WHERE name = '{name}'")
```

If `name` is `'; DROP TABLE pets; --`, **your
table is destroyed.** Real attack — happens
constantly to bad code.

The right way: **parameterized queries.** Use `?`
placeholders:

```python
name = "Whiskers"
cursor.execute("SELECT * FROM pets WHERE name = ?", (name,))
```

The `(name,)` is a tuple with one element. The
database engine substitutes safely — no injection
possible.

For multiple parameters:

```python
cursor.execute(
    "INSERT INTO pets (name, species, age) VALUES (?, ?, ?)",
    ("Polly", "parrot", 7)
)
```

**Always use parameterized queries** when data
comes from outside (forms, URLs, files). We'll
hammer this in Session 8.

#### Stretch — DB Browser for SQLite

A free tool for *viewing* SQLite databases:
[sqlitebrowser.org](https://sqlitebrowser.org).
Download, install, open `pets.db`. **Visual table
view.** Run queries in a UI.

Useful for:

- Inspecting your data.
- Trying queries before putting them in code.
- Editing data without writing code.

For class: optional but helpful.

#### Stretch — multiple tables and JOINs

```python
cursor.execute("""
    CREATE TABLE owners (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    ALTER TABLE pets ADD COLUMN owner_id INTEGER
""")
```

Then a JOIN query:

```sql
SELECT pets.name, owners.name
FROM pets
JOIN owners ON pets.owner_id = owners.id
```

JOINs let you connect data across tables. **Out of
session scope** but worth knowing about.

#### Extension — explore SQL

[SQLBolt](https://sqlbolt.com) — interactive SQL
tutorial.
[SQL Murder Mystery](https://mystery.knightlab.com/)
— learn SQL by solving a murder. Genuinely fun.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your `pets.py` running. Did
  the data persist between runs?
- Did SQL feel different from Python? Same logic,
  different shape.
- For the kids who tried parameterized queries —
  did the SQL injection demo land?
- Anyone install DB Browser? Show your data.

Today you learned:

- **A database** is structured storage with
  powerful queries.
- **SQLite** is built into Python; data lives in
  a single file.
- **SQL** is the language for talking to
  databases.
- **`sqlite3.connect(...)` + `cursor()`** to get
  started.
- **`CREATE TABLE`** to define structure.
- **`INSERT`** to add rows.
- **`SELECT`** to read; **`WHERE`** to filter.
- **`UPDATE`** to change; **`DELETE`** to remove.
- **`conn.commit()`** to save changes.
- **Parameterized queries (`?`)** to prevent SQL
  injection — *required* for any external data.

Next week: **tie SQLite to Flask.** Forms write to
the database; templates display query results. Real
persistent web apps.

### If you missed this session

Open Thonny.

1. Run a few `sqlite3` commands in the Python
   shell to create a table and insert rows.

2. Build the `pets.py` script from Part B.

3. Run it twice — verify data persists.

4. (Stretch) Try parameterized queries.

About 45-60 minutes. By the end you should be
comfortable with basic SQL and the `sqlite3`
module.

### Stretch and extension ideas

- **Parameterized queries** — required practice.
- **DB Browser for SQLite** for visual
  inspection.
- **More SQL** — `ORDER BY`, `LIMIT`, `LIKE`,
  `IN`, `BETWEEN`.
- **Aggregate functions** — `COUNT`, `SUM`,
  `AVG`, `MAX`, `MIN`.
- **Multiple tables** with foreign keys + JOINs.
- **Transactions** — `BEGIN`, `COMMIT`,
  `ROLLBACK`.
- **Indexes** for query speed.
- **SQLBolt or SQL Murder Mystery** — interactive
  practice.

### What's next

Next week: **SQLite in Flask** — every CRUD
operation tied to a route. The guestbook from
Session 5 gets a *real database* — messages
survive restarts. You're now building real
persistent web apps.
