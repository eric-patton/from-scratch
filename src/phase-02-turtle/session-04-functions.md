## Session 4: Functions — making your own commands

*Phase 2 — Python with Turtle · Session 4 of 8*

### What we're learning today

Today is the biggest new idea of Phase 2. You'll learn how to take
a chunk of code and **give it a name** — so that instead of
copying the same code over and over, you just call it by name. A
named chunk of code is called a **function**, and they're how
real programs get built. By the end of class, you'll have written
your own `draw_square` and `draw_house` commands and used them
to build a tiny neighborhood.

### You'll need to remember from last time

- `for i in range(N):` — runs the indented body N times.
- **Indentation matters.** Lines indented under a `for` are
  inside the loop.
- `t.color(...)`, `t.pensize(...)`, `t.penup()`, `t.pendown()`,
  `t.goto(x, y)`, `t.setheading(angle)`.

---

### Part A: Define your own command

Open Thonny and start a new file. Save it as `functions.py`.

#### The motivation

Suppose you want to draw three squares at three different spots
on the stage. With what you know so far, you'd write the same
loop three times, with `goto` calls between them:

```python
import turtle
t = turtle.Turtle()

# square 1
for i in range(4):
    t.forward(60)
    t.right(90)

t.penup()
t.goto(-100, 0)
t.pendown()

# square 2
for i in range(4):
    t.forward(60)
    t.right(90)

t.penup()
t.goto(100, 0)
t.pendown()

# square 3
for i in range(4):
    t.forward(60)
    t.right(90)
```

Three squares. Lots of typing. The same loop, copied three
times. *We just learned loops to avoid copying things — and now
we're copying things again.*

There's a better way.

#### Functions: chunks of code with names

A **function** is a piece of code that you give a name to. Then,
later, you can use that name like a command — and Python runs
the chunk every time you call it.

Here's the syntax:

```python
def draw_square():
    for i in range(4):
        t.forward(60)
        t.right(90)
```

Let's break it down:

- `def` — the keyword that starts a function definition. (It's
  short for "define.")
- `draw_square` — the name you're giving this function. You can
  call it almost anything, but the convention is lowercase with
  underscores, and the name should describe what it does.
- `()` — the parentheses are required (we'll put things in them
  in a minute).
- `:` — the colon, just like a `for` loop.
- The next lines are **indented** — pushed in by 4 spaces. Same
  rule as loops. The indented lines are the function's body.

Notice: typing `def draw_square():` doesn't *do* anything. It
defines the function. The turtle hasn't drawn anything yet. To
*use* the function, you have to *call* it:

```python
draw_square()
```

That's the call. The parentheses again — this time empty,
because we're not passing any information yet.

Now the full program:

```python
import turtle
t = turtle.Turtle()

def draw_square():
    for i in range(4):
        t.forward(60)
        t.right(90)

draw_square()
```

Save. Run. The turtle draws a square.

So far this is just one square — the same as before. But watch
what happens when we want three:

```python
import turtle
t = turtle.Turtle()

def draw_square():
    for i in range(4):
        t.forward(60)
        t.right(90)

draw_square()

t.penup()
t.goto(-100, 0)
t.pendown()
draw_square()

t.penup()
t.goto(100, 0)
t.pendown()
draw_square()
```

Three squares, but only **one** copy of the actual square-drawing
code. The function `draw_square()` got called three times. If we
ever wanted to change how the squares are drawn — say, to use a
different color or a thicker pen — we'd change it in *one place*,
not three.

This is one of the most powerful ideas in all of programming:
**write something once, use it many times.**

#### Functions with parameters

Right now `draw_square()` always draws a square of size 60. What
if we want different sizes?

We can give the function a **parameter** — a piece of information
the function needs in order to do its job. For us, the size:

```python
def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)
```

Look at the differences:

- `def draw_square(size):` — the parameter `size` goes in the
  parentheses.
- `t.forward(size)` — instead of always 60, we use whatever
  `size` was passed in.

To call it, you put the size in the parentheses:

```python
draw_square(50)
draw_square(100)
draw_square(75)
```

Each call draws a different-sized square — the same function,
but with different values for `size`.

Build the full program and try it:

```python
import turtle
t = turtle.Turtle()

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

draw_square(40)
t.penup()
t.goto(-100, 0)
t.pendown()
draw_square(80)
t.penup()
t.goto(100, 0)
t.pendown()
draw_square(60)
```

Three squares, three different sizes, all drawn by the same
function.

**Checkpoint:** *You've defined a function that takes a parameter
and called it more than once with different values.* **This is
the natural stop point if class is cut short.**

---

### Part B: Build a neighborhood

Now we'll do something fun: build a row of houses, each one
drawn by a function.

#### A function for the house

A house is just a square (the body) with a triangle on top (the
roof). Build this in your file:

