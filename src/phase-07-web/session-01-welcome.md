## Session 1: Welcome to the web — your first HTML page

*Phase 7 — Web · Session 1 of 17*

### What we're learning today

You've been writing **programs** — Python that you run
with `python game.py`. The web works differently.
Today you'll write your first **HTML file**, open it in
a browser, and watch the browser turn your text into
a real page. By the end of class, you'll understand
what HTML is, what CSS is, what JavaScript is, and
how all three work together.

You'll also build a (very small) personal page about
yourself.

### You'll need to remember from last time

- **The terminal** (Phase 4 Session 1).
- **A text editor** — Thonny works fine.
- **Your favorite browser.**
- The general idea of files and folders.

### What you'll need today

- A web browser (Firefox, Chrome, Edge — all work).
- Thonny (or any text editor).

---

### Part A: Your first HTML page

#### What's HTML?

**HTML** stands for **H**yper**T**ext **M**arkup
**L**anguage. It's the **structure** of every web page
in existence — what's on the page, organized into
headings, paragraphs, lists, links, images, and so on.

When you visit a website, the *first thing* the
browser downloads is HTML. The browser reads the HTML
and shows you the page.

HTML uses **tags** to mark up content. A tag looks like
`<tagname>...</tagname>`. The opening tag, the
content, the closing tag. Examples:

- `<h1>Hello!</h1>` — a level-1 heading.
- `<p>Some text.</p>` — a paragraph.
- `<a href="...">click me</a>` — a link.

#### Make your first page

Open Thonny. Create a new file. Type this:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My first page</title>
</head>
<body>
    <h1>Hello, web!</h1>
    <p>This is my first HTML page.</p>
</body>
</html>
```

**Save it as `index.html`** in a new folder somewhere
you can find — maybe `~/web/first-page/index.html`.

Now open the file in your browser. Three ways:

1. In your file manager, double-click `index.html`.
2. In your browser, **File → Open File** → pick the
   `index.html`.
3. Drag the file from the file manager into the browser
   window.

You should see:

> # Hello, web!
> 
> This is my first HTML page.

The text "Hello, web!" appears as a big heading. The
text "This is my first HTML page." appears as a normal
paragraph.

**Congratulations.** You wrote a web page.

#### What every line does

```html
<!DOCTYPE html>
```

Tells the browser: "this is HTML5, the modern version."
Always include this at the very top.

```html
<html>
...
</html>
```

The root tag — everything wraps inside this. Like the
outer envelope of the page.

```html
<head>
    <title>My first page</title>
</head>
```

The `<head>` is **invisible** stuff *about* the page —
metadata, the title (shows in the browser tab), links
to CSS, scripts, etc. Anything inside `<head>` does
*not* show up on the page itself.

```html
<body>
    <h1>Hello, web!</h1>
    <p>This is my first HTML page.</p>
</body>
```

The `<body>` is the **visible** stuff. Headings,
paragraphs, images, buttons — everything the user sees.

This shape — `<html>` containing `<head>` and
`<body>` — is the **standard skeleton** of every HTML
page in the world. You'll write it constantly. Memorize
it.

#### Edit and reload

Change the text. Add another paragraph:

```html
<body>
    <h1>Hello, web!</h1>
    <p>This is my first HTML page.</p>
    <p>I am learning HTML in class.</p>
</body>
```

Save. **Reload the browser** (F5 or Ctrl+R / Cmd+R).
The new paragraph appears.

This is the core loop of web development:

1. Edit the file.
2. Save.
3. Reload the browser.
4. See the change.

Repeat forever.

#### Add some structure

Try more tags:

```html
<body>
    <h1>About me</h1>
    <p>My name is Alex. Today I am learning HTML.</p>
    
    <h2>Things I like</h2>
    <ul>
        <li>Pizza</li>
        <li>Soccer</li>
        <li>Reading</li>
    </ul>
    
    <h2>Things I don't like</h2>
    <ul>
        <li>Brussels sprouts</li>
        <li>Loud noises</li>
    </ul>
