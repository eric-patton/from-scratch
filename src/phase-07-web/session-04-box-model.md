## Session 4: The box model

*Phase 7 — Web · Session 4 of 17*

### What we're learning today

Every element on a page is a **rectangular box.**
Headings, paragraphs, images, buttons, even text inside
a span — all boxes. Today we learn the **anatomy** of
those boxes (content, padding, border, margin) and
how to control the *space around things*. Understanding
the box model is the foundation of every layout you'll
ever build.

### You'll need to remember from last time

- **CSS basics** — selectors, properties, the cascade.
- **External stylesheet** linked from `<head>`.
- **Block vs inline** elements (Session 2).
- **Setting properties** with `selector { prop: val; }`.

---

### Part A: The box model

#### Every element is a box

Open your styled page from Session 3. **Right-click any
element → Inspect.** Look at the **Box Model** panel
(usually on the right side of DevTools). You see four
nested rectangles:

```
┌─────────────────── margin ───────────────────┐
│                                              │
│   ┌─────────── border ────────────┐         │
│   │                               │         │
│   │   ┌────── padding ──────┐    │         │
│   │   │                     │    │         │
│   │   │    [ content ]      │    │         │
│   │   │                     │    │         │
│   │   └─────────────────────┘    │         │
│   │                               │         │
│   └───────────────────────────────┘         │
│                                              │
└──────────────────────────────────────────────┘
```

From inside out:

- **Content** — the text or image itself.
- **Padding** — space *inside* the border, between the
  border and the content.
- **Border** — a line around the padding.
- **Margin** — space *outside* the border, between this
  element and others.

That's the **box model.**

The mental model:

- **Padding** = "space inside me, around my content."
- **Border** = "a line at my edge."
- **Margin** = "space outside me, pushing other things
  away."

#### Try it

In your `styles.css`, add:

```css
.demo-box {
    background-color: lightblue;
    border: 5px solid darkblue;
    padding: 20px;
    margin: 30px;
}
```

In `index.html`:

```html
<div class="demo-box">
    This is the content.
</div>
```

Save. Reload. You see a blue box with content inside,
a thick blue border, lots of empty space inside (the
padding), and lots of empty space around it (the
margin).

Open DevTools → Inspect the box. The Box Model panel
shows the numbers you set.

#### Modify each one

Change values one at a time:

- **`padding: 50px;`** — content moves further from
  the border.
- **`border: 10px dashed red;`** — fatter, dashed,
  red.
- **`margin: 100px;`** — pushes other things away
  from this box.
- **`background-color: lightyellow;`** — changes
  inside.

Reload after each. Watch how the box changes.

#### Padding shorthand — top, right, bottom, left

```css
padding: 20px;                  /* all four sides */
padding: 10px 20px;              /* top/bottom 10, left/right 20 */
padding: 10px 20px 30px;         /* top, sides, bottom */
padding: 10px 20px 30px 40px;    /* top, right, bottom, left (clockwise) */
```

Or specify each side:

```css
padding-top: 10px;
padding-right: 20px;
padding-bottom: 30px;
padding-left: 40px;
```

Same for `margin` — same shorthand and same individual
properties (`margin-top`, etc.).

#### Border shorthand

```css
border: 2px solid black;
```

Three values: width, style, color.

Styles include `solid`, `dashed`, `dotted`, `double`,
`groove`, `ridge`. (`solid` is most common.)

You can also do individual sides:

```css
border-bottom: 2px solid #ccc;    /* only bottom */
```

We used this in Session 3 for the divider under the
header.

#### Width and height

By default, block elements take up the **full width**
of their container, and their height adjusts to fit
content.

```css
.box {
    width: 300px;
    height: 200px;
}
```

Now the box is exactly 300×200 pixels.

But here's the gotcha: **width is the content width**,
not the total box width. If you set:

```css
.box {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
}
```

The total width is **350px** (300 + 20 + 20 + 5 + 5).

This is the *original* CSS behavior — confusing and
annoying. So everyone uses the modern fix:

#### `box-sizing: border-box` — the modern default

```css
*, *::before, *::after {
    box-sizing: border-box;
}
```

Add this **at the top** of your `styles.css`. It
applies to every element on the page (`*` is the
universal selector).

Now `width: 300px;` means **total width**, including
padding and border. Way more intuitive.

**Every modern site uses `box-sizing: border-box`.**
Set it once, never think about it again.

#### Display: block, inline, inline-block

Briefly, every element has a `display` property:

- **`block`** — full width, stacks vertically. Default
  for `<div>`, `<p>`, `<h1>`, etc.
- **`inline`** — only as wide as its content, flows
  with text. Default for `<span>`, `<a>`,
  `<strong>`. **Padding and margin sometimes don't
  work as expected** on inline elements (vertical
  margins are ignored).
- **`inline-block`** — flows like inline, but accepts
  width/height/margin like block. Useful sometimes.
- **`flex`** — Session 5.
- **`none`** — element disappears entirely from the
  page (not just hidden — *not rendered*).

You can override the default:

```css
a.button {
    display: inline-block;
    padding: 10px 20px;
    background-color: navy;
    color: white;
}
```

Now an `<a class="button">` looks and behaves like a
real button.

**Checkpoint:** *You've changed padding, margin, and
border on at least one element, and you understand
the difference between padding (inside) and margin
(outside).* **This is the natural stop point if class
is cut short.**

---

### Part B: Card layouts

