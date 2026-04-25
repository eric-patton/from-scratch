## Session 4 — Teacher Notes

*Phase 1, Scratch · Session 4 of 9 · Title: Events — making things
happen when...*

### Purpose of this session

The shift from "one-script programs" to "multiple scripts firing
independently" is a real conceptual jump even though the blocks
themselves are simple. Three jobs, in priority order:

1. **Land the multiple-scripts model.** Up to now, every program had
   one starter block (the green flag) and one stack underneath. From
   today on, sprites can have many scripts, each triggered by its
   own event, each running independently. This is the model that
   real game and app development uses, and most kids will need to
   see it twice before it sinks in.
2. **Get them controlling sprites in real time.** Arrow-key
   movement is the first thing in the curriculum that *feels like a
   game.* Several kids will get visibly excited. Lean into it.
3. **Reinforce "each sprite has its own scripts."** Introduced in
   Session 2's stretch goal, but most kids didn't actually do it.
   Today's Part B forces it. Be ready to walk a few kids through the
   sprite-switching mechanic.

Broadcasts (`broadcast` and `when I receive`) are deliberately *not*
in this session. They're powerful but abstract; better introduced
later when there's a concrete need for them (multi-sprite
coordination in a milestone project, for instance).

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with a fresh Scratch project, ready for you to build
  a multi-event sprite at the projector.
- If projecting, make sure the keyboard you're using actually works
  — kids will see you press keys and watch the cat move. A flaky
  demo here kills momentum.
- Verify Scratch on the W202NA machines specifically — keyboard
  event handling is fine but worth a sanity check.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was loops + the pen.
  Anyone want to show what they drew at home?
- **Part A: events** (~40 min) — concept intro ~5 min, multi-event
  sprite demo ~10 min (three scripts on one sprite), arrow-key
  movement build ~20 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: two-player** (~35 min) — adding the second sprite ~10
  min (sprite-switching mechanic takes time to land), WASD scripts
  ~10 min, two-player play ~10 min (kids will want to race each
  other; let them), wrap-up ~5 min.

If running short, **the WASD/two-player half can be cut.** Part A
gets the conceptual content across; Part B is reinforcement plus the
"this is fun" payoff.

### Teaching Part A

The opening "every program starts with the green flag — but actually
no" framing is the lesson. Make it explicit at the projector:

- Open the Events category. "Look how many other ways to start
  there are. We've only ever used the first one."
- Build the three-script cat (green flag → reset, space → say hi,
  click → turn). **Build them as three separate stacks, side by
  side in the script area.** Kids who try to snap them together
  need to see immediately that they're separate.

When you demo the three-script cat, **trigger each event in order
slowly** — click the flag, then press space (and let the cat say
"Hi!" for the full second), then click the cat. The pause between
each helps kids see "three things, three triggers, three results."

For the arrow-key movement build:

- Walk through the **first** script (right arrow → change x by 10)
  at the projector. Demonstrate `change x` actually moving the cat.
- Then have students build the other three on their own. They'll
  copy the pattern.
- The negative numbers (`-10`) are worth pointing out explicitly —
  some kids will type `10` for left arrow and be confused. "Left is
  negative on the X axis. Down is negative on the Y axis."

