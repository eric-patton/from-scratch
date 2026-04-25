## Session 3: Loops in Python — `for` and `range`

*Phase 2 — Python with Turtle · Session 3 of 8*

### What we're learning today

Last week your code was getting long and repetitive — eight lines
to draw a square, lots of similar lines for the scene. Today
that's about to change. We'll learn the Python version of Scratch's
`repeat` block, called a **for loop**. By the end of class, you'll
draw a square in three lines instead of eight, and you'll be
making patterns that would take *hundreds* of lines without loops.

### You'll need to remember from last time

- Open Thonny, type code, save with `.py`, click Run.
- Every program starts with `import turtle` and
  `t = turtle.Turtle()`.
- `t.forward(N)`, `t.right(N)`, `t.left(N)`, `t.color()`,
  `t.pensize()`.
- `#` starts a comment. Everything after it on the line is
  ignored.
- **Loops from Scratch** (`repeat 4`, `forever`). Same idea, new
  syntax.

---

### Part A: The `for` loop

Open Thonny and start a new file. Save it as `loops.py`.

#### The square, the long way

Let's start by typing the square the way we did in Session 1:

```python
import turtle
t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
```

Run it. A square. Eight lines.

Now look at those eight lines. Two lines repeated four times.
That's exactly what a loop is for: doing the same thing N times
without writing it N times.

#### The square, the loop way

Replace your eight lines with this:

```python
import turtle
t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)
```

Run it. Same square. Three lines instead of eight.

Let's break down what's happening:

- `for i in range(4):` — this means "do the next part 4 times."
  The `range(4)` produces a sequence of numbers from 0 to 3 (which
  is four numbers — Python starts counting at 0, not 1).
- `i` is the **loop variable**. Each time through the loop, `i`
  takes the next value from the sequence (0, then 1, then 2, then
  3). We don't have to *use* `i` in this loop — but the syntax
  requires we name it. Most programmers use `i` by default.
- The **colon** at the end of the `for` line is required. Don't
  forget it.
- The lines underneath the `for` are **indented** — pushed in by
  four spaces. *That's how Python knows they're part of the loop.*

#### Indentation matters in Python

This is the big new thing about Python that didn't exist in
Scratch. **Indentation is part of the grammar.**

In Scratch, you snapped blocks inside the `repeat` block's mouth.
Python uses indentation instead. Lines that are indented under
`for i in range(N):` are inside the loop. Lines that are *not*
indented are outside the loop.

Try this — change the file so the second line isn't indented:

```python
for i in range(4):
    t.forward(100)
t.right(90)
```

Now run it. The turtle moves forward 4 times in a straight line,
then turns once. That's because only `t.forward(100)` is *inside*
the loop. The `t.right(90)` is *outside* — it runs once, after
the loop is done.

Indentation isn't decoration. It's part of what your program
*does*. Be careful with it.

> **Good news:** Thonny indents for you. When you type `for ... :`
> and press Enter, Thonny moves your cursor in 4 spaces
> automatically. Trust it.

> **Heads up:** If you ever copy-paste code from somewhere, the
> indentation may not match. Mixed tabs and spaces is a common
> cause of confusing errors. If your code looks right but won't
> run, check the indentation by clicking each line and looking at
> the cursor position.

#### Try other shapes

Now try changing the loop count and the turn angle:

```python
for i in range(3):
    t.forward(100)
    t.right(120)
```

Run it. A triangle.

Try `range(5)` and `t.right(72)`. A pentagon.

Try `range(6)` and `t.right(60)`. A hexagon.

You probably noticed: number-of-sides times turn-angle always
equals 360. Same pattern as Phase 1 Session 3. Loops just made
it way easier to test.

**Checkpoint:** *You've replaced a manually-typed shape with a
`for` loop, and you've used `range(N)` with a different number to
draw at least one different shape (triangle, pentagon, etc.).*
**This is the natural stop point if class is cut short.**

---

### Part B: Patterns that loops make easy

Now we'll do things that would have been ridiculous to type by
hand.

#### A spiral

Start a new file. Save it as `spiral.py`. Type:

```python
import turtle
t = turtle.Turtle()
t.speed(0)
t.color("blue")

for i in range(50):
    t.forward(i * 2)
    t.right(15)
```

Run it. A blue spiral that grows outward.

