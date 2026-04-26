## Session 2 — Teacher Notes

*Phase 6, Pygame · Session 2 of 14 · Title: Drawing on
the screen*

### Purpose of this session

The drawing toolbox + first creative session in Phase 6.
Five jobs, in priority order:

1. **Land the four primary shape calls.** `rect`,
   `circle`, `line`, `polygon`. Different argument shapes
   for each.
2. **Land the RGB color model.** Three numbers, 0-255.
   The math is approachable; the intuition takes practice.
3. **Land draw order.** Later draws appear on top. This
   is how layered scenes work.
4. **Encourage creative ownership.** Building a *scene
   that's theirs* lights up engagement that "draw a
   rectangle" doesn't.
5. **Set up Session 3 (sprites).** Today is shapes drawn
   from code. Next is images loaded from disk.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame installed.
- Pre-built example scene (the house from Part A) ready
  to demo and modify live.
- A second pre-built scene with text + animation as a
  "wow" target.
- Printout (optional): RGB color reference card with
  ~20 named colors and their values.

**Prep time:** ~15 minutes. Pre-build the two example
scenes and confirm they run.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 1: frame
  loop. Today: more shapes, more colors.
- **Part A: shapes and colors** (~35 min) — RGB ~5 min,
  rect (review) ~5 min, circle ~5 min, line ~5 min,
  polygon ~5 min, build the house together ~10 min.
- **Break** (~5 min).
- **Part B: build your own scene** (~35 min). Roam,
  encourage, problem-solve.
- **Wrap-up** (~10 min). Show-and-tell.

If running short, **the polygon section can be condensed**
(triangles only). The big house build and Part B free-build
are the priorities.

### Teaching Part A

#### RGB intuition

The "mix red, green, and blue light" model is unintuitive
for kids who think in paint mixing (where red + green ≈
brown, and all colors mixed = black). RGB is light mixing,
not paint:

> "These are the three colors of *light*, not paint. Red
> light + green light = yellow light. All three at full
> = white. Zero of all three = black. It's like stage
> lights, not crayons."

Show a quick demo: open three browser tabs with red,
green, blue backgrounds, then squint or step back to see
them blend.

The 0-255 range is unintuitive too. Frame:

> "Each color is a number from 0 (none of that color) to
> 255 (max of that color). Why 255 and not 100? Because
> computers count in eights — and 256 different values
> fits in a single byte. Don't worry about it; just know
> 0 is min and 255 is max."

#### The four shape calls

The argument shapes differ between calls. Drill the
differences:

- **`rect(screen, color, (x, y, w, h))`** — top-left,
  size.
- **`circle(screen, color, (cx, cy), radius)`** —
  *center*, radius.
- **`line(screen, color, (x1, y1), (x2, y2), width)`** —
  two endpoints + thickness.
- **`polygon(screen, color, [points])`** — list of
  points.

The most common bug: using `(x, y, w, h)` for a circle
instead of `(cx, cy)`. Walk through the differences on
the board.

#### Build the house together

Type the house example line by line on the projector.
After each shape, run the program. Kids see it grow:
ground → body → roof → door → sun.

This is also the moment to introduce **draw order**:

> "Notice we drew the body first, then the door on top of
> it. If we drew them in the other order, the door would
> be hidden. Order matters."

Reinforce:

> "Draw from back to front. Background first, then things
> in front of it, then things in front of *those.* Like
> painting layers."

#### The "outline only" trick

The fifth argument (line width) makes the shape hollow.
Show this once and let curious kids experiment.

### Teaching Part B

#### The pick-a-subject moment

