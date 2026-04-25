## Session 6 — Teacher Notes

*Phase 3, Python basics · Session 6 of 16 · Title: Functions
that return values*

### Purpose of this session

Functions in Phase 2 just *did things* (drew on the turtle).
Today they start *giving things back.* This is the conceptual
shift that makes functions genuinely powerful. Five jobs, in
priority order:

1. **Land `return`.** Mechanical at first, but the implication
   is huge. Functions become *expressions* with values, usable
   anywhere a value would work.
2. **Land "function calls are expressions."** The shift from
   "call a function to make something happen" to "call a
   function to get a value" is the new mental model.
3. **Land function composition.** One function's output as
   another's input is the canonical real-world pattern. Today's
   grade calculator demonstrates it.
4. **Light intro to scope.** Variables inside functions are
   local. The "secret variable disappears" demo makes this
   concrete without diving deep into LEGB resolution. Full
   scope is a Phase 4+ topic; today's plant the seed.
5. **Set up Session 7 (number-guessing game).** Today's
   functions-with-returns are exactly what the game needs to
   structure cleanly.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: pre-built grade calculator and rollercoaster
  refactor for "destination preview" if energy flags.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was while loops +
  debugger. Anyone use the debugger on their own code at home?
- **Part A: return** (~40 min) — the two-kinds-of-functions
  intro ~5 min, the `double` example ~10 min, function calls
  as expressions ~10 min, multiple parameters ~5 min, `return`
  ends the function ~5 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: grade calculator** (~35 min) — average function ~5
  min, letter_grade function ~10 min, combining ~10 min,
  scope stretch ~5 min, extension ~5 min.
- **Wrap-up** (~5 min).

If running short, **the rollercoaster refactor extension can
be cut.** The grade calculator is the integration goal.

### Teaching Part A

#### Two kinds of functions

The framing matters. Open with the contrast:

> "Phase 2 you wrote functions that *did* things — drew a
> square, drew a flower. Today you'll write functions that
> *give you back* a value. Like `len("hello")` gives you back
> `5`. That's a function returning a value."

Worth pointing out: they've been *using* return-value functions
for weeks (`int`, `len`, `input` itself). Today they learn how
to *write* them.

#### The `double` example

Walk through at the projector:

```python
def double(x):
    return x * 2

result = double(5)
print(result)
```

Step through what happens:

1. `def double(x):` — define the function.
2. `result = double(5)` — call it with 5.
3. Inside the function: `x` is 5. `x * 2` is 10. `return 10`.
4. Back in main: `result = 10` (because that's what `double(5)`
   gave back).
5. `print(result)` shows 10.

The "return value flows back to the caller" mental model needs
visualization. Some kids will get it instantly; others need
the step-by-step.

#### Function calls as expressions

This is the conceptual shift. Demo:

```python
print(double(5))         # prints 10
print(double(5) + 3)     # prints 13
big = double(double(5))  # 20
```

The first line shows that `double(5)` can be passed directly to
`print`. The second shows it can be added to another number.
The third shows nested calls.

> "A function call with a return value is *just like a
> variable* in terms of how you use it. Anywhere you could
> write a number, you can write a function call that returns
> a number. That's powerful."

Some kids will start playing with this — `double(double(double(2)))`
is `16`. Encourage.

#### Multiple parameters, single return

`add(a, b)` is mechanical. Reinforces parameter syntax from
Phase 2 plus return.

#### `return` ends the function

Critical concept. Worth showing dead code explicitly:

```python
def double(x):
    return x * 2
    print("Never runs!")
```

Run. The print never appears. Show why.

Then the early-return pattern:

```python
def safe_divide(a, b):
    if b == 0:
        return 0
    return a / b
```

The `if b == 0: return 0` exits early. Otherwise the second
`return` runs. Same as `break` in loops conceptually.

This is a common Python idiom — guard against bad input early,
do the real work after.

### Teaching Part B

#### Building the average function

Mechanical. Walk through the parens-around-addition issue:

```python
return (a + b + c) / 3   # correct
return a + b + c / 3     # WRONG — only c is divided
```

Order of operations from math applies in Python. Some kids
will hit this; demo at the projector.

#### Building letter_grade

This is genuinely beautiful — `if/elif/else` with a `return`
in each branch. Walk through how `return` ending the function
means we don't need to be careful about overlapping conditions
(unlike when assigning to a variable in each branch, where
later conditions could overwrite).

#### Combining them

The integration moment. Walk through the data flow:

> "We get three scores from the user. We pass them to
> `average`, which gives us back a number. We pass that number
> to `letter_grade`, which gives us back a letter. We print
> both."

The "one function's output is the next function's input"
pattern is worth naming explicitly:

> "This is one of the most common patterns in real Python.
> Small functions, each doing one thing, chained together."

The `:.1f` formatting specifier is a small new bit. Don't
overdo:

> "The colon-dot-one-f part shows the number with one decimal
> place. There are lots of these formatting tricks; we'll see
> more later. For now just know `:.1f` exists."

