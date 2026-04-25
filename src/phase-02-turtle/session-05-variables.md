## Session 5: Variables and a little math

*Phase 2 — Python with Turtle · Session 5 of 8*

### What we're learning today

You've actually been using variables since Session 3 (the `i` in
`for i in range(N):`) and Session 4 (parameters in your
functions). Today we'll **name our own variables**, do math with
them, and use them to make drawings that grow, shift, and change.
By the end of class, you'll have built a "tower of squares" that
gets bigger as it goes up — driven entirely by a variable.

### You'll need to remember from last time

- **Functions** — `def name(parameter):` to define, `name(value)`
  to call. The body is indented underneath.
- **Loops** — `for i in range(N):` runs the indented body N
  times.
- **The peanut butter rule** is still in effect.
- **Variables in Scratch** — the orange "Make a Variable" blocks,
  `set score to 0` and `change score by 1`. Same idea today,
  different syntax.

---

### Part A: Names for values

Open Thonny and start a new file. Save it as `variables.py`.

#### Make a variable

In Scratch, you made a variable by clicking "Make a Variable." In
Python, you make a variable by writing its name and giving it a
value:

```python
size = 50
```

That's it. The variable `size` now holds the value `50`. No
button to click; no setup required. Just write the name and
assign with `=`.

The `=` sign in Python isn't "equals" the way it is in math —
it's "give the name on the left this value on the right." Some
programmers read `size = 50` out loud as **"size gets fifty."**
That helps remember it's an action, not a fact.

Use the variable in turtle code:

```python
import turtle
t = turtle.Turtle()

size = 50

t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
```

Save. Run. A square of size 50.

Now change the variable to `size = 100`. Save. Run. A square of
size 100.

This is the power of variables: you change *one* number at the
top, and the entire program changes behavior. Imagine if your
square's size appeared in 20 different places in your code —
without variables you'd have to find and change every one.

#### Math with variables

Variables aren't just storage — they're values, so you can do
math on them. Python knows the basic arithmetic operators:

| Operator | Means | Example |
|---|---|---|
| `+` | add | `5 + 3` is `8` |
| `-` | subtract | `5 - 3` is `2` |
| `*` | multiply | `5 * 3` is `15` |
| `/` | divide | `15 / 3` is `5.0` |

You can use them with variables too:

```python
size = 50
big_size = size * 2     # 100
small_size = size / 2   # 25.0
size_plus_ten = size + 10   # 60
```

Variables can hold the *result* of math. They can also use
*other variables* in their math.

#### Changing a variable

You can change what a variable holds. Just assign a new value:

```python
size = 50
print(size)   # prints 50

size = 100
print(size)   # prints 100
```

The most common pattern: change a variable based on its *current*
value:

```python
size = 50
size = size + 10   # now size is 60
size = size + 10   # now size is 70
```

This is the Python equivalent of Scratch's `change size by 10`.
Read it as: "size gets the current size plus 10."

(There's a shorter way to write it: `size += 10` does the same
thing as `size = size + 10`. Either is fine. Use whichever you
find clearer.)

#### Using a variable inside a loop

Now we put it together. Add this to your file:

```python
import turtle
t = turtle.Turtle()

size = 30

for i in range(5):
    # draw a square of the current size
    for j in range(4):
        t.forward(size)
        t.right(90)
    # move up
    t.penup()
    t.right(90)
    t.forward(size)
    t.left(90)
    t.pendown()
    # grow the size for next time
    size = size + 15
```

Save. Run.

A tower of squares! Each one is bigger than the last because
`size` increases by 15 each iteration of the outer loop.

The first square is 30. Then size becomes 45 — second square is
45. Then 60. Then 75. Then 90.

The variable lives across iterations. The loop *and* the variable
work together to produce the growing pattern.

**Checkpoint:** *You've built a drawing that uses a variable that
changes inside a loop, and the visual output reflects the
changing variable.* **This is the natural stop point if class is
cut short.**

---

### Part B: A variable-driven drawing

Now build something more complex with variables.

#### Base goal — a fan of lines

Build a fan of 12 lines, all coming from the same starting point,
each rotated a bit further than the last. The angle is the
variable that changes:

```python
import turtle
t = turtle.Turtle()
t.speed(0)

angle = 0

for i in range(12):
    t.setheading(angle)
    t.forward(100)
    # come back to the start
    t.penup()
    t.backward(100)
    t.pendown()
    # rotate for next line
    angle = angle + 30
```

Save. Run. A fan of 12 lines spreading out in a half-circle.

Notice: `setheading(angle)` uses the variable to point the turtle
in a specific direction each time. After drawing the line, we go
back to the center, then increase `angle` by 30 for the next one.
12 lines × 30 degrees = 360, so they go all the way around.

#### Stretch — multi-color tower

Combine variables and color. Build a tower (like in Part A) but
have the color change with each iteration:

```python
import turtle
t = turtle.Turtle()
t.speed(0)

size = 30
red_amount = 50

for i in range(8):
    # use the variables to set color and draw
    t.color((red_amount / 255, 0.5, 0.5))
    
    for j in range(4):
        t.forward(size)
        t.right(90)
    
    # move up
    t.penup()
    t.right(90)
    t.forward(size)
    t.left(90)
    t.pendown()
    
    # update variables
    size = size + 10
    red_amount = red_amount + 25
```

The `t.color((red_amount / 255, 0.5, 0.5))` line uses an RGB
color (red, green, blue, each from 0 to 1). As `red_amount` grows,
the red part of the color gets brighter — so each square in the
tower has a slightly redder color than the one below it.

Don't worry about the RGB syntax for now — just notice that the
color changes because the variable does.

If RGB feels too much, simpler version: change `pensize` based
on `i`:

```python
t.pensize(i + 1)
```

The first square uses pensize 1, the next 2, etc. Visible
difference, simpler code.

#### Extension — a function

Wrap the tower in a function:

```python
def draw_tower(start_size, count, growth):
    size = start_size
    for i in range(count):
        for j in range(4):
            t.forward(size)
            t.right(90)
        t.penup()
        t.right(90)
        t.forward(size)
        t.left(90)
        t.pendown()
        size = size + growth

draw_tower(20, 5, 10)
# move
t.penup()
t.forward(150)
t.pendown()
draw_tower(40, 3, 20)
```

Now you have a *flexible* tower-drawing function. You pass in
the starting size, how many squares, and how much each one grows.
Two different towers, drawn with one function. This combines
**Sessions 4 + 5** — functions with parameters, plus variables
that change inside the function.

That's how real programs get built.

---

### Wrap-up

Before we leave, share with the room:

- What's the highest size your tower got to?
- Did anyone try the multi-color version?
- For the kids who built the function: did you draw multiple
  towers? What were the parameter values?

You learned today how to **store information in named places** and
do math with it. That's the foundation of every meaningful
program — programs are mostly variables changing over time, with
loops and conditionals deciding when and how.

Variables also gave you a new debugging tool: `print(size)` shows
you the current value of `size` in the shell. When something's
not behaving the way you expect, sprinkling some `print()` calls
around your code is the most common way programmers figure out
what's actually happening.

### If you missed this session

Open Thonny and start a new file. Save it as `variables.py`.
Then:

1. Make a variable: `size = 50`. Build a square that uses
   `t.forward(size)` and run it. Change `size` to `100`, run
   again. Same code, different square.

2. Practice changing variables: `size = size + 10`. Try printing
   it after each change with `print(size)`.

3. Build the tower from Part A — a `for` loop that draws a
   square of size `size` each iteration, then increases `size`
   by 15.

About 30-40 minutes. Watch your indentation; the inner square
loop is indented twice (once for the outer loop, once for being
the inner loop's body).

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Try negative growth: `size = size - 10`. Tower gets smaller
  going up. (When does it become invisible?)
- Use multiple variables in one drawing — `x` and `y` for
  position, `size` for shape. A tower that drifts sideways as
  it grows.
- Try `print(size)` inside the loop to watch the variable change
  in real time. The shell at the bottom of Thonny will show each
  value.
- Use variables for the loop counter math: `for i in range(10):`
  then `t.forward(i * 5)` makes a spiral that grows linearly.
  Combine with `t.right(15)` for the same spiral as Session 3.

### What's next

Next week: **conditionals**. We'll bring back the `if` block,
this time in Python. Combined with variables, conditionals let
your programs *decide* what to do based on the values they're
working with. After that, we have one more session of "putting
it all together" before the milestone project.
