## Session 3: Templates — Jinja2

*Phase 8 — Flask · Session 3 of 13*

### What we're learning today

Returning HTML as Python strings is **ugly.** Today
you learn **templates** — separate `.html` files
Flask reads, with `{{ placeholders }}` for your
data and `{% control %}` blocks for loops and
conditionals. By the end your routes will be tiny
("look up data, render template, send back"), and
your HTML will live in clean, syntax-highlighted
files.

This is the moment Flask code starts to look
*professional*.

### You'll need to remember from last time

- **Flask basics** — `Flask(__name__)`,
  `@app.route`, `app.run`.
- **URL parameters** — `<name>`.
- **HTML structure** — Phase 7.
- **Python dictionaries** — Phase 3.

---

### Part A: Your first template

#### The `templates/` folder

Flask expects HTML files in a folder called
**`templates/`** next to your `app.py`. Make that
folder.

Your project structure:

```
my_app/
├── app.py
└── templates/
    ├── home.html
    └── pokemon.html
```

#### A first template

Create `templates/home.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>Welcome to my Flask site.</p>
</body>
</html>
```

The **`{{ ... }}`** is a **template placeholder.**
Flask replaces it with the value you pass in.

Now in `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",
                           title="My Site",
                           heading="Welcome!")

if __name__ == "__main__":
    app.run(debug=True)
```

Save both. Run. Visit `http://127.0.0.1:5000`.

You see:

```
Welcome!
Welcome to my Flask site.
```

The **template** filled in. Browser tab title: "My
Site."

What's happening:

- **`render_template("home.html", ...)`** — Flask
  reads `templates/home.html`, replaces the
  `{{ ... }}` placeholders with the keyword
  arguments, and returns the result.
- **`{{ title }}`** in HTML becomes **`"My Site"`**
  (the value you passed).
- **`{{ heading }}`** becomes `"Welcome!"`.

You can pass any Python value — strings, numbers,
lists, dicts. The template handles it.

#### Why this is better

Compare:

```python
# Without templates
@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>{title}</title></head>
    ...
    """
```

vs.

```python
# With templates
@app.route("/")
def home():
    return render_template("home.html", title=title, ...)
```

The HTML lives in a `.html` file. Your editor
**syntax-highlights it.** Other people can edit
the design without touching your Python. Reusable.
Professional.

#### Loops in templates

Templates can loop with `{% for %}`:

```html
<ul>
    {% for item in items %}
    <li>{{ item }}</li>
    {% endfor %}
</ul>
```

Note the **two kinds of curly braces:**

- **`{{ ... }}`** — output an expression.
- **`{% ... %}`** — control flow (loops, ifs,
  blocks).

Try it. In `templates/home.html`:

```html
<!DOCTYPE html>
<html>
<head><title>Things I like</title></head>
<body>
    <h1>{{ heading }}</h1>
    <ul>
        {% for item in items %}
        <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

In `app.py`:

```python
@app.route("/")
def home():
    return render_template("home.html",
                           heading="Things I like",
                           items=["pizza", "soccer", "reading"])
```

Save. Reload. **A bulleted list with three items.**

The `for` loop in the template runs through
`items`, generating one `<li>` for each.

Every `{% for %}` needs a matching `{% endfor %}`.
Same with `{% if %}` / `{% endif %}`.

#### Conditionals

```html
{% if user %}
    <p>Hello, {{ user }}!</p>
{% else %}
    <p>Hello, stranger.</p>
{% endif %}
```

In `app.py`:

```python
@app.route("/")
def home():
    return render_template("home.html",
                           user="Alex")
```

Visit `/` — "Hello, Alex!" Comment out the
`user="Alex"` (or pass `user=None`) and reload —
"Hello, stranger."

#### Filters — modify values in templates

The `|` symbol applies a **filter:**

```html
{{ name|upper }}              <!-- HELLO -->
{{ name|lower }}              <!-- hello -->
{{ name|title }}              <!-- Hello -->
{{ items|length }}            <!-- count of items -->
{{ price|round(2) }}          <!-- 19.99 -->
```

Common filters:

- **`upper`, `lower`, `title`** — string case.
- **`length`** — count of items / characters.
- **`round(n)`** — number rounding.
- **`default("???")`** — fallback if value is
  missing.
- **`safe`** — mark HTML as safe (don't escape).

Filters keep templates clean — no need to call
Python helpers.

**Checkpoint:** *You have a template with at least
one `{{ variable }}`, one `{% for %}` loop, and
one `{% if %}` conditional.* **This is the natural
stop point if class is cut short.**

---

### Part B: Refactor the Pokemon viewer

Take the Pokemon viewer from Session 2 and refactor
it with templates.

#### Project structure

```
pokemon_app/
├── app.py
└── templates/
    ├── index.html
    └── pokemon.html
