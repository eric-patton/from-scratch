## Session 3 — Teacher Notes

*Phase 1, Scratch · Session 3 of 9 · Title: Loops — doing things
over and over*

### Purpose of this session

Loops are arguably the single biggest conceptual leap in this entire
phase. This session is doing four jobs:

1. **Land the loop concept.** "Do this thing N times" is the first
   programming idea where the computer does work *you didn't write
   out explicitly*. That's a real conceptual shift, even though
   `repeat` looks innocuous.
2. **Introduce extensions** — specifically the Pen. A small
   meta-lesson: Scratch has more capabilities than what's shown by
   default; you can turn them on. Extensions come back later (sound,
   sensing, music).
3. **Deliver the first "wow" moment of the curriculum.** The cat
   drawing a square is dramatic in a way that walking sequences
   aren't. Several kids will be visibly hooked at this point. Don't
   miss the moment.
4. **Begin pattern recognition.** The polygon stretch (`repeat 4 /
   turn 90`, `repeat 3 / turn 120`, etc.) is the first time students
   are asked to spot a numeric pattern in their own code. This is
   foreshadowing for variables next week and parameterization much
   later.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Scratch open and the **Pen** extension already
  added. (You can add it during class as part of teaching, but having
  it pre-loaded for your own demos prevents fumbling.)
- Verify Pen extension loads on at least one student machine before
  class. Should be fine, but the W202NAs occasionally lag on
  extension load.
- Your demo project should already include a `pen down / move /
  turn / pen up` example you can show as a "here's where we're going"
  preview if energy flags.

**Prep time:** ~15 minutes including pen test on a student machine.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint between.

- **Welcome and recap** (~5 min) — last week was sequences, the
  green flag, "order matters." Quick reminder.
- **Part A: Why loops exist** (~35 min) — the "drag ten move blocks"
  exercise ~5 min, intro to `repeat` ~10 min, square-by-loop reveal
  ~10 min, free experimentation with the number ~10 min.
- **Break** (~5 min).
- **Part B: Drawing with loops** (~40 min) — Pen extension intro ~5
  min, build the square-drawing program ~10 min, polygon
  exploration ~15 min, nested-loop extension for fast finishers ~10
  min.
- **Wrap-up** (~5 min).

If running short, **the polygon stretch is the cuttable piece.** The
square-drawing exercise is the "wow" payoff and shouldn't be cut.

### Teaching Part A

The opening "drag ten move blocks" gag is the setup. **Have them do
it.** Don't tell them in advance that there's a better way. They
need to feel the tedium for the loop's value to land.

- Walk around while they're dragging the ten blocks. You'll see
  several reactions: some kids dutifully drag all ten, some get
  bored and stop at five, some immediately start asking "is there a
  better way?" The kid who asks has just discovered the *motivation
  for loops*. Affirm the question publicly: "Great instinct. Yes,
  there is. We're about to see it."
- When you introduce the `repeat` block, **show its shape first.**
  The mouth is a new visual that kids haven't seen. Drag one out at
  the projector and gesture: "See this opening in the middle? Things
  go inside there."
- The "change the number" exercise (10, 100, 3, 1, 0) is intentional.
  The 0-iteration case in particular is worth noticing — most kids
  expect "0 times" to be an error, not a valid no-op. Mention this
  in passing: "Yep, even zero is allowed. It just doesn't do
  anything."
- The square reveal (`repeat 4 / move 50 / turn 90`) is the lesson
  punchline. **Don't tell them in advance what shape the cat will
  walk.** Let them watch and figure it out. The "ohhhh, it's a
  square!" moment is the whole point.

### Teaching Part B

The Pen extension addition is small but mechanically new. Demo it at
the projector:

- Click the **Add Extension** button (bottom-left, blue `+`). Show
  the menu of extensions. Hover over "Pen" but say "we'll come back
  to others later." Click Pen. Show the new green category.
- Demo the pen with a quick `pen down / move 100` example before
  having them build the full square program. Two seconds of "watch
  this" lands the concept faster than five seconds of explanation.

When they build the full square-drawing program, **walk the room
during the first run.** This is the "wow" moment of the session —
some kids will visibly light up. Catch their eye when it happens.
Public affirmation here ("nice — your code drew that") matters
disproportionately.

For the polygon stretch (3/120, 5/72, 6/60, etc.), let kids
discover the 360 pattern themselves if they can. If a kid is stuck:

- Don't give the formula. Ask: "What do all the numbers add up to?"
  Let them check on their own.
