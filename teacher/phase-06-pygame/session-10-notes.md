## Session 10 — Teacher Notes

*Phase 6, Pygame · Session 10 of 14 · Title: The
grid-world (intro)*

### Purpose of this session

The "you're not just a user, you're a creator" beat —
delivered through Mr. Eric's grid-world. Five jobs, in
priority order:

1. **Land the meta-pitch.** Online learn-to-code sites
   give kids a grid-world to play. *We* are *building*
   one. Frame this clearly.
2. **Get every kid to solve at least 3 puzzles.** Hands
   on the keyboard. Code that makes a character move.
   Tactile.
3. **Land "API hides implementation."** The
   `move_right()` function looks dead simple. Behind it,
   a lot is happening. That separation is real software
   design.
4. **Read the code.** Half the value is reading
   *Mr. Eric's actual code* and understanding it. Sets
   up the extension session.
5. **Set up Session 11 (extending).** Today: read and
   play. Next: modify and add.

### Before class

**Bring:** nothing physical.

**Set up — major prep:**

- **`grid_world.py` must exist.** This is the session's
  central artifact. Build it. Test it. Distribute it
  to every machine.
- The grid_world should support:
  - 8x8 grid with cells visible
  - Character (sprite) at start position
  - Goal (sprite or colored cell)
  - Wall cells (different visual)
  - Movement API: `move_right()`, `move_left()`,
    `move_down()`, `move_up()`
  - Functions append to a `moves` list (not immediate
    movement)
  - Game loop animates character through `moves` list
    one step at a time (with delay)
  - Number keys 1-5 switch puzzles
  - SPACE runs `solve()`
  - R resets character to puzzle start
  - "Solved!" indicator when character reaches goal
- 5 puzzles of escalating difficulty:
  1. Straight line right
  2. Turn the corner (right then down)
  3. Long line (encourages loop usage)
  4. Walls — go around
  5. Snaking path

**Prep time:** ~1-2 hours to build the grid_world the
first time. After that, ~10 minutes per session to
verify and update.

### Timing and flow

Total: ~90 min.

- **Welcome and meta-pitch** (~10 min). "You've
  probably used something like this. Today we're playing
  the one we built."
- **Part A — solve puzzles 1-3** (~25 min). Live demo,
  then kids do their own.
- **Break** (~5 min).
- **Part A — solve puzzles 4-5** (~20 min). Walls and
  snaking path.
- **Part B — read the code** (~25 min). Walk through
  the structure on the projector.
- **Wrap-up** (~5 min). Show-and-tell weird solutions.

If running short, **Part B can be condensed to 10
minutes** — just point out the structure rather than
reading line-by-line.

### Teaching the meta-pitch

The framing matters more than usual today:

> "Some of you have probably used Code.org or Khan
> Academy or similar — they have these little games where
> you write code (or drag blocks) to move a character on
> a grid. Solving puzzles by programming.
>
> We're going to play the same kind of game today. The
> difference: *I built it.* It's the kind of educational
> tool you might have *used* somewhere else. Today
> you're using ours.
>
> Next week: you'll *extend* it. Add puzzles. Add
> abilities. Make it yours. By the end, you've gone from
> consumer of these toys to *creator.*"

This is the core of what makes grid-world meaningful in
*this* curriculum (vs being just another "learn to code"
tool). Drive it home.

### Teaching Part A — the puzzles

#### Live-solve Puzzle 1 first

On the projector, with the kids watching:

```python
def solve():
    move_right()
    move_right()
    move_right()
```

Save. Press SPACE. Character walks. Goal achieved.

Pause. Reset (R). Try a *wrong* solution (only two
move_rights). Watch the character stop short. **Show
the failure mode.** Frame:

> "The character does *exactly* what you wrote. No more,
> no less. Wrote two moves? Two moves. Wrote ten? Ten."

#### Walking around the room

After Puzzle 1 demo, kids attempt Puzzles 2-3 on their
own. Roam. Help with:

- Path planning (suggest sketching on paper).
- Loop syntax (some kids will write `for i = 1 to 7`
  from other languages).
- The "press SPACE to run" mechanic — a few kids will
  forget.

#### Puzzles 4-5 — encourage paper

The walls puzzle benefits from sketching. Hand out
graph paper or just suggest:

> "Draw the grid on a piece of paper. Mark start, goal,
> walls. Then *trace the path* with your finger. Then
> write the moves."

This is real programming practice — plan first, code
second.

#### Loops are the win

The third puzzle (long path) is designed to make loops
feel useful. Some kids will type `move_right()` 7 times
without thinking. After they finish, suggest:

> "Same thing with a loop is two lines."

