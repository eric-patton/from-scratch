## Session 4 — Teacher Notes

*Phase 7, Web · Session 4 of 17 · Title: The box model*

### Purpose of this session

The mental model session for layout. Five jobs, in
priority order:

1. **Land "every element is a box."** Conceptual peg
   for the rest of CSS.
2. **Land padding vs margin.** Inside vs outside. The
   single most common confusion in CSS.
3. **Land `box-sizing: border-box`.** Modern default.
   Set once at the top of every stylesheet.
4. **Build cards.** Universal pattern on the modern
   web. Real practice.
5. **Set up Flexbox (Session 5).** Cards stacked
   vertically next session become cards in a row.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built example with cards.
- A real website with cards (e.g., a news site's home
  page) for "see, real sites use this everywhere."

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 3.
- **Part A: box model anatomy** (~15 min). Diagram
  on the board, then DevTools.
- **Part A: padding/margin/border** (~15 min). Type
  examples, see effect.
- **Part A: width, height, box-sizing** (~10 min).
- **Break** (~5 min).
- **Part B: cards** (~30 min). Type together, then
  kids customize.
- **Wrap-up** (~10 min).

If running short, **the `.btn` stretch can be cut.**
The card layout is the priority.

### Teaching Part A

#### Diagram on the board

Draw the four nested rectangles: content (innermost),
padding, border, margin (outermost). Label each.
Walk through each name *and* what it does:

> "Content is the actual stuff — the text, the image.
>
> Padding is *inside* space. Like the padding inside a
> shipping box that holds the item away from the
> walls. The space between the content and the border.
>
> Border is the edge — a literal line you can see (if
> you set one).
>
> Margin is *outside* space. Pushes other things away
> from this element. The space between this box and
> the next."

The "padding inside a shipping box" analogy works
well. So does:

> "Padding is *my* space. Margin is space *between me
> and others*."

#### DevTools box-model panel

Open DevTools. Inspect any element. Show the box-
model panel.

Point at:
- The numbers in each layer.
- Hovering over a layer highlights it on the page.

> "This is the *truth* of an element's spacing. If
> you can't figure out why something looks weird,
> open this panel. See where the space is."

#### `box-sizing: border-box` — non-negotiable

Spend 5 minutes on this. The default behavior (width =
content only) is genuinely confusing. The fix is one
rule:

```css
*, *::before, *::after {
    box-sizing: border-box;
}
```

Frame:

> "Every modern site does this. Set it at the top of
> every stylesheet you write. Now `width: 300px;`
> means *the box is 300px*, including padding and
> border. Way more intuitive."

The `*` selector matches every element. The
`::before` and `::after` parts catch pseudo-elements
(used for some advanced CSS — won't come up in our
curriculum).

#### Display: block, inline, inline-block

Brief tour:

- **block** — full width, stacks. `<div>`, `<p>`,
  headings.
- **inline** — width = content, flows with text.
  `<span>`, `<a>`, `<strong>`. **No vertical
  margin.**
- **inline-block** — flows but accepts width / height
  / margin. Useful for buttons.
- **none** — gone. Not just hidden — *not rendered*.

The "inline doesn't accept vertical margin" is a
common surprise. Mention but don't drill.

### Teaching Part B

#### Cards are universal

Show real sites with card layouts:

- News sites (article cards on the home page).
- E-commerce (product cards).
- Dashboards (metric cards).
- Portfolios (project cards).

> "Cards are everywhere on the modern web. Today's
> pattern is the foundation."

#### Walk through the card CSS

Type each property. Discuss what it does:

- **`background-color: white;`** — solid background.
- **`border: 1px solid #ddd;`** — subtle border.
- **`border-radius: 8px;`** — rounded corners. Show
  what 0, 8, 20, and 50% look like.
- **`padding: 20px;`** — interior breathing room.
- **`margin-bottom: 20px;`** — separates from the
  next card.
- **`box-shadow: ...`** — subtle depth.

