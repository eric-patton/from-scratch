# Phase 8 — Flask (web apps)

You can build games. You can build websites. You can
make pages that talk to APIs and store data in the
browser. **Now you build the back-end** — a *server*
that responds to web requests, talks to a database,
manages user accounts, and powers real multi-user
applications.

This is the **last phase** of the curriculum. By the
end, you'll have built apps end-to-end — front-end
(browser) AND back-end (server) — like a real
software engineer.

## What this phase is

Thirteen sessions on building web apps with **Flask**
— a small, beginner-friendly Python web framework.
You'll learn how the browser-server conversation
works, how to handle forms, how to store data in a
real database, how to add user accounts, and how to
deploy your app so it's accessible to anyone with
internet.

## What you'll learn

| Session | Idea | What's new |
|---|---|---|
| 1 | Welcome to Flask — first server | The request/response cycle, install, hello world |
| 2 | Routes and URL parameters | Multiple routes, dynamic URLs |
| 3 | Templates — Jinja2 | Variables, loops, conditionals in HTML |
| 4 | Static files + base templates | CSS, images, template inheritance |
| 5 | Forms and POST requests | `request.form`, GET-then-POST |
| 6 | Sessions and flash messages | `session`, cookies, user feedback |
| 7 | SQLite — your first database | What a database is, the `sqlite3` module |
| 8 | Database in Flask — CRUD | SELECT/INSERT/UPDATE/DELETE in routes |
| 9 | User accounts | Signup, login, logout, password hashing |
| 10 | Build a notes app together | Full-stack integration |
| 11 | Deployment | Real public hosting (PythonAnywhere) |
| 12 | Milestone day 1 | Plan + build your full-stack app |
| 13 | Milestone day 2 + demo | Finish + showcase + curriculum close |

## What you'll build

- **Sessions 1-6:** small Flask apps — greetings,
  page-per-route sites, form handlers, simple games.
- **Sessions 7-9:** apps with persistent data and
  user accounts.
- **Session 10:** **a multi-user notes app** — auth,
  database, full UI. Built as a class.
- **Session 11:** deploy that app to a public URL
  with real users (you and your classmates).
- **Sessions 12-13:** *your* full-stack milestone —
  your design, deployed, anyone can sign up and use.

## What you'll need

- **Python 3** — already installed on your machine
  from Phase 3.
- **Flask** — we'll install in Session 1:
  ```
  $ pip install flask
  ```
- **`sqlite3`** — built into Python.
- **A browser** for testing.
- **Thonny** for editing.
- **A PythonAnywhere account** by Session 11 — free,
  set up together.

## How sessions work

Same shape as before:

- **Part A** introduces a concept with a guided
  exercise.
- **Part B** is open practice or a project.
- **Wrap-up** to share what you did.

## How the back-end is different

A few key shifts:

### The server runs your code

In Phase 7, JavaScript ran in the **browser** —
on the user's computer. In Phase 8, Python runs on
the **server** — your code (or, eventually, a code
running in the cloud). Different runtime, different
mental model.

### Multiple users hit your code

A static page served by GitHub Pages handles
millions of visitors with no special logic — every
visitor sees the same files. A Flask app *runs your
Python* on every request, so different users can see
*different things*. Personalized pages. Logins. Per-
user data. Real apps.

### Data lives in a database

In Phase 7, browser localStorage held data — but
*per-user, per-browser*. No sharing. No
multi-device. No history.

A real database stores data centrally. A user logs
in from any device, their data follows. Multiple
users share a system. Real persistence.

### URLs become functions

`@app.route("/about")` says "when someone visits
`/about`, run *this Python function* and return what
it produces." Routes are the bridge between web URLs
and your code.

### What's the same

- **Python.** All your Phase 3-4 + Phase 6 Python
  knowledge applies. Flask is just a library.
- **HTML and CSS.** Phase 7. Templates produce HTML.
- **Forms, JavaScript (optional).** You can mix
  Phase 7 front-end skills into Flask templates.
- **Git + GitHub.** For source control, as before.

## What we're skipping

- **SQLAlchemy / ORMs.** Real production tools, but
  abstract away what's happening. We'll write *raw
  SQL* — clearer for learning.
- **Blueprints, Flask extensions.** Beyond the
  beginner needs.
- **Async (asyncio).** Out of scope.
- **REST API design** as a topic. We'll touch JSON
  responses but not formal REST.
- **Docker, Kubernetes, microservices, CI/CD
  pipelines.** Real production has all of this.
  We're learning Flask itself first.
- **Testing.** Phase 4 covered testing. Adding it
  to Flask is a natural next step but out of phase
  scope.

If you want to learn any of those after the
curriculum, the foundation here makes it much
easier.

## A note about pacing

Phase 8 has **fewer "wow" moments per session** than
Phases 6-7 because the back-end is *plumbing*. The
visible result is often the same — but what's
*behind* the page is fundamentally different.

The big payoffs:

- **Session 5** (forms working) — the first time
  the user *changes data on the server*.
- **Session 7** (database) — your first real
  persistent data.
- **Session 9** (user accounts) — "I have my own
  account on a thing I built."
- **Session 11** (deployment) — your friends can
  sign up and use it.

Push through Sessions 1-4 — they're foundation.
Sessions 5+ are when it gets exciting.

## Where to start

[Session 1: Welcome to Flask](session-01-welcome.md)
sets up your first server.

When you're stuck, the [Getting unstuck](../appendices/getting-unstuck.md)
appendix is the first place to go. The
[Glossary](../appendices/glossary.md) will grow as
Phase 8 introduces back-end terms.

Welcome to the back-end. Last phase. Let's go.