```python
for _ in range(7):
    move_right()
```

The "less typing" angle resonates.

### Teaching Part B — read the code

#### The "moves list" trick is the design insight

The key insight in grid_world is that calling
`move_right()` doesn't *immediately* move the character.
It appends to a list. Then the game loop animates the
list step by step.

Frame:

> "When you write `move_right()`, the character doesn't
> jump there. The function just *records* 'I want to
> move right.' Then the game loop, every 200 milliseconds
> or so, takes the next move from the list and animates
> the character.
>
> Why? Because if `move_right()` actually moved the
> character *immediately*, your `solve()` function would
> finish in microseconds. You'd never see the animation.
>
> So we *separate* the **what** (the moves list) from
> the **when** (the animation playback)."

This is real software design — separation of concerns.

#### Walk through the file structure

Don't read every line. Just point out the four sections:

1. Setup at the top (imports, constants).
2. Puzzles defined as data.
3. Movement API (the student-facing functions).
4. Game loop (input handling, playback, drawing).

For each, point at it on the projector and say what it
does in one sentence.

#### Encourage curiosity

Kids who finish early should read the file actively:

- Where does the character get its position?
- How does the wall check work?
- What happens when `solve()` is called?

These questions set up Session 11 nicely.

### Common stumbles

- **Forgot to press SPACE.** Wrote code, saved, nothing
  happened. Walk through: edit → save → SPACE.
- **`solve()` not modified.** Still has `pass` in it.
- **Indentation wrong.** `move_right()` not inside
  `def solve():`. Walk through the indent.
- **Used wrong function name.** `move_forward()` doesn't
  exist (only the four cardinal directions). Or
  `moveright()` (no underscore). Use the names from the
  handout.
- **Loop syntax wrong.** `for i in 7` instead of
  `for _ in range(7):`.
- **Character "stuck."** Probably hit a wall they didn't
  account for. Reset and re-plan.
- **Multiple SPACES queue moves.** Pressing SPACE twice
  may run `solve()` twice, depending on
  implementation. Reset before re-running.
- **Switched puzzles mid-solve.** Character resets;
  their `solve()` may not work for the new puzzle.

### Differentiation

- **Younger kids (9-10):** Goal is solving Puzzles 1-3.
  Puzzles 4-5 are stretches. Code-reading in Part B
  may be too much; have them play more puzzles instead.
- **Older kids (12+):** All five puzzles + read the
  code. Push them to write helper functions for Puzzle
  5 (the snaking one).
- **Advanced (any age):** Suggest:
  - Refactor every solution to use helper functions
  - Read every line of grid_world.py
  - Suggest improvements they'd make (sets up Session 11)
  - Try to solve a puzzle in *fewer* lines than seems
    possible
- **Struggling:** A kid who can't solve Puzzle 1 is the
  kid you focus on. Most common cause: they didn't save,
  or they edited something other than `solve()`, or
  they don't understand "press SPACE to run."

### What to watch for

- **The "wait, this is like CodeCombat / Code.org"
  reaction.** Some kids will recognize the pattern.
  Affirm. "Yes — and *we built one.*"
- **The "I solved it!" reaction.** Each puzzle solved
  is satisfying. Acknowledge wins.
- **Kids racing to write the *shortest* solution.**
  Encourage. Code golf is real game-dev fun.
- **Kids reading the code.** This is the under-the-hood
  payoff. Encourage with questions: "What do you think
  happens when you press R?"
- **Buddies showing each other their solutions.**
  Encourage — comparing solutions is great learning.
- **Frustration with walls.** The first wall puzzle
  catches kids who didn't plan. Suggest paper.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 11 (extending).** Today: read and play.
  Next: modify and extend. Today's code-reading is the
  prep.
- **Sessions 13-14 (milestone).** A few kids may build
  grid-world variants for their milestone — different
  movement, different goals, different visuals. That's
  great.
- **Phase 7 (web).** Browser-based versions of this
  same toy exist. The student-facing API → real
  implementation pattern shows up everywhere.
- **Phase 8 (Flask).** Same separation: route handlers
  are tiny; the framework does heavy lifting.
- **Career-long callback:** "Read the source" is a real
  programming skill. Kids who can read other people's
  code are way ahead.
- **Peanut butter callback opportunity:** the "moves
  queue up; character does *exactly* what you wrote"
  framing. Bumping into a wall is the literal
  definition of "computer does what you say, not what
  you mean."

### Materials checklist

- [ ] Demo machine with grid_world.py + Pygame
- [ ] grid_world.py distributed to every student machine
- [ ] All 5 puzzles tested and working
- [ ] Optional: graph paper for path planning
- [ ] Projector
- [ ] Class roster
