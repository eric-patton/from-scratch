## Session 5: Conditionals — making decisions

*Phase 1 — Scratch · Session 5 of 9*

### What we're learning today

So far your programs have always done the same thing every time
they ran. Today we'll learn how to make a program *check* something
about the world — "is the cat touching the apple?" — and *decide*
what to do based on the answer. This is called a **conditional**,
and combined with everything you already know, it's enough to build
your first real game.

### You'll need to remember from last time

- **Events** — `when [key] pressed`, `when this sprite clicked`.
- **Each sprite has its own scripts.**
- **Sequences** run top to bottom; **loops** repeat.
- The arrow-key cat you built last week (or its equivalent in the
  catch-up exercise).

---

### Part A: "If something, then do this"

Open Scratch and start a new project.

A **conditional** is the programming idea of "check first, then
decide." In English you use them all the time: "if it's raining,
take an umbrella." The "check" is *is it raining?* The "decision" is
*take an umbrella, or don't.*

Scratch has a block for this. It's in the **Control** category
(orange):

```
if < > then
   <empty>
```

Like the `repeat` block, it has a mouth. Things go *inside* the
mouth, and they only run if the *condition* (the thing in the
diamond at the top) is true.

The diamond shape at the top of the `if` block is a slot for a
**condition** — a question Scratch can answer with yes or no. To
fill the slot, you need a block that's *also* shaped like a diamond.

Take a look at the **Sensing** category (light blue). Notice that
some blocks there are diamond-shaped:

- `<key [space] pressed?>` — answers "is the space key being pressed
  right now?"
- `<touching [Sprite1]?>` — answers "is this sprite touching that
  other sprite?"
- `<touching color []?>` — answers "is this sprite touching that
  color?"
- `<mouse down?>` — answers "is the mouse button being held?"

Each of those answers yes-or-no. You drop one into the diamond slot
of an `if` block, and the inside runs only when the answer is yes.

#### Smooth movement (a callback to last week)

Remember how your cat felt a little choppy when you held down the
arrow key? Conditionals fix that.

Last week you built four scripts, one per arrow key. This week
we'll build *one* script, with conditionals inside a forever loop.

Add a cat to your project (it should be there by default). Build
this:

```
when [green flag] clicked
forever
   if <key [right arrow] pressed?> then
      change x by 5
   if <key [left arrow] pressed?> then
      change x by -5
   if <key [up arrow] pressed?> then
      change y by 5
   if <key [down arrow] pressed?> then
      change y by -5
```

Four `if` blocks, all stacked inside a `forever` loop, all under
one green flag.

The `forever` block (Control, orange) is the loop equivalent of
"keep doing this until I stop you." Inside it, every fraction of a
second, Scratch checks all four `if` blocks. If an arrow key is
being held down, the corresponding `change` block runs — that
fraction of a second, every fraction of a second, while the key is
held.

Click the green flag. Hold an arrow key. The cat moves *smoothly*,
because every fraction of a second the program is asking "is this
key pressed?" and acting on the answer.

That's the same arrow-key movement you built last week, but now it
feels right. That's the power of conditionals plus loops.

**Checkpoint:** *Your cat moves smoothly with the arrow keys when
you hold them down, using a single `forever` loop with four `if`
blocks inside.* **This is the natural stop point if class is cut
short.**

---

### Part B: Catch the apple

Now we'll build something that actually feels like a game.

#### What you're building

An apple sprite falls from the top of the stage. Your cat moves
along the bottom (using your smooth arrow-key movement from Part
A). When the cat catches the apple, the apple says "Yum!" and goes
back to the top to fall again.

It's a tiny game. You'll know if you can catch the apple or not.
That's the whole point.

#### Set up the stage

You already have your cat with smooth arrow-key movement. Two small
adjustments:

- Move the cat to the bottom of the stage. Add `go to x: 0 y: -130`
  inside the `when green flag clicked` script (above the forever
  loop). Now the cat starts near the bottom every time.
- For this game, the cat only needs to move left and right. You can
  delete the `up arrow` and `down arrow` `if` blocks if you want, or
  leave them — your choice.

#### Add the apple

Click the **Choose a Sprite** button (bottom right). In the search
box, type "apple." Pick any apple-looking sprite. (Don't see one?
Any small sprite works. Pick a fruit, a ball, anything that can
"fall.")

