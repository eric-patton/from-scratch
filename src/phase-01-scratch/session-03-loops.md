## Session 3: Loops — doing things over and over

*Phase 1 — Scratch · Session 3 of 9*

### What we're learning today

Today you'll learn one of the most important ideas in all of
programming: how to tell the computer to do something many times,
without writing the same instruction over and over. This is called a
**loop**. By the end of class, you'll have used a loop to make your
cat draw a perfect square — and then you'll see how a tiny change to
the loop turns the square into a triangle, a hexagon, or a flower.

### You'll need to remember from last time

- **Sequences** — code runs in order, top to bottom.
- **The green flag** starts your program.
- The blocks `move`, `turn`, `wait`, and `go to x: y:`.
- **Order matters.**

---

### Part A: Why loops exist

Open Scratch and start a new project. Add a `when green flag
clicked` block, like always.

Now imagine you wanted to make the cat march in a straight line —
take ten little steps, one after another. With what you know so far,
you'd have to drag ten `move 10 steps` blocks and snap them all
together.

Try it. Drag ten of them. It's tedious. Ten is annoying. *A
hundred* would be ridiculous. *A thousand* would be impossible to
build by hand.

Programmers ran into this problem about three seconds after they
invented programming. The solution they came up with is the **loop**:
a way to say "do this a bunch of times" without writing it out a
bunch of times.

#### The `repeat` block

Delete the ten `move` blocks (right-click → delete, or drag them off
to the left).

Now go to the **Control** category (orange blocks). Find this one:

```
repeat [10]
   <empty>
```

It's shaped differently from the blocks you've used so far — it has
a **mouth** in the middle. Blocks go *inside* the mouth, and they'll
run as many times as the number you put in the top.

Snap a `move 10 steps` block inside the mouth, and snap the whole
`repeat` block under your `when green flag clicked` block. You should
end up with this:

```
when [green flag] clicked
repeat [10]
   move 10 steps
```

Click the green flag. The cat takes ten steps in quick succession.

That's a loop. The `move 10 steps` block ran ten times.

#### Try changing the number

Click the `10` in the `repeat` block and change it to `100`. Click
the green flag. The cat zooms across the stage.

Change it to `3`. Three little steps.

Change it to `1`. Just one step. (A loop that runs once is silly,
but the computer will obey.)

Change it to `0`. The cat doesn't move. The loop runs zero times,
which is allowed.

The number controls how many times the inside runs. That's the
whole concept.

#### Multiple blocks inside a loop

You can put more than one block inside the mouth. Try this:

```
when [green flag] clicked
repeat [4]
   move 50 steps
   turn ↻ 90 degrees
```

Click the green flag.

Watch carefully. The cat moves 50 steps, turns 90 degrees, moves 50
steps, turns 90 degrees… four times.

What shape did the cat just walk?

A square.

You just told the computer to draw a square in three lines of code.
Without the loop, you would have written the same two blocks four
times — *eight* blocks instead of three. With a loop that ran 100
times, that would be 200 blocks instead of 3.

This is why loops are one of the most important ideas in
programming.

**Checkpoint:** *Every student should have built a `repeat` loop
with at least one block inside it and clicked the green flag to see
it run.* **This is the natural stop point if class is cut short.**

---

### Part B: Drawing with loops

Now we'll do something more visually satisfying than walking the
cat in invisible squares. We'll have the cat actually *draw* the
square as it walks.

#### Adding the Pen extension

Scratch has extra block categories called **extensions** that
aren't shown by default. We need one called **Pen** to draw.

Look at the bottom-left corner of the Scratch window. There's a blue
square with a `+` icon — the **"Add Extension"** button. Click it.

A list of extensions appears. Find the one called **Pen** and click
it.

A new category called **Pen** (green) now appears in your blocks
panel. You'll see blocks like `pen down`, `pen up`, `set pen color`,
`erase all`, and a few others.

The way `pen` works: when `pen down` is active, the sprite leaves a
trail behind it as it moves. When `pen up`, no trail.

#### Draw a square

Modify your loop program so it looks like this:

```
when [green flag] clicked
erase all
go to x: 0 y: 0
pen down
repeat [4]
   move 100 steps
   turn ↻ 90 degrees
pen up
```

Three new blocks at the top — `erase all` (so old drawings don't
stick around), `go to x: 0 y: 0` (so the cat starts in the middle),
and `pen down` (so the trail starts). And one new block at the end —
`pen up` (so we don't keep drawing if we add more code later).

Click the green flag. Watch the cat draw a square.

That, right there, is the moment programming starts to feel like a
superpower.

#### Try the stretch

The base goal is the square above. If that works:

- **Stretch:** Change the `repeat` to `3` and the `turn` to `120
  degrees`. What shape do you get? Now try `5` and `72`. Now try `6`
  and `60`. There's a pattern. Can you figure it out?
  - *Hint:* Look at the two numbers and how they relate. (If you
    want a really sneaky hint: 4 × 90 = 360. 3 × 120 = 360. 5 × 72 =
    360. The total turning is always 360 degrees, because that's a
    full trip around.)

#### Or the extension

If you finished stretch and want more:

- **Extension:** Use a *nested* loop — a loop inside a loop. The
  inner loop draws a shape; the outer loop turns a little and draws
  it again. Something like this:
  ```
  repeat [12]
     repeat [4]
        move 50 steps
        turn ↻ 90 degrees
     turn ↻ 30 degrees
  ```
  Click the green flag. You should get a beautiful flower-of-squares
  pattern.

### Wrap-up

Before we leave, share with the room:

- What's the coolest shape you got the cat to draw?
- Did you try changing numbers and discover something unexpected?
- If you wanted to draw a 100-sided shape, what would the two
  numbers in your loop be? *(You don't have to actually try it
  unless you want to. But predict.)*

You've now used your first programming concept that *isn't* in the
peanut butter rule. Loops are the first big idea where the computer
does something you didn't tell it to do explicitly — it does the
inside part many times because *you set it up to.* That's a real
shift.

### If you missed this session

Open Scratch and start a new project. Then:

1. Add a `when green flag clicked` block.
2. From the **Control** category, drag out a `repeat 10` block.
   Snap a `move 10 steps` block inside its mouth. Snap the whole
   thing under the green flag. Click the green flag. The cat moves
   ten times in a row.
3. Change the inside to `move 50 steps` *and* `turn 90 degrees`,
   and change the repeat number to `4`. Click the green flag. The
   cat walks a square.
4. Click the **Add Extension** button (bottom-left). Pick **Pen**.
5. Add `erase all`, `go to x: 0 y: 0`, and `pen down` to the top of
   your program (in that order). Click the green flag. The cat draws
   a square.

Then try Part B's stretch goal: change the numbers to draw a
triangle, a pentagon, a hexagon. About 25 minutes of work.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Use `set pen color to` (Pen category) to change the color of your
  drawing.
- Use `set pen size to` to make the lines thicker.
- Make a *spiral* by combining `move` and `turn` *outside* a loop:
  ```
  repeat [50]
     move 5 steps
     turn ↻ 10 degrees
  ```
  Each time around the loop, the cat takes a bigger and bigger swing.
  Actually no — wait, did it? Look carefully. The loop body is the
  same every iteration. So why does it look like a spiral and not a
  circle?
- Try using a `forever` block instead of `repeat`. (Hint: you'll
  need the red stop sign to make it stop.)

### What's next

Next week we'll learn about **events** — how to make sprites react
to keyboard presses, mouse clicks, and other things that happen
*while* a program is running, not just when it starts.
