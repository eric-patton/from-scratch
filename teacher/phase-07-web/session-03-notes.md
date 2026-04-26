## Session 3 — Teacher Notes

*Phase 7, Web · Session 3 of 17 · Title: CSS basics —
selectors, colors, typography*

### Purpose of this session

Add visual to the visible. Five jobs, in priority
order:

1. **Land the three-places-for-CSS distinction** —
   inline, internal, external. Push toward external as
   the default.
2. **Land selectors.** Element, class, ID. Push class
   as the default for styling.
3. **Land the cascade.** Later rules win (mostly).
   Specificity exists but don't drill it.
4. **Get every kid's page styled.** End of session,
   every page should look noticeably *designed* — not
   raw HTML.
5. **Set up the box model (Session 4).** Today's
   `padding`, `margin`, `max-width` glimpses preview
   next week.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built styled version of the demo personal page
  (the one you used in Sessions 1-2).
- Optional: a printout of safe web fonts and a few
  example color palettes.
- Optional: a real website open with DevTools — to
  demo the inspector at the end.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 2.
- **Part A: what's CSS** (~10 min). Three places.
  Selectors. The cascade.
- **Part A: first stylesheet** (~20 min). Type
  together. Link. Reload. See change.
- **Part A: classes and IDs** (~10 min).
- **Break** (~5 min).
- **Part B: style your page** (~30 min). Each kid
  styles. Roam.
- **Wrap-up + DevTools demo** (~10 min).

If running short, **drop the DevTools demo** (cover
in a future session). Getting every kid to a styled
page is the priority.

### Teaching Part A

#### Three places — push external

Show all three quickly:

```html
<!-- Inline -->
<h1 style="color: blue;">...</h1>

<!-- Internal -->
<head><style>h1 { color: blue; }</style></head>

<!-- External (best) -->
<head><link rel="stylesheet" href="styles.css"></head>
```

> "Inline is the worst — every element needs its own
> style. Internal is OK for tiny pages. External is
> what real sites use — one CSS file, many HTML pages
> can share it. Use external from now on."

The `<link rel="stylesheet" href="styles.css">` is a
new tag. Walk through:

- `<link>` — used for various external resources.
- `rel="stylesheet"` — the *relationship* (this is a
  stylesheet).
- `href="styles.css"` — where it lives.

#### CSS rule syntax

Diagram on the board:

```
selector {
    property: value;
    property: value;
}
```

Show on a real example:

```css
h1 {
    color: blue;
    font-size: 48px;
}
```

> "*Selector* says which elements. *Properties* say
> what to change. *Values* say what to change to.
> Ends with `}`."

The semicolons matter. Forgetting one breaks the
*next* declaration silently. Drill briefly.

#### Selectors — element, class, ID

```css
h1 { ... }            /* every <h1> */
.callout { ... }       /* every class="callout" */
#main-title { ... }    /* the one id="main-title" */
```

The dot vs hash distinction is a precision moment some
kids will fumble. Drill.

> "Use **classes** for styling. ID is for one-off
> things — usually for JavaScript or fragment links.
> If you find yourself wanting to style multiple
> things the same way, that's a class."

#### The cascade

```css
h1 { color: red; }
h1 { color: blue; }
```

Result: blue. Because the second rule comes later.

> "Later rules win. That's the 'cascading' in CSS. If
> two rules conflict, whichever the browser sees last
> applies."

Then specificity (briefly):

> "Class beats element. ID beats class. *Specificity*
> is the formal term. But for now: just use classes.
> Don't fight specificity wars."

Show one example of conflict:

```css
p { color: blue; }
.special { color: red; }
```

```html
<p>plain blue</p>
<p class="special">red, because class beats element</p>
```

#### Style the demo page together

Walk through the styling block from the handout. Type
each rule, save, reload. Pause to discuss.

The `body { max-width: 700px; margin: 40px auto; }`
trick is the most magical. Frame:

> "`max-width` limits the page's width. `margin: 40px
> auto;` means 40px top/bottom and `auto` left/right
> — `auto` divides the leftover space evenly, which
> *centers* the content. Real-world pattern."

The `text-decoration: none;` for links + `:hover`
restoration is also worth a beat:

> "Default links are blue and underlined. We can
> remove the underline (`text-decoration: none;`),
> then add it back *only* when hovered (`a:hover`).
> Modern web style."

### Teaching Part B

#### Personality picking

Push every kid to pick a *vibe* before styling. "What
should this page feel like?"

- Bright + friendly?
- Dark + dramatic?
- Retro?
- Minimal?

The vibe drives color and font choices. Without it,
kids pick at random and hate the result.

#### Color palettes

Some kids will pick neon-rainbow colors. Gentle
redirect:

> "Pick 3-5 colors that work together. Less is more.
> [coolors.co] generates palettes — pick one you like,
> use those colors."

#### Walking around

Common help:

- **Forgot the link tag.** Page renders unstyled.
  Check `<head>`.
- **`styles.css` saved in wrong folder.** Browser
  can't find it. Walk through file paths.
- **Selector syntax wrong.** `.foo` vs `foo` vs
  `#foo`. Walk through.