A common pattern on real sites: **cards** — boxes with
content inside, separated by margin, with padding
inside and a subtle border or shadow.

#### Build it

Add to your HTML (inside `<main>`):

```html
<section class="card-row">
    <article class="card">
        <h3>Pong</h3>
        <p>My first complete game from Phase 6. Two paddles, one ball.</p>
        <a href="https://github.com/...">See on GitHub</a>
    </article>
    
    <article class="card">
        <h3>Fruit Catcher</h3>
        <p>Catch falling fruit. Don't catch bombs.</p>
        <a href="https://github.com/...">See on GitHub</a>
    </article>
    
    <article class="card">
        <h3>Todo App</h3>
        <p>My customtkinter project. Add tasks, save to disk.</p>
        <a href="https://github.com/...">See on GitHub</a>
    </article>
</section>
```

Add to your CSS:

```css
*, *::before, *::after {
    box-sizing: border-box;
}

.card {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.card h3 {
    margin-top: 0;
    color: #2c3e50;
}

.card a {
    display: inline-block;
    margin-top: 10px;
    background-color: #3498db;
    color: white;
    padding: 8px 16px;
    border-radius: 4px;
    text-decoration: none;
}

.card a:hover {
    background-color: #2980b9;
}
```

Save. Reload. **You have project cards** stacked
vertically, each one with subtle shadow, rounded
corners, padding, and a styled button-link.

What's new:

- **`border-radius: 8px;`** — rounded corners. (`50%`
  on a square = circle.)
- **`box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);`** —
  subtle drop shadow. Format: `x-offset y-offset
  blur-radius color`.
- **`margin-top: 0;`** — kills the default top margin
  on the `<h3>` (browsers add default margins on
  headings; sometimes you don't want them).
- **`display: inline-block;` on the link** — makes the
  link sized like a real button.

Cards stacking vertically is fine — but they'd look
*better* side-by-side. **That's Flexbox, next session.**

#### Stretch — try other shadows and borders

```css
/* heavier shadow */
box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);

/* shadow on hover */
.card { transition: box-shadow 0.2s; }
.card:hover { box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2); }

/* dashed border */
border: 2px dashed #999;

/* gradient background */
background: linear-gradient(to right, #6a11cb, #2575fc);
```

#### Stretch — `.btn` class

Most sites have a *button* class used everywhere.
Generalize the link styling:

```css
.btn {
    display: inline-block;
    padding: 10px 20px;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    border: none;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.2s;
}

.btn:hover {
    background-color: #2980b9;
}

.btn-secondary {
    background-color: #95a5a6;
}

.btn-secondary:hover {
    background-color: #7f8c8d;
}
```

Now any `<a class="btn">`, `<button class="btn">`, or
`<a class="btn btn-secondary">` gets the right look.

`cursor: pointer;` makes the cursor a hand on hover —
clue for users that something's clickable.

#### Extension — DevTools box-model panel deep dive

Open DevTools. Inspect a card. Look at the **Computed**
tab and **Layout** tab.

The Box Model panel shows your card's exact margin,
border, padding, and content sizes in pixels. Try
changing padding directly in DevTools — see the box
resize live.

This is the **#1 way to debug layout issues** in real
web work.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your card layout. How many cards
  did you add?
- Did the box model click? Can you tell where each box
  starts and ends?
- For the kids who used DevTools — does it feel like
  X-ray vision into the page?
- Anyone discover `border-radius: 50%` (makes circles)?

Today you learned:

- **Every element is a box** with content, padding,
  border, margin.
- **Padding** = inside. **Margin** = outside.
  **Border** = the line at the edge.
- **Shorthand:** `padding: 10px 20px;` and similar.
- **`box-sizing: border-box;`** — modern default,
  always set it.
- **Width and height** — by default, width is content
  only; with `border-box`, width includes padding and
  border.
- **Display:** `block` (stack), `inline` (flow),
  `inline-block` (flow + sizing), `none` (gone).
- **`border-radius`** for rounded corners.
- **`box-shadow`** for shadows.

Cards are everywhere on the modern web. You can build
them.

Next week: **Flexbox** — finally, *real layout.* Cards
side-by-side. Header-content-footer. Centering things
properly.

### If you missed this session

Open Thonny.

1. Open your `index.html` and `styles.css` from
   Session 3.

2. Add `*, *::before, *::after { box-sizing: border-box;
   }` at the top of `styles.css`.

3. Pick one element (a paragraph, the header). Try
   adding padding (inside space), margin (outside
   space), border (the edge line). Reload after each.

4. Build the card layout from Part B with at least 3
   cards.

About 30-45 minutes. By the end you should have a
page with cards.

### Stretch and extension ideas

- **Card hover effect** — change shadow on hover.
- **Different card colors** — use a class like
  `.card.featured { background: yellow; }`.
- **`.btn` reusable class** for buttons across your
  site.
- **`border-radius: 50%`** — circles on any square
  element.
- **`box-shadow` variations** — soft, hard, multiple
  shadows.
- **`transition`** — smooth animations on hover.
- **CSS variables** for spacing:
  ```css
  :root {
      --space-sm: 8px;
      --space-md: 16px;
      --space-lg: 32px;
  }
  .card { padding: var(--space-md); }
  ```

### What's next

Next week: **Flexbox** — modern layout. Cards
side-by-side. Navbars. Headers and footers properly
positioned. The single most useful layout system in
modern CSS.
