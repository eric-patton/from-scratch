## Session 5 — Teacher Notes

*Phase 3, Python basics · Session 5 of 16 · Title: Loops
(deeper) and the Thonny debugger*

### Purpose of this session

Two distinct topics; both significant. The session is busier
than usual but each half is independently complete. Five jobs,
in priority order:

1. **Land the `while` loop.** Conceptually different from
   `for` — runs based on a condition, not a fixed count. Worth
   teaching distinctly so kids know when to use which.
2. **Land the infinite-loop danger.** Every `while` loop must
   eventually make its condition false. The infinite loop demo
   is intentional — they need to experience hitting Stop.
3. **Land the Thonny debugger.** Per CURRICULUM-DECISIONS.md,
   the debugger lands "around session 5." This is the planned
   moment. The debugger is the single most-useful tool for
   debugging that exists; today is when it stops being mystery
   buttons in the toolbar.
4. **Practice "watching execution."** The debugger trains a
   skill: thinking about what the program is *doing* moment by
   moment, not just what the source code says. Kids who learn
   this think about programs differently from kids who don't.
5. **Set up `break` for later use.** Today's intro of `break`
   in `while True:` pattern foreshadows game loops in Phase 6
   (Pygame).

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open. The debugger UI varies slightly
  by Thonny version — verify the bug icon is in the toolbar
  before class. (In some versions it's labeled "Debug current
  script" with a small bug icon; in newer versions it might
  look different.)
- Pre-built `vowel_bug.py` ready to step through at the
  projector.
- Verify F6 (Step Over) works on the demo machine.

**Prep time:** ~20 minutes. Especially: practice the debugger
walkthrough yourself once before class. The first run-through
is awkward; you want to be fluid.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was deeper
  conditionals.
- **Part A: while loops** (~35 min) — `while` intro ~10 min,
  the count-up example ~5 min, guess-the-number version ~10
  min, infinite loop demo ~5 min, `break` ~5 min, checkpoint.
- **Break** (~5 min).
- **Part B: the debugger** (~40 min) — type the buggy program
  ~5 min, run normally to see wrong output ~3 min, debugger
  walkthrough ~20 min, fix the bug ~2 min, practice stepping
  through an earlier program ~10 min.
- **Wrap-up** (~5 min).

If running short, **the practice-on-earlier-program piece is
cuttable.** The debugger walkthrough on `vowel_bug.py` is the
session.

### Teaching Part A

#### `while` intro

The contrast with `for` is the right framing:

> "A `for` loop is great when you know how many times. A `while`
> loop is great when you don't know — when you want to keep
> going *until* something happens."

Demo the count-up example at the projector:

```python
count = 1
while count <= 5:
    print(f"Count is {count}")
    count = count + 1
```

Walk through it line by line. The check-before-each-iteration
pattern is the new mental model:

> "Before every iteration, Python asks: is the condition still
> true? Yes? Run the body. No? Stop."

#### Guess-the-number example

This is more interesting because the loop count isn't known:

```python
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess: "))
    ...
```

The loop runs as many times as it takes. Some kids will guess
right immediately; others will take many tries.

Worth pointing out: the `guess = 0` initialization is needed
because `guess != secret` has to evaluate to True at the start.
You can't use `guess` before it's defined.

#### Infinite loop demo

Critical pedagogical moment. Have students intentionally write
a broken loop:

```python
count = 1
while count <= 5:
    print(count)
    # OOPS — no update!
```

Run it. The shell prints `1` rapidly forever. Some kids will
panic.

> "Don't worry — this is just text scrolling. Hit the red Stop
> button in Thonny."

Every kid should experience this once. It's normal. The point:

> "Every `while` loop needs to do something inside that
> eventually makes the condition false. Otherwise you've made
> an infinite loop. They're easy to make by accident."

After they recover, fix the loop and run it correctly.

#### `break`

The `while True: ... break` pattern is the deliberate-infinite-
loop-with-explicit-exit. Common in real Python:

```python
while True:
    answer = input("Quit? ")
    if answer == "quit":
        break
```

Worth showing once. Don't drill — `break` will come up
naturally in projects later.

### Teaching Part B

This is the meat of the session. Plan to spend most of the
time here.

#### The buggy program

Type the vowel counter at the projector. **Make the bug
deliberately.** When you run it, point at the wrong output:

> "Hello has two vowels — e and o. But the program says 1.
> Why? Could you stare at the code and figure it out?"

Some kids will spot the bug just from reading. That's fine —
say so:

> "Yes, you're right. But sometimes you can't see it from
> reading. Let me show you a way to *watch* the program run
> and see the bug happen."

#### Starting the debugger

Demo at the projector:

- Find the bug icon in the toolbar. (Show it explicitly — it's
  small and easy to miss.)
- Click it.
- The program pauses at the first line. **Highlight the visual
  difference** — the line is highlighted, there's a variables
  panel.

Walk through finding the variables panel. Some kids' Thonny
will have it visible by default; others may need to enable it
(View menu → Variables, or similar).

