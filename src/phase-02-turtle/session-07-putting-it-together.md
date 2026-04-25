## Session 7: Putting it together — a garden scene

*Phase 2 — Python with Turtle · Session 7 of 8*

### What we're learning today

You now know everything in Phase 2: typing, turtle commands,
loops, functions, variables, conditionals. Today we'll combine
all of it into one creative drawing — **a garden of flowers** —
where each flower is drawn by a function, multiple flowers are
drawn by a loop, and the colors and sizes vary based on
conditionals. By the end of class, you'll have a complete scene
that's substantially more sophisticated than anything in Phase 1.

### You'll need to remember from last time

Everything. No, really:

- **Functions with parameters** — `def name(parameter):`
- **Variables and arithmetic** — `size = 50`, `size = size + 10`
- **For loops** — `for i in range(N):`
- **Conditionals** — `if/elif/else`
- **All your turtle commands** — forward, right, left, color,
  pensize, penup, pendown, goto, setheading, circle, write

This is the test: can you put it all together? (Spoiler: yes.)

---

### Part A: Build a flower function

Open Thonny and start a new file. Save it as `garden.py`.

#### Plan the flower

Before any code, think about what a flower looks like in Turtle
terms. We need:

- A **stem** — a vertical line going up from the bottom.
- **Petals** at the top — several circles arranged in a ring.
- A **position** so we can put it somewhere on the stage.
- A **color** so different flowers can look different.
- A **size** so big and small flowers can coexist.

Position, color, size — those are parameters. The stem and
petals are what the function does.

#### Build it

```python
import turtle
t = turtle.Turtle()
t.speed(0)

def draw_flower(x, color, petal_size):
    # move to the bottom of the stem
    t.penup()
    t.goto(x, -100)
    t.pendown()
    
    # draw the stem
    t.color("green")
    t.pensize(3)
    t.setheading(90)   # face up
    t.forward(80)
    
    # draw the petals (8 circles in a ring)
    t.color(color)
    t.pensize(2)
    for i in range(8):
        t.circle(petal_size)
        t.right(45)

# draw one flower
draw_flower(0, "red", 15)
```

Save. Run.

A red flower in the middle of the stage. Stem going up, eight red
circles around the top.

Walk through what's happening:

- `draw_flower` takes three parameters: `x` (where on the stage),
  `color` (petal color), `petal_size` (how big each petal circle
  is).
- The stem is always drawn green and 80 pixels tall.
- The petals loop runs 8 times. Each iteration draws a circle,
  then turns 45 degrees so the next circle starts in a different
  position. 8 × 45 = 360, so they go all the way around.

#### Try it with different parameters

Add three more flower calls:

```python
draw_flower(-150, "yellow", 20)
draw_flower(150, "purple", 12)
draw_flower(-50, "pink", 18)
```

Run. Now you have four flowers across the stage, each different.

This is the same function called four times with four different
sets of arguments. **One function, multiple flowers.** You've
seen this pattern before in Session 4 — the power is the same;
the visual is fancier.

**Checkpoint:** *You have a `draw_flower` function and at least
three flowers on the stage drawn by calling it.* **This is the
natural stop point if class is cut short.**

---

### Part B: A garden with variation

Now we use loops + conditionals to make a *bigger* garden where
the flowers vary in interesting ways.

#### Base goal — a loop-driven row

Use a `for` loop to draw a row of flowers across the stage. Pick
a starting position, increment the x-coordinate each time:

```python
import turtle
t = turtle.Turtle()
t.speed(0)

def draw_flower(x, color, petal_size):
    t.penup()
    t.goto(x, -100)
    t.pendown()
    t.color("green")
    t.pensize(3)
    t.setheading(90)
    t.forward(80)
    t.color(color)
    t.pensize(2)
    for i in range(8):
        t.circle(petal_size)
        t.right(45)

# draw a row of 5 flowers
x = -200
for i in range(5):
    draw_flower(x, "red", 15)
    x = x + 100
```

Run. Five red flowers in a row.

The variable `x` starts at -200 and increases by 100 each
iteration. The loop runs 5 times; the x value drives where each
flower appears.

#### Stretch — different colors per flower

Right now all five are red. Let's make each one a different
color, using a conditional inside the loop to pick the color
based on the iteration number:

```python
x = -200
for i in range(5):
    if i == 0:
        color = "red"
    elif i == 1:
        color = "orange"
    elif i == 2:
        color = "yellow"
    elif i == 3:
        color = "purple"
    else:
        color = "pink"
    
    draw_flower(x, color, 15)
    x = x + 100
```

