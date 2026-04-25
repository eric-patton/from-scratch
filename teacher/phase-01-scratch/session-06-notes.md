## Session 6 — Teacher Notes

*Phase 1, Scratch · Session 6 of 9 · Title: Variables — remembering
things*

### Purpose of this session

Variables are the introduction to *state* — the idea that programs
can remember things between moments. Three jobs, in priority order:

1. **Land variables as "labeled boxes that hold a value."** Set,
   change, read. Three operations, three blocks. Every other use of
   variables in the curriculum builds on this.
2. **Close the loop on the catch-the-apple game.** Last week's game
   ended with kids playing it but obviously missing scorekeeping.
   This week's Part B answers the question they asked unprompted at
   the end of Session 5: "how do I keep score?"
3. **Plant the seed for state-driven thinking.** Almost every
   serious program is "what state am I in, and what should I do
   next?" Variables are the first taste of that.

This session is shorter on new concepts than Session 5 was. It's
simpler conceptually — but the *implications* are large. Take time
to make the "computer remembers" idea concrete.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with the Session 5 catch-the-apple game ready to
  open as the starting point for Part B. (Or be ready to rebuild it
  quickly at the projector.)
- Verify the Variables category is functional on at least one
  student machine. Should be fine; Variables is built-in to all
  Scratch versions.

**Prep time:** ~10 minutes. Just open the apple game and have it
ready.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was the apple game.
  Anyone want to show theirs? Did anyone notice it has no score?
- **Part A: variables** (~35 min) — concept ~10 min (the box
  metaphor), build the click counter ~15 min, add the say-the-
  value script ~5 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: score in apple game** (~40 min) — open the project ~5
  min, add score variable + green-flag reset ~10 min, add change-
  on-catch ~10 min, play time + stretch ~15 min.
- **Wrap-up** (~5 min).

If running short, **the Part B stretch (missed penalty) is the
cuttable piece.** Adding the basic score is the session.

### Teaching Part A

The "box with a number in it" metaphor is the central image. **Lean
on it visually:**

- Draw a box on the whiteboard (or the projector). Write `clicks`
  on the side and `0` inside.
- "When I say `change clicks by 1`, the number inside changes."
  Erase the `0`, write `1`.
- "When I say `set clicks to 0`, the number becomes that value."
  Erase the `1`, write `0`.
- "When I say `(clicks)`, I'm asking for whatever's in the box
  right now. The computer reads it and uses it."

This metaphor will carry kids a long way. Don't rush it.

When you build the click counter at the projector:

- Click **Make a Variable**. Name it `clicks`. Show the dialog.
  Default scope ("For all sprites") is fine — don't get into scope
  yet. Just click OK.
- **Point at the variable display in the corner of the stage.**
  Many kids miss it the first time. "See that? That's our box.
  It shows whatever number is in it, all the time."
- Build the two scripts. Run them. Click the cat repeatedly. The
  number goes up.

The "press space and the cat says (clicks)" script is small but
important — it's the introduction to the rounded `(varname)` block,
which is how variables get used inside other expressions. Many kids
will only use `change` and `set` on day one and not realize `(value)`
exists. The "say it out loud" exercise forces them to use it.

### Teaching Part B

The Part B premise — "remember last week's question? here's the
answer" — is the motivation. Sell it.

If kids don't have their Session 5 project saved, **don't rebuild
the whole thing in class.** Have a copy of the Session 5 endpoint
ready to share via USB or email, or have them work from the catch-up
version on the textbook page (which describes the same build).

The new pieces are small:
1. Make a `score` variable.
2. Add `set [score] to 0` to the cat's green-flag script.
3. Add `change [score] by 1` to the apple's `if touching` block.

That's it for the base goal. ~10 minutes once they have the project
open.

The stretch (missed penalty) builds on Session 5's stretch (the y <
-180 check). If kids did that stretch last week, the only addition
is `change [score] by -1`. If they didn't, they need to first add
the missed-condition block (review of Session 5).

The extension (best variable) introduces the `<>` comparison block
from Operators, plus the rounded `(varname)` blocks used inside
the comparison. This is genuinely a stretch — most kids will need
guidance.

