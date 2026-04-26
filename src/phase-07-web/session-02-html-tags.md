## Session 2: HTML tags and structure

*Phase 7 — Web · Session 2 of 17*

### What we're learning today

Last week you wrote your first HTML page. Today we go
deeper into **how HTML organizes a real page** — the
common tags you haven't met yet (tables, forms,
divs/spans), the **semantic tags** (`<header>`,
`<nav>`, `<main>`, `<footer>`) that real sites use, and
the idea of **nesting** tags inside each other to
build structure. By the end you'll have a properly
structured page that's ready to be styled next session.

### You'll need to remember from last time

- **The HTML skeleton** — `<!DOCTYPE>`, `<html>`,
  `<head>`, `<body>`.
- **Common tags** — `<h1>`-`<h6>`, `<p>`, `<ul>`/`<li>`,
  `<a>`, `<img>`.
- **Attributes** — `src=`, `href=`, `alt=`.
- **The edit → save → reload loop**.

---

### Part A: More tags and nesting

#### Tags inside tags

You've already done this — `<ul>` contains `<li>`s.
That's **nesting** — a tag *inside* another tag.

Nesting is how HTML builds structure. A page is a tree
— tags inside tags inside tags, all the way down.

```html
<body>
    <h1>My page</h1>
    <p>Here's a paragraph with <strong>bold text</strong> in it.</p>
</body>
```

The `<strong>` is *inside* a `<p>`. The `<p>` is
*inside* `<body>`. Nest however deep you need.

**Indentation helps you see the structure:** indent
nested tags by 4 spaces (or 2 — pick one and stick to
it). The browser doesn't care about whitespace, but
*you* (and other humans) do.

#### Inline tags

Some tags wrap a small bit of text *inside* a
paragraph, without breaking onto a new line. These are
**inline** tags:

- **`<strong>...</strong>`** — important / bold.
- **`<em>...</em>`** — emphasized / italic.
- **`<a>...</a>`** — link.
- **`<code>...</code>`** — inline code (monospace).
- **`<span>...</span>`** — generic inline (for
  styling).

Other tags create their own block on the page —
**block** tags:

- **`<h1>` through `<h6>`** — headings.
- **`<p>`** — paragraph.
- **`<ul>`, `<ol>`, `<li>`** — lists.
- **`<div>`** — generic block (for structure).

The mental model: **block** tags stack vertically;
**inline** tags flow with the text.

#### `<div>` and `<span>` — the generic ones

`<div>` (block) and `<span>` (inline) **don't mean
anything** — they're empty containers you wrap around
content for *styling* or *grouping*.

```html
<div class="card">
    <h2>A card</h2>
    <p>Some content.</p>
</div>
```

We'll use `class="..."` heavily next session for CSS.
For now, know that `<div>` is a "this stuff goes
together" wrapper.

#### Tables

For real tabular data — like a schedule or a comparison
chart — use `<table>`:

```html
<table>
    <tr>
        <th>Day</th>
        <th>Activity</th>
    </tr>
    <tr>
        <td>Monday</td>
        <td>Soccer practice</td>
    </tr>
    <tr>
        <td>Wednesday</td>
        <td>Programming class</td>
    </tr>
</table>
```

What's new:

- **`<table>`** — the table container.
- **`<tr>`** — **t**able **r**ow.
- **`<th>`** — **t**able **h**eader cell. Bold by
  default.
- **`<td>`** — **t**able **d**ata cell.

