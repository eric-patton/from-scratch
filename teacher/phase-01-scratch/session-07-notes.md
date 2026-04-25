## Session 7 — Teacher Notes

*Phase 1, Scratch · Session 7 of 9 · Title: Putting it together — a
small game*

### Purpose of this session

This is the synthesis session. Four jobs, in priority order:

1. **Demonstrate that students can build a complete game from
   scratch (no pun intended) using just what they know.** No new
   blocks. No new mechanics. Everything is review and combination.
   This is huge for confidence — they will feel competent.
2. **Introduce the game-over mechanic.** `stop all` is technically
   new but conceptually trivial. The point is the *design lesson*:
   real games have a losing condition, not just a winning one.
3. **Set up Sessions 8-9 (milestone project).** End of class, every
   student should leave thinking about what they want to build for
   their own milestone. The "ideas" list at the end of the student
   handout exists to seed this.
4. **Make absolutely sure every student has a working, playable
   game by end of session.** Some kids are going to want to revisit
   this Apples and Rocks game vs. inventing their own milestone
   from a blank page. That's fine — but they need today's game to
   work first.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with a working Apples and Rocks game ready to show
  at the start as a "this is what we're building" preview.
- Verify the rock sprite is in the Scratch library. Should be —
  there's a "Rocks" sprite traditionally available. If for some
  reason it isn't, any sprite that's clearly distinguishable from
  the apple works.
- Have the Session 5 catch-the-apple project saved somewhere
  shareable, in case any kid lost theirs. Some kids will want to
  reference last week's code.

**Prep time:** ~25 minutes. Build the full Apples and Rocks game
once before class. Play it for two minutes. Tweak the speed numbers
if needed.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was variables. Anyone
  beat their own catch-the-apple high score this week?
- **Part A: rebuild catch-the-apple cleanly with score** (~40 min)
  — preview the finished game ~3 min, build the cat ~10 min, build
  the apple ~20 min, play time + checkpoint ~7 min.
- **Break** (~5 min).
- **Part B: add the rock + game over** (~35 min) — concept ~5 min
  ("real games have a losing condition"), build the rock ~10 min,
  test + tune speeds ~10 min, milestone project preview ~10 min.
- **Wrap-up** (~5 min).

If running short, **the milestone project preview can be cut from
this session** (it's also covered in Session 8's intro). Don't cut
the rock-and-game-over build — that's the new lesson.

### Teaching Part A

The "rebuild from memory" framing matters. Sell it:

- "We're building this from scratch on purpose. Don't open last
  week's project. If you can't build this from memory, that tells
  you something — and we'll fix it together."
- **Don't walk them through it block-by-block at the projector.**
  Have students build it themselves while you walk the room. Help
  the kids who get stuck.
- This is your first chance to see who has *actually* internalized
  Sessions 1-6 vs. who was copying their buddy. Take notes; this
  matters for milestone project pairing.

If a kid is genuinely stuck reproducing the cat or apple from
memory, **point them at the textbook chapters for Sessions 5 and
6.** Don't recap the lessons in class — let the textbook do it. This
is exactly the use case the "If you missed this session" sections
were designed for. They double as references.

The Part A checkpoint is intentionally early in the session. By
~40 minutes in, every student should have a working
catch-the-apple-with-score. That's the foundation for Part B. If
half the room is still struggling at the 40-minute mark, slow Part
B way down and treat it as catch-up time.

### Teaching Part B

The "real games have a losing condition" framing is the new design
lesson. Make it explicit:

- "Right now, you can stand still and play forever. Is that a real
  game? What's missing?" Wait for "you have to be able to lose" or
  similar.
- "Today we add a way to lose. Once we do, this becomes an actual
  game."

Building the rock is mechanically easy — it's the same shape as
the apple's script with two changes (game over instead of score,
no penalty for missing). Walk through the structure at the
projector, then have students build it.

The `stop [all]` block from Control is the new piece. Demo it on
the projector: build a fake script that just does `say "Hello!"`
and `stop all`. Click the green flag. The cat says hello and
everything freezes. "That's it. The whole program stops. That's
how a game ends."

After Part B is built, **let kids play their games for 5-10 minutes
straight.** This is where the session pays off. Some will tune the
speeds (rock at -4, apple at -3, etc.). Some will compete with
their buddy. Some will start asking "can I add another rock?" That's
the milestone-project hook — answer with "yes, that's exactly what
next week is for."

### The milestone project preview

End-of-session, ~10 minutes. The goal is to get every student
*excited* about something they want to build. Don't oversell the
"final demo day" piece — for some kids that's stressful. Frame it
as "you'll have two weeks to make whatever you want."