- If still stuck, ask: "How many degrees is a full turn?" Wait for
  "360." Then: "Notice the relationship between the two numbers in
  your loop?" Most kids will get it from there.

For the nested-loop extension (flower of squares), don't formally
teach nested loops. Show the example code on the projector and say
"try this — see what happens." Kids who copy it and modify it
*are* learning by example, which is fine for an extension activity.

### Common stumbles

- **Forgot `pen down`.** Kid runs the program, cat moves correctly,
  no trail. Universal first-time error. Frequent. Just point at the
  Pen category.
- **Forgot to drag a block *inside* the repeat's mouth.** Kid puts
  `move 50` *under* the `repeat 4` block instead of inside it. Click
  green flag → cat moves 50 once, doesn't repeat. Show them the
  visual: blocks inside the mouth are visibly nested.
- **Square is way too big and walks off-stage.** Their `move`
  distance is too high. Suggest 100 or even 50.
- **Cat ends up rotated and facing the wrong way for next run.** Add
  `point in direction 90` (Motion) at the top of the program before
  the loop. (The "reset" idea from session 2 returns.)
- **Pen drawings stack up across runs.** They didn't `erase all` at
  the top. Easy fix but worth pointing out: "Your program needs to
  clean up after itself before it draws."
- **For the stretch:** kid tries `repeat 7 / turn 50`. Doesn't close
  the polygon (7 × 50 = 350, not 360). Don't fix it for them; let
  them discover the 360 rule.

### Differentiation

- **Younger kids (9-10):** May find the polygon math intimidating.
  That's fine — they don't need to *derive* the 360 rule, just
  notice it. The base goal (square) is the required outcome. Stretch
  is genuinely optional.
- **Older kids (12+):** Will probably figure out the 360 pattern in
  the first or second polygon. Push them to the nested loop
  extension. If they finish that, suggest "draw a star" — that
  requires a slightly trickier turn angle (typically 144°), good for
  thinking.
- **Advanced (any age) with prior programming experience:** May know
  loops conceptually already. Push them on aesthetics: vary `set pen
  color` inside the loop so each iteration draws in a different
  color. Then ask: "How would you make the color change *gradually*?"
  (That's a setup for variables next week.)
- **Struggling:** If a kid isn't grasping that "the inside runs N
  times," do this: have *them* run a program with `repeat 3 / wait
  1 second`. The 3-second pause reinforces the count viscerally.
  Then `repeat 5 / wait 1 second`. The number = the number of
  seconds, because the inside runs that many times, with a 1-second
  wait each.

### What to watch for

- **Buddy assignments should be live by now if not before.** Use
  what you saw in sessions 1-2 to pair kids up. This is the session
  where buddy work starts paying off — the polygon stretch in
  particular is great for buddy collaboration.
- **The "wow" moment.** Watch for it. It's visible. When you see a
  kid's face light up at the cat drawing a square, that's a kid
  who's now hooked on programming. Mental note.
- **Kids who finish base + stretch + extension and are bored.** Rare
  this early, but it happens. Have them help a buddy or open a
  side project: "Try to draw your initials by combining shapes."
- **Kids who are still stuck in Part A by the time you're starting
  Part B.** Don't drag them along behind. Let them keep working on
  the basic loop while the rest move on. They'll catch up via the
  "If you missed this" section at home or with their buddy next week.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Variables (next week, Session 4 — wait, that's events. Variables
  in Session 6).** The polygon stretch is foreshadowing — students
  noticed that two numbers (sides count, turn angle) work together
  to define a shape. When variables come up, you can callback: "You
  know how you had to manually retype the loop count and turn angle
  for each polygon? Variables would let you change one number and
  have everything else update."
- **Forever loops** appear here as a stretch idea but become central
  in Phase 6 (Pygame) where game loops are the structure of every
  game.
- **Nested loops** in the extension foreshadow how grids and
  patterns work in Phase 6. The flower-of-squares pattern is exactly
  the shape of code that draws a tiled background.
- **Pen extension** doesn't come back much in Phase 1 after this —
  it's mostly a one-session tool. But the *concept* of extensions
  does (sound, music, sensing).
- **Peanut butter callback opportunity:** if a kid forgets `pen
  down` and is confused why nothing's drawing, that's a peanut
  butter moment. "What did you tell the computer to do? Did you tell
  it to put the pen down?" The computer didn't guess.

### Materials checklist

- [ ] Demo machine with Scratch open, Pen extension pre-added
- [ ] Working square-drawing demo program ready to show
- [ ] Projector (helpful for the Add Extension demo)
- [ ] Class roster
