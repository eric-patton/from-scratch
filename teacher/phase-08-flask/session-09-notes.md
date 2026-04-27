## Session 9 — Teacher Notes

*Phase 8, Flask · Session 9 of 13 · Title: User
accounts — signup, login, logout*

### Purpose of this session

The "real auth" session. Five jobs, in priority
order:

1. **Land "never store plaintext passwords."**
   Most important security rule of web dev.
2. **Land `generate_password_hash` /
   `check_password_hash`.** Production-grade
   auth in two functions.
3. **Land the auth flow:** signup → INSERT,
   login → SELECT + check, logout → session.pop.
4. **Land `current_user()` + context processor.**
   Universal template access to the logged-in
   user.
5. **Set up Session 10 (notes app).** Today's
   auth becomes the foundation; notes filter by
   user.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny + Flask.
- Pre-built auth app (Part B end-state).
- DB Browser for SQLite to show hashed passwords
  visually.

**Prep time:** ~25 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Sessions
  6-8.
- **Part A: password hashing** (~25 min). The
  rule, the functions, REPL exploration.
- **Break** (~5 min).
- **Part B: build the auth flow** (~45 min).
- **Wrap-up** (~10 min).

If running short, **drop change password and
@login_required stretches.** The base flow
(signup → login → logout) is the priority.

### Teaching Part A

#### "Never store plaintext passwords"

Open with stakes:

> "Single most important security rule of web
> development: *never store passwords as plain
> text.*
>
> Why? Databases get leaked. Hackers steal
> backups. Negligent admins put data on public
> S3 buckets. *Constantly.* In the news monthly.
>
> If your database has plaintext passwords, every
> user's password is exposed. *And many users
> reuse passwords across sites.* Your breach
> becomes their bank's breach.
>
> Solution: store a *hash*. Cryptographic
> one-way scramble."

This isn't fearmongering — it's real. Search
"data breach plaintext passwords" — sites that
got it wrong, every year.

#### "What's a hash"

Diagram:

```
"hello" ──▶ hash function ──▶ "scrypt:32768:..."
                 │
                 ▼
            One-way:
            you can't reverse it
            
"hello" ──▶ hash function ──▶ same hash
```

Frame:

> "Hash function: takes input, outputs a scrambled
> string. *Two key properties:*
>
> 1. **One-way** — can't compute input from hash.
>    No matter how clever, *no way back*.
> 2. **Deterministic** — same input, same hash.
>    Always.
>
> So: hash the password, store the hash. When user
> logs in, hash what they type, compare. *Match
> means correct password — without ever knowing
> the original.*"

#### REPL demo

Walk through in the Thonny shell:

```python
>>> from werkzeug.security import generate_password_hash, check_password_hash
>>> h = generate_password_hash("hello")
>>> h
'scrypt:32768:8:1$abc...long string...'
>>> check_password_hash(h, "hello")
True
>>> check_password_hash(h, "Hello")
False
>>> check_password_hash(h, "")
False
```

Then the salt insight:

```python
>>> generate_password_hash("hello") == generate_password_hash("hello")
False
```

Frame:

> "*Different hashes for the same password!* Why?
> Because the function adds a random *salt*. Even
> if two users have the same password, their hashes
> differ. Prevents 'rainbow table' attacks.
>
> The salt is stored *with* the hash. `check_password_hash`
> reads it, hashes the input the same way, compares."

You don't need to teach salts deeply. Just:
"the function handles it; trust it; use the two
functions, don't roll your own."

#### "Use these functions, don't roll your own"

Real talk:

> "There's a long history of programmers writing
> their own auth and getting it *catastrophically*
> wrong. Use vetted libraries. `werkzeug.security`
> is built into Flask — production-grade, audited.
> *Use it.*"

### Teaching Part B

#### The full app

Walk through the full `app.py` on the projector.
Type live or paste from your prep version.

Key pieces in order:

1. **`init_db()`** — `users` table with `UNIQUE`
   on username.
2. **`current_user()`** helper — read session,
   look up row.
3. **Context processor** — make `current_user`
   available in all templates.
4. **`signup` route** — validate, hash, INSERT,
   handle uniqueness conflict.
5. **`login` route** — find user, check_password_hash,
   set session.
6. **`logout` route** — pop session key.

#### `UNIQUE` + IntegrityError

Walk through:

```python
try:
    conn.execute("INSERT INTO users ...")
except sqlite3.IntegrityError:
    flash("Username already taken.", "error")
```

Frame:

> "The `UNIQUE` constraint on username means SQLite
> *refuses* to insert duplicates — raises
> `IntegrityError`. We catch it and flash the
> error. *The database enforces the rule;* our
> code reports it cleanly."

#### Context processor

```python
@app.context_processor
def inject_user():
    return {"current_user": current_user()}
```

Frame:

