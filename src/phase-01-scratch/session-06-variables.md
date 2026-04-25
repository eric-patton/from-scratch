## Session 6: Variables — remembering things

*Phase 1 — Scratch · Session 6 of 9*

### What we're learning today

Today you'll learn how to make Scratch *remember* a number — like a
score, a count, or a level. Once you can do that, you can finally
turn last week's catch-the-apple game into a real game with a score
on the screen that goes up every time you catch one. The thing
that makes Scratch remember is called a **variable**, and it's one
of the ideas you'll use in every program you ever write.

### You'll need to remember from last time

- **Conditionals (`if` blocks)** and the **forever loop**.
- **Sensing blocks** like `<touching ...?>`.
- **The catch-the-apple game** you built last week (or its
  catch-up version).

---

### Part A: A box with a number in it

Open Scratch and start a new project. Keep the cat.

A **variable** is the programming word for "a labeled box that
holds something." You give the box a name, you put a number in it,
and you can change the number whenever you want. The computer
remembers what's in the box for as long as your program is running.

Real-world example: the score in a basketball game is a variable.
It starts at 0. Every time a team scores, the number goes up. The
scoreboard remembers it. That's all a variable is.

#### Make your first variable

Look at the **Variables** category in the blocks panel (orange — but
a different orange from Control). At the top of it, there's a button
called **Make a Variable**. Click it.

Scratch asks for a name. Type `clicks`. Leave the rest at the
defaults (For all sprites). Click OK.

Several things just happened:

- A new set of blocks appeared in the Variables category, all
  related to your `clicks` variable.
- A small display labeled "clicks" appeared in the top-left corner
  of the stage. That's your variable's value, shown in real time.
  Right now it shows `0`.

#### Use the variable

Build this on the cat:

```
when [green flag] clicked
set [clicks] to 0
```

```
when this sprite clicked
change [clicks] by 1
```

Two scripts. One resets the variable to 0 when you click the green
flag. The other adds 1 to the variable every time you click the
cat.

Click the green flag. The display shows `0`.

Click the cat. The display shows `1`. Click again. `2`. Again. `3`.

You just made the computer remember something. Every click adds
one. The variable holds the running total.

Click the green flag again. Back to `0`. Click the cat. `1` again.
The variable resets when you start over, then counts up from there.

#### Show the variable to the cat

You can also use the variable's value *inside* other blocks. Add a
third script:

```
when [space] key pressed
say (clicks) for 1 seconds
```

The `(clicks)` block (rounded, in Variables — it's the rounded one
right next to your variable name) gives you the current value.

Click the green flag. Click the cat a few times. Press space. The
cat says the current value out loud. Click the cat more. Press
space again. The cat says the new value.

That's the three things you do with a variable: **set** it, **change**
it, and **read** it.

**Checkpoint:** *You have a variable that increases when you click
the cat, resets when you click the green flag, and is displayed by
the cat when you press space.* **This is the natural stop point if
class is cut short.**

---

### Part B: Score in your catch-the-apple game

Now we'll add a score to the game from last week.

#### Open last week's project

Open the catch-the-apple project from Session 5. (If you don't have
it — for example because you missed last week — go back to Session 5
and build the base game first, or use the catch-up version.)

You should have a cat that moves with the arrow keys (smooth
movement, with a forever loop and four `if` blocks) and an apple
that falls from the top, says "Yum!" when the cat catches it, and
resets to a random spot at the top.

#### Add a score variable

Click **Make a Variable** in the Variables category. Name it
`score`. Click OK. The score display appears in the top-left of the
stage.

#### Reset the score on green flag

The cat already has a `when green flag clicked` script. Add to it:

```
when [green flag] clicked
go to x: 0 y: -130
set [score] to 0
forever
   if <key [right arrow] pressed?> then
      change x by 5
   if <key [left arrow] pressed?> then
      change x by -5
```

(Just add `set [score] to 0` somewhere before the forever loop.)

#### Make the apple update the score

Click the **apple** sprite in the bottom-right panel to switch to
its scripts. Find the part where it says "Yum!" and resets to the
top. Add `change [score] by 1` to that block:

```
when [green flag] clicked
go to x: pick random -200 to 200 y: 180
forever
   change y by -3
   if <touching [Sprite1] ?> then
      change [score] by 1
      say [Yum!] for 1 seconds
      go to x: pick random -200 to 200 y: 180
```

Click the green flag. Catch the apple a few times.

The score in the corner goes up every time. You're keeping score in
your own game.

That's the **base goal.**

#### Stretch goal

Add a "missed" penalty. If the apple falls past the bottom of the
stage without being caught, decrease the score by 1.

Find the `if <(y position) < -180>` block from last week's stretch
goal (or add it now). Inside it, add `change [score] by -1`. So:

```
if <(y position) < -180> then
   change [score] by -1
   say [Missed!] for 1 seconds
   go to x: pick random -200 to 200 y: 180
```

Now your score reflects skill — catches add, misses subtract.
Carelessness costs you points.

#### Extension

Add a *second* variable called `best`. Whenever score goes higher
than best, update best. The display now shows two numbers: your
current score, and the best score you've gotten this session.

Add this to a forever loop somewhere (maybe on the cat):

```
forever
   if <(score) > (best)> then
      set [best] to (score)
```

The `<>` comparison is in Operators (green). The `(score)` and
`(best)` rounded blocks are in Variables.

Now you have a "personal best" tracker. It resets when you click
the green flag, but within a single play session, it keeps the
high score visible.

---

### Wrap-up

Before we leave, share with the room:

- What's the highest score you got? Did anyone beat it after
  another few tries?
- For the kids who did the missed-penalty stretch — does it feel
  like a different game when there's a real consequence for
  missing?
- What's another game where the *score* would matter?

You learned the simplest version of one of the biggest ideas in
programming: **state.** Programs that remember something — anything
— between one moment and the next are running on state. Every
website that knows you're logged in, every game that tracks your
progress, every app that holds a counter — all of it is variables,
behind the scenes.

You also closed the loop on something. Your game from last week
was missing one important piece, and now it has it. Real software
gets built that way: ship something, play with it, find what's
missing, add it, repeat.

### If you missed this session

Open Scratch and start a new project. Then:

1. Click **Make a Variable** in the Variables category. Name it
   `clicks`. Click OK.
2. Build the two scripts from Part A: green-flag-resets-to-0, and
   sprite-clicked-changes-by-1. Click the cat to test.
3. Open your catch-the-apple project from Session 5 (or build the
   catch-up version of Session 5 first if you don't have one).
4. Add a `score` variable. Reset it to 0 on green flag. Have the
   apple's "if touching cat" block also `change score by 1`. Click
   the green flag and play. Score goes up each catch.

About 25 minutes of work total.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- Show the variable in a "large" view — right-click on the variable
  display on the stage and pick "large readout." Looks more like a
  real scoreboard.
- Make a "level" variable that increases every time the score hits
  a multiple of 10. Display both score and level.
- Use `hide variable [name]` (Variables category) to hide a
  variable from the stage when you don't want players to see it.
  Useful for variables you're tracking internally but don't want
  shown.
- Tinker with the `set` vs `change` distinction. Try `set score to
  10` and watch the score jump. The difference between "put this
  exact number in the box" and "add this number to whatever's in
  the box" is worth feeling.

### What's next

Next week we'll **put everything together** — sequences, loops,
events, conditionals, sensing, variables — and build a single
small game that uses all of it. After that, you'll plan and build
your own milestone project.