Look at what's happening: each time through the loop, `i` is
different (0, 1, 2, 3, ... 49). And `i * 2` (i times 2) is the
distance the turtle walks. So the first time the turtle walks 0
steps, then 2, then 4, then 6... longer and longer. Combined
with a 15-degree turn each time, it spirals.

This is the first time we've actually *used* the loop variable
`i` for something. It's not just a counter — it's a value we can
compute with. Variables are next week's lesson, so don't worry
about the math yet — just notice that `i` does something.

`t.speed(0)` makes the turtle draw without animation (instant).
On a long loop like this, the animation would take forever.

#### Try the base goal

Pick one:

- **A colorful shape:** Use a loop to draw a many-sided shape
  (like a 12-sided dodecagon, with `range(12)` and `t.right(30)`).
  Make it any color you want.
- **A row of squares:** Use a loop to draw 5 squares in a row,
  each one a small distance apart. (Hint: inside the loop, draw
  a square the long way — without a loop — then move the turtle
  to the next position.)

#### Stretch — nested loops

You can put a loop *inside* another loop. The inside loop runs
all the way through, then the outside loop moves to its next
iteration, then the inside loop runs all the way through again,
and so on.

Try this — the **flower of squares** from Phase 1:

```python
import turtle
t = turtle.Turtle()
t.speed(0)
t.color("purple")

for i in range(12):
    for j in range(4):
        t.forward(50)
        t.right(90)
    t.right(30)
```

Run it. A flower-shaped pattern made of 12 rotated squares.

The outer loop runs 12 times. Each time, the inner loop draws a
square (4 sides), and *then* the outer loop turns 30 degrees.
12 squares × 30 degrees = 360 degrees, so they go all the way
around.

Notice: the inner loop's body is indented *twice* (8 spaces from
the left). Indentation level says how nested you are. The
`t.right(30)` is indented once (4 spaces) because it's inside the
outer loop but outside the inner loop.

This is genuinely confusing the first time. Read it carefully.
Look at the indentation. Run it. Change the numbers and see what
changes.

#### Extension

Make a *colorful* spiral that changes color as it grows. Add
this to the spiral:

```python
import turtle
t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(60):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.right(15)
```

The `colors[i % 6]` part picks a color from the list based on
which iteration we're in. The `%` operator gives the remainder
when dividing — so `i % 6` cycles through 0, 1, 2, 3, 4, 5, 0,
1, 2, 3... and that picks the colors in order, repeating.

If that's confusing right now, that's fine. Just type it and run
it. Lists, indexing, and the `%` operator are things we'll cover
properly in later sessions. For now, enjoy the rainbow.

---

### Wrap-up

Before we leave, share with the room:

- What was the most-sides shape anyone drew?
- Did anyone try the nested-loops flower? What did it look like?
- Did anyone get a confusing indentation error? What fixed it?

You did something today that genuinely changes what you can build.
**Loops are how programmers make patterns, animations, and
anything that involves "do this many times."** From here on out,
you'll use them constantly.

You also met **indentation** as a real grammar rule. That's the
single weirdest thing about Python compared to most other
programming languages. After a couple of sessions it'll feel
normal — for now, just remember: indented = inside, not indented
= outside.

### If you missed this session

Open Thonny and start a new file. Save it as `loops.py`. Then:

1. Build a `for` loop that draws a square:
   ```python
   import turtle
   t = turtle.Turtle()

   for i in range(4):
       t.forward(100)
       t.right(90)
   ```
   Save, run. Watch the square draw.

2. Change `range(4)` and `t.right(90)` to draw a triangle (3
   sides, 120 degrees) and a pentagon (5 sides, 72 degrees).

3. Try the spiral from Part B above.

About 30 minutes. Pay attention to indentation — the lines inside
the loop need to be pushed in by 4 spaces (Thonny does this for
you when you press Enter after the colon).

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Try `range(N)` with a different starting number: `range(5, 15)`
  produces 5 through 14. `range(0, 20, 2)` produces 0, 2, 4, 6,
  ..., 18 (counts by twos).
- Try a `for i in range(360)` loop where the turtle moves 1 step
  and turns 1 degree each iteration. What shape does that draw?
- Try multiple loops in one program. Draw five different shapes,
  one after another, with `penup` / `goto` between them to space
  them out.

### What's next

Next week we'll learn about **functions** — how to take a chunk
of code (like "draw a square") and give it a name, so you can
just say `draw_square()` instead of writing the whole loop every
time. It's the biggest new idea in Phase 2.
