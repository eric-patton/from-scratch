## Session 6 — Teacher Notes

*Phase 2, Python with Turtle · Session 6 of 8 · Title: Conditionals
— `if` in Python*

### Purpose of this session

Conditionals are the last new syntax of Phase 2. The concept is
familiar from Phase 1 Session 5; what's new is the Python syntax
(no diamond shapes; just keywords and operators) and a few
notable gotchas. Five jobs, in priority order:

1. **Land Python's `if/else/elif` syntax.** Mostly mechanical;
   builds on indentation rules they already know.
2. **Land `==` vs `=`.** This is the most common Python typo for
   beginners. `=` assigns; `==` compares. Drive it home today
   so it doesn't haunt them.
3. **Introduce comparison operators.** `> < >= <= == !=`. Six
   operators; mostly familiar from math; quick walkthrough.
4. **Combine everything into one program.** The Part B extension
   (row of growing squares, colored by size) uses every Phase 2
   concept in one program. This is the "you can do this" moment
   — they're a few weeks from being able to design their own
   substantial program.
5. **Set up Session 7 (integration project).** Today's
   integration in the extension is a preview of what Session 7
   does at scale.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open. Have the row-of-growing-squares
  pre-built so you can show the destination if energy flags.
- Test your demo on a student machine if you've changed any
  speeds/colors — make sure the visual is satisfying at the size
  you've chosen.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was variables.
  Anyone build anything cool with the tower function?
- **Part A: making decisions** (~40 min) — `if` ~10 min, `else`
  ~5 min, comparison operators ~10 min, `elif` ~10 min,
  checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: decisions in drawings** (~35 min) — `draw_colored_
  square` base ~10 min, `elif` stretch ~10 min, integration
  extension ~15 min.
- **Wrap-up** (~5 min).

If running short, **the integration extension can be cut** but
it's the most pedagogically valuable part of Part B. Try not to
cut it; cut the elif stretch first if needed.

### Teaching Part A

#### The reframing for `if`

Connect to Scratch immediately:

> "Remember the orange `if` block from Phase 1? Same idea, new
> shape. In Scratch you snapped a sensing block into a diamond
> slot. In Python you write the question after the word `if`
> and put a colon at the end."

Walk through `if size > 50:` at the projector. Same parts
they've seen for `for` and `def`: keyword, condition, colon,
indented body.

Run with `size = 70` (true) and then `size = 30` (false). The
visible difference (printed vs not) is the lesson.

#### `==` vs `=` — the critical distinction

This is the most important moment of Part A. Mark it explicitly:

> "Watch this. `=` (one equals) is *assignment* — you saw it
> last week, `size = 50`. `==` (two equals) is *comparison* — it
> asks if two things are equal. They look almost the same and
> they mean different things. Mixing them up is the most common
> Python mistake in the world."

Demo at the projector:

```python
x = 10        # assigns 10 to x
if x == 10:   # checks if x is equal to 10
    print("yes!")
```

Then deliberately make the typo:

```python
if x = 10:    # SYNTAX ERROR
    print("nope")
```

Run, see the error. Fix it. Run again.

Some kids will do this typo accidentally in Part B. That's fine —
they need to fail at it once to learn. Be ready to point at the
error message and say "remember, == not =."

#### Comparison operators

The table is mechanical. Walk through each operator with one
example. Don't dwell.

The `!=` operator (not equal) often surprises kids. The `!`
character isn't intuitive. Mention: in many programming
languages, `!` means "not." So `!= 5` is "not equal to 5."

If a kid asks why not just write `=/=` or `≠`: real answer is
"keyboards have `!` and `=` but not `≠`, and consistency wins."

#### `elif`

`elif` is the straightforward addition. Walk through how Python
checks each condition in order, stopping at the first true one.

The "first true one wins" behavior is non-obvious. Worth a
sentence:

> "Python checks the conditions top to bottom. As soon as one is
> true, its body runs and the rest are skipped. Even if a later
> condition would also have been true."

Show the size-categories example. With `size = 75`, the `elif
size > 50` runs (since `>50` is true) — but `size > 100` is
checked first and is false, and the `else` is never reached.

Some kids will worry about this — "what if I want to do BOTH
things?" — and the answer is "use two separate `if` blocks
instead of `if/elif`."

### Teaching Part B

#### Base — `draw_colored_square`

Mechanical. Walk through the function definition at the projector
once, then have students build it themselves.

Key teaching beat: **the conditional is INSIDE the function.**
Each call to `draw_colored_square` runs the conditional fresh,
checking the size that was passed in. So one call sees `size =
40` and goes blue; the next sees `size = 80` and goes red.

The function "remembers" how to make the decision; the size
varies per call.

#### Stretch — `elif` version

