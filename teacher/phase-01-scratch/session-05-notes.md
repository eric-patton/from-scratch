## Session 5 — Teacher Notes

*Phase 1, Scratch · Session 5 of 9 · Title: Conditionals — making
decisions*

### Purpose of this session

This is the most ambitious session in Phase 1 so far. Four jobs, in
priority order:

1. **Land conditionals as a concept.** "Check, then decide" is the
   foundation of every interactive program ever written. Combined
   with sensing blocks, conditionals are how programs perceive and
   respond to their environment.
2. **Combine everything.** Sequences, loops, events, and now
   conditionals. The catch-the-apple game uses all four. This is
   the first session where multiple programming concepts work
   together to make something real.
3. **Deliver the second "wow" moment of the curriculum.** The first
   was the cat drawing a square. This one is "I built a game I can
   play." It hits even harder for kids who are starting to wonder
   "when do we make actual games?"
4. **Set up Session 6 (variables).** The catch-the-apple game has
   no scorekeeping because variables haven't been introduced yet.
   Several kids will notice this and ask. That's a perfect setup.

This session is busier than Sessions 2-4. Plan to keep tight time
on Part A so Part B has the room it deserves.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Scratch open and a working catch-the-apple game
  ready to show as a "here's what we're building" preview at the
  start of Part B.
- Verify the apple sprite is in the default Scratch sprite library
  (it has been historically; should still be there). If for some
  reason it isn't, any small sprite works as a substitute.
- Test the smooth-movement script before class. Make sure `change x
  by 5` (not 10) — the speed matters for the game's feel.

**Prep time:** ~20 minutes. Build the demo game once before class so
you're not fumbling in front of students.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was events. Anyone want
  to show their two-player game?
- **Part A: conditionals + smooth movement** (~35 min) — concept
  intro ~10 min (the diamond shape, the if block, sensing), build
  the smooth-movement cat ~20 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: catch-the-apple** (~40 min) — preview the finished game
  ~3 min, set up the cat ~5 min, build the apple ~20 min, play
  time ~7 min, stretch for fast finishers ~5 min.
- **Wrap-up** (~5 min).

If running short, **the stretch goal (missed condition) is the
cuttable piece.** Don't cut Part B itself — the game-building is the
session.

### Teaching Part A

The diamond-shape concept is genuinely new. **Show it visually at
the projector:**

- Drag out an `if` block. Point at the diamond slot. "Anything that
  fits in here has to be the same shape."
- Open the Sensing category. Hover over the diamond-shaped blocks.
  "These all answer yes or no. They fit."
- Hover over the rounded blocks (like `x position`). "These don't
  fit. They give numbers, not yes/no."

If a kid tries to drop a number block into a diamond slot, it won't
snap. The visual feedback is the lesson.

For the smooth-movement build:

- **Make the callback to Session 4 explicit.** "Remember how it was
  choppy when you held the key down? Watch this." Run last week's
  version (or have a kid demo theirs). Then run the smooth version.
  The before/after contrast is the whole motivation.
- Build it at the projector once, slowly. The pattern is `forever {
  if X then Y; if X then Y; ... }` — repetitive and easy to copy
  once they see it.
- Common confusion: kids will try to put each `if` block under its
  own `when key pressed` event. Redirect: "All four `if` blocks go
  inside *one* forever loop, under *one* green flag. We're checking
  the keys ourselves now, not waiting for events to fire."

The number `5` (instead of `10` from Session 4's event-based
movement) is intentional. The forever loop runs many times per
second, so each individual `change x by` should be smaller, or the
cat zooms across the stage faster than the keyboard repeat rate.
Kids may notice this themselves; if they don't, just use 5 without
explaining the reason. They'll feel it if it's wrong.

### Teaching Part B

**Show the finished game first.** Before any building, run your
pre-built catch-the-apple game on the projector. Let kids see what
they're about to build. The motivation matters.

Build the apple together, but encourage independence:

- Walk through the apple's script structure at the projector
  (forever, change y, if touching, say "Yum!", reset).
- **Then stop.** Have students build it themselves. Walk the room.
- The single trickiest block is `pick random -200 to 200`. The
  random block is in Operators (green); it's diamond-shaped;
  dragging it into the `x:` slot of `go to` is unfamiliar. Demo
  this specifically.

**Sprite naming.** When students add an apple, Scratch names it
something like "Apple" by default. The cat is "Sprite1" or "Cat"
(varies by Scratch version). The `if touching [dropdown]` needs to
point at the cat from inside the apple's script. Walk a few kids
through this — it's almost always the source of "my apple won't
trigger Yum" confusion.

Once kids have working games, **give them play time.** Three to
five minutes of just playing each other's games is huge for
motivation. Encourage them to share with their buddy.

