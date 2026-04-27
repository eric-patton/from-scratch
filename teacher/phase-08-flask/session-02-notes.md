## Session 2 — Teacher Notes

*Phase 8, Flask · Session 2 of 13 · Title: Routes
and URL parameters*

### Purpose of this session

The "URLs become input" session. Five jobs, in
priority order:

1. **Land URL parameters with `<name>`.** One
   function, infinite URLs.
2. **Land "the URL is data."** Wikipedia, Twitter,
   YouTube — every dynamic site uses this pattern.
3. **Land type converters.** `<int:n>`, `<float:x>`
   — Flask converts and validates for you.
4. **Build a small data-driven site.** Pokemon
   viewer is the canonical example.
5. **Set up Session 3 (templates).** The "ugly
   HTML in strings" gets fixed next.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built Pokemon viewer (the Part B end-state).
- Pre-built calculator routes (Part B stretch) for
  reference.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 1.
- **Part A: parameterized routes** (~25 min).
  Type live, test multiple URLs.
- **Part A: type converters + multiple
  parameters** (~15 min).
- **Break** (~5 min).
- **Part B: Pokemon viewer** (~30 min).
- **Part B: stretches** (~5 min).
- **Wrap-up** (~5 min).

If running short, **drop the calculator and
query-string stretches.** The Pokemon viewer is
the priority.

### Teaching Part A

#### "URLs are input"

Frame:

> "Last session, your routes were *fixed* —
> `/about`, `/contact`. Today they're *dynamic* —
> the URL itself is input.
>
> Wikipedia URLs: `/wiki/<article>`. Each article
> has its own URL but they all run the *same*
> handler function — read article from database,
> render page.
>
> Twitter: `/<username>`. YouTube:
> `/watch?v=<video_id>`. All the same pattern.
> *Today you learn that pattern.*"

#### `<name>` syntax

```python
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"
```

Three parts:

1. The `<name>` in the route says "match anything
   here, capture as a variable."
2. The `def hello(name):` declares the parameter.
3. The function uses it like any Python variable.

> "The variable name in `<...>` and the function
> parameter must match. Flask connects them."

#### Type converters

```python
@app.route("/double/<int:n>")
```

Walk through:

> "By default URL parameters are strings. But
> `5` from a URL is the string `'5'`, not the
> number 5. Multiplying a string by 2 gives `'55'`
> — *not what we wanted.*
>
> The `<int:n>` converter says 'this part must be
> an integer; pass it as `int`.' Now `n * 2` works
> like math."

Demo: try `/double/5` (works), `/double/abc`
(404 — `abc` isn't an integer).

> "Converters are *also validation*. If the user
> puts something that doesn't match, Flask returns
> 404 automatically. Free input checking."

#### Multiple parameters

Show:

```python
@app.route("/greet/<greeting>/<name>")
def greet(greeting, name):
    return f"{greeting}, {name}!"
```

Visit `/greet/howdy/sam` → "howdy, sam!"

> "Each `<...>` becomes a parameter, in order.
> Build any combination you want."

### Teaching Part B

#### Pokemon viewer is the canonical demo

Walk through line by line. Pause to discuss:

- **`POKEMON` dict** — "this is your *database*
  for now. Real database in Session 7."
- **Home page builds links via loop** —
  programmatic HTML.
- **`POKEMON.get(name.lower())`** — `.get()` is
  safer than `[]` for missing keys. Returns `None`
  instead of crashing.
- **Per-Pokemon styling** — Python builds CSS
  dynamically. Real personalization.

After typing, visit each route. Show the index,
click a Pokemon, see the colored page.

> "*That* is dynamic. The data is in your code.
> The route handler picks the right entry and
> styles a page for it. Real app shape."

#### `.get()` vs `[]`

A real precision moment:

```python
POKEMON.get("missingno")    # None (safe)
POKEMON["missingno"]         # KeyError (crashes)
```

Frame:

> "When you might be missing a key, use `.get()`
> and check the result. Crashes look bad to users.
> Real apps validate and respond gracefully."

This is foundational defensive coding.

#### `abort(404)` for missing items

```python
from flask import abort

if not p:
    abort(404)
```

> "404 is the standard 'not found' status. Browsers
> may show special pages for it; search engines
> won't index it. Better than your custom 'oops'
> message."

#### Query strings vs URL parameters

```
/pokemon/pikachu       → URL parameter (part of path)
/search?q=pikachu      → query string (after ?)
```

Frame:

> "Two different ways to pass data in URLs.
> *URL parameters* are required parts of the path.
> *Query strings* are optional, often for filters
> or search terms.
>
> Reddit: `/r/<subreddit>` is a path parameter.
> Sort: `?sort=new` is a query string."

`request.args.get("q", default)` — pattern.

### Common stumbles

- **Variable name mismatch.** `<name>` but
  `def hello(username):` — Flask error.
- **Forgot the parameter on the function.**
  `def hello():` — Flask error.
- **Type converter wrong.** `/double/5.5` with
  `<int:n>` → 404 (5.5 isn't int). Use `<float:n>`.
- **Trailing slash issues.** `/hello/alex/` vs
  `/hello/alex`. Flask treats them differently
  by default. Either be consistent, or use
  `strict_slashes=False`.
- **`KeyError` from `POKEMON[name]`.** Used `[]`
  instead of `.get()`. Walk through.
- **F-string syntax errors with HTML.** Quotes
  inside f-string conflict with quotes outside.
  Use single inside double or vice versa.
- **`request` not imported.** `from flask import
  request`.
- **Query string returns None.** Forgot the
  default in `.get("q", "")`.

### Differentiation

- **Younger kids (9-10):** Goal is the basic
  parameterized hello + simple personalization.
  Pokemon viewer is a stretch.
- **Older kids (12+):** Push for full Pokemon
  viewer + at least one stretch.
- **Advanced (any age):** Suggest:
  - Calculator routes
  - Type filtering (`/type/fire`)
  - Search with query strings
  - Their own data domain (books, movies, games)
  - 404 handling with custom error page
  - `url_for(...)` to generate URLs
- **Struggling:** A kid who can't get
  parameterized routes working is the kid you
  focus on. Most common cause: variable name
  mismatch.

### What to watch for

- **The "this is how Wikipedia works" reaction.**
  Comparison to real sites lands.
- **Buddies trying each other's URLs** — typing
  weird names into `/hello/<name>`. Encourage.
- **Excitement about data-driven personalization.**
  "Different page for different Pokemon!" Yes.
- **Kids over-styling individual Pokemon pages**
  rather than building more routes. Redirect:
  "Get the routes working first."
- **Kids inventing new data domains** — favorite
  songs, sports teams, etc. Encourage; great
  practice.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 3 (templates).** The HTML-in-strings
  gets cleaned up.
- **Session 4 (templates + static).** Templates +
  CSS files.
- **Session 8 (database CRUD).** Today's
  `POKEMON` dict becomes a real database table.
  Same patterns; data lives in SQLite.
- **Session 9 (user accounts).** `/users/<username>`
  becomes "show *that* user's profile."
- **Phase 7 callback:** the URL pattern matches
  every dynamic site they've used.
- **Career-long callback:** routing + URL
  parameters = the foundation of every web app.
  Next week's templates round it out.
- **Peanut butter callback opportunity:** the
  type-converter mismatch (`<int:n>` with
  `5.5`) → silent 404 is a precision moment.
  Code does what you said; URL didn't match.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built Pokemon viewer
- [ ] Pre-built stretches (calculator, type filter)
- [ ] Projector
- [ ] Class roster
