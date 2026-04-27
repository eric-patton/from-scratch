## Session 5 — Teacher Notes

*Phase 8, Flask · Session 5 of 13 · Title: Forms
and POST requests*

### Purpose of this session

The "data flows the other way" session. Five jobs,
in priority order:

1. **Land GET vs POST distinction.** Read vs send.
2. **Land `methods=["GET", "POST"]` + the
   single-route pattern.** Same URL, different
   behavior based on method.
3. **Land `request.form.get(...)`.** Read submitted
   data.
4. **Land POST-Redirect-GET.** The standard pattern
   that prevents the resubmit warning.
5. **Land server-side validation.** Never trust the
   browser.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built guestbook (Part B end-state).
- Pre-built version with validation + form state
  preservation.

**Prep time:** ~20 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 4.
- **Part A: GET vs POST + `request.form`** (~25 min).
- **Part A: build the simple form** (~15 min).
- **Break** (~5 min).
- **Part A: POST-Redirect-GET + guestbook** (~20 min).
- **Part B: validation** (~15 min).
- **Wrap-up** (~5 min).

If running short, **drop file uploads and
multi-value field stretches.** The base guestbook
+ validation is the priority.

### Teaching the framing

#### "First time the user changes the server"

Open with stakes:

> "Until now, the user *reads* what's on your
> server. They visit pages. They navigate. But
> they don't *change* anything.
>
> Today: forms. The user fills out a form, hits
> submit, the server *receives* their data,
> *processes* it, *stores* it (in memory, for
> now). The web becomes interactive."

This shift matters. Drive it home.

### Teaching Part A

#### GET vs POST on the board

Diagram:

```
GET                          POST
───                          ────
"Give me /about"             "Here's some data,
No body                       process it"
URL only                     Has a body (form fields)
Caching OK                   Don't cache
Idempotent                   Side effects expected
                             
Used by: links,              Used by: form submits,
URL bar                      file uploads
```

Frame:

> "GET is for *fetching* — links, bookmarks,
> typing URLs. POST is for *changing things* —
> form submits, file uploads, anything where the
> server *does something* in response.
>
> Same URL can handle both. We tell Flask which
> methods to accept."

#### `methods=["GET", "POST"]`

```python
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # process form
    else:
        # show form
```

Frame:

> "Default is GET only. List the methods you want
> the route to accept. Then *inside* the function,
> check which method came in and behave accordingly."

#### `request.form` reads submitted data

```python
name = request.form.get("name")
```

Frame:

> "When a form is submitted, the data is in
> `request.form` — a dict-like object. Keys match
> the `name=` attributes on the inputs.
>
> Use `.get('name')` for safety — returns `None` if
> missing, instead of crashing."

The matching: **HTML `name` attribute = `request.form`
key.** Common mismatch.

#### Build the simple echo form

Type live:

```python
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        return f"<h1>Hi, {name}!</h1>"
    return "<form method='post'><input name='name'><button>Send</button></form>"
```

Save. Visit. See the form. Type a name. Submit.
"Hi, Alex!" **First successful POST.**

Pause for the moment.

#### POST-Redirect-GET — the canonical pattern

Show the resubmit problem:

1. Submit form.
2. URL is `/`, but page shows the result.
3. Refresh. Browser asks "resubmit form data?"

Frame as a real bug:

> "If the user refreshes after a POST, the browser
> *resubmits* the form. They get a duplicate. *Bad.*
>
> Fix: after processing, *redirect* — tell the
> browser to GET another URL. The redirect = a
> fresh GET, no form data, no resubmit risk."

```python
return redirect(url_for("home"))
```

Frame:

> "POST → process → redirect → GET → page. The
> standard pattern. *Memorize it.* Every form
> route uses it."

#### Build the guestbook

Live build with `messages = []` storage. Submit
multiple times. Each one appears. Refresh — no
resubmit warning. Real interactive page.

#### "Messages disappear on restart"

Frame:

