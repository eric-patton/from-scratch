## Session 2 — Teacher Notes

*Phase 3, Python basics · Session 2 of 16 · Title: Variables
and types*

### Purpose of this session

Types are one of the foundational mental models in programming.
Until now students have used variables without thinking about
"what kind of thing is in this variable" — Phase 1's variables
were always numbers (scores), Phase 2's were mostly numbers
(sizes, angles) or strings (color names). Today the distinction
gets explicit. Four jobs, in priority order:

1. **Land the three types: int, float, string.** Conceptually
   simple but important. Every value has a type. Different types
   behave differently with the same operators.
2. **Land `int(input(...))` as the canonical pattern for
   numeric input.** This is the most common pattern in
   interactive Python. They'll use it constantly.
3. **Land the `"5" + "3" == "53"` insight.** This single
   example explains why type matters more than any abstract
   discussion ever would. The "huh?" moment is the lesson.
4. **Set up f-strings (Session 3) by being deliberately tedious
   today.** All the `+ str(...) +` concatenation in today's
   examples is *intentionally awkward*. Don't apologize for it.
   Next week's f-strings will feel like a real upgrade.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: have the age calculator pre-built so you can show
  the destination if energy flags.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was print/input.
  Anyone build a fun multi-question program at home?
- **Part A: types** (~40 min) — three types intro ~10 min, the
  `type()` function ~5 min, the `"5" + "3"` reveal ~10 min,
  conversion functions ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: program with math** (~35 min) — age calculator base
  ~15 min, decimal stretch or extension project ~15 min,
  wrap-up ~5 min.
- **Wrap-up** (~5 min).

If running short, **the extension projects can be cut.** The age
calculator is the goal.

### Teaching Part A

#### The three types intro

Walk through the table at the projector. Don't dwell on each one
— just show them and move on. The key insight isn't memorizing
which is which; it's that they EXIST and they're DIFFERENT.

Worth pointing out:
- `5` (no decimal) is `int`.
- `5.0` (decimal point, even with `.0`) is `float`.
- `"5"` (quotes) is `str`.

The same-looking values being different types is the surprise.
Lean on it.

#### `type()` reveal

`type(x)` is just a function that tells you the type. Mechanical.
Have students run the four `type()` calls. Look at the shell
output together. Confirm each one matches what they expected.

Don't get into "why does it say `class 'int'` instead of just
'int'?" That's an OOP detail. Acknowledge briefly: "the `class`
part is technical; for now just notice the `'int'` or `'str'`
part."

#### The `"5" + "3"` reveal

This is the most important moment of the session. Set it up
explicitly:

> "Watch this. I'm going to do two things that look almost the
> same but give totally different answers."

Type at the projector:

```python
print(5 + 3)
print("5" + "3")
```

Run. Show the output:

```
8
53
```

Pause. Let it land.

> "Same numbers. Same plus sign. Different answers. Why?"

Wait for kids to figure it out. Most will get there: "The
quotes make them strings, and `+` does something different with
strings."

Confirm and reframe:

> "Right. With numbers, `+` does math. With strings, `+` sticks
> them together. Python's `+` operator is *type-sensitive* — it
> does different things depending on what's on either side."

This is one of the most common conceptual hurdles in Python. By
making it concrete and visible, you save kids a lot of future
confusion.

#### Type conversion

The conversion functions (`int()`, `float()`, `str()`) are
mechanical. Walk through:

- `int("5")` returns `5` (an int)
- `float("3.14")` returns `3.14` (a float)
- `str(5)` returns `"5"` (a string)

Then the canonical pattern:

```python
age = int(input("How old are you? "))
```

Walk through what's happening:
1. `input("How old are you? ")` prints the prompt and waits.
2. User types `12` and presses Enter.
3. `input` returns the *string* `"12"`.
4. `int("12")` converts the string to the integer `12`.
5. `age = 12` — the variable is now an int.

This is a "function inside a function" pattern. Some kids will
find it confusing at first. The mental model: read inside-out.
First Python runs `input(...)` and gets a string. Then `int(...)`
converts it. Then assignment.

If a kid is confused, walk through it slower with two steps:

```python
raw = input("How old are you? ")    # raw is a string
age = int(raw)                       # age is an int
```

That's the same thing in two lines. Most kids transition to the
one-line version once they've seen the two-line.

### Teaching Part B

#### The age calculator

Mechanical. Walk through the structure once at the projector,
then have students build their own.

Note the structure:
1. Print a banner so the user knows what's happening.
2. Two `int(input(...))` calls to get the numbers.
3. Math on the variables.
4. Print the result with `str()` conversions for any numbers in
   the output.

