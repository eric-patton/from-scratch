## Session 5 — Teacher Notes

*Phase 2, Python with Turtle · Session 5 of 8 · Title: Variables
and a little math*

### Purpose of this session

Variables are mostly review (Phase 1 Session 6 covered the
concept). What's new is the *Python syntax* and the explicit
math operations. Four jobs, in priority order:

1. **Land Python's `=` syntax for assignment.** The biggest
   gotcha: `=` in Python is not "equals" the way math uses it.
   It's "give the variable on the left this value." Reading it
   as "gets" rather than "equals" prevents the most common
   conceptual confusion.
2. **Introduce arithmetic operators.** `+ - * /` are familiar
   from math class but kids haven't typed them as Python yet.
   Quick mechanical addition; takes 5 minutes.
3. **Reinforce variable-as-changing-value.** `size = size + 10`
   is the pattern they need to internalize. The variable's value
   changes over time; later code uses the new value.
4. **Show variables driving visible behavior.** The tower exercise
   is the visible payoff — change one variable's behavior, the
   whole drawing changes. Reinforces "variables matter."

This session is conceptually lighter than Session 4. Sessions 5
and 6 are mostly Python-syntax-for-known-Phase-1-ideas.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: have a finished tower demo to show as the destination.
- Worth pre-trying: the multi-color RGB stretch in Part B uses
  `t.color((r, g, b))` syntax. If you haven't done it before,
  test it on a student machine. Some kids will ask.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was functions.
  Anyone build a neighborhood at home?
- **Part A: variables and math** (~40 min) — `size = 50` and
  the square ~10 min, math operators ~5 min, changing variables
  ~10 min, the tower exercise ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: variable-driven drawing** (~35 min) — fan of lines
  base ~15 min, stretch (multi-color or pensize) ~10 min,
  function extension ~10 min.
- **Wrap-up** (~5 min).

If running short, **the function extension can be cut.** It's
important conceptually but kids will revisit functions in
Session 7's integration project.

### Teaching Part A

#### The `=` reframing

This is the most important pedagogical move of the session. The
`=` sign in math means "is equal to" (a fact). In programming,
`=` means "get assigned to" (an action). They look the same;
they mean different things.

> "When you see `size = 50` in Python, don't read it as 'size
> equals fifty.' Read it as 'size gets fifty' — the box on the
> left gets the value on the right poured into it."

Some kids will mentally convert; some won't. The "gets" reading
sticks better than the "equals" one.

When you get to `size = size + 10`, this becomes critical:

> "If you read this as 'size equals size plus ten,' it makes no
> sense — a number can't be ten more than itself. But if you
> read it as 'size gets the current value of size, plus ten' —
> now it works. We're updating the box."

#### Math operators

Mechanical. Walk through `+ - * /` quickly. Note that division
returns a float (`15 / 3 == 5.0`, not `5`). Don't dwell — it
just is what it is.

If a kid notices and asks "why is it 5.0 not 5?": "Python's
division always gives you decimals. There's also `//` for
integer division if you want a whole number. We'll use `/`
unless that's a problem."

#### `print()`

The handout uses `print(size)` casually. Worth one minute at the
projector:

> "`print()` is a way to see what's in a variable. Whatever you
> put inside the parens shows up in the shell at the bottom of
> Thonny. It's the most useful debugging tool in programming."

This is the foundation for the "sprinkle prints to find bugs"
debugging strategy. Worth introducing now.

#### Updating variables

The `size = size + 10` pattern is the heart of the lesson. Walk
through it carefully:

1. The right side is computed first: `size + 10`
2. The result is then assigned to the variable on the left
3. So if `size` was 50, the right side computes to 60, and then
   `size` becomes 60

Some kids will need to see this stepped through. If a kid
struggles, draw it on the whiteboard:

```
size = 50         [box: 50]
size = size + 10  [computed: 50 + 10 = 60, box becomes 60]
size = size + 10  [computed: 60 + 10 = 70, box becomes 70]
```

Mention `+=` as a shorthand. Don't dwell. Let kids use whichever
they prefer.

#### The tower

The tower exercise puts it all together. A `for` loop runs 5
times. Inside, draw a square (using a nested for-loop), move up,
update `size`. Each iteration uses the *current* value of `size`,
which is bigger than last time.

Walk through what `size` is at each iteration:
- Iteration 0: size = 30 (initial value)
- After: size = 45
- Iteration 1: size = 45
- After: size = 60
- And so on.

If kids find this confusing, slow down and demonstrate with
`print(size)` inserted at the top of the loop body. Watching the
number tick up makes the abstraction concrete.

### Teaching Part B

#### Base — fan of lines

The fan introduces `setheading(angle)` driven by a variable.
Walk through:

- Start `angle = 0`. First line goes east (heading 0).
- After drawing, `angle = angle + 30`. Now angle is 30.
- Next line goes at heading 30 (slightly north of east).
- After, angle = 60. And so on.

12 iterations × 30 degrees = 360 degrees. Same 360 pattern as
polygons in Session 3.

The "go back to center" mechanic (penup/backward/pendown) is
worth pointing out — it's how you reset position without changing
heading.

#### Stretch — multi-color or pensize