> "Stop the server. Restart it. *Messages gone.*
> Why? `messages = []` is a Python variable in
> memory. When the program restarts, memory is
> fresh.
>
> Real apps store data in a *database* — survives
> restarts, survives deploys, lives forever. That's
> Sessions 7-8."

Sets up the database arc.

### Teaching Part B

#### Server-side validation

Frame:

> "Browser-side `required` is *suggestion-level*
> protection. Bad guys can bypass it. *Always*
> validate on the server."

Show:

```python
if not name or not message:
    error = "Name and message are required."
elif len(message) > 500:
    error = "Message must be under 500 characters."
else:
    # process
```

Each branch:

- Validate input.
- Set error on bad input.
- Process on good input.

#### Preserve form state on error

Real UX matters:

> "If the user typed a paragraph and got an error,
> *don't* clear it. Pass the values back to the
> template. Show them in the inputs."

```python
return render_template("form.html",
                       name=name,
                       message=message,
                       error=error)
```

```html
<input value="{{ name|default('') }}">
<textarea>{{ message|default('') }}</textarea>
```

The `|default('')` filter: empty string if `name`
isn't passed (e.g., on first GET).

### Common stumbles

- **Forgot `methods=["POST"]`.** Submit returns
  "Method Not Allowed." Add POST.
- **`request.form.get("nme")`** — typo in key.
  Returns None.
- **Mismatch between input `name` and
  `request.form.get`.** Walk through.
- **POST without redirect.** Refresh → resubmit
  warning.
- **Redirect to wrong route.** `redirect(url_for("hom"))`
  — typo.
- **Form's `method` missing or wrong.** Defaults
  to GET. Add `method="post"` (case-insensitive).
- **CSRF errors.** With Flask-WTF, sometimes
  enabled by default. We're not using it; if a
  kid copies external tutorial code, may hit
  this.
- **Empty form submits go through.** Validation
  missing or insufficient.
- **`request.form` empty.** Form action wrong, or
  not POSTed (form's `method` is GET).
- **Lost form state.** Forgot to pass values back
  on error.
- **HTML escaping in textarea.** Multi-line content
  with HTML chars. Auto-escape handles it.

### Differentiation

- **Younger kids (9-10):** Goal is the simple
  echo form. Guestbook is a stretch.
- **Older kids (12+):** Push for the full
  guestbook + simple validation.
- **Advanced (any age):** Suggest:
  - Form state preservation
  - Multi-input forms with checkboxes/selects
  - Multi-route variant (separate show/process)
  - Delete-message form
  - Edit form for existing messages
  - File uploads
- **Struggling:** A kid who can't get the form
  data appearing is the kid you focus on. Most
  common cause: input `name` mismatch, or
  forgot `methods=["POST"]`.

### What to watch for

- **The "I sent data to my server!" reaction.**
  Real moment.
- **Buddies submitting silly messages to each
  other's guestbooks.** Encourage. (As long as
  the messages are appropriate — that's a real
  community-management lesson.)
- **The "messages disappear on restart"
  realization.** Foreshadows database.
- **Kids skipping `redirect`.** Push the
  POST-Redirect-GET pattern as non-negotiable.
- **Validation enthusiasm.** Some kids will go
  way deep into validation rules. Encourage
  but timebox.
- **Cross-site issues** — kids trying to submit
  *each other's* forms via dev tools. Real
  conversation about CSRF (which we're not
  formally teaching but worth mentioning).

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 6 (sessions + flash).** "Message
  posted!" notification on the next page load.
- **Sessions 7-8 (database).** Persistent storage
  — messages survive restarts.
- **Session 9 (accounts).** Login forms,
  signup forms.
- **Session 10 (notes app).** Forms + auth +
  database = real app.
- **Phase 7 callback:** they styled forms with
  CSS. Same form HTML, now wired to a server.
- **Career-long callback:** form processing is
  *the* core of every web app. Same pattern
  everywhere.
- **Peanut butter callback opportunity:** the
  input-name mismatch (`name="message"` but
  `request.form.get("messege")`) is a precision
  moment. Code does what you wrote.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built guestbook
- [ ] Pre-built guestbook with validation
- [ ] Projector
- [ ] Class roster
