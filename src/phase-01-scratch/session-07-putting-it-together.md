## Session 7: Putting it together — a small game

*Phase 1 — Scratch · Session 7 of 9*

### What we're learning today

You've now learned every basic idea you need to build games:
sequences, loops, events, conditionals, sensing, and variables.
Today we'll *combine all of them* into one small game called
**Apples and Rocks** — catch the falling apples for points, but
dodge the falling rocks or it's game over. By the end, you'll have
a complete, playable game with a score and a real losing condition.

### You'll need to remember from last time

- **Variables** — `set`, `change`, `(read)`, displayed on stage.
- **The `if` block** + **sensing** for collision detection.
- **Forever loops** for things that keep happening.
- **Events** for arrow-key control.
- **Multiple sprites with their own scripts.**

That's basically the whole curriculum so far. Today is the test:
can you put it all together?

---

### Part A: Build the basic game (apples falling, score going up)

Open Scratch and start a new project. (Don't open last week's —
we'll build the whole game from scratch so you remember every
piece.)

This first half is essentially the catch-the-apple game from
Sessions 5 and 6, rebuilt cleanly in one go. If you've kept up,
this should feel like review. That's the point — you're proving to
yourself that you can build this from memory.

#### Set up the cat

Build this on the cat:

```
when [green flag] clicked
go to x: 0 y: -130
set [score] to 0
forever
   if <key [right arrow] pressed?> then
      change x by 7
   if <key [left arrow] pressed?> then
      change x by -7
```

(Make a `score` variable first if you haven't — Variables category
→ Make a Variable → name it `score` → OK.)

The cat sits at the bottom of the stage and slides left/right with
the arrow keys. Score resets to 0 on green flag.

#### Add the apple

Click **Choose a Sprite** (bottom right). Search for "apple" and
add one (or any small fruit/food sprite).

Switch to the apple's scripts (click the apple in the sprite list).
Build:

```
when [green flag] clicked
go to x: pick random -200 to 200 y: 180
forever
   change y by -3
   if <touching [Sprite1] ?> then
      change [score] by 1
      go to x: pick random -200 to 200 y: 180
   if <(y position) < -180> then
      go to x: pick random -200 to 200 y: 180
```

