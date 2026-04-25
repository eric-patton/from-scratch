## Session 7 — Teacher Notes

*Phase 2, Python with Turtle · Session 7 of 8 · Title: Putting
it together — a garden scene*

### Purpose of this session

The Phase 2 synthesis session. Same role as Phase 1 Session 7
(integration project before the milestone). Five jobs, in
priority order:

1. **Demonstrate that students can build something substantial
   from the toolkit they have.** No new concepts. Everything is
   review and combination. A 50-line Python program with
   functions, loops, variables, conditionals — they can do this
   now.
2. **Reinforce function-driven structure.** Today's project is
   built from `draw_flower`, `draw_sun`, `draw_grass` — small
   reusable functions composed into a scene. This is the pattern
   they'll need for their milestone project and for every
   project after.
3. **Set up Session 8 (milestone).** End of class, every kid
   should leave with at least an inkling of what they want to
   build next week. The "ideas" list at the end of the student
   handout exists for the kids who arrive without one.
4. **Build the planning habit.** The flower function intro
   ("before any code, think about what a flower looks like in
   Turtle terms") is the same decomposition habit that will be
   formal in Session 8's planning template.
5. **Note where each kid is, technique-wise.** Today is your
   last chance to assess each student's typing fluency, debugging
   confidence, and creative comfort before they tackle the
   milestone solo. Note who needs handholding for next week.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open. Have the **finished garden
  scene** pre-built so you can show "this is where we're going"
  at the start.
- Pre-test the `t.bgcolor("skyblue")` line — should work, but
  worth confirming on a student machine.

**Prep time:** ~25 minutes. Build the full extension scene once
before class so you know the timing and can answer questions.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was conditionals.
  Anyone build anything cool with conditional colors?
- **Part A: build the flower function** (~35 min) — preview the
  finished scene ~3 min, plan-the-flower discussion ~5 min,
  build the function ~15 min, draw 4 flowers ~10 min, checkpoint
  ~2 min.
- **Break** (~5 min).
- **Part B: garden with variation** (~40 min) — loop-driven row
  ~10 min, conditional color stretch ~15 min, full scene
  extension for fast finishers ~15 min.
- **Wrap-up + milestone preview** (~5 min).

If running short, **the full-scene extension can be cut.** The
loop-driven row + conditional colors is the important part of
Part B; the extension is icing.

### Teaching Part A

#### Preview the finished scene

Open with the finished garden running on the projector. Don't
explain yet — just let them see it.

> "By the end of class, you'll have built this. Plus probably
> one or two of your own variations. Let's get started."

The destination preview lands the motivation.

#### Plan the flower

Before typing code, walk through the design out loud:

> "What do we need? A stem. Petals. A position so we can put it
> somewhere. A color so they can be different. A size so big and
> small can coexist. Position, color, size — those are
> parameters. Stem and petals are what the function does."

This is **decomposition modeled in real time**. Goal #1 of the
curriculum. Make it explicit — name what you're doing.

> "This is the planning step. Before you write code, you decide
> what you're building, what's variable about it, what's fixed.
> If we wrote the stem and petals as separate functions, that
> would also work. We're choosing one function with parameters.
> That's a design choice."

#### Build the function

Walk through at the projector once. Then **stop talking** and
let them build it themselves. Walk the room.

Common things to help with:
- The `setheading(90)` to face up before drawing the stem
- The petals loop (8 × 45 = 360, ring of circles)
- The `t.penup() / t.goto(x, -100) / t.pendown()` pattern at the
  start to position the flower

The function definition uses indentation extensively — function
body is indented once, the petals loop is indented twice. Watch
for kids whose indentation gets confused.

#### Multiple flowers

Once the function works for one flower, calling it three more
times is mechanical. The lesson here is the *power* of having
the function: four flowers, four lines.

### Teaching Part B

#### Base — loop-driven row

The new thing in Part B is using a loop to drive multiple
function calls with varying arguments. Specifically: the variable
`x` starts at -200 and increments by 100 each iteration, so each
call to `draw_flower` gets a different x.

Walk through:

```python
x = -200
for i in range(5):
    draw_flower(x, "red", 15)
    x = x + 100
```

The variable `x` is used as an argument to the function. Each
iteration uses the *current* value, then updates.

This is the same `size = size + 10` pattern from Session 5 but
with a different visible payoff — instead of growing squares,
spreading flowers.

#### Stretch — conditional colors

The `if/elif/else` color-picker is verbose but uses every Phase
2 concept. Walk through:

- The conditional checks `i == 0`, `i == 1`, etc.
- Each branch sets the `color` variable
- Then `draw_flower(x, color, 15)` uses the color

Some kids will notice this is awkward and ask if there's a
better way. **Yes:** lists. Mention briefly:

> "There's a way to do this in two lines using a *list* — a
> kind of variable that holds multiple values. We'll cover lists
> in Phase 3. For now, the if/elif chain works."

If a kid is curious enough to try lists on their own (the
extension hints at it), let them. Don't formally teach.

#### Extension — full scene

The full-scene extension introduces *more functions* —
`draw_sun`, `draw_grass`. Plus `t.bgcolor()` for the
background, plus `t.write()` for the title (callback to
Session 2).

The pedagogical move here is: **the program structure is now
a series of function calls**. The scene is built by composing
functions. That's how real programs are organized:

```
build the sky (bgcolor)
draw the sun
draw the grass
draw the flowers (loop)
draw the title
```

Each line at the top level is a meaningful action. Code that
reads like a story.

Worth pointing out at the projector: "look how readable this
program is. Each line tells you what's happening. Functions
make code readable."

### Common stumbles

- **Forgot the `setheading(90)` before drawing the stem.** Stem
  goes in some random direction depending on what the turtle
  was doing before. Fix: `setheading(90)` to face up explicitly.
- **Petals don't form a ring.** Math error in the turn angle.
  8 × 45 = 360. If they used a different turn (like 90), the
  ring won't close.
- **Function defined but never called.** Common. Symptom: program
  runs, nothing draws. Fix: add a `draw_flower(0, "red", 15)`
  somewhere.
- **Indentation hell.** With three levels of nesting (function +
  for loop + inner for loop), the indentation gets visually
  tangled. Help kids by having them re-type each line carefully,
  or by pointing at the indentation level for each line.
- **Color variable doesn't make it into the function.** Kid sets
  `color` in the conditional but then forgets to pass it: writes
  `draw_flower(x, "red", 15)` (hard-coded) instead of
  `draw_flower(x, color, 15)`. Fix: pass the variable.
- **`bgcolor` doesn't work.** Some Python turtle versions need
  `turtle.bgcolor("skyblue")` instead of `t.bgcolor(...)`.
  Either should work in modern Python. If one breaks, try the
  other.

### Differentiation

- **Younger kids (9-10):** May get the basic `draw_flower`
  function but struggle with the conditional-color stretch.
  That's fine. A row of all-red flowers is a perfectly valid
  base outcome. Push them to the multi-color version only if
  they're ready.
- **Older kids (12+):** Will probably finish base + stretch
  quickly. Push them to the full-scene extension. If they
  finish that, suggest the 2D grid (nested for-loop) or the
  list-based color picker.
- **Advanced (any age):** Will see how to use lists. Let them.
  The list-based version is genuinely better; it just requires
  syntax we haven't taught. Don't penalize early discovery.
- **Struggling:** A kid who can't get the basic flower drawing
  is the kid you focus on. Common cause: forgot to call
  `draw_flower()` after defining it, or indentation got
  scrambled in the function body. Sit with them, walk through
  it once.

### What to watch for

- **The "I built that?" reaction** at the end of Part B. Several
  kids will notice their full scene actually looks like
  something. Affirm. "Yes, you wrote 50 lines of Python and made
  a garden. Six weeks ago you'd never typed Python."
- **Buddies trading ideas.** This session is great for buddy
  collaboration — one buddy adds a sun, the other adds clouds,
  they each contribute pieces to a shared scene. Encourage.
- **Note milestone-project signals.** When kids start adding
  things to their garden ("can I make the petals different
  shapes?", "can I add bees?"), that's the kid telling you
  what they're excited about. Note for next week.
- **Kids who finish everything and start asking "what's next?"**
  Foreshadow the milestone project. "Next week is your turn —
  what would you build if it was your idea?"

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **Milestone project ideas each kid mentioned today:**

The last bullet matters. Note ideas you heard kids excited about
during the session. You'll use these in Session 8 when helping
kids who arrive without a clear plan.

### Connections forward

- **Session 8 (next week, milestone + demo).** Today's preview
  ideas seed next week's planning. Have students bring an idea;
  if they don't, you'll have the suggestion list to reference.
- **Phase 3 Session 1 (Python without turtle).** Today is the
  *last* session with turtle. Phase 3 starts a more general
  Python journey — strings, lists, file I/O, etc. Foreshadow
  lightly: "next phase, we leave the turtle behind and Python
  gets more general."
- **Lists** — mentioned today as a "better way" for the color
  picker. Lands properly in Phase 3.
- **Pygame (Phase 6).** Today's `draw_flower(x, color, size)`
  pattern — a function that takes parameters and draws something
  visual — is exactly the structure of Pygame sprite drawing.
  Today's habits transfer directly.
- **The peanut butter callback opportunity:** when a flower
  doesn't appear where expected because of a `goto`/`setheading`
  issue, that's a precision moment. The turtle did exactly what
  the code said.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Pre-built finished garden scene for the destination preview
- [ ] Projector (helpful for the function decomposition
      walkthrough)
- [ ] Class roster with space to note each kid's milestone idea