```python
def draw_house(size):
    # the body — a square
    for i in range(4):
        t.forward(size)
        t.left(90)
    
    # move up to the top of the square
    t.left(90)
    t.forward(size)
    t.right(90)
    
    # the roof — a triangle
    for i in range(3):
        t.forward(size)
        t.left(120)
    
    # come back down
    t.right(90)
    t.forward(size)
    t.left(90)
```

A few things to notice:

- This function is **longer** than `draw_square`. Functions can
  be as long as they need to be.
- Inside it, we use **two for loops** (one for the square, one
  for the triangle). Functions can have all the same constructs
  any other Python code can.
- The `t.left(90) / t.forward(size) / t.right(90)` block in the
  middle is moving the turtle to where the triangle should
  start, without changing the overall direction it's facing.
  Spatial reasoning is part of functions like this.
- The lines starting with `#` are **comments** — explaining what
  each section does. Useful in longer functions.

#### Build the row

Now use `draw_house()` to make a row of three houses:

```python
import turtle
t = turtle.Turtle()

def draw_house(size):
    # ... (the function from above)

# draw three houses in a row
t.penup()
t.goto(-200, 0)
t.pendown()
draw_house(60)

t.penup()
t.goto(-50, 0)
t.pendown()
draw_house(60)

t.penup()
t.goto(100, 0)
t.pendown()
draw_house(60)
```

Save. Run. Three houses across the bottom of the stage.

This is the **base goal.** Three houses, drawn by your own
function, called three times.

#### Stretch — different sizes and colors

Modify `draw_house` to also take a color:

```python
def draw_house(size, color):
    t.color(color)
    # ... (the rest of the function)
```

Now you can have houses of different sizes and colors:

```python
draw_house(50, "red")
# move
draw_house(80, "blue")
# move
draw_house(60, "green")
```

A function can take as many parameters as you want, separated by
commas. Both inside the `def` and inside the call, the order
matters — `size` is first, `color` is second, every time.

#### Extension — functions calling functions

Build smaller helper functions and have `draw_house` use them:

```python
def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def draw_triangle(size):
    for i in range(3):
        t.forward(size)
        t.left(120)

def draw_house(size):
    draw_square(size)
    # move to top of square
    t.left(90)
    t.forward(size)
    t.right(90)
    draw_triangle(size)
    # come back down
    t.right(90)
    t.forward(size)
    t.left(90)
```

Now `draw_house` is *much* shorter — it just calls the smaller
functions. And `draw_square` and `draw_triangle` could be used
on their own, too. This is how big programs get built: lots of
small functions, each doing one thing well, calling each other.

Try it. Then build an even bigger function — `draw_neighborhood()`
— that calls `draw_house()` three times with different positions
and colors. Now you have:

- `draw_square()` and `draw_triangle()` — small building blocks
- `draw_house()` — uses the small ones
- `draw_neighborhood()` — uses `draw_house()` three times

Three layers of functions, each one calling the layer below it.
Real programs are built like this.

---

### Wrap-up

Before we leave, share with the room:

- What did you build with functions today?
- Did anyone try the functions-calling-functions extension?
- If you wanted to add a sun and moon to your scene, would you
  write `draw_sun()` and `draw_moon()` functions or copy code?
  *(The right answer is: it depends on whether you want to draw
  more than one of them.)*

You learned the single biggest idea in writing reusable code
today. Once you can write functions, you can build programs out
of building blocks instead of typing everything from scratch.
Functions show up in every programming language — Python, the
JavaScript you'll learn in Phase 7, even some of the
spreadsheet formulas your parents probably use at work. The
syntax varies; the idea is universal.

You also met **parameters** — the way functions take in
information. Parameters are how you make one function work for
many situations.

### If you missed this session

Open Thonny and start a new file. Save it as `functions.py`.
Then:

1. Build the basic `draw_square()` function:
   ```python
   import turtle
   t = turtle.Turtle()

   def draw_square():
       for i in range(4):
           t.forward(60)
           t.right(90)

   draw_square()
   ```
   Save, run. A square.

2. Modify it to take a size parameter, and call it multiple times
   with different sizes (with `penup`/`goto` between).

3. Build the `draw_house(size)` function from Part B and call it
   three times to make a row of houses.

About 40 minutes of work. Pay attention to indentation and to
the parentheses (one set in the `def`, one set when you call).

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Default values: write a function as `def draw_square(size=50):`
  and you can call it as either `draw_square()` (uses 50) or
  `draw_square(80)` (uses 80). Useful for making functions easier
  to call.
- A function that draws a polygon of any number of sides:
  `def draw_polygon(sides, length):` using `range(sides)` and
  `360 / sides` as the turn angle.
- A function that takes a color list and draws a row of squares
  in those colors: pass `["red", "blue", "green"]` as a parameter
  and loop through it. (Lists are coming in a later phase, but
  curious students can try.)

### What's next

Next week we'll learn about **variables** — how to give names to
numbers and use them throughout your code. Combined with what you
know now, variables let you build programs that *change behavior*
based on values you set. The neighborhood gets even better.
