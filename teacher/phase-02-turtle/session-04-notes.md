## Session 4 — Teacher Notes

*Phase 2, Python with Turtle · Session 4 of 8 · Title: Functions
— making your own commands*

### Purpose of this session

This is the most conceptually important session in Phase 2.
Functions are the only fundamentally new programming idea in this
phase (everything else is Python syntax for ideas they already
know from Scratch). Five jobs, in priority order:

1. **Land the function concept.** Naming a chunk of code so you
   can call it later by name. This is one of the most universal
   ideas in all programming — it shows up in every language ever
   designed.
2. **Land parameters.** Functions that take input and act on it
   are vastly more useful than fixed functions. Today is the
   first encounter with the idea that information flows *into*
   a function via parameters.
3. **Reinforce indentation.** Function bodies use the same
   indentation rule as loops. Reinforces last week's lesson in a
   different context.
4. **Foreshadow scope, lightly.** Today's functions use `t` from
   the enclosing scope (the `t = turtle.Turtle()` defined
   outside the function). This is "global access" and works
   without explanation. We're not formally teaching scope yet,
   but the pattern they're using today is the pattern they'll
   formalize later.
5. **Demonstrate functions-calling-functions.** The extension
   (small helper functions used by `draw_house`) is the most
   important part of this session for kids ready for it. It's
   how real programs are structured.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open. Have the "draw three squares the
  long way" version pre-built so you can show the contrast.
- Optional: have a finished "neighborhood with three colored
  houses" program ready to show as the destination if energy
  flags.

**Prep time:** ~15 minutes. Build the demos.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was loops. Anyone
  draw something cool with the colored spiral?
- **Part A: defining functions** (~45 min) — the motivation
  (three squares the long way) ~5 min, the function reveal ~15
  min, parameters ~15 min, parameterized squares ~5 min,
  checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: neighborhood** (~30 min) — `draw_house` together ~10
  min, row of houses (base) ~10 min, stretch + extension ~10
  min.
- **Wrap-up** (~5 min).

If running short, **the extension (functions-calling-functions)
is the cuttable piece** — but it's also the most important part
for advanced kids. Try not to cut it; cut Part A's parameters
discussion if absolutely needed (kids can still do Part B with
fixed-size houses).

### Teaching Part A

#### The motivation

Open with the long version on the projector. Three squares,
typed-out loop three times. Look bored.

> "Look at this. We learned loops last week to *avoid* copying
> things, and now I'm copying the same loop three times. There
> has to be a better way. There is."

This is the setup. Don't explain functions yet — let the
motivation breathe for 30 seconds.

#### The function reveal

Now type the function version at the projector. Walk through
each part of the syntax slowly:

- `def` — "this defines a function"
- `draw_square` — "this is the name we're giving it"
- `()` — "the parentheses are required, just like a method call"
- `:` — "colon, just like for-loops"
- Indented body — "everything indented under here is the
  function's body, just like a loop"

Then the call: `draw_square()`. Note that **defining doesn't run
it.** The function only runs when called. This is genuinely
non-obvious — most kids will need to see it explicitly.

> "I just *defined* the function. The turtle hasn't drawn
> anything. Now I have to *call* it — like saying its name out
> loud."

Run. Square draws.

Now show the multi-call version:

```python
draw_square()
t.penup(); t.goto(-100, 0); t.pendown()
draw_square()
t.penup(); t.goto(100, 0); t.pendown()
draw_square()
```

(In the actual code use separate lines, not semicolons. The
shorthand is just for compactness here.)

Three squares, three calls. Same function. The "wait, I just
write it once?" reaction is the lesson landing.

#### Parameters

The parameter concept is the second half of Part A. The shift:

```python
# fixed
def draw_square():
    for i in range(4):
        t.forward(60)
        t.right(90)

# parameterized
def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)
```

Two changes:
- `def draw_square(size):` — parameter goes in the parentheses
- `t.forward(size)` — use the parameter inside

Walk through the call:

```python
draw_square(40)
draw_square(80)
```

> "When you call `draw_square(40)`, Python takes the 40 and uses
> it everywhere `size` appears in the function. Each call is
> independent — the 40 doesn't stick around for next time."

Some kids will get this immediately; some won't. Don't drill it
— Part B will reinforce.

#### A note on `t`

Inside the function, `t.forward(size)` uses `t` even though `t`
isn't a parameter. That's because `t` is defined *outside* the
function (in the global scope) and Python lets functions read
outer variables.

**Don't formally teach scope.** Just say: "the `t` we made up
top is available inside the function too. Functions can use
things you defined outside them."

If a curious kid asks "wait, why didn't we have to pass `t`?":

> "Great question. Python lets functions reach outside themselves
> and use things you defined elsewhere. Most of the time we
> avoid relying on this — we'd rather pass everything in as a
> parameter. But for the turtle, we'll keep using `t` from
> outside because it makes the code shorter. We'll learn the
> formal version later."

That's the honest answer. Move on.

### Teaching Part B

#### Building the house

Walk through the `draw_house` function at the projector. The
spatial logic (move-to-roof-position, draw-triangle, return-to-
base) is genuinely tricky. Be ready for kids to get the
positioning wrong.

The two for-loops inside one function (square + triangle) are
worth pointing out. Functions aren't limited to simple
operations; they can contain whole programs of their own.

#### The row of houses

