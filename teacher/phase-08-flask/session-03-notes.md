## Session 3 — Teacher Notes

*Phase 8, Flask · Session 3 of 13 · Title: Templates
— Jinja2*

### Purpose of this session

Kill the HTML-in-strings ugliness. Five jobs, in
priority order:

1. **Land `templates/` folder convention.** Flask's
   default location.
2. **Land `render_template("name.html", **kw)`.**
   The standard pattern for every dynamic route.
3. **Land Jinja's two syntaxes.** `{{ value }}`
   for output, `{% block %}` for control flow.
4. **Land auto-escaping = security.** Default-safe
   for user data.
5. **Refactor an existing app.** Take Session 2's
   Pokemon viewer; rebuild with templates. Same
   site, much cleaner code.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built Pokemon viewer with templates (the
  Part B end-state).
- Pre-built example showing auto-escaping
  (`/hello/<script>alert</script>`) — to demo XSS
  protection.
- Optional: Pre-built `extends`/`block` example for
  the stretch.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 2.
- **Part A: first template + render_template** (~20 min).
- **Part A: loops, conditionals, filters** (~20 min).
- **Break** (~5 min).
- **Part B: refactor Pokemon viewer** (~30 min).
- **Wrap-up** (~10 min).

If running short, **drop the `extends`/`block`
preview** — it's covered in Session 4.

### Teaching Part A

#### "HTML lives in HTML files"

Frame:

> "Last session, we returned HTML as Python strings.
> Worked, but ugly. Hard to read. Hard to edit.
> *Templates fix this.*
>
> A template is a `.html` file. It looks like
> normal HTML, but with placeholders Flask fills
> in. The Python code says 'render this template
> with these values'; Flask reads the file,
> substitutes the values, returns the result."

#### `templates/` folder

Show creating it:

```
my_app/
├── app.py
└── templates/
    └── home.html
```

Frame:

> "Flask looks for templates in a folder called
> `templates/` — exactly that name, exactly that
> location. It's a convention. *Don't fight it.*"

The convention matters. Get it wrong, Flask errors
with "TemplateNotFound."

#### `render_template`

```python
from flask import render_template

return render_template("home.html",
                       title="My Site",
                       heading="Welcome!")
```

Frame:

> "Three things: filename (relative to `templates/`),
> then keyword arguments. Each kwarg becomes a
> variable available in the template."

Walk through the matching:

```python
render_template("x.html", name="Alex")
```

```html
<h1>Hi, {{ name }}!</h1>
```

> "`name` in Python becomes `{{ name }}` in the
> template. Match the variable names."

#### Two Jinja syntaxes

Drill the distinction:

```html
{{ value }}     <!-- output a value -->
{% block %}     <!-- control flow -->
```

> "Two curly braces (`{{ }}`) for *output* — show
> me this value. Curly + percent (`{% %}`) for
> *control* — loops, ifs, blocks. Both kinds.
> Different purposes."

Common mix-up: kids try `{{ for x in items }}` —
which doesn't work (output syntax for control).

#### Loops + conditionals

The shape:

```html
{% for x in items %}
    ...
{% endfor %}

{% if condition %}
    ...
{% else %}
    ...
{% endif %}
```

Every opening needs an `endfor` / `endif`. Forgot
the closing tag = template error.

> "Same logic as Python — for, if, else. Different
> syntax — wrapped in `{% %}` and explicitly
> closed."

#### Filters

```html
{{ name|upper }}
{{ items|length }}
{{ price|round(2) }}
```

Frame:

> "Filters modify values *in the template*. Saves
> writing helper functions in Python. The pipe `|`
> is the filter operator — like `value | filter`."

Show 3-4 useful ones. Don't drill all of them.

#### Auto-escaping

The security angle:

> "By default, Jinja *escapes* values. If a user
> name is `<script>alert('xss')</script>`, the
> template shows that as literal text — not as a
> running script. *Free protection from XSS attacks.*
>
> If you actually want HTML to render, use
> `|safe` — but only for trusted content. Never
> for user data."

Demo: route a name parameter through the template,
visit `/hello/<script>alert(1)</script>`. The
script tag shows as text. Reassuring.

### Teaching Part B

#### The refactor sequence