The `str()` calls in the output line are tedious. **Don't
apologize for them.** Mention briefly: "yes this is awkward;
there's a better way next week."

#### Stretch — decimals

The float version uses `float(input(...))` instead of `int(...)`.
Same pattern, different conversion function. Math with floats
gives float answers.

The parentheses in `(a + b + c) / 3` are an order-of-operations
moment. If you don't include them, Python computes `c / 3`
first and then adds, which gives wrong answers. Some kids will
discover this; it's worth pointing out when they do.

#### Extension projects

Students pick something they'd want to compute. Encourage
personal relevance — savings, time conversion, distance
conversion, anything they care about.

Walk the room and help with:
- Math errors (operator precedence, especially with division)
- Type errors (forgot to convert input or forgot to str() output)
- Logic errors (their formula doesn't compute what they think)

If a kid wants to do something genuinely complex (e.g., a tax
calculator with multiple brackets), suggest scoping down to the
simplest version first.

### Common stumbles

- **Forgot to convert input.** Symptom: `TypeError: can only
  concatenate str (not "int") to str` or similar. Fix:
  `int(input(...))`.
- **Wrong conversion type.** `int("3.14")` errors because
  `"3.14"` isn't a valid int. Use `float()` for numbers with
  decimals.
- **Forgot to str() the output.** Symptom: same TypeError but
  in the print statement. Fix: wrap numeric variables in
  `str()` when concatenating into a print string.
- **Order of operations.** `a + b / 3` computes `b/3` first.
  Use `(a + b) / 3` for the average of two.
- **`int()` of a non-numeric string.** `int("hello")` errors.
  Mention to kids — input validation is a Phase 13 (try/except)
  topic; for now, kids should just type numbers when prompted.
- **Empty input.** If a kid presses Enter without typing,
  `input()` returns an empty string `""`, and `int("")` errors.
  Easy fix at the user's end (type something); a programming
  fix would need try/except.

### Differentiation

- **Younger kids (9-10):** May find the type abstraction tricky.
  Lean on the `"5" + "3" == "53"` example heavily — it's
  concrete and surprising. Once they get *that*, the abstract
  concept clicks.
- **Older kids (12+):** Will absorb types quickly. Push them on
  the extension projects with more interesting math (e.g., a
  pythagorean theorem calculator, or a "how long until my
  birthday" using the `datetime` module — but datetime is
  beyond what we've taught, so let them discover).
- **Advanced (any age):** May know types from prior experience.
  Push them to write a function that takes a number and returns
  something computed (foreshadows return values in Session 6).
  Or have them write input validation: "ask the user, and if
  they didn't type a number, ask again." That requires `while`
  loops (Session 5) and try/except (Session 13), so they may
  hit walls — that's fine; foreshadow.
- **Struggling:** A kid who can't get the basic age calculator
  working is probably hitting a type confusion. Sit with them.
  Use `print(type(age))` to *show* what type each variable is.
  Visualizing the type makes the concept concrete.

### What to watch for

- **The "ohhh" moment for `"5" + "3"`.** Watch for it. Several
  kids will get it visibly.
- **Frustration at the verbose `+ str(...) +` syntax.** Some
  kids will be annoyed. Reframe as motivation: "yes, this is
  awkward. There's a much better way next week. Today we use
  the awkward way so you appreciate the upgrade."
- **Buddies trading calculator project ideas.** Encourage. The
  variety of "what would you compute?" answers reveals what kids
  care about.
- **Kids who try to skip the conversion.** They'll hit TypeError.
  Don't let them just give up — walk them through reading the
  error and finding the fix. This is debugging practice.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 3 (next week, strings).** F-strings replace the
  awkward `+ str(...) +` mess. Today's tediousness is the
  setup for that upgrade.
- **Session 4 (deeper conditionals).** Comparing numbers
  (`age > 18`) requires int/float types. Comparing strings
  (`name == "Sam"`) requires string types. Type-aware
  comparisons matter.
- **Session 7 (number-guessing game).** Heavy use of
  `int(input(...))` for the user's guess.
- **Session 13 (error handling).** What to do when the user
  types something that *can't* be converted. Today's "just type
  a number when prompted" workaround becomes a real
  problem when users don't follow instructions; try/except is
  the answer.
- **Phase 4 (CLI tools).** Same `input`/`print`/conversion
  pattern, scaled up to bigger programs.
- **Peanut butter callback opportunity:** type errors are
  precision moments. The computer did exactly what was written;
  you tried to add a string and a number, and it can't.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built age calculator
- [ ] Projector (helpful for the `"5" + "3"` reveal)
- [ ] Class roster