Two paths. Both are valid; the RGB version is fancier but uses
math (division by 255) that some kids will find opaque. The
`pensize(i + 1)` version is mechanically simpler and still
visible.

If a kid asks about the RGB syntax:

> "RGB is a way computers describe colors. Three numbers from
> 0 to 1. The first is how much red, the second is green, the
> third is blue. (1, 1, 1) is white. (0, 0, 0) is black. (1, 0,
> 0) is bright red. We'll cover this more later — for now just
> use the formula."

Don't try to teach color theory. Use it as a "trust the formula"
moment.

#### Extension — `draw_tower` function

The big payoff. Wraps the tower in a function with three
parameters: start_size, count, growth. This combines Sessions
4 (functions) and 5 (variables in functions) and shows how the
two compose.

Most kids who finish the stretch should attempt this. The
mechanical pattern is the same as Session 4 (define `def`, call
`function(args)`); the new wrinkle is that the parameter
**becomes a local variable** inside the function.

This is also the first session where we have a function with
both parameters AND internal variables (`size = start_size`).
Don't formally teach scope yet — just let them experience it.

### Common stumbles

- **`size = 50` vs `size == 50`.** Single equals is assignment;
  double equals is comparison (which they'll meet in Session 6).
  Today only `=` matters.
- **Forgetting to update the variable.** Kid writes the loop,
  draws a square, and the variable never changes. Symptom:
  tower is all the same size. Fix: `size = size + 15` *inside*
  the loop body.
- **Updating in the wrong place.** Common: putting the `size +=
  15` *before* drawing instead of after. Result: the first square
  is 45, not 30 (started at 30, incremented immediately, then
  drew). Fix: put the increment *after* the draw.
- **Variable defined inside the loop.** `size = 30` inside the
  loop body resets it every iteration. Tower is all 30+15=45.
  Fix: `size = 30` belongs *outside* the loop, before the
  `for`.
- **`print(size)` showing nothing or showing the wrong thing.**
  The shell shows what's printed during the program's run. If
  the kid expected a number but gets nothing, they probably
  forgot the parentheses or printed something else.
- **RGB color throws an error.** `t.color((r, g, b))` is a
  *tuple* (the double parens). `t.color(r, g, b)` (single
  parens) sometimes also works depending on Python version. If
  one breaks, try the other.
- **Float division surprise.** `15 / 3` is `5.0` not `5`. Most
  kids don't notice. The few who do usually accept "Python
  always uses decimals for /" without further explanation.

### Differentiation

- **Younger kids (9-10):** May get the basic `size = 50` quickly
  but struggle with `size = size + 10`. Sit with them, draw the
  box on paper, walk through how it changes. The concept of
  "the variable changes value over time" is genuinely abstract.
- **Older kids (12+):** Will pick up variables and arithmetic
  fast. Push them to the function extension. If they finish:
  ask them to write a `draw_tower` that ALSO takes a starting
  position (x, y) — combines variables, parameters, and `goto`.
- **Advanced (any age):** Will see variables as obvious. Push
  them to compound the concepts: a function that uses variables,
  and is called multiple times with variables as arguments. The
  `draw_tower(20, 5, 10)` then `draw_tower(40, 3, 20)` pattern
  is the right level.
- **Struggling:** A kid who can't get a basic `size = 50` /
  `t.forward(size)` working in Part A is the kid you focus on.
  Common cause: confused `size = 50` (no quotes) vs
  `size = "50"` (string, doesn't work in turtle commands). Or
  used the variable name with quotes by mistake.

### What to watch for

- **The "I just changed one number and the whole thing
  changed" reaction.** When a kid changes the initial `size = 50`
  to `size = 100` and watches the whole drawing scale. Several
  kids will get this; it's the visible payoff of variables.
- **Buddy collaboration on the fan.** Two buddies, one types
  the structure while the other tweaks numbers — discovers
  patterns by experimentation. Encourage.
- **Kids using `print()` to debug.** First time someone uses
  `print(size)` to figure out what's happening, name it: "great
  use of `print` to see what's going on. That's a real
  debugging trick."
- **Off-by-one errors in the tower.** Kids who use `size = 30`
  initial and `size = size + 15` will end up with sizes 30, 45,
  60, 75, 90. Some will count "5 squares of 30, 45, 60, 75, 90"
  and notice they don't add up to 100, so they think it's
  broken. It's not. The size *is* the side length, not the
  total. Help them visualize.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 6 (next week, conditionals).** Variables today + `if`
  next week = decisions based on values. The "color depends on
  size" pattern in Session 6 directly extends today's variable
  work.
- **Session 7 (integration).** Combines functions, variables,
  loops, conditionals into a single creative project.
- **Phase 3 (Python basics).** Today's `size = size + 10` becomes
  central to all kinds of state-tracking programs (scores,
  health, time, anything that changes over time).
- **Pygame (Phase 6).** Game state IS variables. Player x/y,
  score, lives, level — all variables that change over time.
  Today is the syntactic foundation.
- **Functions + variables compose.** The function extension
  today is the pattern that scales: small reusable functions,
  each working with their own local variables. Phase 8 (Flask)
  takes this all the way.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built tower demo
- [ ] Projector (helpful for the math + tower walkthrough)
- [ ] Class roster
