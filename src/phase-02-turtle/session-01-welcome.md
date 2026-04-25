## Session 1: Welcome to Python — typing instead of dragging

*Phase 2 — Python with Turtle · Session 1 of 8*

### What we're learning today

You spent eight weeks learning how to think like a programmer using
Scratch. Today we move into a real programming language called
**Python** — the kind of language used by people who write apps,
games, and websites for a living. The blocks are gone. You'll be
*typing* code instead of dragging it. By the end of class, you'll
have typed your first Python program, watched a turtle draw on
your screen, and made (and fixed!) your very first error message.

### You'll need to remember from last time

- **Sequences** — code runs top to bottom. Order matters.
- **The peanut butter rule** — computers do exactly what you say,
  not what you mean. (This rule applies *more* to Python, not less.
  You'll see why.)
- That you finished Phase 1 and built your own game. You can do
  hard things.

---

### Part A: Meet Thonny and your first turtle

Open **Thonny** on your computer. It's already installed — look
for a friendly green icon (sometimes it looks like a snail). If
you can't find it, ask your buddy or Mr. Eric.

Thonny is what we'll use instead of Scratch. It's called an
**IDE** (which stands for Integrated Development Environment, but
nobody says that out loud). For now, it's the place where you'll
type your Python code.

#### A tour of Thonny

When Thonny opens, you'll see two main areas:

- **The editor** (the top half, big white area). This is where
  you type your code.
- **The shell** (the bottom half). This is where Python tells you
  things — what your program printed, what error it ran into,
  things like that.

At the top there's a row of buttons. The one we care about today
is the green **Run** button (or you can press the **F5** key on
your keyboard — same thing).

#### Type your first Python program

Click into the editor area at the top. Type this — exactly:

```python
import turtle
t = turtle.Turtle()
t.forward(100)
```

Three lines. Pay attention to the symbols — the parentheses, the
period after `t`, the period after `turtle`. Type them all. Type
them carefully.

Now save your file. Press **Ctrl-S** (or File → Save). Thonny
will ask where to save it and what to call it. Save it somewhere
you'll remember (the desktop is fine for now), and call it
**`first_turtle.py`**. The `.py` part is important — that's how
your computer knows it's a Python file.

Now click the green **Run** button (or press F5).

**A new window pops up** — it's mostly white, with a small
arrow-shape in the middle. That arrow is your turtle. Watch what
happens: the turtle moves forward 100 pixels and stops.

Congratulations. You just wrote and ran a Python program.

#### What just happened

Let's break those three lines down:

- `import turtle` — this tells Python: "I want to use the turtle
  toolbox." Python comes with lots of toolboxes; you have to ask
  for the ones you want. We just asked for the one that does
  drawing with a turtle.
- `t = turtle.Turtle()` — this creates a new turtle and gives it
  the name `t`. (You can name it anything you want, but `t` is
  short and quick to type. Some people name it `bob`. Some name
  it `george`. The turtle doesn't care.)
- `t.forward(100)` — this tells the turtle named `t` to move
  forward by 100 pixels. The number 100 is called an **argument**
  — it's the information you're passing to the command.

Compare that to Scratch:

| Scratch | Python |
|---|---|
| Drag a `move 10 steps` block | Type `t.forward(100)` |
| The cat moves | The turtle moves |

Same idea. Different way of telling the computer.

#### Make a typo on purpose

Now let's break it. Add a fourth line, but spell `forward` wrong:

```python
import turtle
t = turtle.Turtle()
t.forward(100)
t.forwerd(100)
```

Click Run.

The turtle does the first forward. Then it stops, and the **shell
at the bottom** turns red and shows you something like this:

```
AttributeError: 'Turtle' object has no attribute 'forwerd'
```

This is your first **error message**. Don't panic. Error messages
are *trying to help.* Read it carefully.

Translation: "I tried to find a thing called `forwerd` for the
turtle, but the turtle doesn't have anything called `forwerd`.
You probably meant something else."

Fix the typo (change `forwerd` back to `forward`) and run again.
The error goes away. The turtle moves twice.

> **The peanut butter rule strikes again.** You meant `forward`.
> You typed `forwerd`. The computer doesn't know what you meant
> — it only knows what you wrote. Welcome to typing precision.

#### Draw a square

Now let's make the turtle draw a real shape. Replace your code
with this:

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

Save (Ctrl-S). Run (F5).

The turtle walks forward 100, turns right 90 degrees, walks
forward 100, turns again, four times. **A square.**

Look familiar? In Session 3 of Phase 1, you made the cat draw a
square in Scratch with `repeat 4`. We don't have `repeat` yet in
Python — that's *next* week. For now, four times by hand.

**Checkpoint:** *You have a Python program saved as
`first_turtle.py` that draws a square when you press Run.* **This
is the natural stop point if class is cut short.**

---

### Part B: Colors, pen control, and shapes

Now let's make our drawings look better.

#### Colors

Add this line *before* you start drawing the square:

```python
t.color("red")
```

Save and run. The square is red.

Try other colors: `"blue"`, `"green"`, `"purple"`, `"orange"`,
`"pink"`, `"yellow"`, `"black"`. Anything you'd guess, Python
probably knows.

#### Thicker lines

Add this line too:

```python
t.pensize(5)
```

Now the lines are five pixels thick instead of one. Try `pensize(10)`
or `pensize(20)`.

#### Lifting the pen

Sometimes you want to move the turtle without drawing. Use these:

- `t.penup()` — lift the pen, no more drawing
- `t.pendown()` — drop the pen, drawing again

Try this — two squares side by side:

```python
import turtle
t = turtle.Turtle()
t.color("blue")
t.pensize(3)

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.penup()
t.forward(150)
t.pendown()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
```

Two squares with a gap between them. The middle three lines
(penup, forward 150, pendown) move the turtle without drawing.

#### Try this on your own

Pick one of these:

- **Base goal:** Draw a triangle. (A triangle is three sides. The
  turn at each corner is *not* 90 degrees — figure out what it
  should be. Hint: remember the polygon pattern from Session 3 of
  Phase 1.)
- **Stretch:** Draw your initials. Each letter as a few lines.
  Use `penup()` and `pendown()` to skip between letters.
- **Extension:** Draw a simple house. A square for the body, a
  triangle for the roof on top. Use color.

---

### Wrap-up

Before we leave, let's share:

- What was different from Scratch?
- What was harder?
- What was easier?
- Did you get any error messages? What were they?

You did something today that's a big deal. **You typed real
Python code, ran it, made a typo, fixed it, and made the computer
draw something.** That's the entire programming workflow. Every
programmer in the world does that exact loop, every day.

The hard part wasn't the typing. The hard part was getting used
to *being precise* — every character matters, every parenthesis
matters, every period matters. That precision will get easier
fast.

### If you missed this session

Open Thonny on your computer. Type these three lines exactly:

```python
import turtle
t = turtle.Turtle()
t.forward(100)
```

Save the file as `first_turtle.py`. Click the green Run button or
press F5. A window opens; the turtle moves.

Now extend it to draw a square. You'll need four `t.forward(100)`
lines and four `t.right(90)` lines, alternating.

Then add `t.color("red")` and `t.pensize(3)` near the top to make
the square colorful and thick. Save, run.

About 30 minutes of work. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- Try `t.left(90)` instead of `t.right(90)` and see what happens.
- Try `t.backward(50)` to walk the turtle backward.
- Try `t.shape("turtle")` (right after the `t = ...` line). The
  arrow becomes an actual little turtle shape. Then try
  `"square"`, `"circle"`, `"triangle"`, `"arrow"`.
- Try `t.speed(1)` (slow) or `t.speed(10)` (fast). Where does the
  speed matter? Where doesn't it?

### What's next

Next week we'll learn about **all the things the turtle can do**
— moving in different ways, going to specific positions, drawing
patterns. By the end of next week's class, your drawings will
look way fancier.
