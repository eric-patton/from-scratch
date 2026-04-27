## Session 10 — Teacher Notes

*Phase 8, Flask · Session 10 of 14 · Title: Build
a notes app together — foundation*

### Purpose of this session

Foundation of the multi-user app. Five jobs, in
priority order:

1. **Land the multi-user pattern.** Every notes
   query filters by `user_id`. Per-user data
   isolation. Today they see it twice (list +
   create); next week they see it three more
   times.
2. **Land foreign keys.** `user_id INTEGER` +
   `FOREIGN KEY (user_id) REFERENCES users(id)`.
   Real database design.
3. **Wire auth into the new schema.** The
   Session 9 routes still apply; we just have
   a notes table alongside users now.
4. **Land the security framing.** *Why* the
   filter matters. Set up next week's "try to
   break it" demo.
5. **Set up Session 11 (polish).** Today gets
   us to list + create; next week is view,
   edit, delete, and the multi-user demo.

This session used to be "the whole notes app in
one block." That ran 90-120 minutes and rushed
the most important pattern in the phase. Splitting
gives `WHERE user_id = ?` the breathing room it
deserves.

### Before class

**Bring:** nothing physical (maybe energy bars
— this is still a meaty session).

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built foundation app (Part B end-state) —
  fully working, signup, login, list, create.
- Pre-built version of the *full* app (next
  week's end-state) for forward-pointing
  demos if asked.

**Prep time:** ~30 minutes. Build the
foundation once before class.

### Timing and flow

Total: ~90 min — should fit cleanly now.

- **Welcome and recap** (~5 min). Recap
  Sessions 6-9. Frame today as "the foundation
  of the integration moment."
- **Part A: foundation + auth setup** (~30 min).
- **Break** (~5 min).
- **Part B: list + create + per-user filter
  drill** (~40 min).
- **Wrap-up + per-user demo** (~10 min).

If running short, **drop create.** Get to "list
view loads (empty) for a logged-in user" as the
minimum. Create can move to next week.

If running long, **let it run long** — but
don't spill into view/edit/delete. Those are
their own session now.

### Teaching the framing

#### "The foundation moment"

Open with stakes:

> "You have all the pieces. Today they start to
> combine. Auth + database + templates + forms
> + flash = a real full-stack app — which
> we'll finish next week.
>
> By end of today: a working multi-user notes
> *foundation*. Each user signs up, logs in,
> sees their own list of notes, can create new
> ones. Next week we add view, edit, delete,
> and try to break the security.
>
> *This is the shape of every modern web app.*
> Trello, Notion, Twitter, Reddit, your
> bank — all extend this same pattern."

#### "Per-user data" is the new big idea

Frame:

> "The Session 5 guestbook was *everyone's* —
> one shared list. Real apps are *per-user* —
> your data is yours, mine is mine.
>
> The trick: every query for notes includes
> `WHERE user_id = ?`. The database returns
> only *this user's* notes. Same table,
> different filter per user."

Spend extra time on this. It's the most
important pattern in the phase, and the whole
reason to split this session was to give it
room.

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
in. Save time for the per-user filter drill.

### Teaching Part B

#### List notes — the per-user query (drill it)

```python
notes = conn.execute(
    "SELECT * FROM notes WHERE user_id = ? ORDER BY updated_at DESC",
    (user["id"],)
).fetchall()
```

Frame, slowly:

> "*This* query is the entire pattern of
> per-user data. Same `notes` table for every
> user — but the filter narrows it to this
> user's rows.
>
> *Without the filter, every user would see
> everyone's notes.* That's a security
> catastrophe. The `WHERE user_id = ?` is
> non-negotiable.
>
> Every notes query you write today has this
> filter. So does every notes query we write
> next week."

Make it explicit you'll come back to this.
Today they see the filter twice (list, then
the implicit "user_id is set on insert").
Next week they see it three more times (view,
edit, delete) — and they break it on purpose.

#### Create note — the user_id discipline

Walk through. Pause on:

```python
"INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
(user["id"], title, content)
```

> "We hardcode `user_id = current user's id`.
> The user *cannot* set this to someone else's
> id by tampering — it's not in the form.
>
> If the user_id came from a hidden form
> field, users could edit their browser's
> HTML and assign notes to other people.
> *Always set user_id from `current_user()`,
> never from form data.*"

This is real. Many real apps have been
compromised this way.

#### The per-user demo at wrap-up

After the routes work:

1. Sign up as User A. Create some notes.
2. Log out. Sign up as User B.
3. View "your notes." **Empty** — correct.
4. Create User B's notes.
5. Log out. Log back in as User A.
6. **A's notes are still there.**

> "*Two users. Different data. Same app.* This
> is the magic. Per-user state, real
> persistence."

Don't do the URL-tampering "try to break it"
demo today — that's next week, and it's the
hook for Session 11. Save it.

### Common stumbles

- **Forgot `WHERE user_id = ?` on the list
  query.** Major bug — users see everyone's
  notes. Demo and fix. (You'll demo this
  intentionally next week.)
- **Forgot `@login_required`.** Anonymous users
  hit auth-required routes. Add it.
- **`current_user()` returns None.** Session
  expired or not logged in. Walk through.
- **`abort(404)` not imported.** Will appear
  next week — you can pre-import today.
- **Query returns wrong rows.** Forgot to add
  `?` parameter or wrong order.
- **Database file accidentally deleted.**
  Re-run, re-init, lose data. Real-world:
  don't.
- **Notes table created without `user_id`
  column.** Schema typo. Drop the DB file and
  re-run.
- **Kid hardcodes `user_id = 1` while
  testing.** Catch and fix — use
  `current_user()`.

### Differentiation

- **Younger kids (9-10):** Goal is signup +
  list (empty) + create. That's a real
  achievement.
- **Older kids (12+):** Push for full Part A +
  Part B. Stretch: sort options.
- **Advanced (any age):** Push them to read
  next week's spec and try view/edit/delete on
  their own. Or start on a stretch (search,
  empty-state styling).
- **Struggling:** A kid who can't get the list
  page to load is the kid you focus on. Most
  common cause: forgot user filter, or
  `@login_required` import.

### What to watch for

- **The "I built a real app!" reaction.** Some
  kids feel it today (foundation), some feel
  it next week (full CRUD).
- **Buddies signing up for each other's apps.**
  Encourage. Each kid's app is its own
  multi-user world.
- **Excitement about isolation** — User A and
  User B can't see each other's notes. Real
  privacy lesson.
- **"What about editing? Deleting?"** Frame it
  forward: "Next week. We're building this in
  two parts on purpose so the security pattern
  gets the room it deserves."
- **Frustration with the database errors.** If
  a kid added the schema wrong, drop the DB
  and re-run init.
- **Kids deploying mentally to Session 12.**
  "When can I share this with my friends?"
  Two more weeks.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 11 (notes app polish).** Finish
  view/edit/delete and the security demo.
  Today's filter discipline pays off then.
- **Session 12 (deployment).** Their notes
  app goes on the internet. Real users.
- **Sessions 13-14 (milestone).** Many kids
  will build variants of the notes app —
  different domain (recipes, books, journal
  entries) but same shape.
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
  everyone's data. Save the explicit demo for
  next week.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built foundation app
- [ ] Pre-built full app (for forward-looking
      questions)
- [ ] DB Browser for SQLite (optional, useful
      for inspection)
- [ ] Projector
- [ ] Class roster