The "movement feels choppy when you hold an arrow key" issue is
worth naming briefly. **Don't fix it.** It's the natural setup for
Session 5's smoother-movement upgrade using `forever + if key
pressed`. Plant the seed: "we'll fix this next week."

### Teaching Part B

The sprite-switching mechanic is the new mechanical thing this half.
Demo it explicitly at the projector:

- Click "Choose a Sprite" (cat-with-plus, bottom-right). Add any
  sprite.
- **Notice the script area changed** — it's now empty because you're
  looking at the new sprite. Point this out out loud: "the cat's
  scripts are still there, we're just not looking at them."
- Click the cat in the bottom-right panel. Scripts come back.
- Click the new sprite. Scripts disappear (it has none yet).
- Now build a script on the new sprite. Switch back to the cat.
  That script's gone — because it's on the *other* sprite.

This back-and-forth confuses several kids per cohort. Be ready to
sit with them through it.

For the two-player play time: **let it be loud.** Buddies will
absolutely race each other. That's the goal. The session ends with
"this is the most fun thing you've built so far," which sets up
energy for Session 5 (the real game).

### Common stumbles

- **All four arrow scripts snapped into one stack.** Symptom: only
  one direction works. Cause: kid tried to combine the four scripts
  into one stack. Fix: explain that each starter block needs its
  own stack.
- **Negative numbers typed as `-10` vs. `0 - 10` vs. `10 -`.** The
  `change x by` field accepts a number directly. Just type `-10`.
  Don't try to subtract.
- **Cat moves to (0,0) but then nothing else works.** Forgot to add
  the arrow-key scripts, or forgot to click on the cat to make it
  the active sprite before adding them.
- **Adding a second sprite and then the cat stops responding.**
  Confusing — the cat's scripts are still there, just behind the
  scenes. Click the cat in the sprite list to see them again.
- **Scripts on the wrong sprite.** Kid added WASD scripts but to the
  cat instead of the new sprite. Cat now responds to BOTH arrows
  and WASD; new sprite responds to nothing. Click each sprite in
  turn and look at its scripts to diagnose.

### Differentiation

- **Younger kids (9-10):** May struggle with the WASD layout if
  they're not familiar with it. WASD is a gamer convention. If a
  kid is genuinely confused, let them use IJKL or some other
  pattern. The lesson is about *mapping different keys to different
  sprites*, not about WASD specifically.
- **Older kids (12+):** Will probably blow through everything. Push
  them to the extension (clickable third sprite that teleports).
  If they finish that, suggest: "make your cat respond to *six*
  different keys — arrows for movement, space for an action, R to
  reset position." Builds the muscle memory for events.
- **Advanced (any age) with prior Scratch experience:** May already
  know events. Push them to add `wait until <key pressed?>` from
  the Control category. (We're not formally teaching it; let them
  discover.) Or have them buddy a struggling kid through Part B.
- **Struggling:** If a kid isn't getting "each script is separate,"
  walk through the three-script cat with them slowly. Have *them*
  press each key in turn while you point at which script ran. The
  cause-and-effect needs to land visually.

### What to watch for

- The "this is fun" moment when kids realize they can drive the cat
  with the arrow keys. Watch for it. Several kids will visibly light
  up at that point.
- Buddy collaboration in Part B. The two-player WASD/arrow setup is
  ideal for buddies — one keyboard, two players, one stage. If your
  buddy assignments are working, this session will show it. If
  they're not, this is where you'll see it.
- Quietly competitive moments. Some kids will turn the two-player
  setup into "I can catch you" or similar. Don't squash it. This is
  exactly the moment programming starts to feel like creating
  something they own.
- Kids who are still copying the cat-script template into the wrong
  sprite. Common; fix gently and don't make a big deal.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Smooth movement upgrade in Session 5.** The "choppy when held"
  issue from today's arrow-key movement gets fixed next week using
  `forever + if key pressed`. Make sure to call it back: "remember
  how it was a little choppy? That's about to get smooth."
- **Broadcasts** — deferred. Will probably appear in Session 7's
  mini-game when sprites need to coordinate ("ball: I just hit the
  paddle, broadcast 'paddle hit'; paddle: when I receive 'paddle
  hit', do something"). Or Phase 6's Pygame work where the
  equivalent concept is event queues.
- **Multi-sprite scripts model.** Reused in every Pygame project in
  Phase 6 — each game object has its own update logic, all running
  in parallel.
- **Peanut butter callback opportunity:** if a kid's WASD script is
  on the wrong sprite, that's a precision moment. "What did you tell
  the computer? You said 'when W is pressed, change the cat's X.'
  But the cat already had arrow scripts; the new sprite has nothing.
  The computer did exactly what you told it."

### Materials checklist

- [ ] Demo machine with Scratch open
- [ ] Working keyboard (test it on the projector machine first!)
- [ ] Class roster
