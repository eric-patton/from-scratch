## Session 10 — Teacher Notes

*Phase 8, Flask · Session 10 of 13 · Title: Build
a notes app together*

### Purpose of this session

The full-stack integration. Five jobs, in priority
order:

1. **Land the multi-user pattern.** Every query
   filters by `user_id`. Per-user data
   isolation.
2. **Land foreign keys.** `user_id INTEGER
   REFERENCES users(id)`. Real database design.
3. **Build the integration.** Auth + CRUD +
   templates + flash, all working together.
4. **Land "the security check is on every
   route."** `WHERE user_id = ?` matters as much
   as login.
5. **Set up Sessions 11-13.** Real app to deploy
   (Session 11), then milestone.

### Before class

**Bring:** nothing physical (maybe energy bars —
this is a long session).

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built notes app (Part B end-state) — fully
  working.
- Pre-built version with search (stretch) for
  reference.

**Prep time:** ~45 minutes. Build the full app
once before class. This is a substantial app.

### Timing and flow

Total: ~90-120 min — *plan for this to run
long.*

- **Welcome and recap** (~5 min). Recap Sessions
  6-9.
- **Part A: foundation + auth setup** (~30 min).
- **Break** (~5 min).
- **Part B: notes CRUD routes** (~50 min). The
  bulk of the session.
- **Wrap-up + multi-user demo** (~10 min).

If running short, **drop edit and delete.** Get
to "list and create your own notes" as the
minimum.

If running long, **let it run long.** This session
matters. The integration is worth the time.

### Teaching the framing

#### "The integration moment"

Open with stakes:

> "You have all the pieces. Today they combine.
> Auth + database + templates + forms + flash =
> a *real full-stack app*.
>
> By end of session: a working multi-user notes
> app. Each user signs up, logs in, has their
> own private notes. Create, view, edit, delete.
>
> *This is the shape of every modern web app.*
> Trello, Notion, Twitter, Reddit, your
> bank — all extend this same pattern."

#### "Per-user data" is the new big idea

Frame:

> "The Session 5 guestbook was *everyone's* — one
> shared list. Real apps are *per-user* — your
> data is yours, mine is mine.
>
> The trick: every query for notes includes
> `WHERE user_id = ?`. The database returns only
> *this user's* notes. Same table, different
> filter per user."

### Teaching Part A

#### Database schema with foreign keys

Walk through:

```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

Frame:

> "The `user_id` column points at a row in the
> `users` table. The `FOREIGN KEY` declares this
> relationship.
>
> Now we have a *connection* between tables. A
> note belongs to a user. We can query `WHERE
> user_id = ?` to get one user's notes."

The `FOREIGN KEY` is documentation; SQLite doesn't
strictly enforce it by default (you can enable
with `PRAGMA foreign_keys = ON`), but it tells
human readers (and other tools) the relationship.

#### `executescript` for multi-statement SQL

```python
conn.executescript("""
    CREATE TABLE IF NOT EXISTS users (...);
    CREATE TABLE IF NOT EXISTS notes (...);
""")
```

> "Run multiple SQL statements at once. Useful
> for setup. *Not* for queries with parameters —
> use regular `execute` for those."

#### Reuse Session 9 auth

Don't retype. Show the code from Session 9, paste
in. Save time for notes routes.

### Teaching Part B

#### List notes — the per-user query

```python
notes = conn.execute(
    "SELECT * FROM notes WHERE user_id = ? ORDER BY updated_at DESC",
    (user["id"],)
).fetchall()
```

Frame:

> "*This* query is the entire pattern of
> per-user data. Same `notes` table for every
> user — but the filter narrows it to this user's
> rows.
>
> *Without the filter, every user would see
> everyone's notes.* That's a security
> catastrophe. The `WHERE user_id = ?` is
> non-negotiable."

#### Create note

Walk through. Pause on:

```python
"INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
(user["id"], title, content)
```

> "We hardcode `user_id = current user's id`.
> The user *cannot* set this to someone else's
> id by tampering — it's not in the form.
>
> If the user_id came from a hidden form field,
> users could edit their browser's HTML and
> assign notes to other people. *Always set
> user_id from `current_user()`, never from
> form data.*"

This is real. Many real apps have been compromised
this way.

#### View note — the security check

```python
"SELECT * FROM notes WHERE id = ? AND user_id = ?"
```

Frame:

> "Two conditions: ID matches AND user_id
> matches. If a user tries to view note 999 that
> belongs to someone else, the query returns no
> rows → we 404.
>
> *Without the user_id check*, any logged-in user
> could view any note by guessing IDs. Real bug
> in real apps. *Always include the user filter.*"

#### Edit and delete — same security check

Same `AND user_id = ?` pattern. Drill it.

#### Single template for create + edit

```html
<input type="text" name="title"
       value="{{ note.title if note else '' }}">
```

Frame:

> "*One template, two uses.* For create, `note`
> is `None` — empty values. For edit, `note` is
> the row — pre-filled values.
>
> The Jinja conditional handles both. *Don't
> duplicate templates* when one suffices."

#### The multi-user demo

After all routes work:

1. Sign up as User A. Create some notes.
2. Log out. Sign up as User B.
3. View "your notes." **Empty** — correct.
4. Create User B's notes.
5. Log out. Log back in as User A.
6. **A's notes are still there.**

> "*Two users. Different data. Same app.* This
> is the magic. Per-user state, real
> persistence."

#### Try to break it (the security demo)

If you want a security drill:

1. Log in as User B.
2. Look at one of User A's note URLs (you can
   peek by being clever — visit
   `/notes/1`).
3. **Get a 404** because the user_id check
   filters it out.

> "Even if User B *guesses* the note ID, the
> query won't return it. The security check
> protects."

If a kid asks "what if I edit the URL to put
their note ID?": demo it. **404.** Reassure: the
security holds.

### Common stumbles

- **Forgot `WHERE user_id = ?`.** Major bug —
  users see/edit each other's notes. Demo and
  fix.
- **Forgot `@login_required`.** Anonymous users
  hit auth-required routes. Add it.
- **`current_user()` returns None.** Session
  expired or not logged in. Walk through.
- **Form fields don't pre-fill on edit.** Forgot
  `value="{{ note.title }}"` on input.
- **`abort(404)` not imported.** ImportError.
- **Query returns wrong rows.** Forgot to add
  `?` parameter or wrong order.
- **Template variable `note` is None on create.**
  `{{ note.title if note else '' }}` — Jinja
  short-circuits. Fine.
- **Updated_at not updating.** SQL: `UPDATE notes
  SET ..., updated_at = CURRENT_TIMESTAMP`.
- **JS confirm not working.** Browser blocked, or
  wrong syntax. Test.
- **Database file accidentally deleted.** Re-run,
  re-init, lose data. Real-world: don't.

### Differentiation

- **Younger kids (9-10):** Goal is signup +
  list + create. Skip view, edit, delete (or
  just delete).
- **Older kids (12+):** Push for full CRUD.
  Stretch: search.
- **Advanced (any age):** Push for:
  - Search
  - Tags (multi-table)
  - Public notes
  - Markdown rendering
  - Export
  - Sharing (advanced)
  - Pagination
- **Struggling:** A kid who can't get the list
  page working is the kid you focus on. Most
  common cause: forgot user filter, or
  `@login_required` import.

### What to watch for

- **The "I built a real app!" reaction.** Real
  moment. Bigger than any prior milestone in
  scope.
- **Buddies signing up for each other's apps.**
  Encourage. Each kid's app is its own
  multi-user world.
- **Excitement about isolation** — User A and
  User B can't see each other's notes. Real
  privacy lesson.
- **Curiosity about security** — kids may
  attempt to break the user filter. Encourage,
  reassure when it holds.
- **Frustration with the size of the task.**
  This is the longest session. Reassure:
  "Take it step by step. Each route is small."
- **Kids deploying mentally to Session 11.**
  "When can I share this with my friends?"
  Next week.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 11 (deployment).** Their notes app
  goes on the internet. Real users.
- **Sessions 12-13 (milestone).** Many kids will
  build variants of the notes app — different
  domain (recipes, books, journal entries) but
  same shape.
- **Career-long callback:** *every* full-stack
  app uses these patterns. Different
  frameworks, same shape.
- **Phase 7 callback:** their localStorage todo
  is the same idea per-browser. Now it's
  multi-user, with real database.
- **Peanut butter callback opportunity:** the
  forgot-user-filter bug is a precision
  moment. *Code does what you write.* If you
  forgot the filter, the code happily returns
  everyone's data.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built notes app (full)
- [ ] Pre-built version with search (stretch)
- [ ] DB Browser for SQLite (optional, useful
      for inspection)
- [ ] Projector
- [ ] Class roster