</body>
```

Save. Reload. You see two sections, each with a
heading (`<h2>`) and a bulleted list (`<ul>` containing
`<li>` items).

What's new:

- **`<h2>`** — a smaller heading. There's `<h1>`
  through `<h6>`. Pick the right level for the
  importance.
- **`<ul>`** — an **u**nordered **l**ist (bullet
  points).
- **`<li>`** — a **l**ist **i**tem. Goes inside `<ul>`
  (or `<ol>` for numbered lists).

#### A picture

Add an image. First, find or save an image file in your
folder (any PNG or JPG). Let's say it's named
`me.png`.

```html
<img src="me.png" alt="A picture of me">
```

Save. Reload. The image appears.

Two new things:

- **`<img>`** — a self-closing tag (no `</img>`). It's
  empty — has no content between open/close tags.
- **`src="..."`** — an *attribute*. Says **s**ou**rc**e
  — where to find the image file.
- **`alt="..."`** — *alt text*. What screen readers say
  when an image can't be displayed. Always include it
  (real-world accessibility — and required for
  professional sites).

#### A link

```html
<a href="https://en.wikipedia.org/wiki/Web_browser">What's a browser?</a>
```

Save. Reload. The text "What's a browser?" appears as a
link (usually blue and underlined). Click — your
browser navigates to that page.

What's new:

- **`<a>`** — anchor (the original name for "link"
  before "link" became common). Wraps the clickable
  text.
- **`href="..."`** — **h**ypertext **ref**erence. Where
  the link goes.

**Checkpoint:** *You have an HTML page with a heading,
paragraphs, a list, an image, and a link.* **This is
the natural stop point if class is cut short.**

---

### Part B: A page about you

Time to make it yours. Build a personal page about
yourself.

#### Required pieces

- One `<h1>` with your name (or a nickname — your
  choice).
- At least two `<h2>` section headings.
- At least 3 paragraphs total.
- One `<ul>` list with at least 3 items.
- One image (find one online, save to your folder, or
  use one already there).
- One link (to anything you find interesting).

#### Encourage personality

Tell us things. Hobbies, favorite games, books, weird
opinions. **Make it *yours*** — not a template.

Examples of sections:

- "About me"
- "Games I play"
- "Books I'm reading"
- "Music I like"
- "What I'm building right now"
- "Cool stuff online"

#### Save it

Name the file `index.html`. We'll come back to this
page over the next few sessions and *style* it (Session
3 onward) and add interactivity (Sessions 8 onward).
By Session 6 you'll have your real personal homepage.

#### Stretch — more tags

Try these:

- **`<strong>important text</strong>`** — bold,
  emphasized.
- **`<em>italics</em>`** — italic, lightly emphasized.
- **`<br>`** — a line break (no closing tag).
- **`<hr>`** — a horizontal rule (a divider line).
- **`<ol>`** — ordered (numbered) list. Same `<li>`s
  inside.
- **`<blockquote>`** — for quotes.

Look up any of them on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

#### Stretch — view source on a real site

Open any website you like in a browser. Right-click →
**View Page Source** (or press Ctrl+U / Cmd+U). You see
the HTML the website is made of.

Real websites are *huge* HTML documents — sometimes
thousands of lines. But the basic shape is the same:
`<html>` containing `<head>` and `<body>`, with tags
inside. You can read any of it.

This is one of the great things about the web — **every
website's source is visible.** You can learn from any
of them.

#### Extension — add comments

HTML supports comments — text the browser *ignores*.
Useful for notes-to-self:

```html
<!-- This is a comment. The browser doesn't show it. -->
<h2>Things I like</h2>

<!-- TODO: add more sections later -->
```

Comments use `<!-- ... -->`. Useful for explaining
tricky markup or marking sections.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your page. What did you put on
  it?
- Did you find the file → save → reload loop natural?
- Anyone view-source on a real website? See anything
  surprising?

Today you learned:

- **HTML is the structure** of every web page.
- **Tags** look like `<tagname>...</tagname>`.
- **The skeleton** — `<!DOCTYPE html>`, `<html>`,
  `<head>`, `<body>`.
- **Common tags** — `<h1>`-`<h6>`, `<p>`, `<ul>`/`<li>`,
  `<img>`, `<a>`.
- **Attributes** — `src=`, `href=`, `alt=`.
- **The web dev loop** — edit, save, reload.

You wrote a page that runs *in any browser on any
machine in the world.* That's the magic of the web —
universal, no install, just text the browser interprets.

Next week: more tags, semantic HTML, and structuring a
real page.

### If you missed this session

Open Thonny.

1. Create a folder for web stuff. Inside it, create a
   file named `index.html`.

2. Type the basic HTML skeleton (DOCTYPE, html, head,
   title, body).

3. Add an `<h1>` and a few paragraphs in the body.

4. Save. Open `index.html` in a browser by
   double-clicking.

5. Build a small page about yourself with the required
   pieces from Part B.

About 30-45 minutes. By the end you should have an
`index.html` you can open in a browser.

### Stretch and extension ideas

- **More tags** — `<strong>`, `<em>`, `<br>`, `<hr>`,
  `<ol>`, `<blockquote>`.
- **Multiple pages** — make `about.html` and link to
  it from `index.html`. Now you have a tiny site.
- **View source** on a real website. Look at how it's
  structured.
- **HTML reference** — bookmark
  [MDN HTML elements list](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).
- **Try special characters** — `&copy;` (©), `&hearts;`
  (♥), `&amp;` (&), `&lt;` (<), `&gt;` (>). These are
  HTML entities — escape sequences for characters that
  would conflict with tag syntax.

### What's next

Next week: **HTML tags and structure** — semantic HTML
(`<header>`, `<nav>`, `<main>`, `<footer>`), nesting,
and how to organize a real-feeling page.