Read the "ideas" list from the student handout out loud, but
emphasize that **anything they can imagine works.** Some of the
best milestone projects come from kids who go totally off-list.

For kids with no idea: that's fine. Tell them to pick something
from the list as a starting point and modify it. "Catch game with
weird things" is a totally valid project for a kid who just wants
to ship something.

For kids with too many ideas: tell them to pick *one* and write it
down. They can always do the others later.

Some kids will come up with ambitious ideas they can't finish in
two weeks. Don't squash the ambition — but be ready in Session 8 to
help them scope down. "Ambitious project, smaller scope" is a
better experience than "abandoned project."

### Common stumbles

- **Score variable doesn't appear.** Forgot to make it before
  building the cat's script. Easy fix: Make a Variable, then go
  back and add `set [score] to 0` to the cat's green-flag script.
- **The rock and apple are both pointing at "Sprite1" but the
  cat's actually named "Cat" (or vice versa).** Diagnostic: green
  flag, neither sprite triggers the if-touching block. Fix:
  open the dropdown on `if touching` and pick the correct sprite.
- **Game over fires but score keeps going up.** They put the
  score-update block in the wrong place. Walk through what runs
  after `stop all` (nothing) — so the issue is order or scope.
- **Both apple AND rock at the same x value (often 0).** They
  forgot the `pick random` in one of them. Fix: copy the random
  block from the working one.
- **Rock catches the cat instantly because it spawned on top of
  the cat.** Rare but possible. Add `wait 1 seconds` at the start
  of the rock's forever loop so it doesn't trigger immediately.
- **Game over message says "Game Over!" but the rock keeps
  falling.** Forgot `stop all` after the `say` block. Add it.

### Differentiation

- **Younger kids (9-10):** May need more help reproducing the
  apple-game from memory in Part A. That's fine — pair them with
  a buddy who has theirs working, OR pull up the textbook and
  walk through it together. Treat Part A as a guided rebuild for
  them.
- **Older kids (12+):** Will rebuild Part A in 15 minutes and want
  Part B immediately. Let them. They'll have time for stretch and
  extension. Push them to think hard about their milestone idea —
  this is where they'll get to flex.
- **Advanced (any age):** Will breeze through everything. Push
  them to start prototyping their milestone idea in the remaining
  time. "Start your milestone today if you want."
- **Struggling:** If a kid can't reproduce Part A even with help,
  that's a flag. They missed something foundational from Sessions
  4-6. Don't make them sit through Part B — sit with them, find
  what didn't land, and shore it up. Better to leave today with
  Part A working than Part B half-broken.

### What to watch for

- **The "I built this" moment when the rock-game-over fires for
  the first time.** Every kid has a slightly different reaction.
  Some laugh. Some go quiet. Some immediately say "again." All
  good signs.
- Kids who skipped the score variable in their build. They'll
  realize when they catch an apple and nothing visible happens.
  Easy fix.
- Buddy collaboration in Part A. Watch for kids who are *helping*
  vs. kids who are *doing it for* their buddy. Both happen. The
  former is the goal; the latter shortcuts the learning. Gently
  redirect: "let your buddy type that part."
- Milestone-project signals during the preview. Note which kids
  light up at which idea. Use this to inform your buddy
  reassignments for Sessions 8-9 — pair kids with complementary
  project ideas where possible.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **Milestone project ideas each kid mentioned:**

The last bullet matters — start tracking each kid's project idea
this week so you can think about it before Session 8. Some kids
will change their minds; that's fine. The note is for *you*, not
for them.

### Connections forward

- **Session 8 (next week, milestone project work day 1).** Today's
  game ideas list seeds next week's planning. Have students bring
  an idea; if they don't, you'll have the ideas list to reference.
- **Session 9 (milestone project work day 2 + demo day).** This is
  where today's "build something complete" muscle pays off. Kids
  who built Apples and Rocks today will trust themselves to build
  their own game over two weeks.
- **Phase 6 (Pygame).** Today's game shape (player sprite, falling
  hazards, falling collectibles, score, game over) is *exactly*
  the Pygame programming intro pattern. When you get to Phase 6,
  you can callback hard: "remember Apples and Rocks? We're going
  to build that again in Python — and once you have it, you'll
  realize you can build anything."
- **Peanut butter callback opportunity:** the "score doesn't
  update" or "game over but rock keeps falling" stumbles are
  textbook precision moments. The computer did exactly what the
  code said. Find the gap.

### Materials checklist

- [ ] Demo machine with the finished Apples and Rocks game ready
- [ ] Class roster with space to note each kid's milestone idea
- [ ] Optional: copies of the Session 5/6 endpoint projects to share
      via USB if any student lost theirs
