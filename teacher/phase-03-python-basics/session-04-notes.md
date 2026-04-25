## Session 4 — Teacher Notes

*Phase 3, Python basics · Session 4 of 16 · Title: Conditionals
— combining decisions*

### Purpose of this session

Conditionals are familiar from Phase 2 Session 6; what's new
this week is *combining* them. Four jobs, in priority order:

1. **Land `and`, `or`, `not` as combinators.** Most programs
   need to evaluate multiple things at once; today gives them
   the syntax for that.
2. **Introduce booleans implicitly.** `True` and `False` as
   first-class values. Comes up naturally in the extension
   ("the result of a comparison can be saved in a variable").
   Don't dwell on the theory; let the practical use land.
3. **Build a substantive program.** The rollercoaster
   eligibility checker is real — multiple inputs, real logic,
   tiered output. By extension, it shows code that "feels like
   a real program."
4. **Practice debugging logic errors.** Compound conditions can
   be wrong in subtle ways. Today's bugs are more interesting
   than syntax bugs — kids will need to think about whether
   their condition actually checks what they think.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: have the rollercoaster checker pre-built so you can
  show the destination if energy flags.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was strings.
  Anyone build a fun palindrome thing?
- **Part A: and / or / not** (~35 min) — `and` ~10 min, `or`
  ~10 min, `not` ~5 min, combining ~5 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: rollercoaster** (~40 min) — base ~10 min, stretch
  (multi-branch) ~15 min, extension (named variables) ~15 min.
- **Wrap-up** (~5 min).

If running short, **the extension can be cut.** The base + stretch
gives kids a working program with branched feedback.

### Teaching Part A

#### The motivation

Open with the real-world examples — rollercoaster (and),
multiple acceptable names (or), umbrella (not). These connect
to kids' lives without being abstract.

> "Real decisions usually involve multiple things. Can I ride
> the rollercoaster? Depends on age AND height. Can I get into
> this club? Depends on age OR membership. Should I take an
> umbrella? Depends on whether it's NOT sunny. Python has three
> words for these."

Then walk through each with an example. The kids will probably
get `and` and `or` immediately (similar to English). `not` is a
little weirder — it's more useful with boolean variables, less
useful with comparisons.

#### `and` — both

The classic example:

```python
if age >= 13 and height >= 50:
    print("You can ride!")
```

Walk through what `and` does: BOTH parts must be true. If either
is false, the whole thing is false.

Have students try it with different `age` and `height` values.
Watch them discover when it passes and fails.

#### `or` — at least one

The multiple-acceptable-names pattern is common:

```python
if name == "Sam" or name == "Alex":
    ...
```

Worth pointing out: this is verbose. A better Python pattern is
`if name in ["Sam", "Alex"]:` — using a list. But lists are
Session 8. For now, `or` repetition is fine.

#### `not` — invert

`not` is most useful with already-boolean things. Walk through:

```python
is_raining = True
if not is_raining:
    print("No umbrella needed!")
```

vs.

```python
if not age >= 18:
    print("Not yet 18.")
```

The first reads naturally. The second is confusing — most
programmers would write `if age < 18:` instead. Worth
mentioning: "use `not` when the alternative is awkward;
otherwise rewrite the comparison."

#### Combining and parentheses

The order-of-operations issue is real:

> "When you mix `and` and `or`, Python checks `and` first by
> default. That can be surprising. Use parentheses to make the
> order obvious."

Show:

```python
True or True and False
```

Without parens, this is `True` (because `True and False` is
`False`, then `True or False` is `True`). With explicit parens
either way, the meaning is clear.

Don't dwell. Just say "use parentheses when mixing and/or."

### Teaching Part B

#### Base — the rollercoaster

Mechanical. Walk through the structure once at the projector,
then have students build their own. Test with the three
combinations (pass / too young / too short).

The `int(input(...))` is by now familiar. The `and` is the new
piece.

#### Stretch — multi-branch

The four-outcome version is a good practice for `if/elif/else`.
Walk through the logic at the projector:

> "Both pass → ride. Old enough but short → tell them about
> height. Tall enough but young → tell them about age. Neither
> → tell them both."

Some kids will accidentally write the conditions in a way that
overlaps. For example, the second `elif` checks `age >= 13 and
height < 48` — the `age >= 13` is redundant because the first
`if` already failed. But it's still correct.

A more elegant version would just check the failure case:

```python
if not old_enough and not tall_enough:
    ...
```

But that requires booleans. Save for the extension.

#### Extension — named variables

This is the most important conceptual content. Introduce booleans
naturally:

