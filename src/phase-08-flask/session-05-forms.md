## Session 5: Forms and POST requests

*Phase 8 — Flask · Session 5 of 13*

### What we're learning today

So far the user **reads** from your server. Today
they **send data to it.** Forms in HTML, processed
in Python via `request.form`, with the standard
**GET-then-POST** pattern: show the form on GET,
process it on POST, redirect to a result page. By
the end you'll have a guestbook where any visitor
can leave a message.

This is the **first time** the user *changes* what
your server holds.

### You'll need to remember from last time

- **Templates** with `render_template`.
- **Base templates** with `extends` / `block`.
- **Phase 7 Session 7** — HTML forms (`<form>`,
  `<input>`, `<button>`).
- **Lists in Python** — for the guestbook.

---

### Part A: GET vs POST

#### Two kinds of requests

Browsers send two main kinds of requests:

- **GET** — "give me this page." The default for
  every link click and URL typed in the bar. **No
  body** — just URL.
- **POST** — "here's some data; do something with
  it." Used by forms with `method="post"`. **Has
  a body** — the form data.

So far, every route you wrote handled GET. To
handle POST, you tell Flask explicitly:

```python
@app.route("/submit", methods=["GET", "POST"])
def submit():
    ...
```

By default routes only handle GET. Listing
`["GET", "POST"]` means "this route handles both."

#### `request.method` — which one?

Inside the route, check which method the browser
used:

```python
from flask import request

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        # Process the form data
        return "Got your data!"
    else:
        # Show the form
        return "<form method='post'><input name='x'><button>Send</button></form>"
```

**The same URL** can show a form (on GET) and
process the form (on POST). Standard pattern.

#### `request.form` — read submitted data

When a form is submitted, the data is in
`request.form` — a dict-like object keyed by input
`name` attributes:

```html
<input type="text" name="message">
```

```python
text = request.form.get("message")
```

`request.form.get("name")` — same `.get()` pattern
as Python dicts. Returns `None` if missing.

`request.form["name"]` also works but throws an
error on missing keys.

#### Build it — a simple form

Project structure:

```
form_app/
├── app.py
├── templates/
│   ├── base.html
│   └── form.html
└── static/
    └── style.css
```

`templates/form.html`:

```html
{% extends "base.html" %}
{% block title %}Send a message{% endblock %}
{% block content %}
<h1>Send me a message</h1>

<form method="post">
    <label for="name">Your name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="message">Your message:</label>
    <textarea id="message" name="message" rows="4" required></textarea>
    
    <button type="submit">Send</button>
</form>
{% endblock %}
```

Note `method="post"` on the form — this is what
makes the submit a POST.

`app.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return f"<h1>Thanks, {name}!</h1><p>You said: {message}</p>"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
```

Add `templates/base.html` and `static/style.css`
from previous sessions.

Save. Run. Visit `/`. See the form. Type a name
and message. Submit. **You see your data echoed
back.**

You just **received data from the user.** First
time. **The web is now interactive.**

#### The redirect-after-POST pattern

There's a problem with the above. After submit,
the URL is still `/` but the page shows the
result. **Refresh the page** — the browser asks
"resubmit?" because it tries to repeat the POST.
Annoying.

The fix: after processing a POST, **redirect** to
a different URL (or back to the same one, as a
GET). This is the **POST-Redirect-GET** pattern.

Update `app.py`:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage — resets on server restart
messages = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        messages.append({"name": name, "message": message})
        return redirect(url_for("home"))    # GET back to home
    return render_template("form.html", messages=messages)
```

Update `templates/form.html` to show messages:

```html
{% extends "base.html" %}
{% block title %}Guestbook{% endblock %}
{% block content %}
<h1>Guestbook</h1>

<form method="post">
    <label for="name">Your name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="message">Your message:</label>
    <textarea id="message" name="message" rows="4" required></textarea>
    
    <button type="submit">Sign the guestbook</button>
</form>

<h2>Messages</h2>
{% if messages %}
    {% for m in messages %}
    <div class="message">
        <strong>{{ m.name }}:</strong>
        <p>{{ m.message }}</p>
    </div>
    {% endfor %}
{% else %}
    <p>No messages yet. Be the first!</p>
{% endif %}
{% endblock %}
```

Save. Submit a few messages. **Each one appears in
the list.** Refresh — no resubmit warning. Real
guestbook.

Pattern recap:

1. GET `/` → show the form + existing messages.
2. POST `/` → process, store, **redirect** back to
   GET `/`.
3. The redirect = a fresh GET, no resubmit warning.

**Memorize this pattern.** Every form-processing
route uses it.

#### Note on the `messages` list

The `messages = []` lives in your Python module.
It's stored **in memory** — when you stop the
server, the list is gone. Sessions 7-8 add a
**database** so the data really persists.

For now: in-memory is fine for learning the form
pattern.

**Checkpoint:** *Your guestbook accepts messages,
stores them, and shows them on refresh without a
resubmit warning.* **This is the natural stop
point if class is cut short.**

---

### Part B: Validation and feedback

#### Server-side validation

Browser-side `required` attributes catch some
issues but can be bypassed. **Server-side
validation** is the safety net.

```python
@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        
        if not name or not message:
            error = "Name and message are required."
        elif len(message) > 500:
            error = "Message must be under 500 characters."
        else:
            messages.append({"name": name, "message": message})
            return redirect(url_for("home"))
    
    return render_template("form.html", messages=messages, error=error)