(Replace `Sprite1` with whatever your cat is named in the dropdown.
Often it's `Cat` or `Sprite1`.)

The apple falls, gives you a point if the cat catches it, resets to
the top either way (catch or miss).

Click the green flag. Move the cat. Catch some apples. Watch the
score go up.

This is the **base game** — same as before, just rebuilt cleanly.

**Checkpoint:** *You have a working catch-the-apple game with a
visible score that increases when the cat catches apples.* **This
is the natural stop point if class is cut short — Part B adds the
hazard mechanic but isn't required.**

---

### Part B: Add the rock (game over!)

Now we'll make this a real game by adding **risk.** Right now you
can just stand still and you don't lose anything. Boring. Time to
add a falling rock that ends the game if you touch it.

#### Add the rock sprite

Click **Choose a Sprite** again. Search for "rock" — there's a Rocks
sprite in the library. (Or pick anything that looks like something
you wouldn't want to touch — a bug, a skull, a "Block.")

Switch to the rock's scripts. Build:

```
when [green flag] clicked
go to x: pick random -200 to 200 y: 180
forever
   change y by -3
   if <touching [Sprite1] ?> then
      say [Game Over!] for 2 seconds
      stop [all]
   if <(y position) < -180> then
      go to x: pick random -200 to 200 y: 180
```

The rock falls just like the apple, but:

- If it touches the cat: say "Game Over!" for 2 seconds, then `stop
  [all]` (Control category) — this freezes the entire program.
- If it falls off the bottom: reset to top with new random x. (No
  penalty for letting a rock pass — that's actually what you
  *want* to happen.)

Click the green flag. Move the cat. Catch apples. **Dodge the rock.**

When the rock catches you, the cat says "Game Over!" and everything
freezes. Your final score sits on the screen as your record.

You just built a game with a real losing condition. Welcome to
actual game design.

That's the **base goal for today.** If your apples-and-rocks game
runs and ends correctly, you're done.

#### Stretch goal

Right now the apple and the rock fall at the same speed. Make the
rock slightly *faster* than the apple to ramp up the challenge:

In the rock's forever loop, change `change y by -3` to `change y
by -4` or `-5`. Now the rock is harder to dodge.

Then make a *second* apple sprite (right-click the apple in the
sprite list → duplicate). Two apples falling at once means more
points but also more places to be at the wrong moment.

#### Extension

Add a "best" score variable that survives across plays in the same
session. Add to the cat's scripts:

```
when [space] key pressed
if <(score) > (best)> then
   set [best] to (score)
```

(You'll need to make a `best` variable first.)

Now: when you press space at the end of a game (after game over),
your score gets compared to `best`, and `best` updates if you beat
it. Across multiple games, you can keep trying to beat your own
record. Press the green flag to start over each time.

For an even bigger challenge: what if score went DOWN by 1 each
time the apple falls without being caught? Add `change [score] by
-1` inside the apple's `(y position) < -180` block. Now you can
have a *negative* score, and missing apples is genuinely costly.

---

### Wrap-up

Before we leave, a few things to share:

- What was the highest score anyone got before the rock caught
  them?
- Did the rock-faster-than-apple stretch make the game feel
  meaningfully different?
- For the kids who did the "best" extension — does adding a high
  score change how you play?
- **Did anything break in surprising ways while you were building
  it?** This is the most important question. Programmers spend
  most of their time fixing things that broke. Your stories matter.

You did something today that you couldn't have done six weeks ago.
You took a blank Scratch project and built a complete game that has
a goal, a challenge, scoring, and a way to lose. Every video game
you've ever played has those four things. You now know how to put
them in something *you* built.

### Looking ahead to your own project

Next week we start your **milestone project** — *your* game, your
idea, your design. You'll have two weeks to plan, build, and
polish, then you'll show it to the class.

Start thinking now: **what do you want to make?** Some ideas to
get you started:

- A different kind of catch game (catching different things,
  different objectives)
- A maze game where the cat has to reach a goal without touching
  the walls
- A drawing toy (using the pen extension from Session 3)
- A mini-quiz where the cat asks questions and reacts to clicks
- A "boss battle" where you click a sprite many times to defeat it
- An interactive story — multiple sprites, multiple scenes, the
  user clicks to advance
- Anything else you can imagine that uses what you've learned

You don't have to decide today. But come to next week's class with
at least one idea you're excited about.

### If you missed this session

Open Scratch and start a new project. Then:

1. Build the cat with smooth left/right movement at the bottom of
   the stage. Reset score to 0 on green flag. (Part A above.)
2. Add an apple that falls, gives a point on catch, resets either
   way.
3. Add a rock that falls. If it touches the cat: `say "Game Over"
   for 2 seconds`, then `stop [all]`. If it falls off the bottom:
   reset to top.
4. Test it. Catch apples. Try to dodge the rock.

About 30-40 minutes of work.

Then **think about what you want to build for your own project**
next week. Bring an idea.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Add a backdrop (bottom-right Choose a Backdrop button) so the
  game has a setting — a forest, a city, outer space.
- Add a sound effect when the cat catches an apple. (Sound
  category, `start sound`. Some apple sprites come with sound
  effects built in.)
- Make the cat change costume when game over fires (look at the
  Costumes tab — many cats have multiple costumes).
- Add a third "good" sprite (a star, a heart) worth more points
  than the apple. Now you have to choose what to chase.

### What's next

Next week is the start of your **milestone project** — two weeks to
plan, build, and polish your own game. Bring an idea or two. The
final week will be a class demo day where everyone shows what they
built.
