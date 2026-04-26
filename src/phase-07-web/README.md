# Phase 7 — HTML, CSS, JavaScript

You can build games. You can write desktop apps. Now we
make things for **the browser** — websites and web apps
that anyone with internet can visit. No installs, no
"first set up Python." Just a URL.

This is the longest phase yet because the web is three
languages and a lot of new vocabulary. But you have a
strong foundation: every concept (variables, loops,
functions, classes, state machines) shows up here, just
in new syntax.

## What this phase is

About seventeen sessions across three movements:

- **HTML + CSS** (Sessions 1-7) — structure and style.
  Building things you can *see* in a browser.
- **JavaScript** (Sessions 8-11) — adding *behavior* to
  the page. Buttons that do things. Forms that respond.
  Pages that update without reloading.
- **Real apps** (Sessions 12-15) — Canvas mini-games,
  hitting an API, deploying to the world.

Then your milestone — your own web app or game,
**hosted on a public URL** anyone can visit.

## What you'll learn

| Session | Idea | What's new |
|---|---|---|
| 1 | Welcome to the web — first HTML page | HTML basics, the browser as runtime |
| 2 | HTML tags and structure | Semantic tags, nesting, attributes |
| 3 | CSS basics — selectors, colors, fonts | The cascade, selectors, declarations |
| 4 | The box model | padding, margin, border |
| 5 | Flexbox layout | Modern layout |
| 6 | Build a personal homepage | HTML + CSS integration project |
| 7 | Forms — inputs, labels, buttons | Forms that look right |
| 8 | JavaScript — syntax (compared to Python) | `let`/`const`, semicolons, braces |
| 9 | The DOM — querySelector and events | Reach into the page from JS |
| 10 | Build an interactive todo list | JS integration project |
| 11 | localStorage — persistence | State that survives reloads |
| 12 | Canvas — drawing in JS | Like Pygame's `draw`, in the browser |
| 13 | Canvas mini-game | Frame loop, sprites, collision — in the browser |
| 14 | Fetch + JSON — hitting an API | Talk to the world |
| 15 | GitHub Pages — host your work | Your URL on the internet |
| 16 | Milestone day 1 | Plan + build |
| 17 | Milestone day 2 + demo | Finish + showcase |

## What you'll build

- **Sessions 1-7:** small experiments — text pages,
  styled cards, layouts, forms.
- **Session 6:** **a personal homepage** — your first
  real artifact, pure HTML+CSS.
- **Sessions 8-11:** small interactive things —
  counters, calculators, todo lists.
- **Session 13:** **a Canvas mini-game** — Pong or
  similar, but in the browser this time.
- **Sessions 16-17:** *your* milestone web project —
  your design, hosted on a public URL.

## What you'll need

- Same machine as before. **No new installs needed.**
  Web stuff runs in the browser — Firefox or Chrome both
  work.
- Thonny still works as your editor (any text editor
  does, but Thonny is familiar).
- Your **GitHub account** from Phase 6 — we'll use
  GitHub Pages for hosting.
- Your favorite **browser** open and ready.

## How sessions work

Same shape as before:

- **Part A** introduces a concept with a guided exercise.
- **Part B** is open practice or a project.
- **Wrap-up** to share what you did.

## How the web is different

A few notable shifts:

### Three languages, not one

- **HTML** — the *structure* (what's on the page).
- **CSS** — the *style* (how it looks).
- **JavaScript** — the *behavior* (what it does when
  you click).

These three work together. A web page is *all three*.

### The browser is your runtime

In Phase 6, you ran `python game.py`. In Phase 7, you
**double-click an HTML file** (or open it in a browser
via `file:///path/to/index.html`). The browser reads
the HTML, applies the CSS, runs the JavaScript.

No `python` command. No Pygame install. Just a file +
a browser.

### Your work is shareable as a URL

Once you push to GitHub Pages (Session 15), your work
has a real public URL like
`https://YOUR-USERNAME.github.io/my-site`. Send that
link to anyone — they can use your site, no install
needed.

This is a *huge* power. Phase 6 games run on your
machine; Phase 7 sites run *anywhere*.

### JavaScript is not Python

Same ideas, different syntax:

```python
# Python
for i in range(10):
    print(i)
```

```javascript
// JavaScript
for (let i = 0; i < 10; i++) {
    console.log(i);
}
```

You'll spend Session 8 on the syntax differences. After
that the *thinking* is the same.

### CSS is its own language

CSS doesn't really look like a programming language —
no loops, no conditions (well, a few — but rare). It's
more like a list of rules: "this element looks this
way." You'll get used to it fast.

### What we're skipping

To keep things hardware-friendly and approachable, we
**skip a lot of modern web tooling:**

- No Webpack, Vite, Parcel, or any build tool.
- No npm, no `package.json`, no `node_modules`.
- No React, Vue, Angular, or Svelte.
- No TypeScript.
- No CSS frameworks (Bootstrap, Tailwind).
- No CSS Grid (Flexbox covers what we need).
- No CSS preprocessors (Sass, Less).

This is the *original* web — HTML, CSS, JavaScript,
loaded directly from files. It's what every website
*compiles down to* eventually. Frameworks are useful
once you're scaling to large teams or apps, but they
hide what's really happening. You'll learn the
underlying machinery first.

If you want to learn React or another framework after
the curriculum, the foundation here makes that *much*
easier.

## A note about getting frustrated

The web has way more vocabulary than Python or Pygame.
HTML elements, attributes, CSS properties, JS methods —
hundreds of names. **Don't try to memorize them all.**

Real web developers look things up constantly. The
sites everyone uses:

- [MDN Web Docs](https://developer.mozilla.org) — the
  reference. Look up any HTML/CSS/JS thing.
- [caniuse.com](https://caniuse.com) — does this work
  in browsers?
- [css-tricks.com](https://css-tricks.com) — guides
  and tutorials.

You'll bookmark these.

## Where to start

[Session 1: Welcome to the web](session-01-welcome.md)
opens your first HTML page in a browser.

When you're stuck, the [Getting unstuck](../appendices/getting-unstuck.md)
appendix is the first place to go. The
[Glossary](../appendices/glossary.md) will grow as
Phase 7 introduces web-specific terms.

Welcome to the web. Let's go.
