## Session 5 — Teacher Notes

*Phase 7, Web · Session 5 of 17 · Title: Flexbox layout*

### Purpose of this session

The "real layout" session. Five jobs, in priority
order:

1. **Land `display: flex`.** One declaration on the
   parent unlocks the whole system.
2. **Land main vs cross axis.** `justify-content` and
   `align-items` mean different things — drives the
   conceptual model.
3. **Land `gap`.** Modern way to space flex items.
   Cleaner than margin tricks.
4. **Build real-shape layouts.** Navbar, card row,
   header-content-footer. Patterns kids will reuse
   for the rest of Phase 7.
5. **Set up Session 6 (homepage).** Today's layouts
   are the building blocks of the homepage project.

**Note: CSS Grid is deliberately not in this
curriculum.** Don't introduce it as an alternative or
"next thing." Flexbox covers everything we need.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built example with each pattern: navbar, card
  row, header-content-footer.
- A real website with a flex-based layout for
  comparison.
- [flexboxfroggy.com](https://flexboxfroggy.com)
  bookmarked — useful as a stretch / homework.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 4
  (box model).
- **Part A: basic flex** (~15 min). `display: flex`,
  direction, gap.
- **Part A: alignment** (~20 min). `justify-content`,
  `align-items`. The classic centering trick.
- **Break** (~5 min).
- **Part B: real layouts** (~30 min). Navbar, card
  row, sticky footer.
- **Wrap-up** (~10 min).

If running short, **the sticky footer pattern can be
cut.** Navbar + card row are the priority.

### Teaching Part A

#### Frame the shift

> "Until today, every block element got its own line.
> Need things side by side? Hard. Need to center
> something vertically? Worse.
>
> Flexbox solves both. One declaration on a *parent*
> turns the *children* into 'flex items' that can be
> arranged with simple rules."

The mental shift: layout happens on the **container**,
not on each child.

#### `display: flex` is the unlocker

Show the before-and-after:

```css
/* Before */
.row { /* nothing */ }

/* After */
.row { display: flex; }
```

Reload. Children that were stacked are now in a row.

> "One line. That's it. Children of `.row` are now
> flex items. Now we can arrange them."

#### Main vs cross axis — diagram

Draw on the board:

```
Default flex-direction: row

  ←──────── main axis ────────→
  ┌───────┬───────┬───────┐  ↕
  │   A   │   B   │   C   │  cross axis
  └───────┴───────┴───────┘  ↕

Switch to flex-direction: column

  ┌───────┐  ←── cross axis ──→
  │   A   │
  ├───────┤
  │   B   │  main axis
  ├───────┤  ↕
  │   C   │
  └───────┘
```

> "`justify-content` controls the *main* axis.
> `align-items` controls the *cross* axis.
>
> In a row, main is horizontal. So:
> - `justify-content: center` → horizontally centered.
> - `align-items: center` → vertically centered.
>
> In a column, it flips."

This is the conceptual core. Drill it.

#### `gap` — modern spacing

Frame:

> "Want space between items? Use `gap`. One property,
> applied to the parent. Used to require margin
> tricks; now it's clean."

Show old vs new:

```css
/* Old way */
.row > .item { margin-right: 20px; }
.row > .item:last-child { margin-right: 0; }

/* New way */
.row { gap: 20px; }
```

Way better.

#### The classic centering trick

Show this explicitly:

```css
.center-everything {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 200px;
}
```

Demo: a single `<p>` inside, dead center vertically
and horizontally.

> "This used to be a famously hard CSS problem. Whole
> articles were written about it. Now it's three
> lines. Flexbox is *transformative.*"

### Teaching Part B

#### Navbar — the canonical pattern

```css
.site-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 32px;
}
```

Frame:

> "Logo on the left, links on the right. The header
> is a flex row. `justify-content: space-between`
> pushes the first thing to the left and the last
> thing to the right. `align-items: center` centers
> them vertically.
>
> Then the *nav itself* is also a flex row, with
> `gap` between the links. Flex inside flex is
> totally fine — it's how you build complex layouts."

Walk through nesting carefully:

```
header (flex row)
├── .logo
└── nav (flex row, gap)
    ├── a (Home)
    ├── a (About)
    └── a (Projects)
```

Two flex containers, nested.

#### Cards in a row — `flex: 1`

```css
.card-row {
    display: flex;
    gap: 20px;
}

.card {
    flex: 1;
}
```

Frame:

> "`flex: 1` says 'grow to fill available space, share
> equally with siblings.' Three cards, equal thirds.
> Two cards, equal halves. Doesn't matter how many."

`flex` is shorthand for `flex-grow flex-shrink
flex-basis`. The full form (`flex: 1 1 250px`) shows
up in the wrap stretch.

#### Sticky footer pattern

The body-as-flex-column trick:

```css
body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.site-content {
    flex: 1;
}
```

Frame:

> "We make the body a vertical flex column. The
> content area has `flex: 1` — fill all remaining
> space. Header at top, footer at bottom, content
> stretches between them. Even when content is
> short, the footer stays at the bottom of the
> screen."

This is the "sticky footer" pattern. Famously hard
in pre-Flexbox CSS. Now: a few rules.

#### `100vh` is new

> "`vh` = viewport height. `100vh` = the height of
> the browser window. Useful for 'fill the whole
> screen.'"

Other related units: `vw` (viewport width), `vmin`,
`vmax`. Don't drill.

### Common stumbles

- **`display: flex` on the wrong element.** Set on
  the *parent* (the container), not on the items.
- **No effect on `justify-content`.** Often because
  there's only one flex item, or items already fill
  the container.
- **`align-items` doesn't work.** Container has no
  height; cross axis has nothing to align in. Set
  `min-height` or `height` on the container.
- **Items overflow horizontally.** Need `flex-wrap:
  wrap` or smaller items.
- **Confused main vs cross.** Especially after
  switching to `flex-direction: column`. Walk through
  the diagram again.
- **`gap` not working.** Older browser? Generally
  works in everything modern. Check that the parent
  has `display: flex`.
- **Children inheriting flex.** Flex applies only to
  *direct* children. Grandchildren are unaffected
  (unless their parent is also flex).
- **`flex: 1` doesn't make items equal.** Items might
  have different content widths affecting `flex-basis`.
  Force with `flex: 1 1 0` or `flex: 1 0 0`.
- **Navbar items wrap on small windows.** Set
  `flex-wrap: nowrap` on the nav, or smaller items.

### Differentiation

- **Younger kids (9-10):** Goal is the basic row of
  boxes + the navbar. Skip wrap, sticky footer.
- **Older kids (12+):** Push for navbar + card row +
  one of the stretches.
- **Advanced (any age):** Suggest:
  - flexboxfroggy.com (homework)
  - Sticky footer + sidebar combo
  - Responsive card grid with `flex-wrap` + `flex-basis`
  - `align-self` for one-off overrides
  - Nested flex layouts (flex inside flex inside flex)
- **Struggling:** A kid who can't get items in a row
  is the kid you focus on. Most common cause: forgot
  `display: flex` on the parent, or applied it to
  wrong element.

### What to watch for

- **The "centering finally works" reaction.** Some
  kids have tried web stuff before and felt the pain.
  Now they don't. Visible relief.
- **The "I can build a navbar" moment.** First navbar
  is a real "I can build websites" feeling.
- **Buddies copying each other's layouts.** Encourage.
  Real design work.
- **Kids over-using flex.** Some will try to flex
  *everything*, even single items. Push back: only use
  it when arranging items.
- **The "this is so much easier than I expected"
  reaction.** Yes. Modern Flexbox is great. Reaffirm:
  this is why we don't teach Grid yet — Flexbox is
  enough.
- **flexboxfroggy.com discovery.** Some kids will
  play it. Encourage; it's actually good practice.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 6 (homepage).** Today's navbar + card row
  + footer-anchor patterns become the homepage.
- **Session 7 (forms).** Form layouts use flex
  heavily.
- **Sessions 9-10 (DOM).** JS can change layout —
  toggle classes that switch flex direction, etc.
- **Sessions 13 (canvas game).** A page with a canvas
  centered + UI around it uses flex.
- **Phase 8 (Flask).** Templates render flex-based
  layouts. Same skills.
- **Career-long callback:** Flexbox is the *day-to-day*
  layout tool of the modern web. Learning it well
  pays off forever.
- **Peanut butter callback opportunity:** the
  "display: flex on the wrong element" or "expecting
  flex on grandchildren" is a precision moment.
  Browser does what you say, even when wrong.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built navbar example
- [ ] Pre-built card-row example
- [ ] Pre-built sticky-footer example
- [ ] flexboxfroggy.com bookmarked
- [ ] Projector
- [ ] Class roster
