## Session 2 — Teacher Notes

*Phase 2, Python with Turtle · Session 2 of 8 · Title: Telling the
turtle what to do*

### Purpose of this session

Less of a transition than Session 1, but still doing real work.
Four jobs, in priority order:

1. **Build typing fluency.** Last week was the shock; this week is
   the practice. Students should leave today noticeably more
   comfortable typing Python than they were last week. The way
   that happens is by typing more.
2. **Introduce coordinate-based positioning.** `goto(x, y)` and
   `setheading(angle)` are the new mechanics. They unlock
   multi-element drawings, which is the visible payoff of this
   session.
3. **Land "comments" as a real tool.** `# this is a comment` is a
   small syntax addition that pays off all the way through the
   curriculum. Frame it as "leaving notes for yourself or other
   readers." Use it in the demo code.
4. **Set up loops next week.** The "your code is getting long and
   repetitive" feeling is the motivation for loops. Don't fix it
   today — let students experience it. The "wouldn't it be great
   if you could say 'draw a square' instead of eight lines" line
   at the end of the wrap-up is the bridge.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Your demo `scene.py` file pre-built and saved, ready to show
  the finished example at the projector if needed.
- Verify all student machines from last week still have working
  Thonny + turtle. Should be fine; sanity check anyway.

**Prep time:** ~10 minutes. The session is mostly typing practice;
prep is light.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was Thonny + first
  turtle. Anyone draw something cool at home?
- **Part A: new turtle commands** (~40 min) — `goto` ~10 min,
  `setheading` ~10 min, `circle` ~5 min, `write` ~5 min, build
  the sun + house scene together ~10 min.
- **Break** (~5 min).
- **Part B: make it your scene** (~35 min) — choose-your-element
  base goal ~15 min, stretch + extension for the kids who finish
  ~15 min, wrap-up ~5 min.
- **Wrap-up** (~5 min).

If running short, **the Part B stretch can be cut.** The scene-
building exercise (Part A + Part B base) is the session.

### Teaching Part A

The goal of Part A is muscle memory through small additions. Walk
through each new command at the projector, but spend most of your
time letting them type and run.

#### `goto`

Important to land:

- The coordinate system. Most kids know it intuitively from
  Scratch (you covered it in Session 2 of Phase 1). Quick
  callback: "remember the stage in Scratch, with x going left/
  right and y going up/down? Same coordinate system here."
- `(0, 0)` is the middle. Negative x is left. Negative y is down.
- The pattern is **almost always**: `penup()` → `goto(x, y)` →
  `pendown()` → draw. Drill this. Without `penup`, the turtle
  draws a line from wherever it was to the new spot, which is
  almost never what you want.

#### `setheading`

Easier conceptually than `goto`. The four cardinal angles (0, 90,
180, 270) are usually enough. Don't get into 45° or other
intermediate angles unless a kid asks.

The most common mistake: kids forget `setheading` after a `goto`,
draw a line, and it goes the wrong direction because the turtle
was facing wherever it was facing from before. The fix: get into
the habit of "after every `goto`, ask yourself which way the
turtle should be facing."

#### `circle`

Mechanically easy — `t.circle(radius)`. The visual feedback is
satisfying.

