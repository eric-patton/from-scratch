## Session 6: Conditionals — `if` in Python

*Phase 2 — Python with Turtle · Session 6 of 8*

### What we're learning today

Today's the last "new syntax" session of Phase 2. We bring back
the `if` block — but in Python instead of Scratch — and combine
it with everything else you know to make programs that *decide*
what to do based on the situation. Combined with variables, you
can build programs that change behavior based on values you set.
By the end of class, you'll have a function that draws colored
shapes where the *color depends on the size*.

### You'll need to remember from last time

- **Variables** — `size = 50`, `size = size + 10`.
- **Math operators** — `+`, `-`, `*`, `/`.
- **Functions with parameters** — `def draw_square(size):`.
- **The `if` block from Scratch** — "if something, then do this."
- **Indentation matters** — lines inside something are indented.

---

### Part A: Making decisions in Python

Open Thonny and start a new file. Save it as `decisions.py`.

#### The `if` statement

Just like in Scratch, the `if` statement does something **only
when a condition is true.** In Python, it looks like this:

```python
size = 70

if size > 50:
    print("That's a big size!")
```

Walk through:

- `if` — the keyword that starts the conditional.
- `size > 50` — the **condition.** This is a question Python can
  answer with True or False. Is `size` greater than 50? Yes or
  no?
- `:` — the colon (required, just like `for` and `def`).
- The next line is **indented** — it's the body that runs only
  if the condition is true.

Run it. Since `size` is 70, and 70 is greater than 50, Python
prints "That's a big size!"

Now change `size = 70` to `size = 30`. Run again.

This time nothing prints. The condition `30 > 50` is false, so
Python skips the body of the `if`.

#### `else` for the other case

Often you want one thing to happen if the condition is true, and
*something else* to happen if it's false. Use `else`:

```python
size = 30

if size > 50:
    print("Big!")
else:
    print("Small!")
```

If `size > 50`, prints "Big!" Otherwise, prints "Small!"

`else` doesn't need a condition — it just runs whenever the
`if`'s condition was false.

The colon and indentation rules are the same. The body of `else`
is indented underneath, just like `if`.

#### Comparison operators

The condition uses **comparison operators** to compare values.
Python knows these:

| Operator | Means | Example |
|---|---|---|
| `>` | greater than | `5 > 3` is `True` |
| `<` | less than | `5 < 3` is `False` |
| `>=` | greater than or equal to | `5 >= 5` is `True` |
| `<=` | less than or equal to | `5 <= 4` is `False` |
| `==` | **equal to** | `5 == 5` is `True` |
| `!=` | **not equal to** | `5 != 3` is `True` |

The two important ones to be careful about:

- **`==` for "is equal to"** — two equals signs, not one. *One*
  equals sign (`=`) means *assignment* (giving a variable a
  value). *Two* equals signs (`==`) means *comparison* (asking
  if two things are equal). They look the same and they're not.
- **`!=` for "is not equal to"** — the exclamation point means
  "not."

Try a few:

```python
x = 10

if x == 10:
    print("x is exactly 10")

if x != 5:
    print("x is not 5")

if x >= 10:
    print("x is at least 10")
```

Run. All three prints happen, because `x` is 10.

Now change `x = 5`. Only the second prints (`5 != 5` is false,
so the third skips; `5 == 10` is false, so the first skips; but
`5 != 5`... actually that's *also* false. Wait — let me re-read.
With `x = 5`: `5 != 5` is false. So... nothing prints. Try it.)

If you read those three carefully and predicted what would happen
before you ran it — congratulations, you're starting to think
like a programmer.

#### `elif` for multiple cases

Sometimes you want to check several conditions in order. `elif`
(short for "else if") chains them together:

```python
size = 30

if size > 100:
    print("Huge!")
elif size > 50:
    print("Big!")
elif size > 20:
    print("Medium!")
else:
    print("Tiny!")
```

Python checks each condition in order. The first one that's
true, its body runs. If none are true, the `else` body runs.

With `size = 30`: 30 > 100 is false, 30 > 50 is false, 30 > 20
is true → prints "Medium!" The remaining `elif`s and `else` are
skipped.

You can have as many `elif` lines as you want. The `else` at
the end is optional.

**Checkpoint:** *You've built an `if/else` (or `if/elif/else`)
that makes decisions based on the value of a variable.* **This is
the natural stop point if class is cut short.**

---

### Part B: Decisions in your drawings

Now we use conditionals where they really shine — making your
drawings react to the values they're working with.

