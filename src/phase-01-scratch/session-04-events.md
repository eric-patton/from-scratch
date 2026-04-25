## Session 4: Events — making things happen when...

*Phase 1 — Scratch · Session 4 of 9*

### What we're learning today

Up until now, all your programs started one way: you clicked the
green flag. Today we'll learn how to make sprites react to *other*
things — a key being pressed, a sprite being clicked, all kinds of
moments while your program is running. These are called **events**,
and they're how you go from "the program does its thing" to "I'm
controlling the program in real time."

### You'll need to remember from last time

- **Sequences** — code runs in order, top to bottom.
- **The `repeat` loop** — does the inside N times.
- **Each sprite has its own scripts.** When you switch sprites in
  the bottom-right panel, you see *that* sprite's scripts.
- **The green flag is one kind of starter block.** There are others.

---

### Part A: More than one way to start

Open Scratch and start a new project.

So far, every program you've written starts with the same block:

```
when [green flag] clicked
```

That block is in a category called **Events** (yellow). It's not the
only block in there. Take a look at the Events category. You'll see
several other "when X happens" blocks. They all work the same way:
when the thing happens, the script underneath runs.

The two we'll use today:

- `when [space] key pressed` — runs when you press the space key.
  (You can change which key it watches for by clicking the dropdown.)
- `when this sprite clicked` — runs when you click on the sprite
  with your mouse.

A sprite can have **as many scripts as you want.** Each one has its
own starter block, and each one runs independently when its event
fires.

#### Build your first multi-event sprite

Try this. Snap together three separate scripts on the cat:

```
when [green flag] clicked
go to x: 0 y: 0
```

```
when [space] key pressed
say [Hi!] for 1 seconds
```

```
when this sprite clicked
turn ↻ 30 degrees
```

These are three separate stacks of blocks, not one big stack. Don't
try to snap them together. They each have their own starter and
they live separately in your script area.

Now click the green flag. The cat goes to the middle.

Press the spacebar. The cat says "Hi!"

Click on the cat. It turns 30 degrees.

That's three different events triggering three different behaviors,
all on one sprite.

#### Cat that walks with the arrow keys

Now let's make the cat respond to the arrow keys. We want:

- **Right arrow:** cat moves right
- **Left arrow:** cat moves left
- **Up arrow:** cat moves up
- **Down arrow:** cat moves down

That's four scripts. Each one is short:

```
when [right arrow] key pressed
change x by 10
```

```
when [left arrow] key pressed
change x by -10
```

```
when [up arrow] key pressed
change y by 10
```

```
when [down arrow] key pressed
change y by -10
```

`change x by 10` (Motion category) shifts the sprite right by 10
units. `change x by -10` shifts it left. Same idea for y, except y
is up/down.

Build all four scripts. Then press the arrow keys.

Your cat now walks around the stage, controlled by you. You're not
clicking blocks anymore — you're playing a tiny game with a cat you
just programmed.

If the movement feels a little choppy when you hold an arrow key
down — that's because the keyboard takes a moment before it starts
"repeating" the keypress. We'll fix this in a later session. For now,
quick taps work fine.

**Checkpoint:** *You have a sprite with at least three separate
scripts triggered by three different events (one of which is a
keyboard event), and they all work.* **This is the natural stop
point if class is cut short.**

---

### Part B: Two players, one stage

Now let's add a second sprite that responds to its *own* keys.

#### Add a second sprite

Look at the bottom-right corner of the Scratch window. Click the
**Choose a Sprite** button (the cat-with-plus icon). Pick anything
— a dog, a person, a robot. We'll use it as a second player.

When you add the new sprite, the **scripts area in the middle of
the screen switches to that sprite's scripts** — which are empty
right now. Notice the cat's scripts are still there; you just
don't see them while you're looking at the dog. To switch back,
click the cat in the bottom-right panel.

#### Give your second sprite WASD movement

While looking at the second sprite, build four scripts that mirror
the cat's, but using **W, A, S, D** instead of arrow keys:

- `when [w] key pressed` → `change y by 10`
- `when [a] key pressed` → `change x by -10`
- `when [s] key pressed` → `change y by -10`
- `when [d] key pressed` → `change x by 10`

Click the green flag (or just start pressing keys).

Now you have **two sprites controlled independently by two
keyboards-worth of keys.** Try it with a buddy: one of you uses
arrow keys, the other uses WASD. You're both on the same stage at
the same time.

This is the **base goal.** If you got that working, you're done for
today.

#### Stretch goal

Make each sprite do something *interesting* when clicked. The cat
might say something. The other sprite might change costume (look at
the **Costumes** tab at the top of the Scratch window — many sprites
come with multiple costumes).

#### Extension

Build a third sprite — a "ball" or "object" — that doesn't move on
its own but does something when clicked. For example: when clicked,
it teleports to a random spot using `go to x: <pick random> y: <pick
random>` (you'll find `pick random` in the Operators category, the
green blocks).

Now your two players can race to click the ball after it teleports.
A tiny game.

---

### Wrap-up

Before we leave, share with the room:

- What's something cool your sprites do that you didn't expect?
- If you and your buddy played the two-player WASD/arrows version,
  what was harder than you thought it would be?
- If you could add one *more* event to your sprite, what would it
  do?

You learned something important today that's not just about Scratch:
**a program can do many things in response to many different
triggers, all at once.** Real apps work this way. When you click
something on a website, that's an event. When you press a key in a
game, that's an event. You now know what's happening underneath.

### If you missed this session

Open Scratch and start a new project. Then:

1. Look at the **Events** category (yellow blocks). Drag out a
   `when [space] key pressed` block.
2. Snap a `say [Hi!] for 1 seconds` block under it. Press the
   spacebar to test.
3. Drag out a `when this sprite clicked` block. Snap a `turn 15
   degrees` block under it. Click the cat to test.
4. Now build the four arrow-key movement scripts described in Part A
   above (right, left, up, down). About 10 minutes.
5. Then try Part B — add a second sprite, give it WASD movement.

When you come next week, you'll be ready. If anything's confusing,
ask your buddy at the start of class.

### Stretch and extension ideas

- Use `when [any] key pressed` to make a sprite react to *any* key.
  Useful for "press any key to start" effects.
- Use `start sound` (Sound category) to play a sound when an event
  fires. Several sprites come with sound effects built in.
- Add a backdrop to your scene (bottom-right "Choose a Backdrop"
  button). Doesn't change behavior, but makes everything look like
  it belongs somewhere.

### What's next

Next week we'll learn about **conditionals** — how to make your
sprites *decide* what to do based on what's happening, like
"bounce if you hit the wall" or "say 'caught!' if you touch the
apple."
