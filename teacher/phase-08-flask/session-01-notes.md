## Session 1 — Teacher Notes

*Phase 8, Flask · Session 1 of 13 · Title: Welcome
to Flask — your first server*

### Purpose of this session

Phase 8 opener — the back-end pivot. Five jobs, in
priority order:

1. **Land "the server runs your code on every
   request."** Conceptual core of the back-end.
2. **Land the request-response cycle.** Browser
   asks; server answers. Both directions matter.
3. **Land `@app.route` as the bridge.** URL ↔
   Python function.
4. **Get every kid's first server running.** Hands
   on the keyboard, browser hitting localhost.
5. **Set up Sessions 2-3** (more routes,
   templates).

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask
  installed (test ahead of time).
- Pre-built multi-page hello-world site for demo.
- Pre-built JSON-returning route for the stretch.
- The exact `pip install flask` command on the
  projector — kids will need to type it.

**Prep time:** ~20 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and Phase 8 framing** (~10 min). Last
  phase. Back-end. Server runs your code.
- **Part A: install + first server** (~25 min).
  `pip install flask`, type the hello world,
  run, visit in browser.
- **Part A: more routes** (~15 min).
- **Break** (~5 min).
- **Part B: real HTML responses** (~25 min).
- **Wrap-up** (~10 min). JSON / random as
  stretches.

If running short, **drop the JSON stretch.** The
multi-page site (Part B) is the priority.

### Teaching the framing

#### "Last phase, biggest concept"

Open with stakes:

> "This is the last phase of the curriculum.
> Phase 7 ended with your sites on the internet —
> *static* sites, no per-user logic.
>
> Phase 8 changes that. Today you write code that
> runs *on a server*. Multiple users hit it.
> Different users see different things. Real apps.
>
> Same Python you've known since Phase 3. New
> library: Flask. New runtime: server."

#### Request-response cycle on the board

Draw it:

```
    BROWSER                    SERVER
       │                          │
       ├─── GET /about ──────────▶│
       │                          │ (Python runs)
       │                          │
       │◀──── 200 OK ────────────┤
       │      <html>...</html>    │
       │                          │
   (display)                       │
```

Frame:

> "The browser sends a *request* — usually 'GET this
> URL.' The server runs *some code* and sends back
> a *response*. The browser displays whatever came
> back. *That is every web interaction in
> existence.*"

This frame is foundational. Reference it often.

### Teaching Part A

#### `pip install flask`

Walk through. Kids may hit:

- **`pip` not found** — try `pip3` or `python -m pip
  install flask`.
- **Permission denied** — try `pip install --user
  flask`.
- **Network blocked** (school/church) — pre-install
  before class on every machine if needed.

Test on every machine before class if possible. PIP
issues will eat 20 minutes of class time otherwise.

#### Type the hello world

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, web!"

if __name__ == "__main__":
    app.run(debug=True)
```

Type on projector. Pause to discuss:

- **`Flask(__name__)`** — "make an app." Don't
  drill `__name__`; it's just required boilerplate.
- **`@app.route("/")`** — "this function handles
  the URL `/`." Decorator syntax (kids saw `@`
  briefly in Phase 4 testing). Don't dwell.
- **`def home():`** — the route handler function.
  Name doesn't matter; URL matters.
- **`return "..."`** — the response body. Plain text
  becomes the page (browser displays as-is).
- **`app.run(debug=True)`** — start the server.
  `debug=True` enables auto-reload + helpful
  errors.

Run. Open browser. **Hello, web!**

#### `127.0.0.1` vs `localhost`

Mention briefly:

> "Both mean *this machine*. Just shortcuts. The
> server runs on your computer; your browser
> connects to your computer."

The `:5000` is the port. Don't go deep.

#### Auto-reload is magical

Edit the return string. Save. The terminal shows
"Detected change... reloading." Reload browser.
Change appears.

> "*This* is the dev loop. Edit Python, save,
> reload page. The server restarts itself."

#### Add routes incrementally

Each new route = new function with `@app.route`.

```python
@app.route("/about")
def about():
    return "..."
