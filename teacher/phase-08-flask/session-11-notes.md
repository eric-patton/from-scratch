## Session 11 — Teacher Notes

*Phase 8, Flask · Session 11 of 14 · Title: Build
a notes app together — polish*

### Purpose of this session

The integration moment, and the security drill.
Five jobs, in priority order:

1. **Finish the CRUD.** View, edit, delete —
   each with `WHERE user_id = ?` (and edit has
   it twice).
2. **Run the multi-user demo.** Two accounts,
   isolated data. The "this is real" moment.
3. **Run the URL-tampering security demo.**
   Kids try to break their own filters and
   see them hold. Then optionally remove the
   filter to see what *would* happen.
4. **Cement the per-user pattern.** They've
   seen `WHERE user_id = ?` six times across
   two sessions by the time we're done. It
   should be muscle memory.
5. **Set up Session 12 (deployment).** Today
   the app works locally; next week it works
   for the world.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- The foundation from last week, fully
  working.
- Two browser profiles (or one browser +
  incognito) ready for the multi-user demo.
- Pre-built full app with the security demo
  flow practiced.

**Prep time:** ~20 minutes. You already built
the foundation last week.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap
  Session 10. "We left off at list + create.
  Today: view, edit, delete, plus the
  security demo."
- **Part A: view + edit + delete** (~45 min).
  Each route is small — three small builds,
  not one big one.
- **Break** (~5 min).
- **Part B: multi-user demo + try-to-break-it**
  (~25 min). The capstone of the integration.
- **Wrap-up** (~10 min).

If running short, **drop the "remove the filter
to see it break" experiment** — keep the
positive demo (filter holds), skip the negative
demo. Don't drop the URL-tampering attempt
itself; that's the whole point.

### Teaching the framing

#### Open by remembering the filter

> "Last week we built the foundation and the
> per-user filter. Today every new route gets
> the same filter — three more places it has to
> appear. By the end you'll have written
> `WHERE user_id = ?` six times across two
> sessions. *That's the point.* It's the most
> important line of code in the app."

### Teaching Part A

#### View — single note, security check

```python
"SELECT * FROM notes WHERE id = ? AND user_id = ?"
```

Frame:

> "Two conditions: ID matches AND user_id
> matches. If a user tries to view note 999
> that belongs to someone else, the query
> returns no rows → we 404.
>
> *Without the user_id check*, any logged-in
> user could view any note by guessing IDs.
> Real bug in real apps. *Always include the
> user filter.*"

We're going to demo this in Part B. Set up
the expectation now.

#### Edit — security check appears twice

In the edit route, `AND user_id = ?` appears in
both the SELECT (to load the form) *and* the
UPDATE (to save). Drill this:

> "If we forgot the check on UPDATE, a user
> could craft a POST to `/notes/1/edit` with
> form data and overwrite someone else's note
> — even though the form *page* would 404.
> Both queries need the filter."

#### Delete — POST only

```python
@app.route("/notes/<int:note_id>/delete", methods=["POST"])
```

Callback to Session 8: destructive actions are
POST, not GET. A `<a href="/delete">` link can
be triggered by anything that fetches the URL —
spiders, prefetchers, accidental clicks.

#### Single template for create + edit (callback)

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

You wrote this template last week — today it
gets its second use.

### Teaching Part B

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

Encourage buddies to do this on each other's
apps too. Everyone is now a real user of
multiple real multi-user apps.

#### The URL-tampering security demo (the hook)

This is the moment of the session. Walk it
through on your demo:

1. Log in as User B.
2. Note that User A has notes 1 and 2; User B
   has note 3.
3. Visit `/notes/1` directly. **404.**
4. Visit `/notes/1/edit` directly. **404.**
5. Try to POST to `/notes/1/delete` (you can
   demo with a custom HTML form or curl if
   you want to be slick — or just talk
   through it). **No effect; user filter
   protects.**

> "Even if User B *guesses* the right note ID,
> the query won't return it. The security
> check protects."

Then — if you have time and the kids are
hungry — do the **negative demo:**