Make sure you're now editing the **apple's** scripts (click the
apple in the bottom-right panel; the script area should be empty).

Build this on the apple:

```
when [green flag] clicked
go to x: pick random -200 to 200 y: 180
forever
   change y by -3
   if <touching [Sprite1] ?> then
      say [Yum!] for 1 seconds
      go to x: pick random -200 to 200 y: 180
```

A few things to notice in this script:

- `pick random -200 to 200` is in the **Operators** category (the
  green blocks). It's another diamond-shaped block, but it goes
  into the `x` slot of `go to` because that slot accepts numbers.
  It picks a random x-coordinate each time, so the apple appears
  somewhere different.
- `Sprite1` is the cat's name. Scratch may have renamed it; if your
  cat is called something else (like "Cat"), pick *that* name from
  the dropdown.
- The script flow: the apple starts at a random spot at the top
  (y = 180 is near the top), then forever it falls (changes y by
  -3), and on every fall it checks "am I touching the cat?" If yes,
  it says "Yum!" and resets to the top.

Click the green flag. The apple falls. Move the cat with the arrow
keys. Catch it.

You just built a game.

That's the **base goal.** If you got the apple to fall, the cat to
catch it, and the apple to reset — you're done for today.

#### Stretch goal

What happens when the apple reaches the bottom of the stage and the
cat *didn't* catch it? Right now: it just keeps falling forever and
disappears off screen. That's not great game design.

Add a "missed!" condition. Inside the forever loop, after the
existing `if`, add another:

```
if <(y position) < -180> then
   say [Missed!] for 1 seconds
   go to x: pick random -200 to 200 y: 180
```

`y position` is in the Sensing category (it's not a diamond — it's a
rounded block, because it returns a number, not a yes/no answer).
The `<>` comparison is in the Operators category — look for `<` in
the green blocks.

Now if the apple falls past the bottom of the stage (y < -180), it
says "Missed!" and resets to the top. The game has a real
"miss" condition.

#### Extension

Add a *second* falling object. A different fruit, a coin, anything.
Make it fall faster (or slower) than the apple. The cat now has to
catch both, possibly making choices about which to chase.

To add it: the new sprite is just another sprite. Build the same
"forever fall + if touching cat then yum + reset" script on it. The
only thing you change is the speed (`change y by -5` instead of
`-3`, for instance).

Two falling sprites at different speeds is twice as hard. Your buddy
can play it.

---

### Wrap-up

Before we leave, share with the room:

- Did anyone catch the apple ten times in a row? Five?
- What was the trickiest part of getting the apple to reset
  correctly?
- For the kids who did the stretch — what made you decide what
  number to use for "the bottom of the stage"?

You did something bigger today than just learning conditionals. You
combined **events** (arrow keys), **loops** (forever), and
**conditionals** (`if touching`) to build something that looks and
feels like a real game. Every game you'll ever play uses these three
ideas, just with more sprites and more conditions.

You're not even halfway through Phase 1, and you already have
everything you need to build games.

### If you missed this session

Open Scratch and start a new project. Then:

1. Build the smooth arrow-key cat from Part A (one `forever` loop,
   four `if` blocks). About 10 minutes.
2. Add an apple sprite (or any sprite that can "fall").
3. Build the apple's falling-and-resetting script described in Part
   B above. About 15 minutes.
4. Click the green flag. Move the cat. Try to catch the apple.

When you come next week, you'll be ready. If anything's confusing,
ask your buddy at the start of class.

### Stretch and extension ideas

- Use `if/else` (Control category — like `if`, but with two
  mouths). Lets you do "if X then this, otherwise that" in one
  block. More elegant than two `if` blocks for the same situation.
- Make the apple change costume when caught, then change back when
  it resets. (Look at the apple's Costumes tab; try `next costume`.)
- Use `start sound` (Sound category) to play a sound when the cat
  catches the apple.
- Add a `wait 0.05 seconds` block at the end of the apple's forever
  loop. What changes? Why?

### What's next

Next week we'll learn about **variables** — how to make Scratch
remember things, like a score. That'll let you finally turn your
catch-the-apple game into a real game with points.
