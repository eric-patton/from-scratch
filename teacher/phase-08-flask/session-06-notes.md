## Session 6 — Teacher Notes

*Phase 8, Flask · Session 6 of 13 · Title: Sessions
and flash messages*

### Purpose of this session

The "the server remembers you" session. Five jobs,
in priority order:

1. **Land "HTTP is stateless."** Why sessions exist.
2. **Land Flask `session` as a per-visitor dict.**
   Different from Python's "session" in other
   contexts.
3. **Land SECRET_KEY.** Required, simple, security
   foundation.
4. **Land flash messages.** Perfect post-redirect
   feedback mechanism.
5. **Set up Sessions 7-8** (databases). Sessions
   remember per-visitor; databases store
   *everyone's* data.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built session "remember me" demo.
- Pre-built guestbook with flash messages.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 5
  forms.
- **Part A: stateless HTTP + sessions** (~30 min).
- **Break** (~5 min).
- **Part B: flash messages + guestbook
  enhancement** (~40 min).
- **Wrap-up** (~10 min).

If running short, **drop the visit-counter and
permanent-session stretches.** Base session +
flash is the priority.

### Teaching Part A

#### "HTTP is stateless"

Frame:

> "Every request is independent. The server has no
> idea this is the same visitor as a moment ago.
> No memory between requests.
>
> *That's a problem.* How do you remember someone
> typed their name? How do you keep a shopping
> cart? How do you stay logged in?
>
> Solution: *cookies* — small bits of data the
> server gives the browser, the browser sends back
> with every request. *Sessions* are a managed
> cookie that Flask handles for you."

#### Cookies in DevTools

Show:

1. Open DevTools → Application → Cookies.
2. Visit a real site (Wikipedia, etc.). See the
   cookies they set.

> "Real sites use cookies for everything — login,
> preferences, tracking. Today you learn to use
> them yourself."

#### `session` looks like a dict

Frame:

> "Flask's `session` is a *dict-like object* that
> persists across requests for one visitor. Same
> API as a Python dict — `session['name']`,
> `session.get(...)`, `session.pop(...)`.
>
> But its data is stored in a *signed cookie* sent
> back and forth. Flask handles the encoding."

#### `SECRET_KEY` is required

```python
app.secret_key = "anything"
```

Frame:

> "Flask uses the secret key to *sign* the session
> cookie. Without it, a malicious user could edit
> the cookie to claim to be anyone. The signature
> prevents tampering.
>
> For class: any string works. For real apps: long
> random string from a config file or environment
> variable. *Never check the real key into Git.*"

If a kid asks "why?": tell them tampering. The
secret is the proof of authenticity.

#### "Remember me" demo

Walk through:

1. Visit `/` — "Hello, stranger."
2. Submit name — `session['name'] = name`,
   redirect.
3. Page loads — `session.get('name')` returns the
   name.
4. Reload — still there.
5. Close tab, reopen — still there (within
   session lifetime).
6. Click "Forget me" — `session.pop`, gone.

Show DevTools cookie throughout. The encoded blob
is the session. Edit it manually → Flask rejects.

#### Sessions are per *browser*, not per *user*

Frame:

> "Sessions don't know who you are — they know
> *this browser*. Open a different browser, you're
> a fresh visitor. Open incognito, fresh visitor.
>
> Real user accounts (Session 9) tie sessions to
> *people* via a database lookup."

### Teaching Part B

#### "Flash messages = one-shot notifications"

Frame:

> "After a form POST, you redirect. The redirect
> is a fresh GET — no form data, nothing to show
> a 'success' message from. The session would
> work, but you'd have to clear the message
> manually after showing it.
>
> *Flash messages* automate this: store, show
> once, auto-clear. Built into Flask."

#### `flash` and `get_flashed_messages`

Walk through:

```python
flash("Saved!")
return redirect(url_for("home"))
```

```html
{% with messages = get_flashed_messages() %}
    {% for m in messages %}
    <li>{{ m }}</li>
    {% endfor %}
{% endwith %}
```