Now you have a rainbow of flowers. The conditional picks a color
based on `i`, then `draw_flower` uses it.

(Yes, this is verbose. There's a better way using a *list* — but
we haven't covered lists yet. We'll get there in Phase 3.)

#### Extension — a complete scene

Add more elements to make a real garden scene:

- A **sun** in the upper corner.
- **Grass** at the bottom (a horizontal green line).
- **Sky** by changing the background color.
- A **title** at the top using `t.write()`.
- **Variable petal sizes** — make some flowers bigger than others
  using another conditional or by varying the parameter.

Here's a starting structure:

```python
import turtle
t = turtle.Turtle()
t.speed(0)

# set the scene
t.bgcolor("skyblue")

def draw_flower(x, color, petal_size):
    # ... (same as before)

def draw_sun(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.pensize(2)
    t.circle(size)

def draw_grass(y):
    t.penup()
    t.goto(-240, y)
    t.pendown()
    t.color("green")
    t.pensize(8)
    t.forward(480)

# build the scene
draw_sun(180, 120, 40)
draw_grass(-100)

# row of flowers (with the conditional color picker from above)
x = -200
for i in range(5):
    if i == 0:
        color = "red"
    elif i == 1:
        color = "orange"
    elif i == 2:
        color = "yellow"
    elif i == 3:
        color = "purple"
    else:
        color = "pink"
    
    draw_flower(x, color, 15)
    x = x + 100

# title
t.penup()
t.goto(-100, 150)
t.pendown()
t.color("black")
t.write("My Garden", font=("Arial", 24, "normal"))
```

Save. Run.

A complete garden scene: blue sky, yellow sun, green grass,
five colorful flowers in a row, and a title.

This program uses **every concept from Phase 2**: typing the code
in Thonny, turtle commands, multiple sequences (each function is
a sequence), three loops (the petals, the for-loop driving the
row, plus you could argue more), three functions with parameters,
two variables (`x` and `color`) that change inside the loop,
and a conditional choosing the color.

You went from "just typed your first line of Python" to "writing
a fifty-line program with multiple functions and a creative
output" in seven weeks. That's a real arc.

---

### Wrap-up

Before we leave, share with the room:

- What did your garden look like? Anyone do something unexpected?
- For the kids who built the full scene — was anything trickier
  than you expected?
- What would you do differently if you started over?

**Important: start thinking about your milestone project for
next week.** You'll have one session — next week — to plan and
build a Turtle drawing of your *own* design, then show it to the
class. Some seed ideas:

- A **landscape scene** — mountains, trees, a river, a sunset.
- A **fancy pattern** — like a snowflake or a mandala (radial
  symmetry around a center point).
- An **abstract drawing** — colored shapes arranged for visual
  effect.
- A **scene from somewhere you like** — a beach, your room, a
  page from a comic.
- An **animal** built from circles and shapes.
- **Your name** in giant decorated letters.

Don't decide today. But **come to next week's class with at
least one idea you're excited about.**

### If you missed this session

Open Thonny and start a new file. Save it as `garden.py`. Then:

1. Build the `draw_flower(x, color, petal_size)` function from
   Part A. Call it once to draw a single flower.

2. Call it three or four more times with different positions,
   colors, and sizes.

3. Wrap the calls in a `for` loop driven by an `x` variable that
   starts at -200 and increases by 100 each iteration.

4. Add a conditional inside the loop to pick a different color
   for each flower (Part B stretch).

About 40-50 minutes. Pay attention to indentation — the loop
body is indented once, the `if/elif/else` bodies inside the loop
are indented twice.

If you get stuck, ask your buddy at the start of next class.
And **think about what you want to build for your own milestone
project.**

### Stretch and extension ideas

- Replace the `if/elif/else` color-picker with a **list**. (We
  haven't formally taught lists, but a curious student can try:
  `colors = ["red", "orange", "yellow", "purple", "pink"]` and
  then `color = colors[i]` inside the loop. That replaces five
  if/elif lines with one.)
- Add **variation in petal count**. Some flowers have 8 petals;
  some have 6 or 12. Use a parameter for it.
- Build a **2D grid of flowers** using a *nested* for loop
  (outer loop varies y, inner loop varies x). A whole field.
- Add **clouds** to the sky using ovals (or just multiple circles
  side by side).

### What's next

Next week is your **milestone project + demo day**. You'll plan,
build, and demo your own Turtle drawing — your design, your
choices. Bring an idea (or two). After Phase 2, we move into
**Phase 3 — Python basics**, where Python becomes more general:
no more turtle, but lots more of what Python can do.
