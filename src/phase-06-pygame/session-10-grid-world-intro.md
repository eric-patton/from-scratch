## Session 10: The grid-world (intro)

*Phase 6 — Pygame · Session 10 of 14*

### What we're learning today

Today is a little different. Mr. Eric built a game called
**grid-world**, where you guide a character around a grid
to reach a goal — by writing **Python code.** No keyboard
controls; the character moves based on the code you
write. By the end of class you'll have solved several
puzzles and you'll understand how the program works
inside (which sets you up to extend it next week).

Some online learn-to-code sites work like this — drag
blocks to move a robot, solve a puzzle. **You're the
ones building the toy** instead of using someone else's.

### You'll need to remember from last time

- **Sprite classes** — Session 9.
- **Functions** — Phase 3 Session 6.
- **Loops** — `for i in range(N):`.
- **Conditionals** — `if`, `else`.

### What you'll need today

- The `grid_world.py` file Mr. Eric wrote — it'll be on
  your machine before class.

---

### Part A: Play the puzzles

#### What is grid-world?

Open `grid_world.py` in Thonny.

The game shows an 8x8 grid. A character (a small blue
square) starts in one corner. A goal (a yellow square)
is somewhere else. There may be **walls** in between.
Your job: write Python code that gets the character to
the goal.

Run the program. **Press 1, 2, 3, 4, 5** to switch
between the five puzzles. **Press SPACE** to run your
code. **Press R** to reset the character.

Look at the bottom of the file. You'll see something
like:

```python
def solve():
    # === YOUR CODE GOES HERE ===
    pass
```

That `solve()` function is **what gets run** when you
press SPACE. Replace `pass` with calls to the movement
functions.

#### The movement functions

Mr. Eric defined a few functions you can call:

```python
move_right()    # one cell to the right
move_left()     # one cell to the left
move_down()     # one cell down
move_up()       # one cell up
```

Each one moves the character one cell. You see the
character animate from its current cell to the next.

#### Puzzle 1 — straight line

Press **1** to load Puzzle 1. The character is at the
top-left, the goal is three cells to the right. No walls.

Edit `solve()`:

```python
def solve():
    move_right()
    move_right()
    move_right()
```

Save. Press SPACE. The character walks to the goal.
**Solved.**

#### Puzzle 2 — turn the corner

Press **2**. Now the goal is *down* and to the right.
You need to move right several times, then down.

```python
def solve():
    move_right()
    move_right()
    move_right()
    move_right()
    move_down()
    move_down()
```

Save, press SPACE, watch the character solve it.

#### Puzzle 3 — use a loop

Press **3**. The path is long — maybe 7 cells right.
Typing `move_right()` seven times is dumb. Use a `for`
loop:

```python
def solve():
    for _ in range(7):
        move_right()
```

(The underscore `_` means "I'm not using the loop
variable." Convention.)

Save. Press SPACE. **Same result, less code.** That's
why we have loops.

#### Puzzle 4 — walls!

Press **4**. There are walls between you and the goal.
Walking into a wall doesn't move the character (you'll
see it bump). You have to go around.

Plan the path on paper if it helps. Write the moves:

```python
def solve():
    move_right()
    move_right()
    move_down()
    move_down()
    move_right()
    move_right()
    move_down()
```

(Yours might be different depending on where the walls
are.)

#### Puzzle 5 — long path

Press **5**. The grid has a snaking path. Walk it.

Try writing the solution with a mix of loops and
straight calls.

**Checkpoint:** *You've solved at least three puzzles.*
**This is the natural stop point if class is cut short.**

---

### Part B: Look inside the game

The puzzles are fun. The *more interesting* part is how
the program works. Open `grid_world.py` in Thonny and
read through it.

#### What's in the file

Roughly four sections:

1. **Setup** — imports, screen, grid size, colors.
2. **Puzzle definitions** — a list of puzzles, each
   defining start position, goal, and walls.
3. **Movement API** — the `move_right()`, `move_left()`,
   etc. functions. They don't move the character
   *immediately* — they add an instruction to a `moves`
   list.