```

#### `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Pokemon Index</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 60px auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <h1>Pokemon Index</h1>
    <ul>
        {% for name in pokemon %}
        <li><a href="/pokemon/{{ name }}">{{ name|title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/pokemon.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ name|title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 60px auto;
            padding: 20px;
            background: {{ data.color }};
        }
    </style>
</head>
<body>
    <h1>{{ name|title }}</h1>
    <p>Type: {{ data.type }}</p>
    <p>Level: {{ data.level }}</p>
    <p><a href="/">← Back to index</a></p>
</body>
</html>
```

#### `app.py`

```python
from flask import Flask, render_template, abort

app = Flask(__name__)

POKEMON = {
    "pikachu": {"type": "Electric", "level": 25, "color": "#ffeb3b"},
    "charmander": {"type": "Fire", "level": 12, "color": "#ff5722"},
    "bulbasaur": {"type": "Grass", "level": 14, "color": "#4caf50"},
    "squirtle": {"type": "Water", "level": 10, "color": "#03a9f4"},
}

@app.route("/")
def index():
    return render_template("index.html", pokemon=POKEMON)

@app.route("/pokemon/<name>")
def pokemon(name):
    data = POKEMON.get(name.lower())
    if not data:
        abort(404)
    return render_template("pokemon.html", name=name, data=data)

if __name__ == "__main__":
    app.run(debug=True)
```

Save. Run. Visit `/`. Click around. **Same site as
Session 2 — but now the HTML is in `.html` files
and the Python is tiny.**

Compare line counts. The Python file is *much*
shorter. The HTML is properly highlighted in your
editor. Easier to read, easier to change.

This is **the standard Flask shape.** Routes stay
small; templates do the rendering.

#### Auto-escaping (safety)

Type a name with HTML in it: visit `/pokemon/<script>`.

Flask **auto-escapes** the value. The `<script>`
shows as literal text, not as a tag. **You're
safe** from XSS attacks (where a user injects
malicious HTML).

If you actually *want* HTML to render (rarely), use
`|safe`:

```html
{{ user_html|safe }}
```

But default to *not* using `|safe` for any value
that comes from users.

#### Stretch — a base template

Both pages duplicate the `<!DOCTYPE html>...`
boilerplate. Extract a base template (we'll go
deeper next session):

`templates/base.html`:

```html
<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

`templates/index.html`:

```html
{% extends "base.html" %}

{% block content %}
<h1>Pokemon Index</h1>
<ul>
    {% for name in pokemon %}
    <li><a href="/pokemon/{{ name }}">{{ name|title }}</a></li>
    {% endfor %}
</ul>
{% endblock %}
```

The child template **extends** the base, **fills in
the block.** Common HTML lives in one place.

Full coverage of `extends`/`block` is Session 4.

#### Stretch — pass complex data

Templates can iterate over **dictionaries:**

```python
return render_template("index.html",
                       pokemon=POKEMON.items())
```

```html
{% for name, data in pokemon %}
<li>{{ name|title }} — {{ data.type }}</li>
{% endfor %}
```

`{% for k, v in dict.items() %}` — same as Python.

#### Stretch — Jinja math

```html
<p>{{ 5 + 3 }}</p>            <!-- 8 -->
<p>{{ data.level * 100 }}</p>  <!-- 1200 -->
```

Templates can do arithmetic. Useful for derived
values without changing your Python.

#### Extension — template comments

```html
{# This is a Jinja comment — won't show in HTML #}
```

Different from `<!-- HTML comments -->` (which *do*
show in the page source). `{# ... #}` is invisible.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your refactored Pokemon
  viewer. Does it feel cleaner?
- For the kids who tried `extends`/`block` — does
  template inheritance feel powerful?
- Did the auto-escaping demo land? Type `<script>`
  in a URL — it shows as text, not as code.

Today you learned:

- **`templates/`** folder — Flask's convention.
- **`render_template("name.html", var=value)`**
  — render a template with values.
- **`{{ variable }}`** — output a value.
- **`{% for %}`, `{% endfor %}`** — loops.
- **`{% if %}`, `{% else %}`, `{% endif %}`** —
  conditionals.
- **`{{ value|filter }}`** — apply a filter
  (`upper`, `length`, `default`, etc.).
- **Auto-escaping** — values are safe by default.
- **`{# comment #}`** — Jinja comments.

Your Python files now do **logic**; templates do
**display**. Real separation of concerns.

Next week: **static files (CSS, images) and
template inheritance** — clean shared layouts
across your whole site.

### If you missed this session

Open Thonny.

1. Create a `templates/` folder next to your
   `app.py`.

2. Build `templates/home.html` with at least one
   `{{ variable }}`.

3. Update `app.py` to use `render_template`.

4. Add a `{% for %}` loop and `{% if %}`
   conditional.

5. (Stretch) Refactor the Pokemon viewer.

About 30-45 minutes. By the end you should have
your routes returning rendered templates.

### Stretch and extension ideas

- **Refactor the Pokemon viewer** completely.
- **Base template** with `extends`/`block`.
- **Filters** — try every common one.
- **Math in templates.**
- **Multiple templates inheriting from the same
  base.**
- **Looping over dictionaries** with
  `dict.items()`.
- **Date formatting** with the `format_datetime`
  filter (requires Flask-Babel — out of scope but
  worth knowing).
- **Jinja docs** — bookmark
  [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/).

### What's next

Next week: **static files** — CSS, images, JS in
the right folder so Flask serves them — and
**template inheritance** — `{% extends %}` for
shared layouts. Your sites start looking like
real production apps.