Walk through:

1. Make `templates/` folder.
2. Move HTML out of Python into `index.html` and
   `pokemon.html`.
3. Replace concatenated strings with `{{ ... }}`
   and `{% for %}`.
4. Update `app.py` to call `render_template`.
5. Run; site should look identical.

Show the *before* (Session 2 version) and *after*
(template version) side-by-side. The Python file
shrinks dramatically.

> "Same site. *Way* cleaner code. The HTML lives
> in HTML files where editors can syntax-
> highlight; the Python lives in Python where
> it's tiny and focused."

#### Auto-escape in the Pokemon viewer

After refactor, demo: visit `/pokemon/<script>`.
Flask's auto-escape kicks in. The "missing
Pokemon" page shows the script tag as text, not
runs it. Real protection.

#### `extends` / `block` preview

If time:

```html
{# base.html #}
<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

{# index.html #}
{% extends "base.html" %}
{% block content %}
<h1>...</h1>
{% endblock %}
```

Frame as a teaser:

> "Both pages have the same `<!DOCTYPE>` and
> `<html>` boilerplate. We can extract it. *Next
> session* — full template inheritance."

### Common stumbles

- **`TemplateNotFound`.** File isn't in
  `templates/`, or wrong name. Walk through.
- **Mix-up of `{{ }}` and `{% %}`.** Use output
  for control or vice versa. Walk through.
- **Forgot `{% endfor %}` or `{% endif %}`.**
  Jinja errors.
- **Variable not passed.** Used in template but
  not in `render_template` kwargs. Jinja shows
  empty (or errors with `strict_undefined`).
- **Spelling mismatch.** `name=` vs `{{ Name }}`.
- **Imported but didn't use.** `from flask import
  render_template` then never called.
- **HTML inside `{{ }}`.** `{{ <p>foo</p> }}` —
  syntax error.
- **Auto-escape unwanted.** Trying to render HTML
  from a friendly source. Use `|safe`.
- **Filter typo.** `{{ name|uppr }}` — silent
  failure or error.
- **Comment confusion.** `<!-- HTML -->` shows in
  the output; `{# Jinja #}` doesn't. Use the
  right one.

### Differentiation

- **Younger kids (9-10):** Goal is one template
  with one variable. Loops and conditionals are
  stretches.
- **Older kids (12+):** Push for refactored
  Pokemon viewer with loops + conditionals.
- **Advanced (any age):** Suggest:
  - `extends`/`block` preview
  - Custom filter with `@app.template_filter`
  - `{% include %}` for partial templates
  - `with` blocks for scoped variables
  - Macros (Jinja's mini-functions)
- **Struggling:** A kid who can't get the first
  template rendering is the kid you focus on.
  Most common cause: wrong folder name, or
  syntax mix-up between `{{ }}` and `{% %}`.

### What to watch for

- **The "wait, this is so much cleaner" reaction.**
  The Python file shrinking dramatically is a
  visible win.
- **Buddies sharing template tricks.** "Did you
  know about the `|title` filter?" Encourage.
- **Kids over-engineering with Jinja logic.**
  Calculations and complex loops in templates can
  go too far. Push: "if it's complex, do it in
  Python."
- **The `<script>` injection attempt.** Some kids
  will try to break things. Auto-escape catches
  it. Affirm: "Flask is protecting you."
- **Confusion about template variables vs Python
  variables.** They're not the same scope.
  Variables defined in Python are *passed* to the
  template via `render_template`.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 4 (static + base).** Templates +
  shared layouts.
- **Session 5 (forms).** Form processing + render
  templates with errors / messages.
- **Session 8 (database).** Templates render
  database results.
- **Phase 7 callback:** they wrote HTML by hand;
  templates *generate* HTML based on Python data.
- **Career-long callback:** every server-rendered
  framework uses templates (Django, Rails, Laravel,
  etc.). Same shape across languages.
- **Peanut butter callback opportunity:** the
  `{{ }}` vs `{% %}` mix-up is a precision moment.
  Wrong syntax = silent failure or weird error.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built Pokemon viewer with templates
- [ ] Pre-built `<script>` auto-escape demo
- [ ] Optional: `extends`/`block` example
- [ ] Projector
- [ ] Class roster
