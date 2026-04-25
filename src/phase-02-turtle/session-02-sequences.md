## Session 2: Telling the turtle what to do

*Phase 2 — Python with Turtle · Session 2 of 8*

### What we're learning today

Last week you typed your first Python code and made a turtle draw
a square. Today we'll learn more things the turtle can do — jump
to specific spots, face specific directions, draw circles, and
even write text. By the end, you'll be able to draw a small
*scene* with multiple parts: a sun, a house, a tree.

### You'll need to remember from last time

- Open **Thonny**, type code in the editor, **save** with a `.py`
  extension, click **Run** (or press F5).
- Every Python turtle program starts with `import turtle` and
  `t = turtle.Turtle()`.
- `t.forward(N)`, `t.right(N)`, `t.left(N)` for movement.
- `t.color("red")` and `t.pensize(N)` for style.
- `t.penup()` and `t.pendown()` for skipping without drawing.
- **Sequences run top to bottom.** Order matters in Python just
  like it did in Scratch.

---

### Part A: More ways to tell the turtle what to do

Open Thonny, start a new file, and save it as `scene.py`. Type
the standard opening:

```python
import turtle
t = turtle.Turtle()
```

You'll add to it.

#### Jumping to a specific spot: `goto`

In Scratch, you used `go to x: 0 y: 0` to send a sprite to a
specific position. Python turtle has the same idea. The stage has
a coordinate system: the middle is `(0, 0)`, x goes right
(positive) and left (negative), y goes up (positive) and down
(negative).

Add this to your file:

```python
t.penup()
t.goto(100, 50)
t.pendown()
t.forward(50)
```

Save. Run.

The turtle lifts its pen, jumps to the point (100, 50), drops the
pen, and walks 50 forward from there.

You'll use `goto` constantly when you have multiple things to draw
at different positions. Lift the pen, jump, drop the pen, draw.

#### Facing a specific direction: `setheading`

After `goto`, your turtle is *somewhere*, but which way is it
facing? It's facing wherever it was facing before. That's often not
what you want.

`setheading` makes the turtle face a specific direction:

- `t.setheading(0)` — face right (east)
- `t.setheading(90)` — face up (north)
- `t.setheading(180)` — face left (west)
- `t.setheading(270)` — face down (south)

So if you want to draw something that points up, you do:

```python
t.penup()
t.goto(0, 0)
t.setheading(90)   # face up
t.pendown()
t.forward(80)      # draw an upward line
```

Use `goto` *and* `setheading` together when you need to start
drawing in a known place at a known angle. Most multi-part drawings
need both.

#### Circles

The turtle can also draw circles. Add this:

```python
t.penup()
t.goto(-150, 100)
t.pendown()
t.color("yellow")
t.pensize(3)
t.circle(40)
```

Save. Run. A yellow circle of radius 40 appears in the upper-left
area.

`t.circle(40)` draws a complete circle. The circle starts where
the turtle currently is, and the turtle ends up back at that same
spot when the circle is done.

You can also draw a *partial* circle by giving a second argument
— how many degrees of arc to draw. `t.circle(40, 180)` draws a
half-circle.

#### Writing text

The turtle can write text too. Add:

```python
t.penup()
t.goto(0, 150)
t.pendown()
t.color("black")
t.write("My Scene", font=("Arial", 20, "normal"))
```

Save. Run. The text "My Scene" appears at the top of your window.

The `font=("Arial", 20, "normal")` part says what font and size
to use. Don't worry about the syntax for now — just know you can
change `20` to make the text bigger or smaller.

#### Build a scene together

Let's combine everything into a small scene. Start fresh — delete
your code and type this:

```python
import turtle
t = turtle.Turtle()

# the sun
t.penup()
t.goto(150, 100)
t.pendown()
t.color("yellow")
t.pensize(2)
t.circle(30)

# the house body (a square)
t.penup()
t.goto(-50, -50)
t.setheading(0)
t.pendown()
t.color("brown")
t.pensize(3)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
```

Save. Run.

You should see a yellow sun in the upper right and a brown square
(house) below it.