A subtlety worth mentioning if asked but not formally teaching:
the turtle starts the circle from its current position, and walks
*counter-clockwise* by default (because positive angle = left in
turtle's coordinate system). Most kids don't notice; the ones who
do can use `t.circle(-50)` to go clockwise.

#### `write`

Easy mechanically. The font argument syntax (`font=("Arial", 20,
"normal")`) is genuinely confusing — it's a tuple inside a
keyword argument. **Don't try to explain.** Just have them type
it. Treat it as "this is the formula for making text bigger;
change the 20."

A handful of advanced kids will ask "why is it like that?" Honest
answer: "tuples and keyword arguments are concepts we'll learn
later. For now, just use the formula." That's a totally valid
answer and models an important skill: using something useful before
you understand it fully.

#### The built-together scene

This is the moment to introduce comments explicitly. Walk through
the scene code at the projector. Stop at the `# the sun` line:

> "See this hash mark? Anything after a `#` on a line is ignored
> by Python. We use it to leave notes for ourselves and other
> readers. Like little labels saying 'this section draws the sun.'
> They don't change what the program does, but they help anyone
> reading the code understand it."

Then continue. Have the kids type the full scene, including the
comments. Make a point of using comments yourself in any
follow-up demos.

### Teaching Part B

This is mostly hands-off time. Walk the room, help where needed.

Things to encourage:

- **Personal customization.** Some kids will go full-creative;
  their scenes will look nothing like the example. Encourage
  this. Personal investment matters.
- **Use of comments.** When a kid's code starts getting long and
  hard to follow, suggest: "Try adding a `# the tree` comment
  before the tree section. Makes it easier to find things later."
- **Stretch elements.** A kid who finishes the base quickly should
  add more elements, not just stop. The whole point of stretch
  goals is to keep faster kids productively occupied.

Things to redirect:

- **A kid trying to draw something genuinely complex** (e.g., a
  detailed castle, a dragon). Gently push toward simpler shapes.
  Turtle is not great for ornate drawings, especially without
  loops or functions yet. Save ambition for next week's loops.
- **A kid whose drawing keeps "messing up" because the turtle
  didn't end where they expected.** This is usually a missing
  `setheading` after a `goto`. Walk them through diagnosing it:
  "Where do you want the turtle facing when it starts this part?
  Did you `setheading` to that direction?"

### Common stumbles

- **Drawing a line during `goto`.** Forgot to `penup()` first.
  Line goes from previous position to new position.
- **Element drawn in the wrong direction.** Missing `setheading`
  after a `goto`. The turtle was facing some random direction
  from before.
- **Coordinates that put the drawing off-screen.** Stage is roughly
  ±240 wide and ±180 tall. Numbers like `goto(500, 500)` send the
  turtle off-screen and the drawing disappears. Easy fix: smaller
  numbers.
- **Quotes around colors.** `t.color(red)` doesn't work; needs to
  be `t.color("red")`. `red` without quotes is interpreted as a
  variable (which doesn't exist), so you get a `NameError`.
  Reinforce: colors are *strings*, they need quotes.
- **Comma inside parentheses for `goto`.** Some kids type
  `t.goto(100 50)` (forgot the comma). `t.goto(100, 50)` is
  correct. Easy to miss visually.
- **Circle going the wrong way.** Default is counter-clockwise.
  Use `t.circle(-50)` for clockwise. Don't formally teach unless
  asked.
- **Smart-quote contamination.** Same as last week. Curly quotes
  in copied code break things.

### Differentiation

- **Younger kids (9-10):** May still be slow typists. Emphasize
  building one element at a time. Don't let them try to write
  the whole scene at once and then debug — break it into pieces.
  Type the sun, run, see it. Type the house, run, see it. Each
  piece confirmed before adding the next.
- **Older kids (12+):** May try to be clever and combine multiple
  elements before testing. Caution them: "Build small. Test
  often." This is actually the more important programming skill;
  use Part B as a chance to instill it.
- **Advanced (any age):** Will finish base + stretch quickly. Push
  them toward extension. If they finish that, mention `for i in
  range(N):` and let them discover loops a week early. (They've
  earned it.)
- **Struggling:** A kid who couldn't get last week's square to
  work probably needs to redo Part A of last week before Part A
  of this week. Have them sit with their buddy and rebuild the
  square first, then move forward. Don't push them through new
  material until the foundation works.

### What to watch for

- **Kids whose typing is faster this week than last week.** Most
  will be. Note the few who aren't — they may need typing
  practice at home.
- **Kids who are getting frustrated by their drawing not matching
  what they had in mind.** Common; often a `goto` / `setheading`
  positioning issue. Sit with them, narrow down the problem, fix
  it together.
- **Kids who finish their scene and start playing with `circle`
  or `write` variations spontaneously.** That's exactly the
  curiosity you want to encourage. "What does `circle(50, 90)`
  do? Try it." Mr. Eric circulates and is enthusiastic about
  weird discoveries.
- **The "I want to do this 10 times" moment.** Some kids will
  realize that drawing 10 trees would mean copying the same code
  10 times. They're discovering the motivation for loops on their
  own. Confirm: "Yep. That's what we're doing next week. Hold
  onto that thought."

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 3 (next week, loops in Python).** The "your code is
  getting long and repetitive" feeling from today is the
  motivation. Mirror Phase 1 Session 3's setup: drag 10 move
  blocks → ugh → here's `repeat`. Same arc.
- **Session 4 (functions).** The "wouldn't it be nice if I could
  say 'draw a square' in one line" feeling is the *bigger*
  motivation that lands in Session 4. Today's tedium plants the
  seed; loops next week are the first answer; functions in Session
  4 are the deeper answer.
- **Comments will be reused** in every Python session from now on.
  Build the habit early.
- **Multiple turtles** (mentioned in stretch) become genuinely
  useful in Session 4 once functions exist. A function that draws
  a turtle, called multiple times with different turtles, is a
  preview of where this is heading.
- **Coordinate system** lands in Phase 6 (Pygame) where it returns
  for game programming. Don't formally callback until then; just
  reuse the mental model.

### Materials checklist

- [ ] Demo machine with Thonny open
- [ ] Demo `scene.py` pre-built (sun + house) ready to show
- [ ] Projector (helpful for the new commands intro)
- [ ] Class roster
