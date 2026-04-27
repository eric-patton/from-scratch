## Session 1: Welcome to Flask — your first server

*Phase 8 — Flask · Session 1 of 13*

### What we're learning today

Until now your code has run **on the user's
machine** — Pygame games on their computer, web
pages in their browser. Today you write code that
runs **on a server** — a separate program that
listens for requests from browsers and sends back
responses. By the end of class, you'll have a Flask
server running on your machine, browsers can hit
it, and you'll see the request-response cycle live.

### You'll need to remember from last time

- **Python** — Phases 3, 4, 6.
- **The terminal** — `cd`, `python` (Phase 4
  Session 1).
- **HTML** — Phase 7 Sessions 1-2.
- **Browsers** — Phase 7.
- **`pip install`** — for installing Python
  packages.

---

### Part A: The request-response cycle

#### What's a server?

A **server** is a program that listens for
requests from clients (usually browsers) and sends
back responses. The conversation:

```
1. Browser:  "GET https://example.com/about"
2. Server:   reads the URL, decides what to send
3. Server:   "200 OK, here's the HTML for the about page"
4. Browser:  receives, displays the page
```

**Every** website works this way. When you visit
`google.com`:

1. Your browser sends a request to Google's servers.
2. Google's server looks at the URL, processes the
   request.
3. The server sends back HTML (and CSS, JS, images,
   etc.).
4. Your browser displays the page.

In Phase 7, we built only the **client side** —
HTML/CSS/JS in the browser. Today we build the
**server side** — code that listens for requests
and decides what to send.

#### What's Flask?

**Flask** is a Python library for building web
servers. It handles the boring parts (listening on
a port, parsing requests, sending responses) and
lets you focus on **what to do with each request.**

A Flask server is just a Python program. You write
*Python functions* that respond to specific URLs.
When the browser hits that URL, Flask runs your
function and sends the result back.

#### Install Flask

Open a terminal:

```
$ pip install flask
```

If you see "Successfully installed flask-..." you're
good. If `pip` isn't found, try `pip3` or `python -m
pip install flask`.

#### Your first server

Open Thonny. Save a new file as `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, web!"

if __name__ == "__main__":
    app.run(debug=True)
```

Save. Run (Thonny's run button, or `python app.py`
from terminal).

You'll see something like:

```
 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!
```

The server is running. **Open a browser** and visit:

`http://127.0.0.1:5000`

(Or `http://localhost:5000` — same thing.)

You see: **Hello, web!**

That's it. **You wrote a server.** Browser made a
request, your Python code ran, the result came back.

Stop the server with **Ctrl+C** in the terminal.

#### What every line does

```python
from flask import Flask
```

Import the Flask class.

```python
app = Flask(__name__)
```

Create the app. The `__name__` is a Python special
variable — Flask uses it to figure out where to look
for related files. Just type it as shown.

```python
@app.route("/")
def home():
    return "Hello, web!"
```

This is the **route** — the bridge between URL and
function. The `@app.route("/")` says "when someone
visits the root URL `/`, run *this function*." The
function returns the response.

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Run the server when this file is executed directly.
`debug=True` enables auto-reload (the server
restarts when you edit the file) and detailed error
pages.

#### Localhost — what's `127.0.0.1`?

Both **`127.0.0.1`** and **`localhost`** are
shorthand for "this machine." Your server runs on
your computer, and your browser connects to your
computer.

The `:5000` part is the **port number** — like a
specific door on your machine. Flask defaults to
5000. (HTTP uses 80, HTTPS uses 443 — those are the
"front doors" most websites use.)

For now: this is a *local* server. Only your
machine can reach it. Real deployment (Session 11)
puts it on a real public URL.

#### Edit and reload

Change "Hello, web!" to something else (your name,
a quirky greeting, anything). Save.

Watch the terminal — you'll see "Detected change in
'app.py', reloading."

Reload the browser. **The new text appears.** This
is the dev loop — edit Python, save, reload page,
see change.

#### Add another route

```python
@app.route("/about")
def about():
    return "This is the about page!"
```

Save. The server reloads.

Visit `http://127.0.0.1:5000/about` — see your new
page.

**You have a multi-page server.** Each route
function returns whatever HTML (or text) you want.
Add more:

```python
@app.route("/contact")
def contact():
    return "Email me at example@example.com"
```

Visit `/contact` — there it is.

**Checkpoint:** *Your Flask server runs locally,
serves at least 2 different pages, and reloads
when you save.* **This is the natural stop point if
class is cut short.**

---

### Part B: Return real HTML

So far the responses are **plain text.** The
browser tries to interpret them, but without HTML
structure, they look raw. Time to return real HTML.

#### A page with HTML

```python
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Flask Site</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 60px auto;
                padding: 20px;
                background: #f4f1eb;
            }
            h1 { color: #2c3e50; }
        </style>
    </head>
    <body>
        <h1>Welcome!</h1>
        <p>This is my first Flask site.</p>
        <ul>
            <li><a href="/about">About me</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </body>
    </html>
    """
```

