## Session 6: Sessions and flash messages

*Phase 8 — Flask · Session 6 of 13*

### What we're learning today

The HTTP protocol is **stateless** — every request is
independent. The server has no idea this is the same
visitor as a moment ago. **Sessions** fix that:
Flask stores a tiny encrypted cookie in the browser
that lets your code remember things across requests.
**Flash messages** are a one-shot variant — show a
notification on the next page load, then forget. By
the end of class your guestbook will greet returning
visitors by name and confirm their submissions.

### You'll need to remember from last time

- **Forms and POST** — `request.form`, the
  POST-Redirect-GET pattern.
- **Templates** — `render_template`, `{{ }}`,
  `{% if %}`.
- **Python dictionaries** — `session` works like
  one.

---

### Part A: Sessions

#### What's a session?

A **session** is the server's memory of *who's
visiting right now.* Implemented via cookies — the
server gives the browser a small encrypted token,
the browser sends it with every request, the server
decodes it and knows "this is the same visitor."

In Flask, the `session` object **looks like a
dictionary** but persists across requests for a
single visitor.

```python
session["name"] = "Alex"        # save
greeting = session.get("name")   # load on next request
session.pop("name", None)         # delete
```

#### Set up a SECRET_KEY

For Flask to sign session cookies (so they can't be
tampered with), you need a **secret key.** Add to
`app.py`:

```python
app = Flask(__name__)
app.secret_key = "change-me-to-anything-random"
```

For real apps, this should be a long random string,
loaded from a config file or environment variable
— *not* checked into Git. For class, any string
works.

#### Try it — remember a visitor

Open Thonny. Save as `app.py`:

```python
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect(url_for("home"))
    
    name = session.get("name")
    return render_template("home.html", name=name)
```

`templates/home.html`:

```html
<!DOCTYPE html>
<html>
<head><title>Home</title></head>
<body>
    {% if name %}
        <h1>Welcome back, {{ name }}!</h1>
        <p><a href="/logout">Forget me</a></p>
    {% else %}
        <h1>Hello, stranger.</h1>
        <form method="post">
            <label>Your name: <input type="text" name="name" required></label>
            <button type="submit">Remember me</button>
        </form>
    {% endif %}
</body>
</html>
```

Add a logout route:

```python
@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("home"))
```

Save. Run. Visit `/`. **You're greeted as a
stranger.** Type your name. Submit.

**Now reload the page.** You're greeted by name.
**Close the tab.** Reopen. **Still greeted by
name** (within the session lifetime).

That's a session. The server remembers you between
requests.

Click "Forget me" → session cleared → back to
"stranger."

#### Inspect the cookie

Open DevTools → Application → Cookies. You see a
`session` cookie with an encoded value. Click it
— the value is gibberish. **That's the encrypted
session.**

