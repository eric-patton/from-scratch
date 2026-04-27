## Session 12: Deployment — your Flask app on the internet

*Phase 8 — Flask · Session 12 of 14*

### What we're learning today

Your notes app runs on `127.0.0.1:5000` — only
**your computer** can reach it. Today we put it
**on the internet** — at a real public URL where
anyone with the link can sign up and use it. We'll
deploy to **PythonAnywhere** — a free hosting
service designed for Python apps. By the end your
notes app will be at a `<username>.pythonanywhere.com`
URL.

This is the moment your back-end becomes *public*.

### You'll need to remember from last time

- **The notes app** from Sessions 10-11 (or any
  Flask app you want to deploy).
- **Git basics** — clone, push.
- **PythonAnywhere account** (we'll create one
  today).

---

### Part A: Deploy the notes app

#### Why PythonAnywhere?

Static sites (Phase 7) deploy to GitHub Pages —
no server needed. **Flask apps need a running
Python process**, which GitHub Pages can't do.

We need a **Python hosting service.** Options:

- **PythonAnywhere** — free tier, no credit card,
  designed for educators. Easy web UI. *Our
  pick.*
- **Render** — generous free tier, modern. But
  needs more terminal/command-line.
- **Railway, Fly.io, Vercel** — varies.

PythonAnywhere is the kindest entry point for
beginners.

#### Step 1 — Create an account

1. Go to **pythonanywhere.com**.
2. Click **Pricing & signup.**
3. Pick the **"Beginner" account** (free).
4. Fill in username + email + password.
5. Verify your email.

Your username becomes part of your URL:
`<username>.pythonanywhere.com`. Pick something
you're OK with for years.

#### Step 2 — Get your code on PythonAnywhere

There are two ways: upload a zip, or `git clone`
from GitHub. **Git clone is the right way** —
keeps your code in sync.

If your notes app isn't on GitHub yet:

1. Push it to GitHub (Phase 6 Session 7
   refresher).

In PythonAnywhere:

1. Click the **Consoles** tab.
2. Start a **Bash console.**
3. In the console:
   ```
   $ git clone https://github.com/YOUR-USERNAME/notes_app.git
   ```
4. `cd notes_app` and `ls` to verify your files
   are there.

#### Step 3 — Set up the web app

1. Click the **Web** tab.
2. Click **Add a new web app.**
3. Click **Next** through the domain setup
   (free accounts get
   `<username>.pythonanywhere.com`).
4. **Pick "Manual configuration"** (not "Flask"
   — the auto-Flask option is for old setups).
5. **Pick Python 3.10** (or the latest available).
6. Click **Next.**

Now you're on the configuration page for your
web app.

#### Step 4 — Configure WSGI

This is the trickiest step. Find the **Code
section** with **"WSGI configuration file."**
Click the link to edit it.

Replace its contents with:

```python
import sys
import os

# Update this to your username and project folder
project_home = "/home/YOUR-USERNAME/notes_app"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.chdir(project_home)

from app import app as application
```

Walk through:

- **`project_home`** — where your code lives on
  PythonAnywhere. Replace `YOUR-USERNAME` with
  your PythonAnywhere username.
- **`sys.path.insert(0, project_home)`** — tells
  Python where to find your app.
- **`os.chdir(project_home)`** — so SQLite finds
  the DB file in the right folder.
- **`from app import app as application`** —
  imports your Flask app. PythonAnywhere expects
  the app to be called `application`.

Save the WSGI file.

#### Step 5 — Install Flask in PythonAnywhere

In the Bash console:

```
$ pip install --user flask
```

The `--user` flag installs to your user directory
(no system permission needed).

#### Step 6 — Reload the web app

Back in the **Web** tab, scroll up. Click the big
green **Reload** button.

Wait 5-10 seconds.

#### Step 7 — Visit your URL

The URL is shown at the top of the Web tab —
`<username>.pythonanywhere.com`. Click it.

**Your notes app loads.**

Sign up. Log in. Create a note. **Real public
URL.** Send the link to a friend — they can sign
up too.

**You shipped a real multi-user web app to the
internet.**

#### What about updates?

When you change your code locally:

1. Commit and push to GitHub.
2. On PythonAnywhere, in the bash console:
   ```
   $ cd notes_app
   $ git pull
   ```
3. In the Web tab, click **Reload.**
4. Visit the URL — change is live.

A bit more manual than GitHub Pages (which
auto-deploys on push), but workable.

#### When your URL doesn't load

Real talk: deployments break. The first time you
deploy a Flask app, *most* of you will hit *some*
error. That's normal. The fix is always the same
two-step move: **find the error message, fix
what it says.**

**Step 1 — find the error log.** PythonAnywhere
keeps one for every web app. In the **Web** tab,
scroll to the **"Log files"** section. Click the
**"Error log"** link. The most recent entries are
at the bottom. The actual problem is usually in
the *last few lines* — Python's traceback.

**Step 2 — read the last line of the traceback.**
That's the actual error. Common ones:

- **`ModuleNotFoundError: No module named 'flask'`**
  → You skipped `pip install --user flask` (Step
  5 above). Run it. Reload.
- **`ModuleNotFoundError: No module named 'app'`**
  → Your WSGI file's `project_home` path is
  wrong. Fix the path. Reload.
- **`No such file or directory: 'notes.db'`** →
  SQLite can't find your database file. The fix
  is the absolute-path trick from Part B
  (`os.path.join(os.path.dirname(__file__),
  "notes.db")`). Push, pull, reload.