Notice the lines starting with `#` — those are **comments**.
Anything after a `#` on a line is ignored by Python. Comments are
how you leave notes for yourself (or other readers) explaining what
each part of your code does. We'll use them more as our programs
get bigger.

**Checkpoint:** *You have a scene with at least two distinct
elements (a sun and a house, or similar) drawn at different
positions on the stage.* **This is the natural stop point if class
is cut short.**

---

### Part B: Make it your scene

Now make this scene yours. The base goal is small; the stretch
adds to it; the extension lets your imagination loose.

#### Base goal

Add a **third element** to your scene. Pick one:

- **A roof** on top of the house. (Triangle. Use `goto` to position
  the turtle at one corner, `setheading` to face the right way,
  then three `forward`/`left` pairs to draw the triangle. Don't
  forget the third turn at the end so the turtle's heading is
  predictable for whatever comes next.)
- **A tree.** A brown rectangle for the trunk, a green circle for
  the leaves on top.
- **A second sun** of a different color, in another corner.
- **A title.** Use `t.write()` to put your name or a title at the
  top of the scene.

#### Stretch

Add two more elements, of any kind. Mountains in the background.
A second house. A road. A door on the existing house. Something
that makes the scene feel like a place.

Start using comments (`# something`) to label what each part of
your code is. It'll help you find things when the program gets
longer.

#### Extension

Tell a tiny visual story. Add elements that suggest something is
*happening* — a second person/animal, a path, smoke from the
house's chimney, weather (clouds, rain, sun rays). Use as many
turtle commands as you can.

Some commands you haven't formally seen but might want:

- `t.circle(radius, extent)` — partial circle
- `t.shape("turtle")` — make the cursor look like a little turtle
- `t.speed(0)` — turn the turtle drawing animation off (way faster)
- `t.hideturtle()` — hide the cursor entirely after drawing

Try them. The "If you finish early, just try things and see what
happens" energy is exactly the right mindset.

---

### Wrap-up

Before we leave, share with the room:

- What's in your scene?
- What was the trickiest part to position correctly?
- Did anyone discover a turtle command we didn't talk about?

You did something interesting today: you used **multiple parts** of
your code to build one thing. The sun, the house, the tree — each
a separate sequence of commands, all together making one drawing.
That's how every real program works. Big programs are made of
small pieces, each doing one thing.

Your scene is also probably long now — maybe 40 or 50 lines. Some
of those lines repeat. Like the four pairs of `forward(100)` /
`left(90)` to draw the square. Wouldn't it be great if you could
say "draw a square" instead of typing those eight lines?

You can. That's next week.

### If you missed this session

Open Thonny and start a new file. Save it as `scene.py`. Then:

1. Build the standard opening (`import turtle` and
   `t = turtle.Turtle()`).
2. Practice with `goto`: `t.penup()`, `t.goto(100, 50)`,
   `t.pendown()`, `t.forward(50)`. Run and see the turtle jump.
3. Practice with `setheading`: `t.setheading(90)`, `t.forward(50)`.
   The turtle now draws a line going up.
4. Practice with `circle`: `t.color("yellow")`, `t.circle(40)`.
   The turtle draws a yellow circle.
5. Now build the scene from Part A above (sun + house). Then add
   one more element (Part B base).

About 30-40 minutes of work. If you get stuck, ask your buddy at
the start of next class.

### Stretch and extension ideas

- Use `t.fillcolor("red")` and surround a shape with
  `t.begin_fill()` / `t.end_fill()` to fill it with color, not
  just outline.
- Use `t.bgcolor("skyblue")` to set the background color of the
  whole window.
- Use multiple turtles. After `import turtle`, do
  `t = turtle.Turtle()` and `s = turtle.Turtle()`. Now you have
  two turtles you can control independently. (Hint: this gets way
  more useful when we have loops next week.)

### What's next

Next week we finally get **loops** in Python. Remember when you
typed eight lines to draw a square last week, and your house this
week? Next week you'll do it in three. By the end of class, you'll
be drawing patterns that would take *hundreds* of lines by hand.