The shadow value is gnarly:

```css
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
```

Frame: "x-offset, y-offset, blur-radius, color." 0 x
+ 2 y means "drop shadow only down." Slight blur.
Very transparent black.

#### `margin-top: 0;` on the heading

Default browser styles add margin to headings. When a
heading is the *first* thing in a card, the top
margin pushes it down weirdly inside the padding.
Reset:

```css
.card h3 {
    margin-top: 0;
}
```

Demo: comment out the `margin-top: 0;`. See the
heading shoved down. Add it back. Heading sits at
the top.

#### The link-as-button pattern

```css
.card a {
    display: inline-block;
    padding: 8px 16px;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 4px;
}
```

Frame:

> "An `<a>` is inline by default — width = content,
> no proper padding/sizing. Change `display:
> inline-block` and now it accepts padding. Add a
> background, color, and border-radius — looks like
> a button."

This pattern is used *everywhere* on the web.

### Common stumbles

- **Padding moves the wrong way.** They expected
  padding to push things *outside*; it actually adds
  space *inside*.
- **Margin not collapsing as expected.** Vertical
  margins between adjacent block elements *collapse*
  — only the larger one shows. Don't drill, but
  mention if asked.
- **Width includes padding without `border-box`.**
  Hard to debug. Always set `box-sizing` first.
- **Vertical margin on inline elements.** Doesn't
  work. Use `inline-block` or `block`.
- **`border-radius: 50%` on non-square element.**
  Becomes an ellipse, not a circle. Make square first.
- **Color in `box-shadow` missing alpha.** Hard
  shadow. Use `rgba` for soft.
- **Cards full width.** Looks weird. Constrain with
  `max-width` on the parent (next session: Flexbox
  side-by-side).
- **Heading inside card has weird top space.**
  Browser default margin. Reset with `margin-top: 0`.
- **Border-radius without overflow:hidden.** Inner
  elements (like images) can poke past rounded
  corners. Add `overflow: hidden;` to the rounded
  parent if needed.

### Differentiation

- **Younger kids (9-10):** Goal is one card with
  basic padding/border. Don't push past that.
- **Older kids (12+):** Push for full card layout
  with multiple cards + button-styled links.
- **Advanced (any age):** Suggest:
  - Multiple card classes (.card, .card-featured)
  - Hover transitions
  - CSS variables for consistent spacing
  - Image inside cards (hero images)
  - Dark-mode variants
- **Struggling:** A kid who can't tell padding from
  margin is the kid you focus on. Use the shipping-
  box analogy. Use DevTools.

### What to watch for

- **The "I see how this works" moment.** When DevTools
  highlights the boxes on hover. Visceral.
- **Buddies critiquing each other's cards.** Real
  design feedback. Encourage.
- **Excitement about shadows.** Some kids will go
  shadow-crazy. Suggest restraint.
- **Comparison to real sites.** "These look like
  real cards on real sites." Yes. Affirm.
- **Cards-stacking-vertically frustration.** A few
  kids will want them side-by-side. Reassure: "Next
  week — Flexbox."

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 5 (Flexbox).** Today's vertically-stacked
  cards become side-by-side cards.
- **Session 6 (homepage).** Today's `.card` and
  `.btn` patterns become the homepage's main
  building blocks.
- **Session 7 (forms).** Form inputs are also boxes —
  same model applies.
- **Sessions 9-10 (DOM).** JS can change box model
  properties — `element.style.padding = '20px'`.
- **Phase 8 (Flask).** Templates render boxes; same
  CSS skills.
- **Career-long callback:** the box model is *the*
  layout primitive of the web. Everything else builds
  on it.
- **Peanut butter callback opportunity:** the
  padding-vs-margin / inside-vs-outside confusion is
  a precision moment. Easy to write and have it look
  wrong.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built card example
- [ ] Real website with card-based design for
      reference
- [ ] Projector
- [ ] Class roster
