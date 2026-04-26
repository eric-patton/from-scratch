## Session 3: CSS basics — selectors, colors, typography

*Phase 7 — Web · Session 3 of 17*

### What we're learning today

Your HTML page works. It looks like a 1995 textbook —
all default fonts, plain blue links, no colors. Today
we add **CSS** (Cascading Style Sheets) — the language
that controls *how things look*. By the end you'll
have styled your personal page with colors, fonts, and
text alignment, and it'll feel like an actual website.

### You'll need to remember from last time

- **HTML structure** — `<header>`, `<main>`,
  `<section>`, `<footer>`, etc. (Session 2).
- **Tags and attributes** — `<a href="...">`,
  `<img src="...">`.
- **Block vs inline** distinction.
- **The edit → save → reload loop**.

---

### Part A: Your first styles

#### What's CSS?

**CSS** stands for **C**ascading **S**tyle **S**heets.
It's a language separate from HTML for describing how
HTML elements should *look*.

CSS doesn't really look like a programming language —
no loops, no conditions. It's a list of **rules**:

```css
selector {
    property: value;
    property: value;
}
```

A rule says: "elements that match *this selector*
should have *these properties*."

Example:

```css
h1 {
    color: blue;
    font-size: 48px;
}
```

Reads as: "Every `<h1>` element should be blue, with
font size 48 pixels."

#### Three places to put CSS

CSS can live in three places. From "good for tiny
quick changes" to "good for real sites":

**1. Inline (worst — avoid for real work):**

```html
<h1 style="color: blue;">Hello</h1>
```

The `style="..."` attribute. Quick, but each element
needs its own copy. Mess.

**2. Internal (in `<style>` block in `<head>`):**

```html
<head>
    <style>
        h1 {
            color: blue;
        }
    </style>
</head>
```

All styles in one place per page. OK for small pages.

**3. External (separate `.css` file — best):**

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

CSS lives in `styles.css`. Multiple pages can share
the same stylesheet. **This is what real sites use.**
Use this from now on.

#### Make your first CSS file

Open Thonny. In your project folder (next to your
`index.html`), create a new file. Save as
`styles.css`. Type:

```css
h1 {
    color: darkred;
    font-family: Arial, sans-serif;
}

p {
    color: #333;
    font-size: 18px;
    line-height: 1.5;
}
```

Now in `index.html`, add the link in `<head>`:

```html
<head>
    <title>My page</title>
    <link rel="stylesheet" href="styles.css">
</head>
```

Save both files. Reload your `index.html` in the
browser. **Your headings are dark red, paragraphs are
dark grey, and everything's in Arial.**

You styled a page. **You're a CSS developer now.**

#### What changed

- **`color: darkred;`** — text color.
- **`font-family: Arial, sans-serif;`** — try Arial
  first, fall back to *any* sans-serif font if Arial
  isn't available.
- **`color: #333;`** — a hex color code (more on this
  below).
- **`font-size: 18px;`** — text size in pixels.
- **`line-height: 1.5;`** — space between lines (1.5 =
  1.5× the font size). Great for readability.

#### Colors

CSS supports several color formats. The common ones:

**Named colors** — about 140 of them: `red`, `blue`,
`green`, `pink`, `darkred`, `tomato`, `dodgerblue`,
`mediumseagreen`, `cornflowerblue`, etc. Find them all
on [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color).

```css
h1 { color: tomato; }
```

**Hex codes** — 6-digit `#rrggbb` (red, green, blue
in hex):

```css
h1 { color: #ff5050; }    /* tomato-ish */
h1 { color: #333; }        /* dark grey */
h1 { color: #fff; }        /* white */
h1 { color: #000; }        /* black */
```

(`#fff` is short for `#ffffff` — when each pair has
the same two digits, you can write just one.)

**RGB** — same as Pygame:

```css
h1 { color: rgb(255, 80, 80); }
```

**RGBA** — RGB plus alpha (transparency 0-1):

```css
h1 { color: rgba(255, 80, 80, 0.5); }    /* 50% transparent */
```

Pick whichever feels comfortable. Hex is most common
in real CSS.

#### Selectors

A **selector** says *which* elements get the rule. So
far you've used **element selectors** — by tag name.
There are more:

**Element selector** — by tag:

```css
h1 { color: red; }    /* every <h1> */
p { color: blue; }     /* every <p> */
```

**Class selector** — by `class` attribute (note the dot):

```css
.callout {
    background-color: yellow;
    padding: 10px;
}
```

In HTML:

```html
<p class="callout">This stands out.</p>
<div class="callout">So does this.</div>
```

Both elements get the styling because they have
`class="callout"`. **Classes are how you style
specific things.**

**ID selector** — by `id` attribute (note the hash):

```css
#main-title {
    font-size: 60px;
}
```

In HTML:

```html
<h1 id="main-title">Hi!</h1>
```

IDs should be **unique per page** — only one element
can have a given `id`. Classes can be used many times.

> Rule of thumb: **use classes for styling.** IDs are
> more for JavaScript and fragment links (Session 2).

#### Combine selectors

```css
h1, h2, h3 {
    font-family: Georgia, serif;
}
```

Comma-separated selectors apply the same rules to
multiple element types.

```css
header h1 {
    color: white;
}
```

Space-separated means **descendants** — "every `<h1>`
that's *inside* a `<header>`."

```css
.card h2 {
    color: navy;
}
```

"Every `<h2>` inside an element with class `card`."

That's the start of CSS's power — targeting elements
based on context.

#### The cascade — last rule wins

When two rules apply to the same element and conflict,
**the later one wins** (with some exceptions for
specificity, see below):

```css
h1 { color: red; }
h1 { color: blue; }
```

Result: `<h1>` is blue.

This is what "Cascading" in "Cascading Style Sheets"
means — rules cascade down, later overrides earlier.

#### Specificity (briefly)

When two rules conflict, more *specific* selectors
win:

- Element selectors are weakest.
- Class selectors are stronger.
- ID selectors are stronger still.

```css
p { color: blue; }            /* every <p> */
.special { color: red; }       /* <p class="special"> wins */
#unique { color: green; }      /* <p id="unique"> wins over both */
```

For now: **prefer classes for everything**. Don't fight
specificity wars; they're confusing and lead to bad
CSS.

#### Style your personal page

Open `index.html` and `styles.css` from earlier
sessions. Add some real styling. Try:

```css
body {
    font-family: Georgia, serif;
    background-color: #f4f1eb;
    color: #333;
    max-width: 700px;
    margin: 40px auto;
    padding: 20px;
}

header {
    text-align: center;
    border-bottom: 2px solid #ccc;
    padding-bottom: 20px;
}

h1 {
    color: #2c3e50;
    font-size: 42px;
}

h2 {
    color: #c0392b;
    font-size: 28px;
}

a {
    color: #2980b9;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```

Save. Reload. **Your page now looks designed** — a
neutral background, centered content, clear typography,
links that aren't default-blue.

A few new things in there:

- **`body`** — styles the whole page.
- **`max-width: 700px;`** — limits the page width
  (otherwise text spans the whole window — hard to
  read).
- **`margin: 40px auto;`** — vertical margin 40px,
  horizontal `auto` (centers the page horizontally).
- **`text-align: center;`** — centers text.
- **`border-bottom: 2px solid #ccc;`** — a thin grey
  line under the header.
- **`text-decoration: none;`** — removes the default
  underline on links.
- **`a:hover`** — a **pseudo-class** that applies *only
  when the mouse is over* the link. Restores
  underline on hover.

**Checkpoint:** *Your personal page has a custom
font, custom colors, and a max-width with centered
layout.* **This is the natural stop point if class is
cut short.**

---

### Part B: Make it look like *yours*

The CSS above is a starting point. Now make it
*yours*. Pick a personality — bright and friendly,
dark and dramatic, retro and pixel-y, minimal and
clean. Then style accordingly.

#### Try different fonts

CSS includes only the fonts installed on the user's
system. Common safe ones:

- `Arial` — sans-serif, classic
- `Helvetica` — sans-serif, clean (Mac)
- `Georgia` — serif, friendly
- `Times New Roman` — serif, classical
- `Courier New` — monospace
- `Comic Sans MS` — yes, this exists
- `Verdana` — sans-serif, web-friendly

Always include a fallback:

```css
body { font-family: Georgia, "Times New Roman", serif; }
```

#### Web fonts (stretch)

For real font variety, use **Google Fonts** — free
fonts hosted on Google's CDN. Example:

```html
<head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter&family=Lobster&display=swap">
    <link rel="stylesheet" href="styles.css">
</head>
```

```css
body { font-family: 'Inter', sans-serif; }
h1 { font-family: 'Lobster', cursive; }
```

[fonts.google.com](https://fonts.google.com) lets you
pick any font and gives you the link.

#### Build a color palette

Don't pick colors at random — pick a **palette** of 3-5
that work together. Resources:

- [coolors.co](https://coolors.co) — generate
  palettes.
- [color.adobe.com](https://color.adobe.com) — Adobe's
  color tool.

Apply consistently across your page.

#### Stretch — try other properties

Each of these is one CSS property to play with:

- **`text-align: left | center | right | justify;`** —
  text alignment.
- **`font-weight: bold | normal | 400 | 700;`** —
  bold or not.
- **`font-style: italic | normal;`** — italic.
- **`text-transform: uppercase | lowercase | capitalize;`**
- **`letter-spacing: 2px;`** — between letters.
- **`background-color: ...;`** — element background.
- **`background-image: url('image.jpg');`** — image
  background.
- **`opacity: 0.7;`** — semi-transparent.

Look up any of them on
[MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#properties).

#### Stretch — pseudo-classes

We saw `:hover`. Others:

- **`a:visited`** — already-visited links.
- **`button:active`** — while being clicked.
- **`input:focus`** — when the user clicked into the
  field.
- **`p:first-child`** — first paragraph in its parent.
- **`li:nth-child(odd)`** — every other list item
  (alternating colors!).

```css
li:nth-child(even) {
    background-color: #f0f0f0;
}
```

Alternating list-item backgrounds. Looks great.

#### Extension — DevTools inspector

In your browser, **right-click any element → Inspect**.
A panel appears showing the HTML and the CSS that's
applied. You can **change CSS values live** to
experiment.

Try it on your page. Try it on a real website. **This
is how real web developers work** — inspect, tweak,
copy the changes back to your file.

Ctrl+Shift+I (or Cmd+Opt+I) opens DevTools too.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your styled page. What
  personality did you go for?
- Did anyone use Google Fonts? Show the result.
- Anyone use DevTools? Did it feel powerful?
- Did the cascade ever bite you? (Two rules conflicted
  and you couldn't figure out which won?)

Today you learned:

- **CSS** is the styling language for the web.
- **External `.css` files** linked from `<head>` are
  the standard.
- **Selectors:** element (`h1`), class (`.callout`),
  ID (`#main`), descendant (`.card h2`).
- **Properties:** `color`, `background-color`,
  `font-family`, `font-size`, `text-align`,
  `line-height`, `margin`, `padding`, `border`.
- **Color formats:** named (`red`), hex (`#ff5050`),
  RGB (`rgb(...)`), RGBA (with alpha).
- **The cascade:** later rules win; specificity matters.
- **Pseudo-classes:** `:hover`, `:focus`, `:nth-child`.
- **DevTools inspector** for live experimentation.

Next week we go deeper into **the box model** —
margin, padding, border. The math of *space around
things*.

### If you missed this session

Open Thonny.

1. Create a `styles.css` file next to your
   `index.html`.

2. Link it in `<head>`:
   `<link rel="stylesheet" href="styles.css">`.

3. Style at least: body, h1, h2, p, a. Try colors,
   fonts, and at least one `:hover`.

4. Save both. Reload `index.html`.

About 30-45 minutes. By the end your page should look
*designed*, not raw.

### Stretch and extension ideas

- **Build a color palette** with a tool. Apply across
  your page.
- **Google Fonts** for font variety.
- **More pseudo-classes** — `:nth-child`, `:first-of-type`.
- **CSS variables** — define colors once, use
  everywhere:
  ```css
  :root {
      --primary: #2c3e50;
      --accent: #c0392b;
  }
  h1 { color: var(--primary); }
  ```
- **Comments in CSS** — `/* this is a comment */`.
- **Transitions** — animate on hover:
  ```css
  a {
      color: navy;
      transition: color 0.3s;
  }
  a:hover {
      color: red;
  }
  ```

### What's next

Next week: **the box model** — every element on a
page is a rectangular *box*. Understanding margin,
padding, border, and how they combine is the key to
controlling space and layout.