Save. Reload. A table appears (probably without
borders — we'll style it next week).

⚠️ **Don't use tables for *layout*.** Real-1990s websites
used tables to position columns and rows of content.
Modern web uses **Flexbox** (Session 5) for that.
Tables are for *actual tabular data* only.

#### Semantic tags — what real pages use

In Session 1 you used `<div>` (or no wrapper) for page
sections. Modern HTML has **specific tags** for the
common parts of a page:

- **`<header>`** — the top of the page (logo, title,
  banner).
- **`<nav>`** — navigation links (menu).
- **`<main>`** — the main content area.
- **`<section>`** — a thematic section of content.
- **`<article>`** — a self-contained piece (like a
  blog post).
- **`<aside>`** — sidebar / related links.
- **`<footer>`** — the bottom of the page (copyright,
  contact links).

These work *exactly like `<div>`* for the browser —
generic block containers. The difference: they
**describe what they contain**.

#### A real page structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>Alex's homepage</title>
</head>
<body>
    <header>
        <h1>Alex's Homepage</h1>
        <p>Welcome to my page!</p>
    </header>
    
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="projects.html">Projects</a>
    </nav>
    
    <main>
        <section>
            <h2>Latest projects</h2>
            <ul>
                <li>Pong in Pygame</li>
                <li>Fruit catcher</li>
            </ul>
        </section>
        
        <section>
            <h2>About me</h2>
            <p>I'm learning to code.</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 Alex</p>
    </footer>
</body>
</html>
```

Save. Reload. **Looks the same as if you used `<div>`s**
(no styling yet). But the structure is *meaningful*.

Why use semantic tags?

- **Search engines** understand them. Your site shows
  up better in Google.
- **Screen readers** (used by blind users) navigate
  by them.
- **You and other developers** can read the markup
  and instantly know what's what.

Modern best practice: **use semantic tags whenever they
fit.** Use `<div>` only when nothing else does.

**Checkpoint:** *You have a page using semantic tags
(at least `<header>`, `<main>`, `<footer>`) with
nested content.* **This is the natural stop point if
class is cut short.**

---

### Part B: Restructure your personal page

Take the personal page from Session 1 and restructure
it with semantic tags.

#### What to do

1. Open your `index.html` from last week.

2. Wrap the title and intro in a `<header>`.

3. Add a `<nav>` with at least one link (it can link
   back to itself for now — we'll add real pages
   later).

4. Wrap the main content (the sections, lists, etc.)
   in a `<main>`.

5. Wrap each major section in `<section>`.

6. Add a `<footer>` at the bottom (copyright, your
   name, the year).

#### Add a navigation menu

A typical site has a nav menu at the top. Try:

```html
<nav>
    <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</nav>
```

The `href="#about"` is a *fragment link* — it scrolls
to an element with `id="about"` on the same page.

Add IDs to your sections:

```html
<section id="about">
    <h2>About me</h2>
    ...
</section>
```

Now clicking "About" in the nav scrolls to that
section. Real navigation.

#### Stretch — make a multi-page site

Right now you have `index.html`. Add `about.html` and
`projects.html`:

```html
<!-- about.html -->
<!DOCTYPE html>
<html>
<head><title>About</title></head>
<body>
    <header>
        <h1>About me</h1>
    </header>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="projects.html">Projects</a>
    </nav>
    <main>
        <p>More about me here.</p>
    </main>
</body>
</html>
```

Same skeleton, different content. Each page links to
the others via the nav.

You now have a **real multi-page website.** Three
files. Browser navigates between them. This is what
most websites are.

#### Stretch — a project showcase table

Add a table for your Pygame projects:

```html
<table>
    <tr>
        <th>Project</th>
        <th>Phase</th>
        <th>What it does</th>
    </tr>
    <tr>
        <td>Snake</td>
        <td>6</td>
        <td>Classic snake game</td>
    </tr>
    <tr>
        <td>Fruit catcher</td>
        <td>6</td>
        <td>Catch falling fruit</td>
    </tr>
</table>
```

#### Extension — special characters

HTML "escapes" certain characters with `&...;` codes:

- `&lt;` — `<` (less-than)
- `&gt;` — `>` (greater-than)
- `&amp;` — `&` (ampersand)
- `&copy;` — © (copyright)
- `&hearts;` — ♥
- `&middot;` — · (middle dot)
- `&nbsp;` — non-breaking space (a space that doesn't
  break onto a new line)

Use them when you want a literal `<` (which would
otherwise look like a tag).

```html
<p>The HTML for a heading is &lt;h1&gt;.</p>
```

Renders as: "The HTML for a heading is <h1>."

#### Extension — meta tags

In `<head>`, you can add **meta** tags that don't show
on the page but tell browsers / search engines /
social media about it:

```html
<head>
    <title>Alex's homepage</title>
    <meta charset="UTF-8">
    <meta name="description" content="Alex's personal homepage with projects and stuff.">
    <meta name="author" content="Alex">
</head>
```

Always include `<meta charset="UTF-8">` — this tells
the browser to expect modern Unicode characters
(emoji, accented letters, etc.). Without it, weird
characters can render wrong.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your restructured page. Did it
  feel cleaner with semantic tags?
- For the kids who built multiple pages — show
  navigating between them.
- Did the table feel different from a list? When would
  you use one vs the other?
- Anyone discover a new tag they liked?

Today you learned:

- **Nesting** — tags inside tags. Indent for clarity.
- **Block vs inline** tags. Block stacks, inline flows.
- **`<div>` and `<span>`** — generic containers.
- **Tables** — `<table>`, `<tr>`, `<th>`, `<td>`. For
  real tabular data.
- **Semantic tags** — `<header>`, `<nav>`, `<main>`,
  `<section>`, `<article>`, `<aside>`, `<footer>`.
- **Fragment links** — `href="#section-id"`.
- (Stretch) **Multi-page sites** with shared
  navigation.
- (Stretch) **HTML entities** — `&copy;`, `&amp;`,
  etc.
- (Stretch) **Meta tags** in `<head>`.

Next week we **add CSS** — colors, fonts, spacing.
Your page will start to *look like a real website.*

### If you missed this session

Open Thonny.

1. Open your `index.html` from Session 1 (or create
   a new one).

2. Restructure with semantic tags — `<header>`,
   `<nav>`, `<main>`, `<section>`s, `<footer>`.

3. Add a navigation menu with at least 3 links.

4. (Stretch) Make a second page (`about.html`) and
   link between them.

About 30-45 minutes. By the end you should have a
properly structured page using semantic HTML.

### Stretch and extension ideas

- **Tables for tabular data** — schedules, comparisons,
  lists of projects.
- **Multi-page site** with nav linking between pages.
- **HTML entities** for special characters.
- **Meta tags** in `<head>` for descriptions.
- **Figure and figcaption:**
  ```html
  <figure>
      <img src="cat.jpg" alt="My cat">
      <figcaption>This is my cat, Whiskers.</figcaption>
  </figure>
  ```
- **Details and summary** — collapsible sections:
  ```html
  <details>
      <summary>Click to reveal</summary>
      <p>Hidden content!</p>
  </details>
  ```
  Try it. The browser handles the show/hide
  automatically.
- **Read [MDN's HTML elements list](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)**.
  There are dozens. Skim them.

### What's next

Next week: **CSS** — adding *style* to your HTML.
Colors, fonts, sizing, spacing. Your page will go from
"raw HTML" to "looks like a website."