> "When you write `age >= 13`, that whole thing has a value —
> either True or False. You can save that value in a variable,
> just like a number or a string."

Demo:

```python
old_enough = age >= 13
print(old_enough)   # True or False
```

The variable `old_enough` now contains a boolean. Variables can
hold booleans just like they can hold numbers and strings.

> "Booleans are the third type — True and False, with capital
> T and F. They're what comparisons return."

The "list all failures" version is a nice extension:

```python
if not old_enough:
    print("- You're too young.")
if not tall_enough:
    print("- You're too short.")
```

Two separate `if`s (not `if/elif`) so both can fire if both
apply. Worth pointing out: "two separate ifs let both run; an
if/elif chain only runs the first true one."

### Common stumbles

- **Operator precedence with `and`/`or` mixed.** Use parens.
- **Using `and` when they meant `or` or vice versa.** Logic
  error, not syntax. Walk through what they want vs. what they
  wrote.
- **`if x == 5 or 10:`** — common typo. The `or 10` is its own
  expression (truthy because non-zero). They probably meant
  `if x == 5 or x == 10:`. Each comparison needs its own full
  comparison.
- **Capital letters for True/False.** Python's booleans are
  `True` and `False` (capital first letter). `true` and `false`
  give NameError.
- **Using `=` instead of `==` in conditions.** SyntaxError.
  Same as Phase 2 Session 6.
- **`not` precedence.** `not age >= 18` is the same as `not
  (age >= 18)`, not `(not age) >= 18`. Most kids won't hit this
  in basic code; mention if needed.
- **Forgetting that `not` flips True to False.** Common mental
  model bug. Walk through truth tables if needed.

### Differentiation

- **Younger kids (9-10):** May struggle with truth tables (the
  abstract "T and F → T or F" stuff). Stick to concrete
  examples (age, height, names). Don't formalize.
- **Older kids (12+):** Will pick up the operators quickly.
  Push them to the named-variables extension. If they finish:
  ask them to add a third condition (e.g., "must not have
  motion sickness") and rework the logic.
- **Advanced (any age):** May know boolean logic from math
  (Boolean algebra, set theory). Encourage them to use the
  `bool()` function and explore truthiness — what counts as
  True/False when not a comparison? (Answer: 0, "", None,
  empty list/dict are False; everything else is True. Python
  rule.) Or have them write the "list all failures" version
  with a function.
- **Struggling:** A kid who can't get `and` or `or` working in
  Part A is probably hitting a syntax error or missing the `:`
  on the `if`. Walk through. The combined-condition concept
  isn't usually the problem; the syntax is.

### What to watch for

- **Logic errors.** Today's bugs are more interesting than
  syntax bugs because they're about *what the program means*,
  not what it can parse. When a kid says "my program runs but
  gives wrong answers," celebrate — that's real debugging.
- **The "ohhh" moment for booleans.** When kids realize
  `old_enough = age >= 13` saves a True/False value, several
  will visibly process this. The "comparisons return values"
  insight is genuinely surprising for many.
- **Buddies arguing about logic.** The rollercoaster eligibility
  rules can spark debate ("what about a 13-year-old who's just
  turned 13?"). Encourage. Logic discussions are exactly the
  thinking we want.
- **Frustration with operator precedence.** When a kid hits a
  surprise from `and`/`or` order, walk through it carefully.
  This is a real Python gotcha; better to learn it now with
  parens than to struggle silently.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 5 (next week, loops + debugger).** Compound
  conditions appear in `while` loops constantly. The debugger
  helps trace what your conditions are evaluating to.
- **Session 7 (number-guessing game).** Combined conditions for
  things like "guess is too high but not way too high."
- **Session 12 (hangman).** "Did the player guess this letter
  AND is it in the word?" — combined conditions everywhere.
- **Session 13 (try/except).** Booleans are involved in error
  handling — `try: ... except: ...` is conditional in spirit.
- **Phase 6 (Pygame).** Game logic is mostly compound
  conditionals: "if the player is at this position AND has
  this many points, win." Today's syntax is the foundation.
- **Phase 8 (Flask).** Web apps make decisions like "if the
  user is logged in AND has admin permissions, show the admin
  page." Same pattern.
- **Peanut butter callback opportunity:** the `if x == 5 or 10`
  bug is a precision moment. The computer did exactly what was
  written; you wrote a sloppy comparison; the computer
  evaluated `or 10` as "10 is truthy" and the if always ran.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built rollercoaster checker
- [ ] Projector (helpful for the truth-table-ish demos)
- [ ] Class roster
