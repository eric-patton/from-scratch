## Session 11: The grid-world (extending)

*Phase 6 — Pygame · Session 11 of 14*

### What we're learning today

Last week you played the grid-world. This week you
**make it yours.** You'll add at least one new puzzle of
your own design. Going further: add a new movement
ability, a new game element (a gem to collect, a tile
that does something), or change how a puzzle works. By
the end you'll have a grid-world *you* designed — the
kind of educational toy you used to be a *user* of.

This is the creator session.

### You'll need to remember from last time

- **Grid-world basics** — Session 10.
- **The structure of `grid_world.py`** — puzzles,
  movement API, game loop.
- **Sprite classes** (Session 9) — for new game
  elements.
- **Lists, dictionaries, conditionals, functions** —
  Phase 3.

---

### Part A: Add a puzzle

The simplest extension. Each puzzle is just **data** —
start position, goal position, and a list of walls.
Adding one is a few lines.

#### Find the puzzles list

Open `grid_world.py`. Find where the puzzles are defined
— probably near the top, looking something like:

```python
puzzles = [
    {
        "name": "Straight line",
        "start": (0, 0),
        "goal": (3, 0),
        "walls": []
    },
    {
        "name": "Turn",
        "start": (0, 0),
        "goal": (4, 4),
        "walls": []
    },
    # ... etc
]
```

(Yours might look slightly different. The point is: each
puzzle is a dictionary with a few key bits of data.)

#### Add your own

Add a new dictionary to the list. Pick a start, a goal,
and any walls you want:

```python
{
    "name": "My puzzle",
    "start": (0, 7),
    "goal": (7, 0),
    "walls": [(2, 5), (3, 5), (4, 5), (4, 4), (4, 3)]
},
```

The walls are `(x, y)` cells. Sketch on paper first if
it helps.

Save. Run `grid_world.py`. Your puzzle should appear as
the next number (if you had 5 puzzles, your new one is
puzzle 6 — press 6 to load it).

Solve your own puzzle. Make sure it's actually
*solvable*.

#### Test it on a friend

Have your buddy try to solve your puzzle without you
telling them how. Notice:

- Was it too easy? Too hard?
- Did your buddy try a path you didn't expect?
- Were the walls placed cleanly?

Iterate. Adjust walls or goal position. **You're now
designing levels.** This is real game design work.

#### Stretch — a series of puzzles with a theme

Add 3-5 puzzles that get progressively harder. A "level
pack" you designed.

**Checkpoint:** *You've added at least one puzzle of
your own design.* **This is the natural stop point if
class is cut short.**

---

### Part B: Add a feature

The puzzles work. Now add a new *capability* to the
game. Pick one or more.

#### Option 1 — collect a gem

Add a "gem" to puzzles. Walking onto its cell collects
it. Goal: reach the goal *with* the gem.

Steps:

1. Add `gems` to puzzle dicts (a list of cells where
   gems are):
   ```python
   {
       "name": "Gem run",
       "start": (0, 0),
       "goal": (7, 7),
       "walls": [],
       "gems": [(3, 3), (5, 5)]
   },
   ```

2. Track collected gems in game state:
   ```python
   collected_gems = set()
   ```

3. When the character moves to a gem cell, collect it:
   ```python
   # In the move-step code:
   if (char_x, char_y) in current_puzzle.get("gems", []):
       collected_gems.add((char_x, char_y))
   ```

4. Check at the end: only "solved" if all gems collected:
   ```python
   if (char_x, char_y) == current_puzzle["goal"]:
       if len(collected_gems) == len(current_puzzle.get("gems", [])):
           print("Solved!")
       else:
           print("You missed a gem.")
   ```

5. Draw gems in the draw loop (a yellow dot in each gem
   cell). Don't draw the ones already collected.

This adds *real* puzzle design — the player has to plan
a path that includes detours.

#### Option 2 — turn-based movement

Instead of `move_left()` and `move_right()`, give the
character a *facing direction*. Add `turn_left()`,
`turn_right()`, and `forward()`.

Steps:

1. Track facing direction in game state:
   ```python
   facing = "right"    # or "left", "up", "down"
   ```