- **Forgot semicolons.** Subtle. The next property is
  silently ignored.
- **Hex code wrong format.** `#ff5` (3 chars works),
  `#ff55` (4 doesn't), `#ff5500` (6 works), `#ff550`
  (5 doesn't). Hex must be 3 or 6 digits.

#### "It looks the same"

A few kids will style and reload and see no change.
Always check:

1. Is the `<link>` in `<head>`?
2. Is `href` pointing at the right file?
3. Did you save `styles.css`?
4. Did you reload (hard reload: Ctrl+Shift+R)?

90% of "no change" is one of those four.

### Teaching DevTools

Save this for end of class if time allows. Walk
through:

1. Right-click any element on the page → **Inspect**.
2. The DevTools panel opens, showing the HTML and CSS.
3. In the CSS panel, **change a value** (color, font-
   size). The change appears live in the page.
4. **Add a new property** by clicking inside the
   selector's block.

> "This is how real web developers work. Inspect,
> tweak, see the change instantly. When you like it,
> copy the change to your file."

Mention: changes here are *temporary* — they vanish
on reload. The file is the source of truth.

### Common stumbles

- **`<link>` outside `<head>`.** Doesn't always work,
  or works inconsistently. Put it in `<head>`.
- **Wrong filename.** `styles.css` vs `style.css`.
  Stay consistent.
- **Missing semicolons.** Especially after the last
  property — Sass and others require it; CSS doesn't,
  but adding one always works.
- **Hex not 3 or 6 chars.** Browser ignores invalid
  values silently.
- **Confused dot/hash.** `.classname` for classes,
  `#idname` for IDs. Drill.
- **Selectors apply to wrong things.** `header h1`
  matches `h1` *inside* `header` — not just any `h1`.
  Walk through.
- **Specificity bites.** A more-specific selector
  earlier in the file overrides a less-specific one
  later. Confusing for kids. Resolve by using classes
  consistently.
- **Quotes in `font-family` for multi-word fonts.**
  `font-family: Times New Roman;` errors; needs
  `font-family: "Times New Roman";`.
- **Browser caching.** Hard reload (Ctrl+Shift+R)
  after CSS changes.

### Differentiation

- **Younger kids (9-10):** Goal is body styling +
  one heading + one link. Don't push past that.
- **Older kids (12+):** Push for full styling +
  classes + Google Fonts.
- **Advanced (any age):** Suggest:
  - CSS variables (`:root { --primary: ...; }`)
  - More pseudo-classes (`:nth-child`, `:focus`)
  - Transitions (`transition: color 0.3s;`)
  - Background images
  - Box shadow (`box-shadow: 2px 2px 5px gray;`)
- **Struggling:** A kid who can't get any styling
  applied is the kid you focus on. Most common cause:
  link tag missing or wrong path.

### What to watch for

- **The "wait, my page is *pretty*" reaction.** First
  styled page is satisfying. Pause for it.
- **Buddies trading color palettes.** Encourage.
- **Kids inspecting real websites.** Encourage. Reading
  real CSS is the best way to learn.
- **Kids wanting to use 17 different fonts.**
  Redirect: "Pick 1 or 2."
- **Frustration with specificity.** "Why isn't my rule
  working?" Walk through.
- **Excitement about DevTools.** Real moment for
  curious kids — "I can change *anything*?" Yes.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 4 (box model).** Today's `padding`,
  `margin`, `border` glimpses become the full
  treatment.
- **Session 5 (Flexbox).** Today's `display: ...` (when
  it comes up) becomes `display: flex`.
- **Session 6 (homepage).** Today's styling becomes
  the polished homepage.
- **Sessions 9-10 (DOM).** JavaScript can *change*
  CSS — `element.style.color = 'red'` or
  `element.classList.add('active')`. Today's class
  knowledge directly enables this.
- **Phase 8 (Flask).** Server-rendered pages are still
  HTML + CSS. Same skills.
- **Career-long callback:** CSS is *the* visual
  language of the web. Every framework, every site,
  ends in CSS.
- **Peanut butter callback opportunity:** the
  semicolon / dot / hash precision is a real precision
  moment. Browser silently ignores wrong syntax.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built styled personal page
- [ ] Optional: color palette / font reference printout
- [ ] Optional: a real website for DevTools demo
- [ ] Projector
- [ ] Class roster