For the stretch (missed condition): the y-position comparison block
is the new mechanic. `y position` from Sensing (rounded) plus `<`
from Operators (also a comparison block). Together they form a
diamond that fits in the `if`. Some kids will get it instantly;
some will need help finding both halves.

### Common stumbles

- **`if` block diamond slot empty.** Kid built `if then change x by
  5` with nothing in the diamond. Symptom: the inside never runs (or
  Scratch shows it grayed out). Fix: add a sensing block to the
  diamond.
- **Round block in diamond slot.** Kid tried to drop `x position`
  (rounded) into an `if`'s diamond slot. Doesn't snap. Symptom:
  they keep trying. Explain: rounded gives numbers, diamond gives
  yes/no, only diamond fits.
- **All four `if` blocks NOT inside the forever loop.** Symptom: cat
  moves once per click of the green flag and then nothing. Fix: drag
  the `if` blocks *into* the forever block's mouth.
- **Cat moves too fast or too slow.** Adjust the `change x` value.
  5 is a good starting number; some kids will want 10 (faster) or 3
  (slower). Let them tune.
- **Apple's `if touching` set to the wrong sprite.** Kid set it to
  the apple itself, or to "edge", or to nothing. Fix: open the
  dropdown and pick the cat by name.
- **Apple resets to the same x position every time.** Kid used `go
  to x: 0 y: 180` (no random). Easy fix: drag a `pick random` block
  into the x slot.
- **Apple keeps saying "Yum!" forever once it touches the cat.** The
  apple touched the cat, ran the inside, but `say` doesn't move the
  apple, so it's still touching the cat, so it says Yum again,
  forever. Fix: make sure the `go to` block (reset) comes
  *immediately* after `say` so the apple moves away from the cat.
- **The forever loop is missing entirely.** Symptom: the apple does
  one thing and stops. Fix: wrap the whole behavior in a forever
  loop.

### Differentiation

- **Younger kids (9-10):** May get overwhelmed by the multiple
  scripts in different sprites. Sit with them and walk through "we
  switch to the apple now → these scripts are the apple's → click
  the cat → those scripts are the cat's." The two-sprite mental
  model takes time to land for younger kids.
- **Older kids (12+):** Will probably finish base + stretch quickly.
  Push them to the extension (second falling object). If they want
  more: ask them to make the apple change costume on catch (next
  costume / wait / next costume / etc.), or to play a sound on
  catch.
- **Advanced (any age) with prior programming:** Will recognize this
  as standard game-loop logic. Push them to introduce a "lives"
  concept — the apple's missed condition counts up to 3, and at 3,
  game over. (They'd need a counter, which is a variable, which we
  don't have until next week — so they'd hit a wall. Foreshadow
  variables: "you've discovered exactly what we're learning next
  week.")
- **Struggling:** If a kid can't get the smooth-movement cat working
  in Part A, they won't keep up with Part B. Sit with them through
  Part A. Don't move them to Part B until the cat moves smoothly.
  If absolutely necessary, pair them with an advanced buddy who can
  rebuild it together.

### What to watch for

- The "I built a game" moment in Part B. Watch for it. Kids who get
  the catch-the-apple working will visibly *play* it for a couple
  of minutes before they admit they're done. That's the right
  reaction. Affirm it: "yeah, you built a game."
- Buddy collaboration is huge in Part B. Some kids will help their
  buddy debug the apple's script before finishing their own. That's
  the buddy system working — name it publicly.
- Kids who finish base and don't go for stretch. Some are
  perfectionists who keep tweaking; some are content with "it
  works." Both are fine. Don't push them to stretch unless they
  seem bored.
- The first kid to ask "how do I keep score?" That's the variables
  hook for Session 6. "Great question. Hold onto that — it's
  literally next week's lesson."

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Variables (Session 6).** The "score" question is going to come
  up unprompted. Variables let you remember a number that changes
  over time — perfect for scorekeeping. The catch-the-apple game
  becomes scoreable next week.
- **Game loop pattern.** `forever { check things, do things }` is
  the structure of every game and most interactive apps. We just
  built one. Pygame in Phase 6 uses the same shape, just more
  explicit.
- **`if/else`.** Mentioned as a stretch idea but not formally
  taught. Most kids will encounter it organically; if not, formally
  introduce in Session 7's mini-game.
- **Sensing blocks beyond what we used.** `touching color`,
  `loudness`, `timer`, `mouse x`, etc. are all available but
  deferred. Phase 1 uses just enough sensing to make games
  possible; Phase 6 (Pygame) will revisit the full sensing model.
- **Peanut butter callback opportunity:** the "apple says Yum
  forever once touched" stumble is a classic precision moment. The
  computer did exactly what you said — say Yum, check again, still
  touching, say Yum, check again... You forgot to tell it to move
  away first.

### Materials checklist

- [ ] Demo machine with Scratch open
- [ ] Pre-built catch-the-apple game ready to show as preview
- [ ] Class roster
