## Session 14: Milestone day 2 + demo + curriculum close

*Phase 8 — Flask · Session 14 of 14 — last
session of the entire curriculum*

### What we're learning today

This is **the last session.** Eight phases. Eight
milestones. Today: finish your full-stack app,
deploy your final version, demo your **live URL**
to the class. Your classmates sign up. Your work
is on the internet for real.

Then we close out the journey.

### You'll need to remember from last time

- **Your project plan** from last week.
- **Your deployed URL.**
- **Git push + PythonAnywhere reload** for
  updates.
- **Everything from Phases 1-8.**

---

### Part A: Final polish

You have about 35 minutes to finish.

#### What "finished" means

Same three rules as always:

1. **It runs without crashing** under normal use.
2. **It does what your plan said** — at least
   the simplest version.
3. **You can explain how it works.**

#### Phase 8-specific polish

- **Verify the live URL works.** Push, pull,
  reload, visit. Don't assume.
- **Test signup as a fresh user.** From your
  phone, or a different browser, or incognito
  mode.
- **Check error log** on PythonAnywhere — any
  errors? Fix.
- **Test on a phone if you can.**
- **Window title** — `<title>` tag.
- **Real `secret_key` from env var** if you
  want production polish.
- **`.gitignore`** for `*.db` so production
  data isn't in your repo.
- **README on the repo** with description,
  live URL, screenshots if you have them.
- **All committed and pushed.** `git status`
  should say "working tree clean."
- **Pulled and reloaded on PythonAnywhere.**

#### Buddy test

About 15 minutes in: **swap URLs with your
buddy.** They sign up on your app. They use it.
You do the same.

For Phase 8 specifically: your buddy is now a
*real user* of your *real app*. Their data
joins yours in the same database. **Real
multi-user testing.**

Notice things they get wrong (control
confusion, unclear next step). Real UX.

**Checkpoint:** *Your project runs at a live
URL, your buddy signed up successfully and
used it.* **This is the natural stop point if
class is cut short — but today, demo time is
next.**

---

### Part B: Demo day + curriculum close

Each person gets **5-7 minutes** (longer than
usual — last demo).

#### How a demo works

When it's your turn:

1. **Show your URL.** Open it on the projector.
2. **Sign up live** as Mr. Eric (or someone
   else fresh).
3. **Use your app.** Walk us through what it
   does.
4. **Have a classmate sign up on their
   machine** during your demo.
5. **Show your repo.** GitHub URL, `git log`.
6. **Tell us about it.** What it is, who it's
   for, what was hard.
7. **Show the database** if you can (DB
   Browser locally, or a screenshot).
8. **One question from the audience.**

For your last demo: take your time. **You built
something real.**

#### After everyone demos

Mr. Eric will say specific things about each
project. Then **we close out the curriculum.**

### What you accomplished — this phase

- **A full-stack web app.** Auth + database +
  templates + UI.
- **Deployed to a public URL.** Real users
  signed up.
- **Eighth milestone shipped.**

### What you accomplished — the whole curriculum

Let's count.

You shipped **eight projects** across **eight
phases.** Most adults have shipped *zero.* You
have eight. Three of them are **on the
internet.**

The phases:

1. **Scratch** — visual programming. Sequences,
   loops, events, conditionals, variables.
2. **Python Turtle** — typing instead of
   dragging. Functions. Same ideas, real
   syntax.
3. **Python basics** — strings, lists, dicts,
   files, error handling. The full beginner
   Python.
4. **Intermediate Python + CLI + Git** —
   multi-file programs, classes, version
   control, testing.
5. **customtkinter** — desktop GUIs. Real apps
   with windows, buttons, forms.
6. **Pygame** — 2D games. Frame loop, sprites,
   collisions, sound, your custom grid-world.
7. **HTML/CSS/JavaScript** — the front-end. The
   browser as runtime.
8. **Flask** — the back-end. Python on a
   server. Multi-user apps.

You've covered:

- **Three programming languages** — Python,
  JavaScript, plus HTML/CSS as markup
  languages.
- **Three runtimes** — desktop (Pygame,
  customtkinter), browser (HTML/JS), server
  (Flask).
- **Real software engineering practice** —
  Git, GitHub, deployments, multi-file
  organization, testing.
- **Real security practice** — password
  hashing, parameterized queries, per-user
  data isolation.