> "Flash on the POST. Display in the template.
> The `get_flashed_messages()` call retrieves *and
> removes* — they only show once.
>
> If no flash → no messages → nothing renders."

#### `with_categories=true`

Categories are huge for styling:

```python
flash("Posted!", "success")
flash("Wrong format.", "error")
```

```html
{% for category, msg in messages %}
<li class="flash flash-{{ category }}">{{ msg }}</li>
{% endfor %}
```

CSS:

```css
.flash-success { background: lightgreen; }
.flash-error { background: lightcoral; }
```

> "Two-tuple unpacking — the message comes back as
> `(category, text)`. Use the category as a class,
> style with CSS."

#### Flash display in `base.html`

The placement matters:

> "Put the flash display in `base.html` — every
> page automatically shows pending flashes. Then
> any route that does `flash(...)` followed by
> redirect → user sees the message on the next
> page.
>
> *That's the magic.* No per-page setup. Universal
> notification system."

#### Update the guestbook

Live build:

```python
flash("Both fields required.", "error")
# OR
flash("Message posted!", "success")
```

Submit empty → red error. Submit valid → green
success. Reload after success → flash gone.

> "*That's* real UX. Every form-processing route
> uses this pattern."

### Common stumbles

- **`RuntimeError: secret key not set`.** Forgot
  `app.secret_key`. Add it.
- **Session doesn't persist.** Browser blocking
  cookies, or different browser tabs not sharing.
  (Most browsers share between tabs in the same
  window.)
- **Session stale.** Edited the secret key →
  invalidates all existing sessions. Restart =
  fresh sessions.
- **`flash()` not showing.** Template doesn't
  call `get_flashed_messages()`. Or it's in a
  template that *isn't* rendered after the
  redirect.
- **Categories ignored.** Forgot
  `with_categories=true` in
  `get_flashed_messages`.
- **Flash shows twice.** Called `flash` twice for
  the same message. Or template calls
  `get_flashed_messages` twice.
- **Session storing too much.** Cookie is
  size-limited (~4KB). Don't put big lists in
  session — use database.
- **Session security misconception.** Sessions are
  *signed* (anti-tamper) but not *encrypted*
  (visible if intercepted). Don't put secrets in
  sessions.
- **Cookie blocked by browser.** Privacy modes
  may block. Tell user; or test in normal mode.

### Differentiation

- **Younger kids (9-10):** Goal is the basic
  remember-name demo. Flash + categories are
  stretches.
- **Older kids (12+):** Push for the full
  guestbook with flash messages.
- **Advanced (any age):** Suggest:
  - Permanent sessions
  - Visit counter via session
  - Theme preference (dark/light) in session
  - Session-based shopping cart
  - Multiple flash categories with custom styling
- **Struggling:** A kid who can't get session
  working is the kid you focus on. Most common
  cause: forgot `app.secret_key`, or
  cookies blocked.

### What to watch for

- **The "the server remembers me!" reaction.**
  First successful session = real moment.
- **Cookie inspection in DevTools.** Some kids
  will try to decode the cookie value. Real
  curiosity.
- **Buddies sending links to each other** — they
  realize sessions don't transfer (different
  browsers).
- **Excitement about flash messages.** Real UX
  feel.
- **Kids putting passwords in sessions.** Strongly
  redirect — sessions are visible. Use Session 9's
  password hashing instead.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 7 (SQLite).** Persistent storage —
  database survives restarts. Sessions are
  per-visitor; databases are app-wide.
- **Session 9 (accounts).** Login uses session
  to track who's logged in (`session['user_id']`).
- **Session 10 (notes app).** Per-user notes via
  session + database.
- **Phase 7 callback:** localStorage was browser-
  side persistence. Sessions are server-side
  per-visitor.
- **Career-long callback:** session management is
  in every web framework. Same shape across
  Django, Rails, Express, etc.
- **Peanut butter callback opportunity:** the
  forgot-`secret_key` runtime error is a precision
  moment. Flask refuses to use sessions without
  it.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built remember-me demo
- [ ] Pre-built guestbook with flash
- [ ] DevTools Application tab familiar
- [ ] Projector
- [ ] Class roster
