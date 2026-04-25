## Session 2 — Teacher Notes

*Phase 1, Scratch · Session 2 of 9 · Title: Sequences and the stage*

### Purpose of this session

This is the first session where students build something
*intentionally*. Three jobs, in priority order:

1. **Land "order matters" as a concept.** Last week was about
   precision (peanut butter). This week is about *sequence*. The
   same blocks in a different order produce different behavior. This
   is one of the foundational ideas of programming and it generalizes
   to everything that follows.
2. **Introduce the green flag as the start trigger.** Until now, kids
   were clicking individual blocks. The green flag is their first
   "this is how a program begins" concept. They'll use it every
   single session for the rest of Phase 1.
3. **Get every student to a "I built a thing on purpose" moment.**
   The Part B scripted scene is small but real. They start with a
   blank project and end with a runnable scene. That arc matters.

If you only get through Part A, that's still fine — you've delivered
the conceptual goods. Part B is reinforcement.

### Before class

**Bring:** nothing physical. This session is all on-screen.

**Set up:**

- Open Scratch on your demo machine before class so you can show the
  green-flag-clicked block without fumbling through the menus.
- Verify Scratch loads on every student machine. (You did this last
  week, but a kid may have closed it and now it won't relaunch on
  the W202NAs without a small wait. Reboot if needed.)
- If you're projecting, mirror your screen. The Events category
  (yellow) is at the bottom of the block list and easy to miss; a
  shared screen helps everyone find it together.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint between.

- **Welcome and recap** (~5 min) — peanut butter callback if anyone
  brings it up; quick check that Scratch is open on every machine.
- **Part A: Sequences** (~40 min) — concept + green flag intro ~10
  min, build the 4-block sequence ~10 min, "now break it"
  reordering exercise ~15 min, reset/checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: Scripted scene** (~35 min) — talk-it-through phase ~5
  min, building the scene ~20 min, stretch/extension for fast
  finishers ~10 min, wrap ~5 min.

If running short, **Part B is the cuttable half.** Part A delivers
both the concept (sequence/order) and the new tooling (green flag,
wait, basic motion). Cutting Part B costs reinforcement, not
material.

### Teaching Part A

The whole point of Part A is the moment when a student moves the
`wait` block to a new position and watches the behavior change.
Engineer for that moment.

- **Don't pre-explain "order matters."** Let them experience it
  first. Have them build the 4-block sequence and run it. Then say
  "okay, now drag the wait block to the very top." Let them notice
  on their own.
- **Use the projector or your demo machine for the initial build.**
  Make sure everyone gets the right blocks snapped in the right
  order before they run it. The lesson is "order matters" — it lands
  better if the *first* run does what you'd expect, then the
  *modified* run is the surprise. If a kid's first run is already
  broken because they snapped blocks wrong, the lesson muddies.
- **Land the line out loud:** "Same blocks. Different order.
  Different program." Make eye contact when you say it. This is the
  thesis statement of the session.
- **The reset trick (`go to x: 0 y: 0`) is genuinely useful.** A few
  kids will resist it because they think they should "just be
  careful" not to drift. Frame it as: "Real programmers make their
  programs reset themselves. You'll thank yourself in five minutes
  when you've clicked the green flag forty times."

### Teaching Part B

Two things to model before they start:

- **Talk through it in plain words first.** Walk to the whiteboard
  (or just to the front of the room) and say out loud: "the cat
  starts here, walks to here, says hello, waits, walks off here."
  This is the decomposition habit that goal #1 is about. Naming the
  steps before coding them is the move you want to instill.
- **Show them where to find each block.** Briefly show `glide`,
  `say`, and how to set the x coordinate on `go to`. Then *stop
  helping* and let them build.

During build time, walk the room. Look for:

- **Kids who skipped the "talk it through" step** and are flailing
  with random blocks. Pull them back: "Tell me what's supposed to
  happen first."
- **Kids who got the base scene working in 5 minutes.** Push them to
  stretch (second sprite). Don't let them sit idle.
- **Kids stuck on coordinates.** The stage is roughly 480 wide × 360
  tall, with (0,0) in the middle. Many will guess that x = 0 is the
  left edge. Walk them through it once at the projector.

### Common stumbles

- **"Nothing happens when I click the green flag."** Almost always:
  the blocks aren't snapped to the green-flag block. They have to
  *touch* visually. If there's a tiny gap, the green flag triggers
  nothing.
- **Cat already off-screen, can't see what's happening.** Drag the
  cat back to the middle of the stage with the mouse. (This is the
  motivation for the reset trick.)
- **Glide vs. move confusion.** `move 10 steps` is instant. `glide 2
  secs to x: 0 y: 0` takes 2 seconds. Some kids use `move` and then
  add `wait` thinking they're "animating" — gently clarify.
- **Forgot to add a sprite for Part B stretch.** The "second sprite
  responds" bit only works if there's a second sprite. Make sure
  they added one (bottom-right "Choose a Sprite" button).
- **Two sprites, one set of scripts.** A common stumble:
  student writes scripts under the cat sprite, then adds a second
  sprite expecting it to also run those scripts. Each sprite has its
  own scripts. They'll need to *switch sprites* in the bottom-right
  panel and add scripts to the second one separately.

### Differentiation

- **Younger kids (9-10):** May struggle with the coordinate system
  for `go to x: y:`. Show them the trick: drag the cat to where you
  want it on the stage, then look at the X and Y values that update
  in the sprite's properties (top-right). Now use those numbers in
  the block. Coordinates from observation, not from math.
- **Older kids (12+):** Often blow through Part A and want more.
  Push them on Part B's stretch (second sprite) and extension
  (dance). If they finish all of that, ask them to use `repeat`
  blocks (foreshadowing next week) or to make the cat draw something
  with the pen extension. Don't formally introduce loops yet — let
  them discover them.
- **Advanced (any age) with prior Scratch experience:** Same as
  above. Also, ask them to help a buddy who's stuck on Part B —
  start the mentor habit.
- **Struggling:** If a student isn't getting Part A's "order
  matters" concept, sit with them for two minutes. Have *them*
  drag the wait block to a different position and predict what will
  happen before clicking the green flag. The prediction is the
  thinking step that needs to land.

### What to watch for

- Kids who finish Part A's "now break it" exercise without seeming
  to notice the behavior actually changed. Some kids click run, see
  "stuff happened," and call it done. Ask them: "Was that the same
  thing as before? What was different?" Force the comparison.
- Buddy candidates. By end of session 2 you should be ready to make
  initial buddy assignments — either at end of class today or
  start of session 3. Pair confident-and-explored with
  tentative-or-new.
- The kid who's *still* afraid to break things. Today's lesson is
  literally "break things on purpose to learn." If a kid won't do
  it, gently push: "Drag that block. I dare you. It's fine."

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sequences are the substrate for everything.** Every session from
  here on builds on "code runs in order." Loops, conditionals,
  functions — all of them are ways to *modify* sequences.
- **The green flag will be in every Scratch session.** No need to
  re-explain it; just expect them to use it.
- **The "talk it through first" habit** introduced in Part B is the
  decomposition skill named in goal #1. Reinforce it every session
  by asking: "Before you write any code, tell me what it's supposed
  to do."
- **Coordinate trick (drag cat → read x/y → use in block)** comes
  back when we get to Pygame in Phase 6 — same coordinate system
  conceptually.

### Materials checklist

- [ ] Demo machine with Scratch open
- [ ] Projector (optional, but useful for the Events category tour)
- [ ] Class roster
