## Session 9: User accounts — signup, login, logout

*Phase 8 — Flask · Session 9 of 13*

### What we're learning today

You have a database. You have sessions. Today they
combine into **user accounts** — signup, login,
logout, and the holy "I have my own account on a
thing I built" moment. You'll also learn the
critical security rule: **never store plaintext
passwords.** By the end of class your app will let
multiple people sign up, log in, and stay logged
in across visits.

### You'll need to remember from last time

- **Sessions** — `session["key"] = value`
  (Session 6).
- **SQLite + Flask** — `get_db`, `init_db`,
  parameterized queries (Session 8).
- **Forms** — POST with validation (Session 5).
- **Flash messages** — for "logged in" / "wrong
  password" feedback (Session 6).

---

### Part A: Password hashing — the critical rule

#### Never store plaintext passwords

The single most important security rule of web
development:

> **Never store passwords as plain text.**

If your database is ever leaked (data breach,
hacker, careless backup), every password is exposed
— and many users reuse passwords across sites. *Your
breach becomes their bank's breach.*

The fix: store a **hash** of the password, not the
password itself.

#### What's a hash?

A **hash function** takes input → outputs a
fixed-length scrambled string. Two key properties:

- **One-way.** You can't compute the input from
  the hash.
- **Deterministic.** Same input → same hash, every
  time.

So when a user signs up, you hash their password
and store the hash. When they log in, you hash
what they typed and compare to the stored hash —
match means correct password.

**You never need to know the original password.**
And neither does an attacker who steals the
database.

#### Use `werkzeug.security`

Flask ships with `werkzeug` (a related library)
that has secure password helpers. Use them.

```python
from werkzeug.security import generate_password_hash, check_password_hash

# When signing up:
password_hash = generate_password_hash("my_password")
# Store password_hash in the database, NOT "my_password"

# When logging in:
if check_password_hash(stored_hash, "what_user_typed"):
    # correct password
else:
    # wrong password
```

`generate_password_hash` produces a long string
like:

```
scrypt:32768:8:1$abc...
```

Includes the algorithm, salt, and hash. Self-
contained. Just store it.

`check_password_hash` parses it, hashes the input
the same way, compares, returns True/False.

**Don't** roll your own hashing. Use these
functions. Production-grade security in two lines.

#### Try it

Open the Python shell:

```python
>>> from werkzeug.security import generate_password_hash, check_password_hash
>>> h = generate_password_hash("hello")
>>> h
'scrypt:32768:8:1$...long string...'

>>> check_password_hash(h, "hello")
True
>>> check_password_hash(h, "Hello")
False
>>> check_password_hash(h, "")
False
```

The hash changes every time (because of random
salt), but `check_password_hash` matches correctly
each time:

```python
>>> generate_password_hash("hello") == generate_password_hash("hello")
False
>>> # Different hashes — but both match "hello"
```

This is how passwords work everywhere on the
internet.

**Checkpoint:** *You understand why we hash
passwords and how to use the two werkzeug
functions.* **This is the natural stop point if
class is cut short.**

---

### Part B: Build the auth flow

Time to build it. We'll add `users` to a Flask app
with signup, login, and logout.

#### Project structure

```
auth_app/
├── app.py
├── auth.db
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── signup.html
│   └── login.html
└── static/
    └── style.css
```

#### `app.py` — full code

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "dev-secret"

