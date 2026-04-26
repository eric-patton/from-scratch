## Session 6 — Teacher Notes

*Phase 7, Web · Session 6 of 17 · Title: Build a
personal homepage*

### Purpose of this session

The HTML/CSS integration moment. Five jobs, in
priority order:

1. **Land integration.** Sessions 1-5 each taught one
   piece. Today they all combine into a real site.
2. **Land step-by-step building.** 7 steps, each one
   visible. *Don't skip the runs* — same advice as
   Phase 6 Session 6 (Pong).
3. **Make it real.** This homepage will be hosted
   publicly in Session 15. Push every kid to make it
   *theirs* — real name, real content, real personality.
4. **Land CSS variables (`:root`).** Best place to
   introduce them — the homepage benefits from a
   centralized palette.
5. **Set up Session 7 (forms).** Today's site is
   read-only. Forms come next, then JS to wire them
   up.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built finished homepage (the Step 7 end-state)
  open in another tab for "this is what we're aiming
  for."
- A stretch version with CSS variables, multi-page,
  responsive design — for advanced kids.
- Have a few real-world examples of personal sites
  bookmarked (kid-friendly examples — game devs'
  portfolios, illustrators, etc.).

**Prep time:** ~25 minutes. Build the full homepage
once before class.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 5.
  Today: integration.
- **Part A — sketch** (~10 min). Quick paper sketch.
- **Part A — Steps 1-7** (~50 min). Type live.
- **Break** (~5 min, can be inserted around step 4).
- **Part B — make it yours** (~15 min). Customize
  content and colors.
- **Wrap-up** (~5 min). Show-and-tell tour.

If running short, **stop at Step 6** (skip the footer)
and skip Part B's CSS variables. The visible result
matters more than every code feature.

### Teaching Part A

#### Sketch first

Five minutes. Paper. Push every kid:

> "Sketch the rough layout before you code. Where's
> the navbar? Where's your name? Where do project
> cards go? Five minutes — really sketch."

Without this, kids skip directly to code and lose
their way.

#### Type the HTML

Type the entire HTML on the projector. Pause to
explain semantic tags as you hit them
(`<header class="navbar">`, `<section id="about">`).

The `id` attributes (e.g., `id="about"`) tie to the
nav fragment links (`href="#about"`) — Session 2
callback.

#### Build CSS in steps

The 7 steps build the visual incrementally. After
each, kids reload and see the change. The
**transformation moments** are:

- Step 2 → 3: navbar appears (suddenly looks like a
  site).
- Step 3 → 4: hero section with gradient (looks
  *modern*).
- Step 5 → 6: cards appear in a row with hover
  effect (looks *interactive*).

These are the "wait, this looks like a real site"
moments. Pause for them.

#### CSS variables (intro)

When you get to Part B, frame variables clearly:

> "Notice we use `#3498db` in three places. What if
> we want to change it later? Find-and-replace is
> error-prone. CSS variables solve this:
>
> ```css
> :root {
>     --accent: #3498db;
> }
> ```
>
> Then use `var(--accent)` everywhere. Change the
> variable in one place, the whole page updates."

This is real production CSS practice.

#### `linear-gradient` is the "wow"

Several kids will go wild with gradients after this.
Encourage briefly — gradients are fun — but redirect
if they spend 20 minutes tweaking.

#### `transform: translateY(-4px)` on hover

Real modern web polish. Frame:

> "When you hover the card, it lifts up 4 pixels. Tiny
> motion. Combined with the bigger shadow, it feels
> like the card is rising. *That's* the kind of
> small detail that makes sites feel polished."

#### Don't go overboard with steps

Each step should fit on a single screen of the
projector. Don't combine — small steps so kids can
follow.

### Teaching Part B

#### "Make it yours" is the assignment

Push every kid to actually replace content with
their own. Catch the kids who leave "Alex" or the
demo paragraph in:

> "Whose page is this? Yours. Then it shouldn't say
> Alex. Replace every word."

#### Color personality

The four palettes in the handout are starting points.
Kids pick one and modify, or invent their own. The
key: **be consistent.** Use the same colors throughout.

#### Real images

If they have project screenshots or photos, encourage
adding. If not, suggest taking screenshots of their
Pygame projects or finding free CC0 images.

### Common stumbles

- **Skipped a step.** Most failures here. "Which step
  did you last save and run successfully?"
- **CSS in wrong file.** Edited HTML inside the CSS
  block. Walk through.
- **`<link>` to stylesheet broken.** Wrong path or
  wrong filename.
- **Layout broken on overflow.** Cards too wide,
  navbar wrapping. Check `flex-wrap` and content
  widths.
- **Hover effect doesn't work.** Forgot the
  `transition` rule. Or the property change isn't
  hovering.
- **Font fallback chains misordered.** `font-family:
  Inter, sans-serif;` — make sure the comma-separated
  list ends with a generic family.
- **Gradient looks weird.** Try different angles
  (`90deg`, `135deg`, `to right bottom`). Pick colors
  that contrast.
- **`max-width` on body or main vs section.** Affects
  centering. Walk through.
- **Sticky footer not at bottom.** Body needs to be a
  flex column with `min-height: 100vh`. Plus
  `flex: 1` on `<main>`.
- **CSS variables don't work.** Old browser? IE? Not
  an issue in modern browsers.
- **Image too big or small.** Use `max-width: 100%;`
  to prevent overflow.

### Differentiation

- **Younger kids (9-10):** Goal is finishing the
  steps. Customizing content is a stretch. Don't
  push CSS variables.
- **Older kids (12+):** Push for full customization
  + at least one stretch (variables, favicon,
  responsive).
- **Advanced (any age):** Push for:
  - CSS variables for full palette
  - Multi-page site (about.html, projects.html)
  - Sticky navbar
  - Smooth scroll
  - Responsive design with `@media`
  - Real screenshots of their projects
- **Struggling:** A kid who can't get the navbar
  laid out is the kid you focus on. Most common
  cause: confused with selectors, or `display: flex`
  on wrong element.

### What to watch for

- **The "this looks like a real site" reaction.**
  Multiple moments — navbar, hero, cards. Pause for
  them.
- **Buddies critiquing each other's color choices.**
  Encourage. Real design review.
- **Kids customizing way past the structure.**
  Adding new sections, animations, etc. Encourage
  if they finished the base; redirect if they haven't.
- **Kids reluctant to put themselves on the page.**
  Real names, real photos, real interests. Some kids
  hesitate; reassure that this is for their own
  portfolio. Privacy concerns: nicknames are fine.
- **Kids excited about Section 15 (deploy).**
  "Wait, this goes on the internet?" Yes. They're
  building real things.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 7 (forms).** Forms add to this homepage —
  contact form, sign-up, comment box.
- **Sessions 8-11 (JS).** This page becomes
  interactive — dark-mode toggle, live filtering, etc.
- **Session 15 (GitHub Pages).** This homepage gets
  hosted at `<username>.github.io`. Public URL.
- **Sessions 16-17 (milestone).** Many kids will
  build off this homepage as their starting point.
- **Career-long callback:** developer portfolios are
  real. Many devs use a personal site as their public
  face. Today's homepage is the first version.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built finished homepage
- [ ] Pre-built advanced version (CSS variables,
      multi-page, responsive) for reference
- [ ] Real personal sites bookmarked for inspiration
- [ ] Optional: paper for sketching
- [ ] Projector
- [ ] Class roster