1. Comment out `AND user_id = ?` from the
   view route's SELECT.
2. Restart Flask. Refresh `/notes/1` as
   User B.
3. **A's note appears.** That's the security
   hole.
4. Put the filter back. Refresh. **404
   again.**

> "*The filter is the difference between a
> journal app and a journal-app-shaped
> security incident.*"

If a kid asks "what if I edit the URL to put
their note ID?": demo it. **404.** Reassure:
the security holds.

#### Encourage breaking it on their own

Once the demo lands, have buddies try the
URL-tampering on each other's apps. *Real*
penetration testing, age-9 edition. Kids
*love* this when it works.

### Common stumbles

- **Forgot `WHERE user_id = ?` on view, edit,
  or delete.** Demo, fix. (Or use the
  intentional-removal demo to show what
  happens.)
- **Forgot the `AND user_id = ?` on the
  UPDATE statement** even though it's on the
  SELECT. Subtle — drill.
- **`abort(404)` not imported.** Add it to the
  imports.
- **Form fields don't pre-fill on edit.**
  Forgot `value="{{ note.title }}"` on input.
  Or forgot to pass `note` to the template.
- **Updated_at not updating.** SQL: `UPDATE
  notes SET ..., updated_at = CURRENT_TIMESTAMP`.
- **JS confirm not working.** Browser blocked,
  or wrong syntax. Test.
- **Delete route returns "Method Not Allowed."**
  Forgot `methods=["POST"]`.
- **List page no longer links to view.** Forgot
  to wrap the title in `<a>`.
- **The "remove the filter" experiment leaves
  the filter removed.** Save the kid by walking
  them back through. *Always* put the filter
  back.

### Differentiation

- **Younger kids (9-10):** Goal is view + edit
  working. Skip delete or do it last. Focus on
  the multi-user demo over the security demo.
- **Older kids (12+):** Full CRUD + the
  security demo + at least one stretch
  (search is the most rewarding).
- **Advanced (any age):** Push for:
  - Search
  - Tags (multi-table — real database design)
  - Public notes
  - Markdown rendering
  - Export
  - Sharing (advanced)
  - Pagination
- **Struggling:** A kid who can't get edit
  working is the kid you focus on. Most common
  cause: missing `AND user_id = ?` on the
  UPDATE, or `note` not passed to the template.

### What to watch for

- **The "I built a real app!" reaction.** Real
  moment. Bigger than any prior milestone in
  scope.
- **Buddies trying to break each other's
  apps.** Encourage *enthusiastically* — this
  is real engineering culture (red team / blue
  team). Reassure when filters hold.
- **Excitement when the negative demo
  shows what would break.** "Oh, *that's* why
  the filter matters." That's the moment.
- **Curiosity about other security
  vulnerabilities.** "What if the password
  hashing was broken?" Great question.
  Brief answer; can come back to it.
- **Frustration with the size of the task.**
  Reassure: "Three small routes. Each is
  smaller than what you did last week."
- **Kids deploying mentally to Session 12.**
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

- **Session 12 (deployment).** Their notes
  app goes on the internet. Real users.
- **Sessions 13-14 (milestone).** Many kids
  will build variants of the notes app —
  different domain (recipes, books, journal
  entries) but same shape. *The per-user
  filter discipline transfers directly.*
- **Career-long callback:** *every* full-stack
  app uses these patterns. Different
  frameworks, same shape. The
  forgot-the-filter bug is a real category
  of security incident across the industry.
- **Phase 7 callback:** their localStorage
  todo is the same idea per-browser. Now
  it's multi-user, with real database.
- **Peanut butter callback:** the
  forgot-user-filter demo is the precision
  moment. *Code does what you write.* If
  you forgot the filter, the code happily
  returns everyone's data.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Two browser profiles (or browser +
      incognito) for the multi-user demo
- [ ] Pre-built full app with the security
      demo flow practiced
- [ ] DB Browser for SQLite (optional, useful
      for inspection)
- [ ] Projector
- [ ] Class roster