def get_db():
    conn = sqlite3.connect("auth.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

def current_user():
    """Returns the logged-in user row, or None."""
    user_id = session.get("user_id")
    if not user_id:
        return None
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    conn.close()
    return user

@app.context_processor
def inject_user():
    """Make `current_user` available in all templates."""
    return {"current_user": current_user()}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        
        if not username or not password:
            flash("Both fields required.", "error")
        elif len(password) < 4:
            flash("Password must be at least 4 characters.", "error")
        else:
            conn = get_db()
            try:
                conn.execute(
                    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                conn.commit()
                conn.close()
                flash(f"Account created! Please log in.", "success")
                return redirect(url_for("login"))
            except sqlite3.IntegrityError:
                conn.close()
                flash("Username already taken.", "error")
    
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        
        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()
        
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password.", "error")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out.", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
```

That's the *full auth system.* Walk through key
pieces:

- **`UNIQUE` on the `username` column** — the
  database refuses duplicates. We catch
  `sqlite3.IntegrityError` to tell the user.
- **`current_user()` helper** — reads
  `session["user_id"]`, looks up the user, returns
  the row (or None if not logged in).
- **`@app.context_processor`** — makes
  `current_user` automatically available in every
  template. No need to pass it from each route.
- **Login flow** — find user, check_password_hash,
  set session.
- **Logout** — clear the session key.

#### Templates

`templates/base.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <a href="{{ url_for('home') }}">Home</a>
            {% if current_user %}
                <span>Logged in as <strong>{{ current_user.username }}</strong></span>
                <a href="{{ url_for('logout') }}">Log out</a>
            {% else %}
                <a href="{{ url_for('login') }}">Log in</a>
                <a href="{{ url_for('signup') }}">Sign up</a>
            {% endif %}
        </nav>
    </header>
    
    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% for category, msg in messages %}
            <div class="flash flash-{{ category }}">{{ msg }}</div>
            {% endfor %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

The nav switches between "log in / sign up" and
"logged in as X / log out" based on
`current_user`. **The base template handles auth
display universally.**

`templates/home.html`:

```html
{% extends "base.html" %}
{% block content %}
{% if current_user %}
    <h1>Welcome, {{ current_user.username }}!</h1>
    <p>You are logged in.</p>
{% else %}
    <h1>Welcome!</h1>
    <p>Please <a href="{{ url_for('login') }}">log in</a>
       or <a href="{{ url_for('signup') }}">sign up</a>.</p>
{% endif %}
{% endblock %}
```

`templates/signup.html`:

```html
{% extends "base.html" %}
{% block title %}Sign up{% endblock %}
{% block content %}
<h1>Sign up</h1>
<form method="post">
    <label>Username: <input type="text" name="username" required></label>
    <label>Password: <input type="password" name="password" required></label>
    <button type="submit">Create account</button>
</form>
{% endblock %}
```

`templates/login.html`:

```html
{% extends "base.html" %}
{% block title %}Log in{% endblock %}
{% block content %}
<h1>Log in</h1>
<form method="post">
    <label>Username: <input type="text" name="username" required></label>
    <label>Password: <input type="password" name="password" required></label>
    <button type="submit">Log in</button>
</form>
{% endblock %}
```

Note `<input type="password">` — browsers show
dots instead of letters.

Save everything. Run.

#### Test the flow

1. Visit `/`. **"Welcome! Please log in or sign
   up."**
2. Click sign up. Pick a username and password.
3. Submit. **"Account created! Please log in."**
4. Click log in. Use the same credentials.
5. Submit. **"Welcome back, alex!"** — and the
   nav shows "Logged in as alex" with a Log out
   button.
6. Visit `/`. **"Welcome, alex!"**
7. Log out. Back to "stranger" state.
8. Try to log in with the wrong password. **"Invalid
   username or password."**
9. Try to sign up with the same username again.
   **"Username already taken."**

**You have a working auth system.** Real signup,
real login, real password hashing.

#### Inspect the database

Open `auth.db` in DB Browser for SQLite (Session 7
stretch). Look at the `users` table. **The
password_hash column is gibberish** — long encoded
strings. Even if someone steals the database, the
passwords are protected.

#### Stretch — protect routes (require login)

Often you want certain routes to require login.
Pattern:

```python
@app.route("/secret")
def secret():
    if not current_user():
        flash("Please log in.", "error")
        return redirect(url_for("login"))
    return "Top secret content!"
```

A decorator makes this cleaner:

```python
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user():
            flash("Please log in.", "error")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

@app.route("/secret")
@login_required
def secret():
    return "Top secret content!"
```

Apply `@login_required` to any route — it's
auto-protected.

#### Stretch — "Remember me" with session lifetime

```python
from datetime import timedelta

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # ... existing logic ...
        if user and check_password_hash(...):
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=30)
            session["user_id"] = user["id"]
            ...
```

Now sessions last 30 days even after browser
close.

#### Stretch — change password

A new route — must be logged in, must verify old
password:

```python
@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        old = request.form.get("old_password")
        new = request.form.get("new_password")
        user = current_user()
        
        if not check_password_hash(user["password_hash"], old):
            flash("Wrong current password.", "error")
        else:
            conn = get_db()
            conn.execute(
                "UPDATE users SET password_hash = ? WHERE id = ?",
                (generate_password_hash(new), user["id"])
            )
            conn.commit()
            conn.close()
            flash("Password changed.", "success")
            return redirect(url_for("home"))
    
    return render_template("change_password.html")
```

#### Extension — email field, password reset

Real apps include an email column for password
reset. Out of session scope (involves sending
email — needs SMTP setup), but mention as the
next step.

#### Extension — admin role

Add an `is_admin` column. Some routes only allow
admins:

```python
if not current_user() or not current_user()["is_admin"]:
    abort(403)
```

The basis of any role-based system.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your signup / login flow
  working. Try wrong password — does it fail
  cleanly?
- Did inspecting `password_hash` in the database
  drive home why we hash?
- For the kids who tried `@login_required` —
  does the decorator pattern feel powerful?
- Anyone notice that you can have *multiple
  accounts* in the same database now?

Today you learned:

- **Never store plaintext passwords.** Always
  hash.
- **`werkzeug.security`** has the right
  functions: `generate_password_hash` and
  `check_password_hash`.
- **The `users` table** with username,
  password_hash, created_at.
- **`UNIQUE` constraint** on username — database
  prevents duplicates.
- **Signup → hash and INSERT.**
- **Login → SELECT user, check_password_hash,
  set `session["user_id"]`.**
- **Logout → `session.pop`.**
- **`current_user()` helper** + context processor
  for templates.
- **`@login_required` decorator** to protect
  routes.

You can build any **multi-user app** now. The
auth pattern is universal.

Next week: **the notes app** — combine auth +
database + templates + forms into one complete
multi-user web app. The full-stack moment.

### If you missed this session

Open Thonny.

1. Build the full `app.py` from Part B.

2. Build all four templates.

3. Test the signup → login → logout flow.

4. Inspect `auth.db` to see hashed passwords.

5. (Stretch) Add `@login_required`.

About 60-90 minutes — this is a substantial
session.

### Stretch and extension ideas

- **`@login_required` decorator** for protecting
  routes.
- **Permanent sessions** with custom lifetime.
- **Change password** route.
- **Username availability check** via fetch (Phase
  7 callback) before submit.
- **Account deletion** (with password
  confirmation).
- **Email field** for future password reset.
- **Role / admin** column.
- **Last login timestamp** on the users table.
- **Force HTTPS** in production (configuration —
  out of session scope but real concern).

### What's next

Next week: **build a notes app together** — the
full-stack integration. Auth + database +
templates + forms = a real multi-user app where
each user has their own private notes. Phase 5
and Phase 7 had todo apps; Phase 8 makes them
*multi-user*.