Adding `elif` is mechanical. The interesting part is the
*thresholds*. Some kids will tweak the cutoffs (40, 80) to get
different transition points. Encourage. This is how real
programmers tune: "what feels right? Try it, run it, adjust."

#### Extension — full integration

The 12-square row uses every Phase 2 concept:

| Concept | Where it appears |
|---|---|
| Sequences | The whole program runs top-to-bottom |
| Loops | `for i in range(12):` and inner `for i in range(4):` |
| Functions | `def draw_colored_square(size):` |
| Parameters | `size` parameter passed to the function |
| Variables | `size = 10`; `size = size + 8` |
| Arithmetic | `size + 15`, `size + 8` |
| Conditionals | `if/elif/else` inside the function |

**Walk this through at the projector after they've built it.**
Point at each concept and name it: "see, here's a function call,
here's the variable changing, here's the conditional inside the
function, here's the loop driving everything." Make the
integration visible.

> "Six weeks ago you'd never typed Python. Today you wrote a
> program that uses every idea programmers use to build real
> software. The hard part isn't done — there's a lot still to
> learn — but the *foundation* is in place."

### Common stumbles

- **`=` instead of `==` in `if`.** SyntaxError: "invalid syntax."
  Easy fix: add a second `=`. Common; don't make a big deal.
- **Forgetting the colon after `if/elif/else`.** SyntaxError.
  Same as `for` and `def`. The fix is always the same.
- **Wrong indentation under `if/else`.** Confused mix of "what's
  inside the if" vs "what runs after." Fix: re-indent carefully,
  or rewrite from scratch with proper indentation.
- **`if` body is empty (just a comment).** Python wants
  *something* to run. If the body is empty, write `pass` (a
  do-nothing statement). Most kids won't hit this; mention if
  they do.
- **`elif` written as `else if`.** Other languages use `else if`;
  Python uses `elif`. Easy correction.
- **`==` working but condition still doesn't seem right.** Often
  a logic bug, not a syntax bug. Walk through what the kid
  *thinks* the condition checks vs. what it actually checks.
- **Comparing different types.** `if "5" == 5:` is False — a
  string is not the same as a number. Most kids won't hit this
  in turtle code, but worth knowing it exists.

### Differentiation

- **Younger kids (9-10):** May get confused by `==` vs `=`. Be
  patient; this is genuinely confusing. The fix on each error
  becomes routine after a few attempts.
- **Older kids (12+):** Will pick up the syntax fast. Push them
  to the integration extension hard. If they finish: ask them
  to add a *fourth* color tier or to combine `and`/`or` for
  multi-condition checks.
- **Advanced (any age):** May know boolean logic from math. Push
  them to write conditions with `and`/`or`/`not`. Or have them
  build a function that takes multiple parameters and uses
  conditionals based on combinations. Or: a function that
  "validates" its input — `if sides < 3: print("invalid")`
  before drawing.
- **Struggling:** A kid who can't get the basic `if/else`
  working in Part A is probably hitting the `==`/`=` confusion
  or indentation. Sit with them. Walk through line by line.

### What to watch for

- **The "ohhhh" moment for `==`.** First time someone hits the
  `=` typo, gets the error, fixes to `==`, and the program
  runs. Several kids will visibly process this.
- **Frustration at indentation errors.** Kids who get sloppy
  with indentation will hit IndentationError. Frame as "Python
  is being helpful — pointing at exactly where things are
  off."
- **Kids comparing their conditional outputs.** "Mine printed
  'Big!' but yours printed 'Small!' — what's different?"
  Encourage. This is debugging thinking.
- **Kids who finish the extension (full integration) and
  realize what they just did.** That's the
  "I can build real things now" moment. Don't undersell it.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 7 (next week, integration project).** Today's
  extension is a preview. Next week is the full creative
  project. Today's "you have all the tools now" framing is the
  setup.
- **Session 8 (milestone).** Same shape as Phase 1 — students
  plan a project, build it, demo it. Today's integration
  exercise gives them confidence they can build something real.
- **Pygame (Phase 6).** Conditionals are the heart of game
  logic — "if the player touches the goal, they win"; "if the
  enemy is close, attack." Today's syntax is the same as
  Pygame's; the contexts will get more interesting.
- **Flask (Phase 8).** Web apps are conditional all the way
  down — "if the user is logged in, show this page; otherwise,
  show the login form." Today's `if/elif/else` is the
  foundation.
- **The peanut butter callback opportunity:** the `=` vs `==`
  confusion is a perfect precision moment. The computer did
  exactly what was written; you wrote `=` (assignment) when you
  meant `==` (comparison). Be specific.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Pre-built row-of-growing-squares as a destination preview
- [ ] Projector (helpful for the `==`/`=` distinction demo)
- [ ] Class roster