2. Add the new functions:
   ```python
   def turn_left():
       moves.append("turn_left")
   
   def turn_right():
       moves.append("turn_right")
   
   def forward():
       moves.append("forward")
   ```

3. Handle the new move types in the playback:
   ```python
   if move == "turn_left":
       # rotate facing direction
       directions = ["up", "left", "down", "right"]
       facing = directions[(directions.index(facing) + 1) % 4]
   if move == "turn_right":
       directions = ["up", "right", "down", "left"]
       facing = directions[(directions.index(facing) + 1) % 4]
   if move == "forward":
       # move in the current facing direction
       if facing == "right": char_x += 1
       elif facing == "left": char_x -= 1
       # ... etc
   ```

4. Draw the character with a small arrow showing facing.

Now puzzles can require *spatial reasoning* —
"forward, turn left, forward" instead of memorizing
cardinal directions.

#### Option 3 — ice tiles

Some cells are "ice." Stepping on ice slides the
character one extra cell in the same direction.

Steps:

1. Add `ice` to puzzles (a list of icy cells).

2. After each move, check if the character is on ice:
   ```python
   if (char_x, char_y) in current_puzzle.get("ice", []):
       # slide one more cell in the same direction
       if last_direction == "right" and not blocked: char_x += 1
       # ... etc
   ```

3. Draw ice tiles with a different color (light cyan).

Ice changes the game from "execute moves" to "predict
slides." Real puzzle-game mechanic.

#### Option 4 — multi-character

Add a *second* character. Both have to reach goals.

Steps:

1. Add second character position and goal to puzzles.

2. Two sets of movement functions:
   ```python
   def move_right():    # moves character 1
       moves.append(("char1", "right"))
   
   def move_right_2():    # moves character 2
       moves.append(("char2", "right"))
   ```

3. Playback handles both characters separately.

#### Extension — visual polish

Make the grid-world *look* nicer. Some ideas:

- Better character sprite (your own art).
- Animated background.
- Sound effects on each move (Session 8).
- Particle effect when goal is reached.
- A "moves remaining" counter (limit moves per puzzle).
- A "best solution" tracker (fewest moves wins).

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your new puzzle. Have a buddy try
  it.
- For the kids who added a feature — demo it.
- What's the most creative puzzle in the room?
- For kids who added gems / ice / facing direction —
  did your design make new kinds of puzzles possible?

Today you went from **using** Mr. Eric's grid-world to
**building on** it. You added puzzles. Maybe new
abilities. Maybe new game elements.

This is the loop of real software work:

1. Use a thing.
2. Read its code.
3. Modify it.
4. Add to it.
5. Now it's yours.

Every program you'll ever work on professionally
started out as someone else's. The skill is being able
to *step into* and *extend* that work. **You just did
that.**

Three sessions left in Phase 6:

- Session 12: Game state — title screens, game over,
  multiple "scenes."
- Sessions 13-14: **Your milestone game.**

You have everything you need now. The milestone is
about putting it all together.

### If you missed this session

You'll need `grid_world.py` (your modified version from
last week, or a fresh copy from the class folder).

1. Read through the file. Find the puzzles list.

2. Add at least one new puzzle. Solve it. Have a friend
   try.

3. (Stretch) Pick one feature from Part B (gems, facing,
   ice, multi-character) and implement it.

About 60-90 minutes. By the end you should have a
grid-world that's noticeably *yours*.

### Stretch and extension ideas

- **All four feature options above** combined.
- **A puzzle editor** — UI for designing puzzles
  visually instead of editing code. Click cells to
  place walls. Click to place start/goal/gems. Save
  to a file.
- **Save and load puzzles from JSON** — extend the
  puzzle data to a file that can be edited outside the
  code.
- **A "share your puzzle" mode** — print the puzzle
  data to console; classmate pastes it into their
  grid-world.
- **Animation polish** — character bobs while moving,
  glows when reaching goal.
- **A scoring system** — fewer moves = higher score.
- **Push your modified grid-world to GitHub.** It's a
  real project now. (Session 7 callback.)

### What's next

Next week: **game state** — title screens, gameplay,
game over screens. The structural pattern that turns
your games from "single screen" into "real games with
multiple scenes."