#### Stretch — scope demo

The "secret variable disappears" demo is the scope intro.
Type at the projector:

```python
def double(x):
    secret = x * 2
    return secret

print(double(5))
print(secret)      # ERROR
```

Run. The first print works. The second errors:

```
NameError: name 'secret' is not defined
```

> "What happened? `secret` was created inside the function.
> When the function ended, the variable disappeared. It's
> *local* to the function. Code outside can't see it."

This is genuinely surprising for kids — variables in their
mental model "exist forever" up to this point. Land it
gently:

> "This is actually a *good* thing. It means functions can
> have their own variable names without interfering with the
> rest of your code. Two functions can both use a variable
> called `x` and they don't conflict — each one's `x` is
> separate."

Don't dive into the LEGB rule or global vs. local discussion.
Today's intro is enough.

#### Extension — rollercoaster refactor

The functional refactor of the rollercoaster checker is the
"holy grail" demo of return-value functions. Three small
focused functions, composed together, where the main logic
reads like English:

```python
if can_ride(age, height):
    ...
```

vs. last week's:

```python
if age >= 13 and height >= 48:
    ...
```

Same logic, different abstraction level. The function-named
version is what kids will find easier to read in larger
programs.

### Common stumbles

- **Forgot `return`.** The function does its work but gives
  nothing back. Symptom: `result = double(5)` then
  `print(result)` shows `None`. Fix: add `return`.
- **`return` outside a function.** SyntaxError. Easy fix.
- **Code after `return` that should run.** Kid puts important
  code after the `return` thinking it'll execute. Demo: it
  doesn't.
- **`return` vs `print`.** Common confusion. `print` shows
  text on the screen. `return` gives a value back to the
  caller. They're *different*. A function can do both, do
  one, do neither — depends on what's needed.
- **`return` in a loop.** Returns immediately and exits the
  function. Sometimes wanted; sometimes not. If a kid wants
  to "stop the loop" they probably want `break`, not `return`.
- **Calling a function instead of writing it.** `print(double)`
  (without parens) prints the function object, not its result.
  Add parens.
- **Capturing return value but not using it.**
  `result = double(5)` then never using `result`. Walk through:
  why save a value you won't use?

### Differentiation

- **Younger kids (9-10):** May find return-value functions
  abstract. Stick to concrete examples (double, add). The
  grade calculator is great for them — the math is familiar.
- **Older kids (12+):** Will pick up returns quickly. Push
  them to the rollercoaster refactor. If they finish: ask
  them to write a function that returns the *largest* of
  three numbers (uses if/elif). Or have them break the grade
  calculator into more functions.
- **Advanced (any age):** May know returns from prior
  experience. Push them to multiple return values via tuples
  (`return a, b, c` then `x, y, z = func()`). Or write a
  function that calls itself (recursion) — like a factorial
  function.
- **Struggling:** A kid who can't get a basic `double`
  function returning correctly is the kid you focus on.
  Common cause: forgot `return`, used `print` instead, or
  forgot to capture the return value. Walk through the
  mental model: "the function is a machine; you put in 5,
  the machine gives you back 10. `return` is what gives back."

### What to watch for

- **The "wait, I can use a function call anywhere?"
  realization** when kids see `print(double(5) + 3)` work.
  Several kids will visibly process this.
- **The "secret variable disappears" surprise** in the
  scope stretch. The "variables don't leak out" rule is
  often counterintuitive.
- **Buddies trading function ideas.** "Write a function that
  returns ___" is a great brainstorming pattern. Encourage.
- **Kids using the debugger** on their grade calculator. The
  Step Into button (F7) becomes useful for stepping inside
  function calls. Don't push, but if a kid asks what Step
  Into does, today's a good time to show.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 7 (next week, number-guessing game).** Today's
  return-value functions structure the game cleanly:
  `def get_guess(): return int(input(...))`,
  `def check_guess(guess, secret): return ...` etc.
- **Session 8+ (lists, dicts, files).** Many built-in functions
  return values: `len()`, `sum()`, `max()`, `min()`, `sorted()`.
  Kids will see the pattern they learned today everywhere.
- **Phase 4 (intermediate Python).** Modules and classes
  expose functions and methods that return values. Today's
  mental model is the foundation for everything.
- **Phase 6 (Pygame).** Functions that return positions,
  collisions, sprite states — heavy use of return values.
- **Phase 8 (Flask).** Web routes return responses. Same
  conceptual model.
- **Scope** — formal scope discussion happens in Phase 4 when
  modules and `import` need it. Today plants the seed.
- **Peanut butter callback opportunity:** the "forgot return,
  function returns None" bug is a precision moment. The
  computer did exactly what was written; you didn't tell it
  to give anything back, so it gave back nothing.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built grade calculator + rollercoaster
      refactor
- [ ] Projector (helpful for the function composition demo)
- [ ] Class roster