### Common stumbles

- **Variable display shows `0` and never changes.** Likely cause:
  the script that should change it is on the wrong sprite, or the
  `set` block runs every time inside the forever loop instead of
  just once at green flag. Walk through what runs when.
- **`set` vs `change` confusion.** A kid uses `set [score] to 1`
  inside the apple's catch block, expecting it to count up. Result:
  score is always exactly 1 after a catch. Fix: use `change`, not
  `set`. Worth taking 30 seconds to make this distinction at the
  projector if more than one kid hits it.
- **Score resets in the middle of play.** Caused by a stray `set
  [score] to 0` block inside a forever loop or inside the apple's
  catch block. Find it, move it.
- **`(score)` rounded block dropped into a Boolean diamond slot.**
  Doesn't fit. Same shape lesson as Session 5: rounded fits in
  rounded slots, diamond fits in diamond slots. The `<>` block in
  Operators (which IS diamond-shaped) is the bridge — it accepts
  two rounded blocks and outputs a yes/no.
- **Two variables with the same name (one for "all sprites," one
  "for this sprite only").** Shouldn't happen with our defaults
  but if a kid clicks around the New Variable dialog, it might.
  Easy fix: delete the duplicate.

### Differentiation

- **Younger kids (9-10):** Variables are abstract enough that some
  9-year-olds will need extra time on the box metaphor. Repeat it
  if needed. The click-counter exercise is concrete enough that
  most will get it from doing.
- **Older kids (12+):** Will grasp variables almost immediately
  (most have seen counters in math). Push them to the extension
  (best variable). If they finish: ask them to add a "level"
  variable that goes up every 10 points. (Modular arithmetic is in
  Operators: `mod`. Don't formally teach; let them discover.)
- **Advanced (any age) with prior programming:** Will recognize
  variables as the standard concept. Push them to think about
  scope: "If two sprites both need to read score but only one
  changes it, what should the variable's scope be?" (We're not
  formally teaching this; it's a thinking question.)
- **Struggling:** If a kid can't get the click counter working in
  Part A, they won't keep up with Part B. Sit with them. Have them
  literally point at the box on the whiteboard while you say what's
  in it changes. Very concrete; very visual.

### What to watch for

- The "ohhhh" moment in Part A when the variable display first
  ticks up. Watch for it. Variables click in a satisfying way once
  the visual feedback registers.
- The kid who immediately starts asking about more advanced things
  ("what if score is more than 100?", "can I have a variable that
  remembers between sessions?"). Encourage the curiosity but
  redirect to today's scope. Cloud variables and persistence are
  Phase 6+ territory.
- Buddies helping each other open last week's project. Some kids
  forgot to save, some have it on a different computer. Buddy
  collaboration to share files (USB stick, etc.) is genuine
  problem-solving.
- **The first kid to ask "can I have more than one variable?"** The
  answer is yes — and the extension uses two — so this is a perfect
  natural transition to the extension.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 7 (next week, "Putting it together").** The score
  variable + game-over mechanic introduced today carries directly
  into the apples-and-rocks integration game.
- **Phase 3 (Python basics).** Variables in Python are the same
  concept, just with `=` syntax instead of `set` blocks. The mental
  model transfers cleanly.
- **State-driven programming everywhere.** Pygame games (Phase 6),
  Flask web apps (Phase 8), customtkinter forms (Phase 5) — all
  use variables as their primary mechanism for tracking state.
  This session is the first encounter with the idea.
- **Scope.** Not formally taught yet. Will come up in Python when
  function-local vs module-level variables matter. For now, "all
  sprites can see this variable" is the only scope model.
- **Peanut butter callback opportunity:** the `set` vs `change`
  confusion is a precision moment. The computer did exactly what
  you said: you said "set to 1," it set it to 1, every time. You
  meant "increase by 1." Be specific.

### Materials checklist

- [ ] Demo machine with Session 5 apple game ready to open
- [ ] Whiteboard or projector for the box metaphor (optional but
      helpful)
- [ ] Class roster