> "Returns a dict; every key in the dict becomes
> a variable available in *every* template.
> `current_user` is now usable anywhere — base.html,
> any page — without passing it from each route.
>
> Use sparingly. Common ones: current user,
> site config, navigation data."

#### Walk through templates

Especially `base.html`:

```html
{% if current_user %}
    <span>Logged in as <strong>{{ current_user.username }}</strong></span>
    <a href="{{ url_for('logout') }}">Log out</a>
{% else %}
    <a href="{{ url_for('login') }}">Log in</a>
    <a href="{{ url_for('signup') }}">Sign up</a>
{% endif %}
```

Frame:

> "*The base template handles the auth UI
> universally.* Every page automatically shows the
> right state. No per-page code."

#### Test it together

Live demo:

1. Sign up. **Account created!**
2. Log in. **Welcome back, alex!**
3. Reload. **Still logged in** — session cookie.
4. Log out. **Stranger again.**
5. Wrong password. **Invalid.**
6. Duplicate username. **Already taken.**

Pause for the *real auth working* moment.

#### Inspect hashed passwords

Open `auth.db` in DB Browser for SQLite. Show
the `users` table. **password_hash column is
gibberish** — long encoded strings.

> "*Even if someone steals this file*, the
> passwords are protected. They'd need to *brute-
> force* every hash individually — practically
> impossible for strong passwords."

This is the visceral payoff.

#### `@login_required` decorator (stretch)

If time:

```python
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user():
            flash("Please log in.", "error")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated
```

Frame:

> "Decorator wraps a function with auth check.
> Apply to any route — instantly protected. Real
> production pattern."

Don't drill the decorator mechanics; just show
the pattern.

### Common stumbles

- **Forgot to import `werkzeug.security`
  functions.** ImportError. Add the import.
- **Stored plaintext password.** Either by accident
  (forgot to hash) or by misunderstanding. Catch
  by inspecting the database.
- **`check_password_hash` arguments wrong.** Order
  is `(hash, password)`, not the reverse.
- **Logging in just by setting session manually.**
  Some kids might think "I'll just set
  `session['user_id'] = 1`" — bypassing password
  check. *Show* what real auth does. (Also: don't
  let users craft their own session — Flask signs
  it.)
- **Missing UNIQUE constraint.** Allows duplicate
  usernames. Walk through.
- **Caught wrong exception.** `IntegrityError` is
  specific to constraint violations.
- **Forgot to commit.** INSERT without
  `conn.commit()` — silent failure.
- **Empty password validation missing.** User
  signs up with empty password — hashes empty
  string. Check before hashing.
- **Login form sends username in URL** (GET
  instead of POST). Password visible in browser
  history. Always POST.
- **Forgot `<input type="password">`.** Plaintext
  visible while typing.

### Differentiation

- **Younger kids (9-10):** Goal is signup +
  login working. Skip change-password and
  decorator.
- **Older kids (12+):** Push for the full app +
  `@login_required`.
- **Advanced (any age):** Suggest:
  - Change password route
  - Permanent sessions
  - Account deletion
  - Email field
  - Admin role with `is_admin`
  - Login throttling (basic)
  - JS form validation (Phase 7 callback)
- **Struggling:** A kid who can't get signup
  working is the kid you focus on. Most common
  cause: forgot to hash, or mismatched form
  fields.

### What to watch for

- **The "I have an account!" reaction.** Real
  moment — ownership.
- **Buddies trying to log into each other's
  accounts.** Real attack practice. Should fail.
- **Excitement about the password hash.** Some
  kids will try every password to see hashes
  change. Encourage.
- **Kids inventing weak passwords.** Real lesson:
  password strength matters too.
- **Privacy questions** — "what happens if I
  forget my password?" Real concern. Real apps
  add password reset (out of scope).
- **Kids treating the demo like a real account.**
  Reinforce: this is local; deploy is Session 12
  for real publicness.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sessions 10-11 (notes app).** Each user has
  their own notes. `WHERE user_id = ?` in
  queries; security demo across both sessions.
- **Session 12 (deployment).** Multi-user app
  hosted on a real URL. *People can sign up and
  use it.*
- **Sessions 13-14 (milestone).** Their milestone
  apps will likely have user accounts.
- **Phase 5/6/7 callback:** all the previous
  todo/notes/games stayed local; this is the
  multi-user version.
- **Career-long callback:** auth is *every*
  app. Same pattern (with refinements) across
  every framework.
- **Peanut butter callback opportunity:** the
  forgot-to-hash bug is *the* security
  precision moment. Code does what you wrote;
  if you wrote 'store the password,' it stores
  the password.

### Materials checklist

- [ ] Demo machine with browser + Thonny + Flask
- [ ] Pre-built auth app
- [ ] DB Browser for SQLite (to show hashed
      passwords)
- [ ] Projector
- [ ] Class roster
