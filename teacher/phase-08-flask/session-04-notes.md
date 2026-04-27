## Session 4 — Teacher Notes

*Phase 8, Flask · Session 4 of 13 · Title: Static
files and base templates*

### Purpose of this session

Production shape. Five jobs, in priority order:

1. **Land `static/` folder convention.** CSS, JS,
   images live there.
2. **Land `url_for('static', filename='...')`.**
   The right way to link static files.
3. **Land template inheritance.** `{% extends %}`
   and `{% block %}`. The single biggest
   organizational tool in Jinja.
4. **Land "one source of truth" for shared
   layout.** Change navbar in `base.html`, every
   page updates.
5. **Set up Session 5 (forms).** Today's clean
   templates make form pages easier.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built example with static CSS + base
  template + 3 child pages.
- An example image to drop into `static/`.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 3.
- **Part A: static files + url_for** (~25 min).
- **Break** (~5 min).
- **Part B: base template + extends/block** (~40 min).
- **Wrap-up** (~15 min).

If running short, **drop `{% include %}` and
`block.super()` stretches.** Base + child
template inheritance is the priority.

### Teaching Part A

#### `static/` is convention

Just like `templates/`, the folder name matters:

> "Flask serves anything in `static/` automatically,
> at URLs starting with `/static/`. Put your CSS,
> images, JS files there. *Don't* invent your own
> folder name."

Show the folder structure on the projector. Most
projects have:

```
static/
├── style.css
├── script.js (if used)
├── images/
│   └── ...
└── fonts/ (if used)
```

#### Why `url_for` over hardcoding

Frame:

> "You *could* write `<link href='/static/style.css'>`.
> Works fine on localhost.
>
> But `{{ url_for('static', filename='style.css') }}`
> is the *right* way. Why? Because real apps get
> deployed to all sorts of URLs — sometimes at
> `example.com/myapp/`, not `example.com/`. URLs
> shift. `url_for` adjusts automatically.
>
> Habit: *always* use `url_for` for static and
> route URLs."

The discipline matters more than the immediate
benefit.

#### `url_for` syntax

```html
{{ url_for('static', filename='style.css') }}
```

Two parts:

- **First arg** — view name (`'static'` is a
  built-in).
- **`filename=`** — the path inside `static/`.

For files in subfolders:

```html
{{ url_for('static', filename='images/logo.png') }}
```

#### Inspect in browser

Open DevTools → Network. Reload. Show:

- The HTML page request.
- The CSS file request (separate).

> "Two requests. The browser asks for the page
> first, sees the `<link>`, asks for the CSS,
> applies it. *That's how every styled page
> works.*"

### Teaching Part B

#### "Stop copy-pasting the boilerplate"

Frame:

> "Every page so far has the same DOCTYPE, HTML,
> head, navbar boilerplate. Two pages? Manageable.
> Five? Tedious. Ten? Nightmare.
>
> Template inheritance fixes this. *One* file with
> the shared structure (`base.html`). Each page
> just provides the *unique* content."

#### Build base.html on the projector

Type live:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2026</p>
    </footer>
</body>
</html>
```

Frame each block:

> "`{% block title %}My Site{% endblock %}` says:
> 'this is a *fillable spot* called title. Default
> content is "My Site". Children can replace it.'
>
> Same for content. Empty default; children fill
> in."

#### Build a child template

```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<h1>Welcome</h1>
<p>Hello!</p>
{% endblock %}
```

Walk through:

> "`{% extends 'base.html' %}` *must* be the first
> non-comment line. Says: I'm based on this.
>
> Then any `{% block %}` defined here *replaces*
> the matching block in the base."

Render. The page has the navbar, footer, **and**
the new content.

#### Demo "change once, update everywhere"

Edit `base.html`. Change the navbar. Save. Reload
multiple pages. **All updated** — you only
changed one file.

> "*That's* the win. Single source of truth."

#### `url_for` for routes

If time:

```html
<a href="{{ url_for('about') }}">About</a>
```

Frame:

> "Same `url_for`, but for *your routes* instead of
> static files. The first arg is the function name
> from `def about():`.
>
> Why? If you rename the route URL but not the
> function, `url_for` still finds the right URL.
> If you rename the function, you'd have to update
> the `url_for` calls — but at least Flask errors
> noisily.
>
> Either way: better than scattered hardcoded
> URLs."

### Teaching the stretches

#### `{% include %}` for partials

If time, show:

```html
{# _card.html #}
<div class="card">
    <h3>{{ title }}</h3>
</div>
```

```html
{% include "_card.html" %}
```

Frame:

> "Partials are pieces — not full pages. Underscored
> filename signals 'this isn't a page on its own,
> just a chunk to include elsewhere.'"

Don't drill — preview only.

### Common stumbles

- **Static file 404.** Wrong folder name (must be
  `static/`), or wrong filename in `url_for`.
- **CSS not applying.** Hard reload (Ctrl+Shift+R).
  Or wrong selector for the HTML.
- **`url_for` syntax wrong.**
  `url_for(static, filename=style.css)` (no
  quotes) — error. Need quotes.
- **Forgot `{% extends %}` line.** Child renders
  as standalone — no base content.
- **`{% extends %}` not first.** Must be the
  first thing.
- **Block name mismatch.** Defined `{% block content %}`
  in base but `{% block contents %}` in child —
  silent failure (block isn't filled, default
  shown).
- **Forgot `{% endblock %}`.** Jinja error.
- **Multiple inheritance attempts.** Templates
  can only `extends` one base. (Use `{% include %}`
  for composition instead.)
- **Image not in `static/`.** Forgot to move/copy.

### Differentiation

- **Younger kids (9-10):** Goal is the basic
  static CSS + one base + one child. Don't push
  past that.
- **Older kids (12+):** Push for 3+ pages
  inheriting base + `url_for` for routes.
- **Advanced (any age):** Suggest:
  - Multiple `{% block %}` (title, content,
    extra_head)
  - `{% include %}` for partials
  - `block.super()` for appending
  - Custom error templates (`templates/404.html`)
  - Favicon
  - Mobile-responsive base layout
- **Struggling:** A kid who can't get the static
  CSS loading is the kid you focus on. Most
  common cause: wrong folder name, or
  `url_for` syntax.

### What to watch for

- **The "I changed one file, every page
  updated" reaction.** Real moment.
- **Buddies refactoring each other's sites** to
  use base templates. Encourage.
- **Kids skipping `url_for`** because hardcoded
  works. Push the discipline.
- **Kids over-inheriting** — multiple levels of
  base templates. Mention "you *can*, but most
  sites have just one or two levels."
- **CSS Phase 7 muscle memory.** They already
  know flexbox and the box model. Reaffirm —
  same skills apply here.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 5 (forms).** Forms are usually their
  own template extending the base.
- **Session 8 (database).** Templates render
  database-driven content within the base
  layout.
- **Session 10 (notes app).** The notes app uses
  base + content blocks heavily.
- **Phase 7 callback:** they wrote multi-page
  static sites with shared CSS. Today: same
  pattern, generated.
- **Career-long callback:** template inheritance
  is universal. Django, Rails, Laravel, even
  React's component composition — same idea.
- **Peanut butter callback opportunity:** the
  block-name typo (`content` vs `contents`) is
  a precision moment. Silent failure — block
  isn't filled.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built static + base template example
- [ ] Sample image for static demo
- [ ] Projector
- [ ] Class roster
