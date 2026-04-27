## Session 11 — Teacher Notes

*Phase 8, Flask · Session 11 of 13 · Title:
Deployment — your Flask app on the internet*

### Purpose of this session

The "back-end goes public" session. Five jobs, in
priority order:

1. **Get every kid's notes app on a real URL.**
   The single most important outcome.
2. **Land "static hosting won't work for Flask."**
   Python needs to run on a server.
3. **Land the PythonAnywhere flow.** Account →
   git clone → WSGI config → install → reload.
4. **Land deploy-via-git-pull.** Update locally,
   push, pull on server, reload.
5. **Set up Sessions 12-13 (milestone).**
   Milestone projects must be deployed.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Mr. Eric's own pre-deployed PythonAnywhere
  notes app — to demo the URL working.
- A walkthrough screenshot or pre-made guide for
  the PythonAnywhere UI (the UI changes
  occasionally — fresh screenshots help).
- Each kid needs their notes app on GitHub
  before class — verify in the days leading up.
- Identify any kids missing GitHub setup or
  whose notes app isn't ready.

**Prep time:** ~45 minutes — pre-deploy a fresh
notes app, document any UI changes, identify
problem kids.

### Timing and flow

Total: ~90 min — possibly tight given setup
overhead.

- **Welcome and recap** (~5 min). Recap Session
  10. "Today: it goes public."
- **Part A: PythonAnywhere account creation** (~10 min).
- **Part A: git clone + web app + WSGI** (~30 min).
- **Part A: install + reload + verify** (~15 min).
- **Break** (~5 min).
- **Part B: production polish** (~15 min).
- **Wrap-up** (~10 min). URL share-around.

If running short, **drop production polish.** The
URL working is the priority.

### Teaching the framing

#### "GitHub Pages won't work"

Open with the contrast:

> "Phase 7 — your sites went on GitHub Pages.
> Free, easy, instant. *But* GitHub Pages is
> *static* — it serves files. Your Flask app
> needs *Python running on a server*. GitHub
> Pages can't do that.
>
> We need a Python *host* — a service where your
> app actually runs. Several options. We'll use
> PythonAnywhere — free, beginner-friendly,
> designed for educators."

#### "PythonAnywhere is the gentlest entry"

Brief landscape:

> "Real production: Render, Fly.io, Railway, AWS,
> DigitalOcean, Heroku (rip free tier). All
> require terminal/CLI familiarity, often
> Docker, often credit cards.
>
> PythonAnywhere has a *web UI* for everything.
> Free tier no credit card. Designed for
> students. *Perfect for class.*
>
> When you grow into bigger apps, you'll
> graduate to other hosts. Today: PythonAnywhere."

### Teaching Part A

#### Account creation

Walk through on the projector. Most kids manage.
The Beginner tier (free) requires:

- Username (becomes part of URL — pick wisely)
- Email
- Password
- Email verification

Some kids may hit:

- Username taken (try variants)
- Verification email delayed (gmail usually
  fast; some school emails slower)
- Already have an account from another class
  (use it)

Have a fallback plan for the kid whose email
verification doesn't arrive.

#### Bash console + git clone

Show the **Consoles** tab. Start a Bash console.

```
$ git clone https://github.com/USERNAME/notes_app.git
```

Verify with `ls`. Walk through the standard "is
the repo public, public URL correct, etc."
checks.

For private repos: PythonAnywhere supports
deploy keys but it's a hassle. Push for public
repos for class.

#### Web app setup

Walk through the wizard:

1. Web tab → Add a new web app.
2. Domain: free option.
3. **Manual configuration** (don't pick "Flask"
   — it's an old setup).
4. Python 3.10 (or latest).

Slow down. UI clicks aren't obvious without
visual guidance.

#### WSGI file editing

This is the trickiest moment. The WSGI file
controls how PythonAnywhere finds your app.

```python
import sys
import os

project_home = "/home/YOUR-USERNAME/notes_app"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.chdir(project_home)

from app import app as application
```

Walk through every line:

- **`project_home`** — must be the *exact* path
  where they cloned. Use their username.
- **`sys.path.insert`** — Python's import path.
  Without it, `from app import app` fails.
- **`os.chdir`** — sets current directory. Why?
  So `sqlite3.connect("notes.db")` finds the DB
  file. (Better fix: absolute path in the
  notes_app — Part B.)
- **`from app import app as application`** —
  imports the Flask app, renames to
  `application` (PythonAnywhere's expected
  name).

Each kid edits *their own* WSGI file with their
own username and project name. Common mistake:
copy-pasting Mr. Eric's username.

#### `pip install --user flask`

In bash console:

```
$ pip install --user flask
```

The `--user` flag is essential. Without it,
PythonAnywhere may complain about permissions.

Some kids' notes apps may need other packages
(e.g., `flask-wtf` if they used WTForms). Each
gets installed similarly.

#### Reload + visit URL

Reload button in Web tab. Wait 5-10 seconds.
Visit the URL.

**The URL working** = the moment of truth.
Common failure modes:

- Error page → "Something went wrong" →
  inspect the error log (link in Web tab).
- 502 Bad Gateway → app crashed on startup,
  see error log.
- 404 → wrong URL, or app didn't bind.

The error log shows traces. Walk through.

#### "Send the URL to your parents"

Some kids will instantly want to. Encourage —
real ownership.

### Teaching Part B

#### Production polish (briefly)

Cover:

- **Real `secret_key`** from env var.
- **Absolute path** for database.
- **`requirements.txt`** for deps.
- **`.gitignore`** for `*.db`.

Frame:

> "Real production polish. Class-version works
> as-is, but these are habits worth forming."

If running short, mention briefly and skip
hands-on for some.

### Common stumbles

- **GitHub repo private.** Public is needed for
  free PythonAnywhere git clone. Make public.
- **Wrong username in WSGI.** Imports fail.
  Fix the path.
- **`from app import app` fails.** Wrong file
  name or path. Check `ls` in the bash
  console, verify `app.py` is in
  `~/notes_app/`.
- **`flask` not installed.** ImportError. `pip
  install --user flask`.
- **DB file path wrong.** SQLite errors. Use
  absolute path (Part B fix).
- **Error log shows secret_key error.** Forgot
  `app.secret_key` in code. Add it.
- **Reload doesn't take effect.** Browser cache.
  Hard reload, or clear and try.
- **First reload takes a long time.** Normal —
  PythonAnywhere wakes the worker.
- **App works once, then errors.** Maybe DB
  file permissions. Check error log.
- **Static files (CSS) 404.** PythonAnywhere
  serves them via the web UI's "Static files"
  section in the Web tab. Set the URL
  `/static/` to map to `/home/USER/PROJECT/static/`.

### Differentiation

- **Younger kids (9-10):** Goal is the URL
  working. Skip Part B polish.
- **Older kids (12+):** Push for Part B basics
  — `secret_key` from env, absolute DB path.
- **Advanced (any age):** Suggest:
  - Try a different host (Render or Fly.io)
  - Custom domain
  - HTTPS-only redirect
  - Logging to file
  - Disable signup (closed app)
- **Struggling:** A kid who can't get the URL
  working is the kid you focus on. Most common
  cause: WSGI typo, or repo on GitHub is
  private/missing.

### What to watch for

- **The "MY URL!" reaction.** Real, big.
- **Buddies signing up for each other's apps.**
  Real multi-user testing. Encourage.
- **Privacy concerns** — apps now have *real*
  signups. Address sensitively. Apps can be
  taken down.
- **Excitement about parents using it.** "Can
  they really sign up?" Yes.
- **Frustration with WSGI.** Expected. Walk
  through patiently.
- **Static files broken.** Common — needs the
  Web tab static-files mapping.
- **Cross-app spam.** Some kids might create
  spam accounts on each other's apps. Address
  if it happens — community-management lesson.
- **Kid asking "what about HTTPS?"**
  PythonAnywhere provides it free at
  `<username>.pythonanywhere.com`. Real.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sessions 12-13 (milestone).** Their
  milestone goes live by demo. Today's deploy
  skill is required.
- **Career-long callback:** real apps deploy.
  Real engineers do this constantly.
  Different hosts, same flow (clone, configure,
  install, run).
- **Phase 7 callback:** their static sites are
  on GitHub Pages. Their Flask apps are on
  PythonAnywhere. Different hosts for different
  needs.
- **Peanut butter callback opportunity:** the
  WSGI typo or wrong-username path is a
  precision moment. Server does what you said,
  not what you meant.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Mr. Eric's example deployed app to demo
- [ ] PythonAnywhere account ready for demo
- [ ] Pre-class email to parents about
      PythonAnywhere account creation (if
      needed for younger kids)
- [ ] Visual walkthrough or screenshots of
      PythonAnywhere UI (UI changes!)
- [ ] List of kids whose notes apps aren't on
      GitHub yet — fix before class
- [ ] Projector
- [ ] Class roster