Mostly mechanical once `draw_house` works. Three calls with
different positions. Walk the room; help kids whose houses end
up in weird positions (usually a `goto` or `setheading` issue).

#### Stretch — color parameter

Adding a second parameter is the moment kids see "functions can
take multiple inputs." Walk through the syntax:

- `def draw_house(size, color):` — comma between parameters
- `draw_house(50, "red")` — comma between arguments
- Order matters — `size` is first, `color` is second, in both
  the definition and the call

#### Extension — functions calling functions

This is the most important extension in Phase 2. **Push every kid
who finishes the stretch to attempt this.**

Walk through the structure at the projector:

```
draw_square()    — small, draws a square
draw_triangle()  — small, draws a triangle
draw_house()     — calls both
```

Kids will want to know: "is `draw_house` calling `draw_square`
weird?" No. **Functions can call any other function**, including
ones you wrote yourself. This is how all real programs work.

The mental model: functions are like vocabulary words. Once
you've defined a word, you can use it in defining another word.

### Common stumbles

- **Forgot the colon after `def name(...)`.** Same as for-loops:
  SyntaxError. Most-forgotten character.
- **Indentation of function body.** Same as for-loops. Thonny
  auto-indents but watch for kids who manually undo it.
- **Defining the function but never calling it.** Symptom: the
  program runs but draws nothing. The function is defined but
  no `draw_square()` call exists. Walk them through:
  `def draw_square():` makes the function, `draw_square()` runs
  it.
- **Calling without parentheses.** Some kids type
  `draw_square` (no parens) thinking that runs it. It doesn't —
  it just *names* the function without calling it. Add the `()`.
- **Calling with parens but no argument when one is required.**
  `draw_square()` after `def draw_square(size):` gives a
  "missing 1 required positional argument" error. Fix: pass a
  size: `draw_square(60)`.
- **Parameter name vs argument value confusion.** Some kids will
  pass the parameter NAME instead of a value:
  `draw_square(size)` (using `size` as the argument). Without a
  variable named `size` at the call site, this is a NameError.
  Walk through what's happening.
- **Function defined inside another function (or inside a loop).**
  Rare but possible. Functions should be at the top level
  (un-indented). If a kid accidentally indents the `def`, the
  function won't be available outside.
- **`t.left(90)` vs `t.right(90)` confusion in the house body.**
  The house's body uses `left` to draw a square going
  counter-clockwise (so the turtle ends pointing the right way
  for the roof). Some kids will use `right` and end up rotated
  the wrong direction. Spatial reasoning issue; help debug
  visually.

### Differentiation

- **Younger kids (9-10):** May get the basic idea but struggle
  with multi-parameter functions. Prioritize the base goal (one
  parameter, multiple calls) before pushing them to the
  color-parameter stretch. Functions-calling-functions is
  probably too much for the youngest kids today.
- **Older kids (12+):** Will absorb both function definition and
  parameters quickly. Push them to the extension hard. Once
  they have functions-calling-functions, suggest they make a
  garden using a `draw_flower()` that calls `draw_petal()` and
  `draw_stem()`.
- **Advanced (any age):** May want to know about return values.
  Honest answer: "yes, functions can return things — but only
  when there's something useful to return. With turtle drawing,
  the function does its work directly on the turtle, so there's
  nothing to return. Return values become important when we're
  doing math on Session 5 or 6." Defer.
- **Struggling:** A kid who can't get a basic `draw_square()`
  function working in Part A is the kid you focus on. Most
  common cause: forgot to call the function after defining it.
  Sit with them, define + call together, see the square, repeat.

### What to watch for

- **The "wait, I write it once?" reaction.** First time a kid
  calls their function the second time and sees the same shape
  appear. Note who lights up.
- **The "I want to make ten of these" instinct.** Several kids
  will want to call their function many times. Encourage —
  ten houses in a row is a perfectly fine project for someone
  who finishes the base.
- **Buddy collaboration.** Functions are great for buddies because
  one buddy can write `draw_square()` and the other can write
  `draw_triangle()`, then they both use both. Encourage this
  pattern when you see it forming naturally.
- **Kids who skip parameters and hard-code values inside the
  function.** Symptom: their function only ever does one thing.
  Push: "What if you wanted a smaller one? You'd have to write
  a whole second function. Or — what if you made the size into a
  parameter?"

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 5 (next week, Variables and math).** Variables show up
  in two places: as parameters (which we just met) and as
  standalone names (`x = 5`). Today's parameters are halfway to
  variables. Next week makes the connection explicit.
- **Session 6 (Conditionals).** Combined with functions, you can
  write functions that do different things based on parameters
  (`if size > 50: t.color("red") else: t.color("blue")`). Phase
  6 game programming uses this constantly.
- **Session 7 (integration project).** Today's functions are the
  primary structuring tool for Session 7's drawing project.
  Expect kids to define multiple functions and call them in
  artful combinations.
- **Phase 3 (Python basics).** Functions return *here*, formally
  including return values, scope, default arguments, type hints.
  Today's intuitive use becomes formalized.
- **Every later phase** uses functions everywhere. customtkinter,
  Pygame, Flask — all are written as collections of functions
  and methods. Today is the conceptual foundation.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] "Three squares the long way" pre-built for the contrast
- [ ] Optional: finished neighborhood demo for "where we're
      going"
- [ ] Projector (helpful for the function-reveal moment)
- [ ] Class roster