4. **Game loop** — handles input (1-5, SPACE, R), runs
   `solve()` when SPACE is pressed, animates the
   character through the moves list one by one.

#### Why "build a list of moves"?

When you call `move_right()`, the character doesn't
*instantly* jump to the next cell. Instead, the function
**records** "move one cell right" in a list. Then the
game loop processes the list one move per (say) 200ms,
animating each step.

This is a cool design pattern: **separate the "what to
do" from the "when and how to do it."**

#### What's each function look like?

A peek:

```python
char_x = 0
char_y = 0
moves = []

def move_right():
    moves.append("right")

def move_left():
    moves.append("left")

# ... etc.

def reset():
    global char_x, char_y, moves
    char_x, char_y = current_puzzle["start"]
    moves = []
```

Each move function just appends to the moves list. The
game loop reads from the front of the list and animates
each step.

#### Walls

Walls are stored as a set of `(x, y)` cell positions.
When the game tries to move the character into a wall
cell, it skips the move (the character "bumps" but
doesn't go through).

#### Why is this useful to understand?

Two reasons:

1. **You'll extend it next week.** Adding a new puzzle,
   a new movement function, or a new feature requires
   knowing the structure.
2. **It's a real example of separating concerns.** The
   *student-facing API* (`move_right()`) is dead simple.
   The *implementation* (animate the list, check walls,
   etc.) is hidden. Real software design.

#### Stretch — write your own puzzle solution efficiently

Some puzzles can be solved more elegantly. Try:

- Puzzle 5 with a single `for` loop and a sequence of
  moves inside.
- Solving with **functions you write yourself.** For
  example:

```python
def go_right_then_down(n):
    for _ in range(n):
        move_right()
    for _ in range(n):
        move_down()

def solve():
    go_right_then_down(3)
    go_right_then_down(2)
```

You're using functions to build *higher-level*
movement primitives. This is real programming.

#### Stretch — make a deliberately silly solution

Try solving a puzzle by:

- Going way past the goal and looping back.
- Going back and forth before reaching it.
- Using `move_left()` after `move_right()` (cancel out).

Watch the animation. The character does *exactly* what
you say. Even when it's silly.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — which puzzle was your favorite?
- For the kids who used loops — did the code shrink?
- For the kids who wrote their own helper functions —
  show one off.
- Did anyone make a deliberately silly solution? Show
  the audience.

Today you played a **code-to-control-a-character** game
— like the ones online learn-to-code sites use, but you
typed real Python (no blocks). And you peeked at the
code that makes it work.

You also saw a real software pattern: **a small,
clean API** (the `move_X()` functions) hiding a more
complex implementation (the animation loop, wall
checking, multiple puzzles). That's how good libraries
are designed.

Next week you'll **extend** the grid-world. Add new
puzzles. Add new movement abilities. Make it yours.

### If you missed this session

You'll need the `grid_world.py` file. Get it from a
classmate or from the class shared folder.

1. Open `grid_world.py` in Thonny. Run it.

2. Try each puzzle. Press 1-5 to switch.

3. Edit `solve()` to write code that gets the character
   to the goal. Press SPACE to run.

4. Read through the code. Try to figure out where the
   movement API is implemented.

About 45-60 minutes. By the end you should have solved
all five puzzles and understand the structure of the
program.

### Stretch and extension ideas

- **Solve every puzzle in fewer lines.** Use loops and
  helper functions. Code golf with intent.
- **Solve every puzzle without using `move_left()` or
  `move_up()`.** (Backtracking only when forced.)
- **Write a single `solve()` that handles multiple
  puzzles.** (Hard — will need conditionals based on
  current puzzle.)
- **Read every line** of `grid_world.py`. Make sure you
  could explain each section.
- **Add comments** where the code is unclear. Good
  practice — and helpful for next week's work.

### What's next

Next week: **extend the grid-world.** You'll add at
least one puzzle of your own design. The kids who go
deeper will add new movement abilities (turn left,
collect a gem, jump over a tile). The grid-world stops
being Mr. Eric's and starts being yours.