```

Show the error in the template:

```html
{% if error %}
<div class="error">{{ error }}</div>
{% endif %}
```

Add to `static/style.css`:

```css
.error {
    background-color: #ffe5e5;
    color: #c0392b;
    padding: 12px;
    border-left: 4px solid #c0392b;
    margin-bottom: 16px;
}
```

Try submitting empty (after removing `required` from
the input): **error message appears.** Try a 600-
character message: error.

#### Stretch — preserve form state on error

When the error shows, the form is empty again. Bad
UX. Fix by passing the previous values back:

```python
return render_template("form.html",
                       messages=messages,
                       error=error,
                       name=name,
                       message=message)
```

In the template:

```html
<input type="text" id="name" name="name" value="{{ name|default('') }}" required>
<textarea id="message" name="message" rows="4" required>{{ message|default('') }}</textarea>
```

Now after an error, the form keeps what the user
typed. Real UX practice.

#### Stretch — different forms, different routes

You can have separate routes for showing vs.
processing:

```python
@app.route("/submit-form")
def show_form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def process_form():
    name = request.form.get("name")
    # process...
    return redirect(url_for("show_form"))
```

The form's `action="/submit"` posts to the second
route.

**The single-route GET-or-POST is more common** —
keep both behaviors together. But knowing the
multi-route variant exists is useful.

#### Stretch — checkboxes and selects

```html
<input type="checkbox" name="newsletter" id="newsletter">
<label for="newsletter">Subscribe to newsletter</label>

<label for="topic">Topic:</label>
<select name="topic" id="topic">
    <option value="general">General</option>
    <option value="bug">Bug report</option>
</select>
```

```python
newsletter = request.form.get("newsletter")    # "on" if checked, None if not
topic = request.form.get("topic")              # "general" or "bug"
```

For checkboxes, the value is `"on"` (or whatever
`value=` you set) when checked, `None` (missing)
when unchecked. Use `if newsletter:` to check.

#### Extension — multiple values

For multi-select or multiple checkboxes with the
same name, use `request.form.getlist`:

```html
<input type="checkbox" name="hobbies" value="reading">
<input type="checkbox" name="hobbies" value="coding">
<input type="checkbox" name="hobbies" value="music">
```

```python
hobbies = request.form.getlist("hobbies")    # ["reading", "coding"]
```

Returns a list of all values for that name.

#### Extension — file uploads

```html
<form method="post" enctype="multipart/form-data">
    <input type="file" name="upload">
    <button type="submit">Upload</button>
</form>
```

```python
file = request.files.get("upload")
if file:
    file.save(f"static/uploads/{file.filename}")
```

The `enctype` is required for file uploads. Beyond
that — pretty straightforward. (Real apps need to
sanitize filenames and check types.)

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your guestbook. How many
  messages?
- Did the GET-then-POST-then-redirect pattern make
  sense?
- For the kids who added validation — what error
  did you trigger?
- Anyone notice messages disappear when the server
  restarts? **That's why we need a database
  (Session 7).**

Today you learned:

- **GET vs POST** — read vs send data.
- **`methods=["GET", "POST"]`** to handle both.
- **`request.method`** to check which.
- **`request.form.get("name")`** to read form
  data.
- **POST-Redirect-GET pattern** — redirect after
  processing to avoid resubmit warnings.
- **`redirect(url_for("route_name"))`** for
  redirects.
- **Server-side validation** — never trust the
  client.
- **`request.form.getlist`** for multi-value
  fields.

The **first time** the user changes data on your
server. **The web is no longer read-only.**

Next week: **sessions and flash messages** —
remember things across requests, show one-time
notifications.

### If you missed this session

Open Thonny.

1. Build a simple form template with name and
   message inputs.

2. Set up `app.py` with a single route handling
   both GET and POST.

3. Use `request.form.get(...)` to read the data.

4. Implement the POST-Redirect-GET pattern with
   `redirect(url_for(...))`.

5. (Stretch) Add server-side validation.

About 45-60 minutes. By the end you should have a
working guestbook.

### Stretch and extension ideas

- **Server-side validation** (above).
- **Preserve form state on error.**
- **Checkboxes, selects, multi-value fields.**
- **File uploads** (advanced).
- **CSRF protection** with Flask-WTF (advanced —
  out of curriculum scope).
- **Form deletion** — delete-message buttons (uses
  POST to `/delete/<id>`).
- **Edit messages** — edit form on GET, save on
  POST.

### What's next

Next week: **sessions and flash messages** — the
server *remembers* visitors across requests
(session cookies), and you can flash one-time
messages like "Message sent!" that show on the
next page load.