#### Stepping through

This is where you slow down and let it land.

Click Step Over (F6) once.

> "What's in the variables panel now? `word` is `"hello"`.
> That's because `word = "hello"` just ran."

Step again. `vowel_count` is `0`.

Step into the for loop. **Make a big deal of `letter`:**

> "Look at this — `letter` is `'h'`. The loop is starting; it
> picked the first character. Watch what happens as we step."

Step into the if. The if condition evaluates to False (h not in
aeiou). Skip the body.

Step. Loop continues. `letter` is now `'e'`.

Step. The if condition is True. Run the body.

Step. **`vowel_count` becomes 1.** Big moment.

Step through the rest of the loop. Each vowel resets
vowel_count to 1.

> "There's the bug. Every vowel sets vowel_count to 1. It
> never adds. It just overwrites."

Then fix it: `vowel_count = vowel_count + 1`. Run normally.
Correct output.

> "That's the debugger. You can use it on any Python program
> to watch what's happening. It's the most useful tool you'll
> learn this whole phase."

#### Practice on an earlier program

Have students open one of their earlier programs (rollercoaster,
name analyzer, age calculator). Run with the debugger. Step
through. Watch variables.

The point isn't to find a bug — it's to *practice* using the
debugger so it's not scary later. Walk the room and help kids
who are confused about the buttons.

If a kid asks "what's Step Into vs Step Over?":

> "Step Over runs the next line. Step Into goes *inside*
> a function call, so you can debug what's happening inside.
> For today, Step Over is enough."

### Common stumbles

- **Forgot to update the loop variable.** Infinite loop. Hit
  Stop, read the code, find the missing update.
- **Off-by-one in the while condition.** `while count <= 5`
  vs `while count < 5` — different number of iterations.
  Kids will discover this.
- **`while True:` without `break`.** Infinite loop with no
  exit. Same fix as above.
- **`break` at the wrong indent level.** `break` only exits
  the loop it's directly inside. If a kid puts `break` inside
  a nested loop, it only exits the inner one.
- **Debugger UI confusion.** The first time using the debugger
  is genuinely confusing. Be patient. Walk individual kids
  through the step-over button.
- **The variables panel not showing up.** Some Thonny
  configurations hide it by default. Look in View menu.
- **Pressing F5 (Run) instead of the bug icon.** Runs normally,
  not in debug mode. Easy to redo.
- **Debugger seems "stuck" mid-line.** Some lines have
  sub-steps (function calls, evaluations). Step Over moves
  through them all.

### Differentiation

- **Younger kids (9-10):** May find the debugger overwhelming.
  Focus on Step Over only. Don't introduce Step Into or
  breakpoints unless they ask.
- **Older kids (12+):** Will pick up `while` and the debugger
  fast. Push them to use the debugger on a more complex earlier
  program (their Phase 2 garden, for instance). Real practice.
- **Advanced (any age):** Suggest `continue` (skip to next
  iteration) and breakpoints (click in the margin). Or have
  them write a guess-the-number game with limited tries (a
  while loop with a counter and a `break` after N attempts).
- **Struggling:** A kid who can't get a basic `while` loop
  working in Part A is the kid you focus on. Most common
  cause: forgot to initialize the variable, or forgot to
  update it. The infinite-loop demo helps internalize the
  "must update" rule.

### What to watch for

- **The "ohhh I can SEE the bug" reaction during the debugger
  walkthrough.** Some kids will visibly process this. Affirm.
  This is the moment debugging stops being magic.
- **Frustration with the debugger UI.** First-time use is
  always awkward. Reassure that it gets easier.
- **Kids who skip the practice on their own programs.** Push
  them — the muscle memory is what makes the debugger useful
  later.
- **The first kid to use the debugger to find a bug in their
  own code.** Note them. They've internalized the most
  important debugging skill in programming.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **Debugger walkthrough effectiveness** — did the vowel_bug
  demo land?

### Connections forward

- **Session 6 (next week, return values).** When you're
  debugging functions that return values, Step Into becomes
  much more useful. Foreshadow.
- **Session 7 (number-guessing game).** The exact pattern from
  today's `while guess != secret` example. They've already
  seen the structure.
- **Session 12 (hangman).** The main game loop is `while not
  game_over:`. Today's `while` patterns scale up directly.
- **Phase 6 (Pygame).** Game loops are infinite `while True:`
  loops with `break` for game over. Same pattern.
- **Reading Error Messages appendix** — currently a stub. The
  debugger complements error message reading: errors tell you
  WHERE; the debugger shows you HOW you got there. The
  appendix is worth filling in soon.
- **Peanut butter callback opportunity:** infinite loops are
  pure peanut butter. The computer did exactly what was
  written; you wrote a loop with no way out; the computer
  loops forever. Be specific.

### Materials checklist

- [ ] Demo machine with Thonny, debugger UI verified
- [ ] Pre-built `vowel_bug.py` ready to step through
- [ ] Projector (essential — the debugger is hard to demo
      without)
- [ ] Class roster
