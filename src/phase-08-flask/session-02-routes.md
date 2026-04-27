## Session 2: Routes and URL parameters

*Phase 8 — Flask · Session 2 of 13*

### What we're learning today

Last week each route was a fixed URL — `/about`,
`/contact`. Today we make routes **dynamic** — URLs
like `/user/alex` where the `alex` part becomes a
*variable* in your Python function. By the end of
class you'll have a server that personalizes pages
based on the URL — different greetings for different
names, different views for different items.

This is the foundation of every personalized web
app.

### You'll need to remember from last time

- **Flask basics** — `Flask(__name__)`,
  `@app.route("/")`, `app.run(debug=True)`.
- **The request-response cycle** — browser asks,
  server answers.
- **Returning HTML strings.**
- **F-strings** — `f"Hello, {name}!"`.

---

### Part A: Dynamic URLs

#### URL parameters with `<name>`

Add a route with a `<...>` part:

```python
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"
```

The angle brackets `<name>` capture the part of the
URL there as a **variable**. Whatever the user puts
in the URL becomes the `name` parameter of your
function.

Try it. Open `app.py` and add:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Try /hello/yourname"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
```

Save. Run. Visit:

- `http://127.0.0.1:5000/hello/alex` → "Hello, alex!"
- `http://127.0.0.1:5000/hello/sam` → "Hello, sam!"
- `http://127.0.0.1:5000/hello/world` → "Hello, world!"

**Same route, different responses.** The URL is the
input.

This is huge. **One function handles infinite URLs**
— for every name, a personalized greeting.

#### How it works

The `@app.route("/hello/<name>")` line tells Flask:

1. Match URLs that look like `/hello/SOMETHING`.
2. Capture the `SOMETHING` part as a variable
   called `name`.
3. Pass it as an argument to the function.

The function name (`def hello(name):`) takes that
argument. Use it however you want — interpolate
into a string, query a database, look up data.

#### Multiple parameters

```python
@app.route("/greet/<greeting>/<name>")
def greet(greeting, name):
    return f"{greeting}, {name}!"
```

Visit `/greet/howdy/sam` → "howdy, sam!"
Visit `/greet/welcome/alex` → "welcome, alex!"

Each `<...>` becomes a function parameter, in order.

#### Type converters

By default, URL parameters are **strings.** For
other types, add a converter:

```python
@app.route("/double/<int:n>")
def double(n):
    return f"{n} doubled is {n * 2}"
```

The `<int:n>` says "this part must be an integer,
and pass it as an `int`."

Visit `/double/5` → "5 doubled is 10"
Visit `/double/abc` → 404 (not a valid integer)

Built-in converters:

- **`int`** — integers.
- **`float`** — decimal numbers.
- **`string`** (default) — anything except `/`.
- **`path`** — anything *including* `/` (use for
  file paths).

#### Build it — a personalized page

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 60px auto;">
        <h1>Welcome!</h1>
        <p>Try these pages:</p>
        <ul>
            <li><a href="/hello/alex">/hello/alex</a></li>
            <li><a href="/hello/sam">/hello/sam</a></li>
            <li><a href="/double/7">/double/7</a></li>
            <li><a href="/double/100">/double/100</a></li>
        </ul>
    </body>
    </html>
    """

@app.route("/hello/<name>")
def hello(name):
    return f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 60px auto;">
        <h1>Hello, {name}!</h1>
        <p>Welcome to the site, {name}.</p>
        <p><a href="/">← Back home</a></p>
    </body>
    </html>
    """

@app.route("/double/<int:n>")
def double(n):
    return f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 60px auto;">
        <h1>Double of {n} is {n * 2}</h1>
        <p>Triple is {n * 3}, square is {n * n}</p>
        <p><a href="/">← Back home</a></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
```

Save. Visit `/` to see the home page with links.
Click each. **Personalized pages, dynamic math.**

**Checkpoint:** *Your server has at least one
parameterized route.* **This is the natural stop
point if class is cut short.**

---

### Part B: Build something with parameters

Time to use parameters for real.

#### Build a Pokemon viewer

A page per Pokemon. Hardcoded data for a few:

```python
from flask import Flask

app = Flask(__name__)

POKEMON = {
    "pikachu": {"type": "Electric", "level": 25, "color": "#ffeb3b"},
    "charmander": {"type": "Fire", "level": 12, "color": "#ff5722"},
    "bulbasaur": {"type": "Grass", "level": 14, "color": "#4caf50"},
    "squirtle": {"type": "Water", "level": 10, "color": "#03a9f4"},
}

