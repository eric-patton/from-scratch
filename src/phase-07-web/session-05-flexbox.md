## Session 5: Flexbox layout

*Phase 7 — Web · Session 5 of 17*

### What we're learning today

Boxes by default **stack vertically** — each one on
its own line. To put boxes **side-by-side**, or to
*center* something properly, you need a layout system.
**Flexbox** is the modern answer. By the end of class
you'll have built side-by-side cards, a navbar with
logo + links, and a header-content-footer layout. This
is *real layout* — the kind every modern site uses.

### You'll need to remember from last time

- **The box model** — padding, margin, border.
- **`box-sizing: border-box;`** at the top of your
  CSS.
- **Display values** — block, inline, inline-block.
- **Card pattern** from Session 4.

---

### Part A: The Flexbox basics

#### What's Flexbox?

**Flexbox** is a CSS layout system designed for
**arranging items in a row or column**, with smart
control over spacing, alignment, and sizing.

The key shift in mental model:

- **Without Flexbox:** every block element gets its own
  line. Each is on a row by itself.
- **With Flexbox:** you can say "these things go in a
  row, evenly spaced, vertically centered."

#### The basic recipe

Flexbox needs **a container** with `display: flex;`,
and the **direct children** become flex items.

```html
<div class="row">
    <div class="card">A</div>
    <div class="card">B</div>
    <div class="card">C</div>
</div>
```

```css
.row {
    display: flex;
}
```

That's it. The three `.card`s now sit **in a row**
instead of stacking.

Try it. Open your `index.html`. Add this somewhere in
`<main>`:

```html
<div class="row">
    <div class="box">A</div>
    <div class="box">B</div>
    <div class="box">C</div>
</div>
```

Add CSS:

```css
.row {
    display: flex;
}

.box {
    background-color: lightblue;
    padding: 30px;
    margin: 5px;
    border: 2px solid darkblue;
}
```

Save. Reload. **Three boxes in a row.** No floats, no
positioning, no tables. Just `display: flex;`.

Now remove `display: flex;` from `.row`. Reload.
**Three boxes stacked vertically** (back to default).

That one rule is the difference. Pretty powerful.

#### Direction — row or column

By default, Flexbox arranges children in a **row**.
You can switch to a column:

```css
.row {
    display: flex;
    flex-direction: column;
}
```

Now items stack vertically — but with all of
Flexbox's other powers.

The two values you'll use 99% of the time: `row`
(default) and `column`.

#### `gap` — spacing between items

Want space between items? **Use `gap`:**

```css
.row {
    display: flex;
    gap: 20px;
}
```

20-pixel gap between each item, **automatically.** You
no longer need margin-right on each item or any of
the old hacks.

Add `gap` to your `.row`. Watch the boxes get evenly
spaced.

#### `justify-content` — main axis alignment

The **main axis** is the direction of `flex-direction`
— row by default, so the main axis is **horizontal.**
`justify-content` controls alignment **along the main
axis**.

The values:

- **`flex-start`** (default) — items at the start
  (left, in a row).
- **`flex-end`** — items at the end (right).
- **`center`** — items centered horizontally.
- **`space-between`** — items spread out, no space
  on the edges.
- **`space-around`** — items spread out, equal space
  around each.
- **`space-evenly`** — items spread out, equal space
  *between and around*.

```css
.row {
    display: flex;
    justify-content: space-between;
}
```

Try each. Watch the items reposition.

#### `align-items` — cross axis alignment

The **cross axis** is perpendicular to the main axis
— for a row, it's **vertical.** `align-items` controls
alignment along the cross axis.

The values:

- **`stretch`** (default) — items fill the container's
  height.
- **`flex-start`** — items at the top.
- **`flex-end`** — items at the bottom.
- **`center`** — items vertically centered.

This is the **#1 reason most people start using
Flexbox**: vertical centering used to be *hard*. Now
it's one rule:

```css
.row {
    display: flex;
    align-items: center;
}
```

If the row is taller than its items (because of, say,
a `min-height`), the items center vertically inside.

#### Centering anything (the classic trick)

```css
.center-everything {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 200px;
    background-color: #eee;
}
```

```html
<div class="center-everything">
    <p>I'm centered both ways!</p>
</div>
```

The `<p>` ends up dead center, both horizontally and
vertically. **The classic problem of CSS, solved in
three lines.**

**Checkpoint:** *You can put items in a row, change
direction, add gaps, and align them with
`justify-content` and `align-items`.* **This is the
natural stop point if class is cut short.**

---

### Part B: Real layouts

Time to use Flexbox for the things real sites do.

#### A navbar (logo + links)

Most sites have a navbar with a logo on the left and
links on the right. Flexbox does this perfectly.

```html
<header class="site-header">
    <div class="logo">My Site</div>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="projects.html">Projects</a>
    </nav>
</header>
```

```css
.site-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 32px;
    background-color: #2c3e50;
    color: white;
}

.logo {
    font-size: 24px;
    font-weight: bold;
}

.site-header nav {
    display: flex;
    gap: 24px;
}

.site-header a {
    color: white;
    text-decoration: none;
}

.site-header a:hover {
    color: #3498db;
}
```

