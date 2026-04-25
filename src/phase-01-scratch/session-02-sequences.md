## Session 2: Sequences and the stage

*Phase 1 — Scratch · Session 2 of 9*

### What we're learning today

Last week you played around in Scratch and got the cat to do silly
things. Today we'll do the same kinds of things, but *on purpose*.
You'll learn how to start a program with the green flag, how to make
a sprite do several things in a row, and what happens when the order
of those things is wrong. By the end you'll have built a tiny
scripted scene — your first real program.

### You'll need to remember from last time

- **Computers do exactly what you say.** No guessing. (The peanut
  butter rule.)
- **Scratch is on your computer** and you know how to open it.
- **Blocks snap together like LEGO** in the script area.
- **The green flag runs your program. The red stop sign halts it.**

---

### Part A: Telling the cat what to do, in order

Open Scratch and start a new project. (File menu → New, or just
restart Scratch.)

#### What "in order" means

Last week you clicked individual blocks and watched the cat react.
That works, but it's not really programming yet — *you* were the one
deciding when each block ran. A real program does several things in
order, all on its own, after you start it once.

The way you start a program in Scratch is the **green flag**. You've
already seen it — it's the green triangle at the top of the stage.
We need a block that says "when the green flag is clicked, do this."
That block lives in the **Events** category (yellow blocks).

Drag this one out:

```
when [green flag] clicked
```

It looks a little different from other blocks — it has a curved top
and no notch above it, because nothing snaps *on top* of it. It's a
*starting* block. Things snap *below* it.

#### Build a sequence

Snap these blocks together, in this order, under the green flag:

```
when [green flag] clicked
move 50 steps
wait 1 seconds
turn ↻ 90 degrees
move 50 steps
```

The `wait 1 seconds` block is in the **Control** category (orange).
The others you've already met.

Now click the green flag at the top of the stage.

The cat moves 50 steps, pauses for one second, turns 90 degrees, and
moves 50 more steps. Every time. In that order. Click the green flag
again and it does the same thing again from wherever it ended up.

That's a **sequence** — a list of instructions that runs from top to
bottom. It's the most basic kind of program.

#### Now break it

Programmers learn fastest by breaking things on purpose, so let's
break this on purpose.

Drag the `wait 1 seconds` block to the *top* of the stack, right
under the green-flag block, so the order is now:

```
when [green flag] clicked
wait 1 seconds
move 50 steps
turn ↻ 90 degrees
move 50 steps
```

Click the green flag. What happened? The cat sits still for one
second, then does the rest. Same blocks. Different order. Different
behavior.

Try it again with the `turn` block at the very end, after both
moves. Now the cat moves in a straight line and only turns when
it's done. Same blocks. Different order. Different behavior.

This is the second-most-important rule of programming, after the
peanut butter one:

> **Order matters. The same instructions in a different order make a
> different program.**

#### Reset the cat

If your cat has wandered to a weird spot or is facing a weird way,
that's fine — but it's annoying when you're trying to test your
program. Two ways to reset:

- Click and drag the cat back to the middle of the stage with your
  mouse.
- Add a `go to x: 0 y: 0` block (Motion, blue) at the very top of
  your program, right under the green flag. Now every time you click
  the green flag, the cat starts from the middle.

The second one is what programmers usually do: make the program reset
itself. We'll come back to this idea a lot.

**Checkpoint:** *You should have a program that starts with a green
flag, includes at least three blocks in a row, and behaves
differently when you change the order of the blocks.* **This is the
natural stop point if class is cut short — Part B builds on this but
isn't required.**

---

### Part B: A scripted scene

Now let's build something that feels like a tiny piece of a story.

#### What you're building

A short scene where the cat enters from the left side of the stage,
walks to the middle, says "Hello!", waits, and walks off to the
right side.

That's the **base goal.** It's a little harder than what we did in
Part A because there are more steps and you have to think about
positions and timing.

#### How to think about it

Before you start clicking, talk through it in plain words. What does
the cat need to do, in order?

1. Start at the left side of the stage.
2. Walk to the middle.
3. Say "Hello!" for two seconds.
4. Wait a moment.
5. Walk off to the right.

That's a sequence. Now you need to find the right blocks.

- **Start at the left side:** `go to x: -200 y: 0` (Motion). The
  stage is about 480 wide, so x = -200 is near the left.
- **Walk to the middle:** several `move 10 steps` blocks, or one
  `glide 2 secs to x: 0 y: 0` block (also Motion). The `glide`
  version is smoother — try both and see which you like.
- **Say "Hello!" for two seconds:** `say [Hello!] for 2 seconds`
  (Looks, purple).
- **Wait a moment:** `wait 1 seconds` (Control).
- **Walk off to the right:** `glide 2 secs to x: 240 y: 0`.

Snap them all under your `when green flag clicked` block. Click the
flag. Watch your scene.

#### Try the stretch goal

If your base scene works and you have time:

- **Stretch:** Add a second sprite — a person, a dog, anything from
  the sprite library. Have *them* say something back to the cat
  before the cat walks off. (Tricky part: you'll need to give the
  second sprite its own `when green flag clicked` block, because
  every sprite has its own scripts.)

#### Or the extension

If you finish stretch and still have time:

- **Extension:** Make the cat do a short dance in the middle of the
  scene. A dance is just a sequence — turn a little, move a little,
  turn back, move back, in some pattern that looks like dancing.

Don't worry about making it perfect. "Looks like dancing" is the
goal, not "actual dance choreography."

---

### Wrap-up

Before we leave, let's share:

- What did your scene do?
- Did anything happen that you didn't expect?
- Did you have to change the order of blocks to get something to
  work?

**Done for today** doesn't mean **done with the topic.** Sequences
will come back every week from here on out. You'll get plenty more
practice.

### If you missed this session

Open Scratch on your computer. Start a new project. Then:

1. Drag a `when green flag clicked` block (yellow, Events) into the
   script area.
2. Snap a `move 50 steps` block underneath it.
3. Snap a `wait 1 seconds` block underneath that.
4. Snap a `turn 90 degrees` block underneath that.
5. Snap one more `move 50 steps` block underneath.
6. Click the green flag. Watch the cat.
7. Now drag the `wait` block to a different position in the stack.
   Click the green flag. Watch what changes.

Then try the scripted scene from Part B above. The base goal — cat
enters, walks to middle, says hello, walks off — is the catch-up
exercise. About 20 minutes of work.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Use `glide` blocks instead of `move` blocks for smoother motion.
- Add a backdrop (look at the bottom-right corner, "Choose a
  Backdrop" button). Set the scene somewhere — a forest, a city,
  outer space.
- Make the cat change costume at some point in the scene. Sprites
  often have multiple costumes built in. Look at the **Costumes**
  tab at the top of the Scratch window.

### What's next

Next week we'll learn about **loops** — how to make the cat do
something twenty times without dragging twenty blocks.