- **Design patterns** that show up in *every*
  app you'll ever build.

You're a **real software engineer.** Not yet
expert — but you have the foundation. From here,
every framework, every language, every
specialty is *more learning on top of solid
ground.*

### What's next?

This curriculum is over. **Your career as a
programmer is just starting.**

Some directions to consider:

#### Keep building

The projects you built are *yours.* Keep
adding to them. Add features. Polish. Share
with more people.

The single best way to grow as a programmer is
**building things you care about.** Pick a
problem in your life. Build a tool that fixes
it. Repeat.

##### A few seed projects to try this week

If you want a concrete next step (and momentum
this week, while everything is fresh), pick one
of these:

- **A habit tracker.** Like the notes app, but
  tracks *streaks* — every day you check off "I
  did the thing," and the longest current
  streak is shown. New table: `checkins`. Same
  per-user filter, same auth.
- **A reading log.** Title, author, date
  finished, rating, notes. List. Sort by date
  or rating.
- **A bookmark manager.** Save URLs with tags.
  Search by tag.
- **Extend one of your milestones.** Pick the
  milestone you're proudest of and add *one*
  feature you wished you'd had time for.
- **A tiny tool you actually need.** A timer
  for chores, a calculator for something
  specific to your life, a checklist for your
  morning routine. *Real things you'd use.*
- **Port a Phase 6 game to JavaScript.** Phase
  7 Sessions 12-13 covered Canvas. Take your
  Pygame milestone and rebuild it in the
  browser, where anyone can play.
- **An API + a front-end.** Build a Flask app
  that returns JSON, and a Phase-7-style HTML
  page that uses `fetch` to load and display
  the data. Real full-stack, your design.

Pick one. Build the simplest version this
weekend. Send Mr. Eric the URL when it works.

#### Contribute to open source

Browse [github.com](https://github.com). Find
projects you use (Pygame, Flask, anything).
Read the README. Look at issues. Try fixing
one.

Open-source contribution is **how real
programmers learn from each other.** Free
education at any level.

#### Learn a framework

JavaScript: try **React** or **Vue.** Browser
apps with rich UIs.

Python: try **Django** (bigger than Flask,
more "batteries included") or **FastAPI**
(modern API framework).

The patterns you learned here transfer.
Frameworks add structure on top.

#### Pick a specialty

Some directions real engineers go:

- **Web dev** (front-end, back-end, full-stack)
  — what we did.
- **Mobile** (iOS with Swift, Android with
  Kotlin, cross-platform with React Native or
  Flutter).
- **Game dev** (Unity, Godot, Unreal — bigger
  than Pygame, but the same mental model).
- **Data science / ML** (Python continues —
  pandas, NumPy, scikit-learn, PyTorch).
- **Systems** (Rust, C, Go — closer to the
  metal).
- **DevOps / Cloud** (AWS, Docker, Kubernetes
  — running things at scale).

You don't have to pick now. Try things. See
what excites you.

#### Learn things outside programming

The best programmers know things *besides*
programming. Math, design, music, writing,
biology, history — anything you care about
makes you a better engineer of solutions in
that domain.

Being good at code AND good at one other thing
beats being just good at code.

#### Read code

Real projects on GitHub. Frameworks. Open-
source tools. **Reading code is how you learn
to write better code.**

You can read any of them. *That's the magic of
the web.*

#### Stay curious

The single thing every great engineer has in
common: **curiosity.** Why does this work? How
does that work? What would happen if I changed
this?

If you stay curious, you'll be a programmer
for life.

### A note from Mr. Eric

You did the work. You showed up week after
week. You built when it was hard. You shipped
when it was scary. You demoed when you were
nervous.

**You earned this.**

Whatever you build next, remember: every
expert was once a beginner. The best engineers
in the world started where you are. The only
difference is they kept building.

Keep building.

### What's next (literally)

There's no formal "Phase 9." This is the end of
the From Scratch Programming Class.

But programming has no end. You can:

- Keep extending your milestone projects.
- Pick a new project from the seed lists.
- Read MDN, Real Python, Pygame docs, Flask
  docs.
- Watch tutorials on YouTube (lots of free,
  high-quality content).
- Help a friend learn to code — **teaching is
  the best way to deepen what you know.**

If you ever want to come back and ask Mr.
Eric a question — about code, about a
project, about what to learn next — **come
back.**

### Final note

You're a programmer.

Welcome.