- **`Something went wrong :-(` with no traceback.**
  → The Python version mismatch (you picked
  Python 3.10 in setup but PythonAnywhere
  defaulted to a different one in the Web tab).
  Check the **"Python version"** dropdown in
  the Web tab.

**Step 3 — fix it locally first.** Don't edit code
on PythonAnywhere directly. Edit on your own
machine (where you can test), commit, push,
`git pull` on PythonAnywhere, reload. Always.

> **Two more callbacks for "did you forget?"** —
> *Did you push your latest commit to GitHub?*
> Did you `git pull` on PythonAnywhere after?
> Did you click **Reload** in the Web tab? All
> three are required for your changes to show
> up. Forgetting any one of them is the most
> common deploy frustration.

You'll get fast at this loop with practice. Real
production engineers do this exact dance every
day.

**Checkpoint:** *Your notes app is at a public
URL. Anyone can sign up.* **This is the natural
stop point if class is cut short. (Today's
goal.)**

---

### Part B: Make it production-ready (basics)

#### Set a real `secret_key`

Your local `app.secret_key = "dev-secret"` is
*fine* for class but ridiculous for production.
Use an environment variable:

```python
import os

app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")
```

In PythonAnywhere, set the env var. In the
**Files** tab, edit `~/.bashrc` and add:

```
export SECRET_KEY="some-long-random-string"
```

Or (PythonAnywhere-specific) in the Web tab,
scroll to **Environment variables** and add it
there.

For class: optional polish. Real apps require it.

#### Update the database file path

Your `sqlite3.connect("notes.db")` uses a
relative path. PythonAnywhere may run from a
different directory. Use an absolute path:

```python
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "notes.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
```

`__file__` is the current Python file's path.
`os.path.dirname(__file__)` is its folder. Joining
with "notes.db" gives a full path.

This *just works* regardless of working
directory.

#### Add a real `requirements.txt`

A standard Python file listing your dependencies.
Create `requirements.txt`:

```
Flask
```

(Just one line for now. Real apps list every
package.)

Then on PythonAnywhere:

```
$ pip install --user -r requirements.txt
```

Installs everything in the file. Real-project
practice.

#### Add a `.gitignore`

You shouldn't commit the database file (it has
production data) or `__pycache__`:

`.gitignore`:

```
*.db
__pycache__/
.env
```

If you've already committed `notes.db`, remove
it from Git tracking:

```
$ git rm --cached notes.db
$ git commit -m "Stop tracking db"
$ git push
```

Now the database stays on PythonAnywhere only —
not in your GitHub repo.

#### Stretch — turn off debug mode

In production:

```python
if __name__ == "__main__":
    app.run(debug=False)
```

Debug mode shows error tracebacks to users —
*never* in production. PythonAnywhere ignores
your `app.run()` (it uses WSGI), so this is
fine for class. Still good practice.

#### Stretch — disable signup

If you don't want random people signing up to
your app, comment out the signup route or add
an invite-code check.

#### Stretch — share with your class

Each student deploys. Pass URLs around. Sign up
on each other's apps. **Real users for real
apps.**

#### Stretch — log to a file

For debugging deployed issues:

```python
import logging
logging.basicConfig(filename="app.log", level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home accessed")
    return ...
```

In PythonAnywhere, view the log file in the
Files tab. Real production debugging.

#### Extension — custom domain

If you have a domain (~$10/year), you can point
it at your PythonAnywhere app. Free tier
supports it. **Out of class scope** — but
worth knowing.

#### Extension — try other hosts

For curiosity, try **Render** or **Fly.io**.
Each has a free tier. Different deployment
flow (more git-based, less UI). Real-world
practice.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — **show your URL.** Open it on
  the projector. Sign up, create a note.
- Have a classmate visit your URL on their
  machine. **Two-person test of your app.**
- Did the deploy feel like a *moment*? Your
  back-end is on the internet now.
- For the kids who set up their `.gitignore`
  and absolute paths — was the polish worth
  it?

Today you learned:

- **Static hosting (GitHub Pages) doesn't work
  for Flask** — needs a running Python process.
- **PythonAnywhere** — free Python hosting for
  beginners.
- **WSGI file** — tells the host how to find
  your app.
- **`--user` install** for dependencies.
- **`git pull` + Reload** for updates.
- **Absolute paths** (`__file__`-based) for
  database files.
- **`.gitignore`** to keep db files out of Git.
- **Environment variables** for secrets.
- **`requirements.txt`** for dependency tracking.

Your back-end is on the internet. Anyone with
the URL can sign up and use your app. That's
**real shipping.**

Next two weeks: **your milestone full-stack
app.** Your design, your code, your URL.

### If you missed this session

Sign up at pythonanywhere.com. Then:

1. Push your notes app to GitHub if you haven't.

2. In PythonAnywhere bash console: `git clone`
   your repo.

3. Add a new web app (Manual configuration,
   Python 3.10).

4. Edit the WSGI file to point at your folder
   and import your `app`.

5. `pip install --user flask`.

6. Reload the web app.

7. Visit the URL.

About 45-60 minutes. By the end you should have
a public URL.

### Stretch and extension ideas

- **Real `secret_key` from env var.**
- **Absolute path for DB.**
- **`requirements.txt` with all deps.**
- **`.gitignore`** for `*.db`, `__pycache__/`.
- **Disable debug** in production.
- **Logging to a file.**
- **Custom domain** (if you own one).
- **Try Render or Fly.io** for comparison.
- **HTTPS only** redirect.

### What's next

Next two weeks are *yours.* You plan and build a
**full-stack milestone** — your design, your
data, your users. By Session 14's demo, your app
will be at a real URL anyone in the world can
visit.

Bring an idea. Or come empty-handed — we'll have
a seed list.