@app.route("/")
def home():
    links = ""
    for name in POKEMON:
        links += f'<li><a href="/pokemon/{name}">{name.title()}</a></li>'
    return f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 60px auto;">
        <h1>Pokemon Index</h1>
        <ul>{links}</ul>
    </body>
    </html>
    """

@app.route("/pokemon/<name>")
def pokemon(name):
    p = POKEMON.get(name.lower())
    if not p:
        return f"<h1>No Pokemon named {name}</h1>"
    return f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 60px auto; background: {p['color']}; padding: 20px;">
        <h1>{name.title()}</h1>
        <p>Type: {p['type']}</p>
        <p>Level: {p['level']}</p>
        <p><a href="/">← Back to index</a></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
```

Save. Visit `/` — see the index. Click any Pokemon.
**A page styled in their color, with their data.**

What's new:

- **`POKEMON` dictionary** — your "database" for
  now. Each key is a name; value is data.
- **The home page builds links by looping** through
  the dictionary keys.
- **`POKEMON.get(name.lower())`** — `.get()`
  returns `None` if the key isn't found (vs `[name]`
  which would crash).
- **Different background color per Pokemon** —
  Python builds CSS dynamically.

This is the **shape of every dynamic site.** Data
in a structure, route looks up by parameter, page
displays.

#### Stretch — fallback / 404

Right now `/pokemon/missingno` returns "No Pokemon
named missingno" but with HTTP status 200 (success).
Better: return a *real* 404:

```python
from flask import abort

@app.route("/pokemon/<name>")
def pokemon(name):
    p = POKEMON.get(name.lower())
    if not p:
        abort(404)
    return f"""..."""
```

`abort(404)` triggers a 404 response. Browsers
handle it specially.

#### Stretch — query parameters with `request.args`

Some sites use **query strings** like
`/search?q=pokemon&color=red`. Flask reads them via
`request.args`:

```python
from flask import request

@app.route("/search")
def search():
    q = request.args.get("q", "")    # default empty if missing
    return f"<h1>You searched for: {q}</h1>"
```

Visit `/search?q=alex` → "You searched for: alex"
Visit `/search?q=pikachu` → "You searched for:
pikachu"

Query parameters are common for filters, search
terms, and optional info. Different from URL
parameters (`<name>`) which are required parts of
the path.

#### Stretch — multiple Pokemon per type

```python
@app.route("/type/<typename>")
def by_type(typename):
    matches = [name for name, p in POKEMON.items()
               if p["type"].lower() == typename.lower()]
    items = "".join(f'<li><a href="/pokemon/{n}">{n}</a></li>'
                    for n in matches)
    return f"""
    <html>
    <body>
        <h1>{typename.title()}-type Pokemon</h1>
        <ul>{items}</ul>
        <p><a href="/">← Back</a></p>
    </body>
    </html>
    """
```

Visit `/type/fire` → list of Fire Pokemon.
Visit `/type/water` → list of Water.

#### Extension — favorite books / movies / songs

Adapt the Pokemon pattern to your favorite
*anything*. A dictionary of items, a route per item,
links from the home page. Same pattern, different
domain.

#### Extension — calculator routes

```python
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return f"{a} × {b} = {a * b}"
```

Visit `/add/5/3`, `/multiply/7/8`, etc. A calculator
in URLs.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your routes. What URLs did
  you build?
- For Pokemon-builder kids — what's your favorite
  Pokemon's color?
- Did the "one function, infinite URLs" idea click?
- Anyone try `request.args` for query strings?

Today you learned:

- **`<name>`** in routes captures URL parts as
  parameters.
- **Type converters:** `<int:n>`, `<float:x>`.
- **Multiple parameters:** `<a>/<b>`.
- **`request.args.get("q")`** for query strings.
- **`abort(404)`** for "not found" responses.
- **One route function handles infinite URLs.**

This is the foundation of every personalized site.
Wikipedia: `/wiki/<article>`. Twitter:
`/<username>`. YouTube: `/watch?v=<video_id>`. All
the same pattern as today.

Next week: **templates** — separate HTML files
Flask reads, with placeholders for your data. The
end of HTML-in-Python-strings.

### If you missed this session

Open Thonny. You need Flask installed (Session 1).

1. Build the basic `app.py` with `/`, `/hello/<name>`,
   and `/double/<int:n>` routes.

2. Test in browser with several different URLs.

3. (Stretch) Build the Pokemon viewer.

4. (Stretch) Add a `/search` route using
   `request.args`.

About 30-45 minutes. By the end you should have a
server with at least one parameterized route.

### Stretch and extension ideas

- **Pokemon viewer** with a dictionary "database."
- **Favorite-things** site — books, movies, games.
- **Calculator routes** — add, multiply, etc.
- **Query strings** with `request.args`.
- **404 handling** with `abort`.
- **Path converters** — `<path:filename>` for paths
  with slashes.
- **Multiple converters in one route** —
  `/range/<int:start>/<int:end>` returns a list.
- **`url_for(...)`** — generate URLs from function
  names. Cleaner than hardcoding `/hello/...`.
  Preview Session 4.

### What's next

Next week: **templates** — separate HTML files
Flask reads, with placeholders. We replace the
ugly multi-line strings with clean `.html` files.
This is where Flask code starts to look
*professional*.