If someone tampered with this value, Flask would
reject it (because the signature wouldn't match).
That's why the SECRET_KEY matters.

#### Sessions are *per browser*

Sessions are stored as cookies, so each *browser*
has its own session. Open a different browser (or
incognito) — you're a fresh visitor. **The session
isn't user accounts** (those come in Session 9);
it's just "this specific browser."

**Checkpoint:** *Your app remembers a visitor's name
across page loads via the session.* **This is the
natural stop point if class is cut short.**

---

### Part B: Flash messages

#### The need

After a form POST, you redirect (Session 5 pattern).
But how do you tell the user "Got it!" on the next
page? You can't put it in the URL (ugly). You can't
put it in `request` (that's the *next* request).
You can use the session — but you'd have to clear
it manually.

**Flash messages** are the solution: store a
one-shot message, displayed on the next request,
auto-cleared after.

#### `flash` and `get_flashed_messages`

```python
from flask import flash

@app.route("/submit", methods=["POST"])
def submit():
    # ... process ...
    flash("Saved!")
    return redirect(url_for("home"))
```

In any template (usually base.html):

```html
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul class="flashes">
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
{% endwith %}
```

The `{% with %}` block creates a temporary variable
scoped to the block. `get_flashed_messages()`
returns the list of pending messages **and removes
them** — they only show once.

#### Add to the guestbook

Take the guestbook from Session 5. Add flash:

```python
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        
        if not name or not message:
            flash("Both fields required.", "error")
        else:
            messages.append({"name": name, "message": message})
            flash("Message posted!", "success")
        
        return redirect(url_for("home"))
    
    return render_template("guestbook.html", messages=messages)
```

The second arg to `flash` is a **category** — useful
for styling:

```python
flash("Saved!", "success")
flash("Wrong password.", "error")
flash("Heads up.", "warning")
```

In the template, get them with categories:

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul class="flashes">
            {% for category, msg in messages %}
            <li class="flash flash-{{ category }}">{{ msg }}</li>
            {% endfor %}
        </ul>
    {% endif %}
{% endwith %}
```

Style with CSS:

```css
.flashes { list-style: none; padding: 0; }
.flash { padding: 12px; margin-bottom: 8px; border-radius: 4px; }
.flash-success { background: #d4edda; color: #155724; }
.flash-error { background: #f8d7da; color: #721c24; }
.flash-warning { background: #fff3cd; color: #856404; }
```

Save. Submit a form. **A green "Message posted!"
appears.** Submit empty. **A red error appears.**
Reload. **Messages gone** (one-shot).

#### Where to put the flash display

Best place: **`base.html`** — every page shows
flashes. Then any route can `flash(...)` and it
shows on the next page load.

Update `templates/base.html`:

```html
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    
    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <ul class="flashes">
                    {% for category, msg in messages %}
                    <li class="flash flash-{{ category }}">{{ msg }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </main>
</body>
```

Now any flash anywhere in your app shows up on the
next render. Beautiful.

#### Stretch — "remember me" checkbox

Some sites have "remember me" — sessions persist
beyond browser close.

Flask sessions default to **session lifetime** (when
the browser closes). Make them permanent:

```python
session.permanent = True
app.permanent_session_lifetime = timedelta(days=30)
```

Now sessions last 30 days even if the browser
closes.

#### Stretch — multiple flashes per request

Multiple flashes accumulate:

```python
flash("Welcome back!", "success")
flash("Don't forget to verify your email.", "warning")
return redirect(url_for("home"))
```

Both show on the next page. Useful for "saved AND
here's a note" scenarios.

#### Stretch — view counter using session

```python
@app.route("/")
def home():
    visits = session.get("visits", 0)
    session["visits"] = visits + 1
    return f"You've visited {session['visits']} times."
```

Each visit, the counter goes up. Stored per-browser.
Real personalization.

#### Extension — store more than strings

Sessions can hold any JSON-serializable data:

```python
session["cart"] = ["pizza", "soda", "chips"]
session["user"] = {"name": "Alex", "level": 5}
```

Lists, dicts, all fine. (Same data types as JSON.)

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show the "remember me" demo. Did
  closing/reopening keep your name?
- Did seeing the session cookie in DevTools click?
  That's the actual storage.
- For the kids who added flash messages — show one
  popping up.
- Anyone notice the difference between session and
  flash?

Today you learned:

- **HTTP is stateless** — every request is
  independent.
- **Sessions** = server-signed cookies storing
  per-visitor state.
- **`session["key"] = value`** — store.
- **`session.get("key")`** — read.
- **`session.pop("key", None)`** — delete.
- **`app.secret_key`** required for sessions.
- **Flash messages** = one-shot per-visit
  notifications.
- **`flash("...")`, `flash("...", "category")`**.
- **`get_flashed_messages(with_categories=true)`**.
- **Put flash display in base.html** — works
  everywhere.

This is the foundation of **personalization** and
**user feedback** in any web app. Sessions remember
who; flashes confirm what.

Next week: **SQLite** — your first real database.
Data that survives server restarts.

### If you missed this session

Open Thonny.

1. Add `app.secret_key = "..."` to `app.py`.

2. Use `session["name"] = ...` and
   `session.get("name")` to remember a visitor's
   name.

3. Add a logout route that clears the session.

4. (Stretch) Add flash messages to your form.

About 30-45 minutes. By the end your app should
remember visitors by name and show flash messages.

### Stretch and extension ideas

- **Permanent sessions** with custom lifetime.
- **Multiple flashes per request.**
- **Categories with custom CSS.**
- **Visit counter** via session.
- **Store complex data** (lists, dicts) in
  session.
- **Session-based shopping cart** — add items,
  view cart, clear.
- **Theme preference** stored in session.

### What's next

Next week: **SQLite** — your first real database.
Move beyond in-memory `messages = []` and store
data that *survives server restarts*. Just Python
+ SQL, no Flask yet. Then Session 8 ties them
together.