Free-form creative time can paralyze some kids ("I don't
know what to draw"). The seed list helps. So does:

> "Pick the *easiest* idea. A smiley face is six shapes.
> A house is what we just built. A robot is rectangles
> and circles. Don't try to make art — make *shapes that
> look like a thing.*"

#### Roam constantly

This is the heart of the session. Walk around. Ask:

- "What are you building?"
- "Can I see what you have so far?"
- "Have you tried [adjacent idea]?"

Kids who finish quickly: push them to the stretch goals
(text, animation, mouse-follow, gradient).

#### When a kid is stuck on color choice

Give a specific suggestion. "Your sky is too dark — try
`(180, 220, 255)`." Don't dwell on color theory; suggest
specific values that look good.

#### Animate-one-thing is the killer feature

Kids who animate a piece of their scene get the *biggest
delight* of the session. A bird flying across, a sun
moving, a bouncing ball. Push curious kids toward this.

### Common stumbles

- **`(x, y, w, h)` vs `(cx, cy)` confusion.** Drawing a
  circle with rect-style args. Walk through the API
  difference.
- **Color out of range.** `(300, 100, 50)` errors —
  values must be 0-255. Cap them.
- **Forgot the comma.** Color tuple `(255 100 50)` is a
  syntax error. Need commas.
- **Drawing outside the loop.** Shape appears once then
  disappears (because `screen.fill` erases it). Push
  drawing inside the loop, after `fill`.
- **Drew before fill.** Shape never appears (gets erased
  by the fill that follows). Order: fill first, then
  draw, then flip.
- **Polygon points list is empty or has one point.**
  Pygame errors. Need at least 3.
- **Polygon points in clockwise vs counter-clockwise**
  doesn't matter for solid fill. Mention only if
  someone asks.
- **Line width = 0.** No line appears. Use 1 or higher.
- **Text won't show.** Forgot to `blit` it. `font.render`
  alone doesn't draw — it makes a Surface that needs
  `blit`.

### Differentiation

- **Younger kids (9-10):** Goal is a recognizable scene
  with 4-6 shapes. Smiley face works well. Don't push
  text or animation.
- **Older kids (12+):** Push for the stretch goals.
  Especially animation — it adds the "wow."
- **Advanced (any age):** Suggest:
  - A scene that animates multiple things at once
  - Scenes that respond to mouse / keyboard
  - Recursive patterns (a tree drawn with smaller copies
    of itself)
  - Loops that draw many copies of a shape (a row of
    flowers, a starfield)
- **Struggling:** A kid who can't get one shape on screen
  is the kid you focus on. Most common cause: typo in
  arguments, draw outside the loop, or fill order.

### What to watch for

- **The "I made a thing" reaction.** When a kid finishes
  their first scene, they should look slightly proud.
  Acknowledge it.
- **Excessive perfectionism.** Some kids will spend 40
  minutes tweaking colors on the same scene. Gentle nudge:
  "Looks great. Want to try animating one piece?"
- **Color experimentation.** Some kids will discover the
  joy of `(0, 0, 0)` to `(255, 255, 255)` and just play
  with colors. Let them.
- **Buddies sharing palettes.** Encourage. "I used
  `(180, 80, 200)` for purple — try it" is real
  collaboration.
- **Kids who try to draw something too detailed** (a
  realistic person, a complex car). Redirect to simpler
  shapes.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 3 (sprites).** Drawing shapes is for
  prototypes. For real art, you load images. Today's
  scene could be drawn faster with a single image — but
  drawing teaches the coordinate system.
- **Session 4 (input).** Today's mouse-follow extension
  is a teaser.
- **Session 6 (Pong).** Pong is mostly rectangles drawn
  every frame in updated positions. Today + Session 1 +
  movement = Pong.
- **Phase 7 (web).** HTML Canvas has nearly the same API:
  `ctx.fillRect`, `ctx.arc`, `ctx.fillStyle`. Today's
  mental model transfers directly.
- **Peanut butter callback opportunity:** the `(x, y, w, h)`
  vs `(cx, cy)` confusion is a precision moment. Each
  shape has its *own* shape of arguments — generic
  guessing fails.

### Materials checklist

- [ ] Demo machine with Pygame installed
- [ ] Pre-built house scene (Part A end-state)
- [ ] Pre-built advanced scene (text + animation)
- [ ] Optional: RGB color reference card printout
- [ ] Projector
- [ ] Class roster