#### Base goal — colored squares by size

Build a function that draws a square, but **colors it red if
big and blue if small**:

```python
import turtle
t = turtle.Turtle()
t.speed(0)

def draw_colored_square(size):
    if size > 60:
        t.color("red")
    else:
        t.color("blue")
    
    for i in range(4):
        t.forward(size)
        t.right(90)

# draw a few squares of different sizes
draw_colored_square(40)
t.penup()
t.forward(60)
t.pendown()
draw_colored_square(80)
t.penup()
t.forward(100)
t.pendown()
draw_colored_square(50)
```

Save. Run.

You should see three squares: small blue, big red, medium blue.
The function decides the color based on the size each time it's
called.

This is small but powerful. You've combined functions
(Session 4), variables (Session 5), and conditionals (today) into
one little decision-making drawing function.

#### Stretch — three categories with `elif`

Add a third size category. Use `elif`:

```python
def draw_colored_square(size):
    if size > 80:
        t.color("red")
    elif size > 40:
        t.color("orange")
    else:
        t.color("blue")
    
    for i in range(4):
        t.forward(size)
        t.right(90)
```

Now squares are red, orange, or blue depending on size. Try
calling with various sizes (20, 50, 90, etc.) and see the colors.

#### Extension — a row of growing squares with conditional colors

Combine all of Phase 2 into one program: a loop that draws a
growing row of squares, colored by size:

```python
import turtle
t = turtle.Turtle()
t.speed(0)

def draw_colored_square(size):
    if size > 80:
        t.color("red")
    elif size > 40:
        t.color("orange")
    else:
        t.color("blue")
    
    for i in range(4):
        t.forward(size)
        t.right(90)

size = 10
for i in range(12):
    draw_colored_square(size)
    # move to next position
    t.penup()
    t.forward(size + 15)
    t.pendown()
    # grow
    size = size + 8
```

Save. Run.

A row of 12 squares, growing from small (size 10) to large (size
98). The colors transition: blue, blue, blue, blue, orange,
orange, orange, orange, orange, red, red, red. The conditional
inside the function picks the color; the loop drives the size
forward.

This program uses **every concept from Phase 2 so far**:
typing, sequences, loops, functions with parameters, variables,
arithmetic, AND conditionals — all in one ~25-line program. You
just built that.

---

### Wrap-up

Before we leave, share with the room:

- What did your conditional decide on?
- For the kids who built the row of growing squares — does the
  color transition feel right, or would you tweak the
  thresholds?
- Did anyone try a condition with `and` or `or`? (Hint: those
  let you combine multiple conditions, like `if size > 20 and
  size < 50:`. We didn't formally cover them, but they work.)

You learned today how to make programs that **decide** —
based on values, based on variables, based on what's happening.
Combined with everything else, you now have the full toolbox
that powers most of what computers do: store information
(variables), repeat actions (loops), respond to inputs (events,
which we'll see again in Pygame), bundle code (functions), and
make decisions (conditionals).

That's basically what programming *is*. The rest is mostly
applying these building blocks to specific problems.

### If you missed this session

Open Thonny and start a new file. Save it as `decisions.py`.
Then:

1. Build the basic `if/else`:
   ```python
   size = 30

   if size > 50:
       print("Big!")
   else:
       print("Small!")
   ```
   Run. Then change `size = 70` and run again. Different output.

2. Try `elif` with three categories — small, medium, large.

3. Build the `draw_colored_square(size)` function from Part B
   above. Call it three times with different sizes.

About 30 minutes. Watch indentation — the body of `if`, `elif`,
and `else` is indented underneath each one.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Combine conditions with `and`: `if size > 20 and size < 50:`.
  Both conditions must be true.
- Combine with `or`: `if size < 10 or size > 100:`. Either
  condition can be true.
- Use `not`: `if not size > 50:` is the same as `if size <= 50:`.
  Sometimes one reads better than the other.
- Conditional inside a loop, deciding what to draw each
  iteration:
  ```python
  for i in range(8):
      if i < 4:
          # draw a triangle
          pass
      else:
          # draw a square
          pass
  ```
  Make a row that's half triangles, half squares.

### What's next

Next week we **put it all together** — sequences, loops,
functions, variables, conditionals — and build a creative
drawing project that uses all of it. (Phase 1 also had events;
Turtle doesn't really do events, so we save the event stuff for
Phase 6 when we start writing real games in Pygame.) After next
week is the milestone session, where you'll plan and build your
*own* drawing project.
