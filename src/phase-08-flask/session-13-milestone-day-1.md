## Session 13: Milestone project work day 1

*Phase 8 — Flask · Session 13 of 14*

### What we're learning today

Today is *your* day. You'll plan a full-stack web
app — your design, your data, your users — and
start building it. Next week you finish, deploy,
and **demo your live URL** to the class. This is
your **eighth and final milestone** of the
curriculum.

### You'll need to remember from last time

- **Templates** — extends/block, partials.
- **Database** — get_db, CRUD, parameterized
  queries.
- **Auth** — signup, login, hashed passwords,
  current_user.
- **Forms** — POST-Redirect-GET, validation.
- **Flash messages** for feedback.
- **Deployment** — PythonAnywhere.

---

### Part A: Plan your project

#### The plan

Take paper or open a blank text file. Answer these
nine questions:

1. **What's the app?** *(One sentence. "A
   recipe-sharing site." "A polling app." "A
   reading log.")*

2. **Who's it for?** *(Yourself? Class? General
   public?)*

3. **Does it need user accounts?** *(Almost
   always yes for Phase 8 milestones.)*

4. **What does each user do?** *(Sign up, log in,
   then... what?)*

5. **What database tables?** *(`users` plus what?
   Each table: name + columns.)*

6. **What routes?** *(Each URL + what it does.
   At minimum: home, signup, login, logout, list,
   create, view, edit, delete.)*

7. **What templates?** *(One per route, usually.)*

8. **What's the simplest version?** *(Build this
   FIRST. No fancy features. Just core flow.)*

9. **What's one stretch feature?** *(After core
   works.)*

#### Phase 8 requirements

Your milestone must:

- **Use HTML + CSS + Python (Flask).**
- **Have user accounts** (signup, login, logout
  with hashed passwords).
- **Have a database** with at least 2 tables
  (`users` + one other).
- **Have full CRUD** for at least one entity
  (create, read, update, delete).
- **Be deployed to a public URL** by the demo —
  PythonAnywhere or another host.
- **Be usable by multiple users** — your
  classmates should be able to sign up and use
  it.

Bonus:

- Extra tables / relationships.
- Search / filter.
- Public + private content.
- File uploads.
- API endpoints (JSON returns).
- Real CSS polish.

#### If you don't have an idea

Pick one and modify:

**Personal apps (your data only):**

- **Reading log** — track books, ratings,
  reviews.
- **Habit tracker** — daily check-in for habits.
- **Goal tracker** — long-term goals with
  progress.
- **Workout log** — exercises, sets, dates.
- **Movie / show watchlist** — to-watch and
  watched.
- **Recipe collection** — categorized, with
  ingredients.
- **Quote collection** — favorite quotes by
  source.
- **Daily journal** — date-tagged entries.

**Multi-user apps (community):**

- **Class profile site** — each kid has a card
  with their interests.
- **Class wiki** — shared editable pages.
- **Recipe sharing** — submit and browse
  others' recipes.
- **Book club** — vote on next book, discuss.
- **Polls / voting** — create polls, vote, see
  results.
- **Q&A site** — ask questions, others answer.
- **Photo gallery** with comments.
- **Trivia game** — questions, scores per
  user, leaderboard.

**Game / interactive apps:**

- **Multi-user trivia** with high scores per
  user.
- **Word game** — guess the word, score per
  user.
- **Memory game** with persistent best times.
- **Choose-your-own-adventure** with saved
  progress.

**Tools / productivity:**

- **Group todo list** — shared, multi-user
  permissions.
- **Class scheduler** — assignments + due
  dates.
- **Note-taking** (extension of Sessions 10-11).
- **Bookmark manager** — save URLs with tags.
- **Pomodoro / time tracker** with stats.

**Variants of in-class projects:**

- **The notes app from Sessions 10-11** with new
  features (tags, search, public mode,
  sharing).
- **A guestbook (Session 5/8) + accounts** so
  posters are users.

Pick one. Spend two minutes. Don't overthink.

#### Show Mr. Eric

When your plan is ready, show it to Mr. Eric.
He'll either say "go build it" or ask one
question.

#### Set up the project + deploy day 1

```
$ mkdir my_app && cd my_app
$ touch app.py
$ git init
$ git add app.py
$ git commit -m "Initial setup"
```

Push to GitHub:

1. Create a new public repo on GitHub.
2. `git remote add origin ...` + `git push -u
   origin main`.

**Then deploy to PythonAnywhere right now,**
before any real code:

1. PythonAnywhere bash console: `git clone` your
   repo.
2. Add a new web app (Manual config, Python 3.10).
3. Edit WSGI file.
4. `pip install --user flask`.
5. Reload.
6. Visit URL — should show some kind of error
   (no code yet) or "Hello world" if you wrote
   one.

**Why deploy day 1?** Same reason as Phase 7
Session 16: catch deployment issues *now*, not
the night before demo. Every commit can be
deployed via `git pull` + Reload.

#### Build the simplest version first

Look at your answer to question 8. Build *that*
first. Get a window on screen — even just signup
+ login working. Then iterate.

For each significant change:

1. Make the change locally.
2. Test in browser at `127.0.0.1:5000`.
3. Commit + push.
4. **PythonAnywhere bash:** `cd my_app && git
   pull`.
5. **PythonAnywhere web tab:** Reload.
6. Verify on the public URL.

This is **the real deploy loop.** Do it for every
significant change.

#### Use what you've learned

- **Auth** from Session 9.
- **Multi-table database** from Sessions 10-11.
- **Templates with extends** from Session 4.
- **Forms with POST-Redirect-GET** from Session 5.
- **Flash messages** from Session 6.
- **Per-user data isolation** with `WHERE
  user_id = ?` from Sessions 10-11.

The complete patterns are in Sessions 1-12.

### Wrap-up

Last 5 minutes: each of you, in one sentence,
share **your project idea + your live URL.**
(URL might just show "Hello world" right now —
that's OK.)

Bring your project (code + URL) next week. We'll
finish, then demo.

If you got far, **commit, push, pull, reload**
before next week so the public URL is current.

### If you missed this session

Open Thonny and a terminal.

1. Spend 10-15 minutes answering the nine planning
   questions.

2. Set up your project + GitHub + PythonAnywhere.

3. Build the simplest version (signup + login at
   minimum).

4. Push and deploy.

About 90-120 minutes total. By next week:

- Working signup and login at a public URL.
- At least one feature beyond auth (e.g., a
  list of items the user has created).
- Several Git commits.
- The deploy loop comfortable.

If you don't have an idea, the seed list is your
starting point.

### Stretch and extension ideas

If your base is working and you want to add more:

- **Real CSS polish** (Phase 7 callback).
- **Mobile-responsive design.**
- **Search / filter** for your data.
- **Public + private modes** for content.
- **Multiple data types / tables** —
  relationships.
- **Image uploads.**
- **API endpoints** that return JSON.
- **Email notifications** (advanced).
- **README** with screenshots.
- **Cross-link from your Phase 7 homepage** —
  unified portfolio.

### What's next

Next week is the **last session of the entire
curriculum.** You'll finish, polish, deploy your
final version, and demo to the class.

Bring your laptop. Bring your URL. Bring your
enthusiasm. Last big climb.