The `"""..."""` is a Python multi-line string —
perfect for HTML.

Save. Reload. **A real page** with styling and
links.

The issue: writing HTML inside a Python string is
*ugly*. It's hard to read, hard to maintain. We'll
fix this in Session 3 with **templates** — separate
HTML files Flask reads.

For today, just see that you *can* return any HTML
you want.

#### Each route, its own page

Build a small site with three pages, each its own
route, each with its own HTML.

`app.py`:

```python
from flask import Flask

app = Flask(__name__)

PAGE_STYLE = """
<style>
    body {
        font-family: Arial, sans-serif;
        max-width: 600px;
        margin: 60px auto;
        padding: 20px;
        background: #f4f1eb;
    }
    h1 { color: #2c3e50; }
    nav a { margin-right: 16px; color: #3498db; }
</style>
"""

NAV = """
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/projects">Projects</a>
</nav>
"""

@app.route("/")
def home():
    return f"""
    <html>
    <head><title>Home</title>{PAGE_STYLE}</head>
    <body>
        {NAV}
        <h1>Hi, I'm Alex.</h1>
        <p>Welcome to my site.</p>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return f"""
    <html>
    <head><title>About</title>{PAGE_STYLE}</head>
    <body>
        {NAV}
        <h1>About me</h1>
        <p>I'm 12 years old. I'm learning Flask.</p>
    </body>
    </html>
    """

@app.route("/projects")
def projects():
    return f"""
    <html>
    <head><title>Projects</title>{PAGE_STYLE}</head>
    <body>
        {NAV}
        <h1>Projects</h1>
        <p>I've built games, apps, and websites.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
```

Save. Visit `/`, `/about`, `/projects`. **Three
linked pages, all served by your Python server.**

Notice the **f-strings** to insert the shared style
and nav. Even with this, the code is repetitive —
templates (Session 3) eliminate the repetition.

#### Stretch — return JSON

Real APIs (like the ones from Phase 7 Session 14)
return JSON. So can you:

```python
from flask import jsonify

@app.route("/api/info")
def api_info():
    return jsonify({
        "name": "My API",
        "version": "1.0",
        "items": ["thing1", "thing2", "thing3"]
    })
```

Visit `http://127.0.0.1:5000/api/info` — you see
JSON in the browser.

That's the start of building **your own API.**
Phase 7's `fetch` could call this. **You can make
your own backend now.**

#### Stretch — random response

Make `/joke` return a random joke from a list:

```python
import random

JOKES = [
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "There are 10 types of people. Those who understand binary and those who don't.",
]

@app.route("/joke")
def joke():
    return random.choice(JOKES)
```

Visit `/joke`. Reload. Different joke each time.

**The server runs Python on every request.** That's
the whole point of the back-end — *dynamic*
responses.

#### Extension — see the request

```python
from flask import request

@app.route("/info")
def info():
    return f"You came from {request.user_agent}"
```

`request` is Flask's object representing the
current incoming request. You can read all sorts of
stuff: who's asking, what URL, what data they sent.

We'll use `request.form` heavily in Session 5 for
forms.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your server. What pages did
  you make?
- Did the request-response cycle make sense? Browser
  asks, server answers.
- For kids who tried the JSON or random joke
  routes — that's the back-end's superpower:
  *dynamic* responses.

Today you learned:

- **A server is a program** that responds to web
  requests.
- **Flask** = Python web framework.
- **`pip install flask`** to install.
- **`@app.route("/")`** — bridge between URL and
  function.
- **`app.run(debug=True)`** — start the dev server
  with auto-reload.
- **`http://127.0.0.1:5000`** — local server URL.
- **Each route returns** HTML (or text or JSON).
- **Server runs Python on every request** —
  responses can be different each time.

You're writing **the back-end** now. Same Python
as before, different runtime.

Next week: **routes with parameters** — URLs like
`/user/alex` where the part after `/user/` becomes
input to your function.

### If you missed this session

Open a terminal.

1. `pip install flask`.

2. Create `app.py` with the basic Flask hello-world.

3. Run with `python app.py`.

4. Visit `http://127.0.0.1:5000` in a browser.

5. Add 2-3 more routes with their own HTML.

About 30-45 minutes. By the end you should have a
multi-page Flask server running locally.

### Stretch and extension ideas

- **Return JSON** from a route.
- **Random responses** with `random.choice`.
- **Read the request** with `request.user_agent`,
  `request.headers`, etc.
- **Custom error pages** — `@app.errorhandler(404)`
  for not-found.
- **Set the port** — `app.run(debug=True, port=8000)`.
- **Multiple files** — Flask apps can be split
  across modules. Out of scope for today.
- **Try `flask` from terminal** — instead of `python
  app.py`, set `FLASK_APP=app` and `flask run`.

### What's next

Next week: **routes and URL parameters** — making
URLs like `/user/alex` where the `alex` part
becomes a variable in your Python function. The
foundation for personalized pages.