Save. Reload. **A real navbar.** Logo on the left,
links on the right, all vertically centered, evenly
spaced, hoverable.

The two Flexbox containers:

1. The header itself: row with logo on one end and nav
   on the other (`justify-content: space-between`).
2. The nav: row of links with `gap` between them.

#### Cards in a row

Take the cards from Session 4. Wrap them in a flex
row:

```html
<section class="card-row">
    <article class="card">...</article>
    <article class="card">...</article>
    <article class="card">...</article>
</section>
```

```css
.card-row {
    display: flex;
    gap: 20px;
}

.card {
    flex: 1;    /* each card grows equally */
}
```

Save. Reload. **Three cards side-by-side, each
taking equal width.**

The `flex: 1` property is shorthand for "this item
should grow to fill available space, sharing equally
with siblings." Three cards with `flex: 1` get equal
thirds. Two cards with `flex: 1` get equal halves.

You can also set `flex` to other numbers:

```css
.card-main { flex: 2; }    /* twice as wide */
.card-side { flex: 1; }
```

#### Header-content-footer (a column layout)

A site with a sticky header, expanding content area,
and footer at the bottom:

```html
<body>
    <header class="site-header">...</header>
    <main class="site-content">...</main>
    <footer class="site-footer">...</footer>
</body>
```

```css
body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.site-content {
    flex: 1;    /* take all available space */
}
```

Now the body is a vertical flex column. Header at
top, footer at bottom, content fills everything in
between. **Even when the page is mostly empty, the
footer sits at the bottom of the screen.**

`100vh` = 100% of the viewport height (the browser
window). The body is at *least* that tall.

#### Stretch — wrapping for many cards

If you have many cards (more than fit in one row),
they overflow. Solution: `flex-wrap`:

```css
.card-row {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.card {
    flex: 1 1 250px;    /* grow, shrink, base width */
}
```

Now cards wrap to the next line as needed. Each card
is at least 250px wide.

`flex: 1 1 250px;` is the long form of `flex`. Three
parts:
- **flex-grow** — how much to grow (1 = grow).
- **flex-shrink** — how much to shrink (1 = shrink if
  needed).
- **flex-basis** — base width (250px).

This is **responsive design** — the layout adapts to
screen size.

#### Stretch — a sidebar layout

Two-column layout: sidebar on the left, content on the
right:

```html
<div class="layout">
    <aside class="sidebar">Sidebar</aside>
    <main class="main-content">Main content</main>
</div>
```

```css
.layout {
    display: flex;
    gap: 20px;
}

.sidebar {
    flex: 0 0 200px;    /* don't grow, don't shrink, 200px wide */
}

.main-content {
    flex: 1;    /* fill the rest */
}
```

Sidebar is fixed at 200px; main content takes the
rest. Real sites use this everywhere.

#### Extension — restyle your homepage

Take your `index.html` from previous sessions and use
Flexbox to:

1. Add a navbar at the top with logo + links.
2. Put your project cards in a row (use `flex-wrap`).
3. Make the footer stick to the bottom.

By the end, your page **looks like a real website** —
navigated, card-laid-out, footer-anchored.

(Next week we make it the *full personal homepage* as
a complete integration project.)

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your Flexbox layout. What did
  you build?
- Did vertical centering finally work? (Anyone who
  tried web stuff before today knows the pain.)
- For the kids who tried `flex-wrap` — does the
  responsive behavior feel modern?
- What clicked first: `justify-content` or
  `align-items`?

Today you learned:

- **Flexbox** = modern layout for rows and columns.
- **`display: flex;`** on the parent.
- **`flex-direction: row | column;`** sets the main
  axis.
- **`gap`** for spacing between items.
- **`justify-content`** for main-axis alignment.
- **`align-items`** for cross-axis alignment.
- **`flex: 1`** to make items grow equally.
- **`flex-wrap`** for items overflowing to new rows.
- **`100vh`** for full-viewport-height.

Flexbox is **the most useful CSS feature** for
day-to-day work. Almost every layout you'll build for
the rest of the curriculum (and beyond) uses it.

Next week: **a personal homepage** — your
integration project. HTML + CSS + Flexbox combined
into one polished site.

### If you missed this session

Open Thonny.

1. Add the basic flex example to your page (a `.row`
   with three boxes inside).

2. Try `justify-content: center` and `align-items:
   center`.

3. Convert your project cards (Session 4) to a flex
   row using `display: flex` and `flex: 1`.

4. (Stretch) Add a navbar with `justify-content:
   space-between`.

About 45-60 minutes. By the end you should have at
least two flex layouts working.

### Stretch and extension ideas

- **Responsive cards** with `flex-wrap`.
- **Two-column layout** with sidebar.
- **Sticky footer** with column flex on body.
- **Nested flex** — a flex inside a flex (totally
  fine, common).
- **Visual reference:** [flexboxfroggy.com](https://flexboxfroggy.com)
  — a game for practicing Flexbox. Genuinely fun.
- **`align-self`** on individual items to override
  `align-items` for that one item.
- **`order`** on items to rearrange visually without
  changing HTML order.
- **`justify-content: space-between` patterns** —
  navbars are the canonical use.

### What's next

Next week: **build a personal homepage.** HTML + CSS
+ Flexbox combined. Your real first website.