```

Show the URL in the browser. **Each route is its
own page.** Real multi-page server.

The function name doesn't have to match the URL,
but it's good practice.

### Teaching Part B

#### "HTML inside Python is ugly"

Frame this honestly:

> "Returning HTML as a Python multi-line string
> *works*. But it's ugly. Hard to read. Hard to
> change.
>
> Templates fix this — separate `.html` files Flask
> reads. We get there in Session 3. Today: just
> see that you *can* return any HTML you want."

The shared `PAGE_STYLE` and `NAV` constants show
the *problem* templates solve. Don't apologize for
the ugliness — name it.

#### F-strings for HTML

```python
return f"""
<html>
<head><title>{title}</title>{PAGE_STYLE}</head>
<body>
    {NAV}
    <h1>{heading}</h1>
</body>
</html>
"""
```

F-strings = Python interpolation in HTML. *Works*
but is fiddly with escaping. Templates (Session 3)
are cleaner.

#### JSON as a stretch

The `from flask import jsonify` + `return
jsonify({...})` shows that responses don't have to
be HTML. Real-world routes often return JSON for
API consumers.

Frame:

> "Phase 7 used `fetch` to call APIs. *You can build
> APIs.* Just return JSON instead of HTML. Same
> route pattern."

This is genuinely empowering — they can build the
back-ends for their own apps.

#### Random joke = back-end's superpower

```python
@app.route("/joke")
def joke():
    return random.choice(JOKES)
```

Reload. Different joke. Reload. Different.

> "*That's* the back-end. Code runs on every
> request. Responses can be different. The browser
> can't do this on its own — it just renders what
> arrives."

This frames "why have a back-end" cleanly.

### Common stumbles

- **`pip install flask` fails.** Network, permissions,
  or wrong pip. Walk through.
- **`ModuleNotFoundError: No module named 'flask'`.**
  Installed for wrong Python version. `python -m
  pip install flask` ensures install matches the
  Python you're running.
- **`OSError: [Errno 98] Address already in use`.**
  Another Flask server is running on port 5000.
  Stop it (Ctrl+C in old terminal) or change port:
  `app.run(debug=True, port=5001)`.
- **Browser shows raw text instead of HTML.** The
  return value isn't being interpreted as HTML.
  Add `<!DOCTYPE html>` and full HTML structure.
  (Browsers are usually forgiving but render
  weirdly without it.)
- **404 on a route.** Typo in the URL or in
  `@app.route`. Trailing slash matters: `/about`
  vs `/about/`.
- **Changes don't appear.** `debug=True` missing;
  server didn't reload. Or browser cached. Hard
  reload.
- **Server stopped, browser shows "can't reach
  page."** Restart with `python app.py`.
- **Forgot `if __name__ == "__main__":`** —
  `app.run()` outside it can cause issues with
  some run methods. Just include it.
- **Indentation errors.** Python rules apply. Walk
  through.
- **Returning a non-string.** Returning a dict or
  list directly works in newer Flask (auto-jsonifies)
  but explicit `jsonify(...)` is clearer.

### Differentiation

- **Younger kids (9-10):** Goal is the basic
  hello-world server + 2-3 plain text routes.
  Real HTML is a stretch.
- **Older kids (12+):** Push for the multi-page
  site with shared style.
- **Advanced (any age):** Suggest:
  - JSON API route
  - Random response (joke, fact, color)
  - Read request data (user_agent, headers)
  - Custom 404 page
  - Multiple servers on different ports
- **Struggling:** A kid who can't get the server
  running is the kid you focus on. Most common
  cause: pip install issue, or syntax error in
  app.py.

### What to watch for

- **The "I wrote a server!" reaction.** Real moment.
- **Buddies showing each other their pages on each
  other's URLs** (won't work — localhost is
  per-machine). Mention this; deployment in
  Session 12 fixes it.
- **Kids excited about JSON** — "I can build my
  own API?" Yes.
- **Frustration with HTML-in-Python ugliness.** Yes.
  Templates fix it.
- **The "what's the difference between Flask and
  what I built in Phase 7?" question.** Phase 7
  was the *front-end* (HTML/CSS/JS); Flask is
  the *back-end* (Python on a server). The
  full-stack split.
- **Kids thinking the URL is shareable** —
  reassure: "this is just on your machine.
  Session 12 makes it public."

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 2 (routes + parameters).** Today's
  static routes become dynamic.
- **Session 3 (templates).** The "ugly HTML in
  strings" gets fixed.
- **Session 5 (forms).** The browser can *send
  data* via POST. Server processes.
- **Session 12 (deployment).** The local server
  becomes a public URL.
- **Phase 7 callback:** their `fetch` calls
  could hit a Flask server they wrote. Full-stack
  unlocked.
- **Career-long callback:** Flask is real
  production tech. Powers Instagram, Pinterest
  (parts of), tons of internal tools, plus
  countless personal projects.
- **Peanut butter callback opportunity:** the
  `pip install flask` for the wrong Python
  version is a real precision moment. The
  computer installed exactly what you said,
  just for the wrong interpreter.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built multi-page hello-world
- [ ] Pre-built JSON example
- [ ] Tested `pip install flask` on every machine
- [ ] Projector
- [ ] Class roster
