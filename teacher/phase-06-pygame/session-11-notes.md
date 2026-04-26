## Session 11 — Teacher Notes

*Phase 6, Pygame · Session 11 of 14 · Title: The
grid-world (extending)*

### Purpose of this session

The "you're a creator now" payoff. Five jobs, in
priority order:

1. **Get every kid to add at least one puzzle.** This
   is the base goal. Touch the codebase, modify the
   data, see your change run.
2. **Land the read-modify-extend loop.** Real-world
   software work *always* starts with someone else's
   code. Today's the explicit teach moment for that
   skill.
3. **Push some kids beyond data — into adding a feature.**
   Gems, ice, facing, multi-char. Each option teaches
   real game-mechanic design.
4. **Encourage testing on buddies.** Designing puzzles
   that someone else can solve = real game design.
5. **Set up Sessions 13-14 (milestone).** Today's
   "extending an existing project" rehearses the
   milestone work.

### Before class

**Bring:** nothing physical.

**Set up:**

- The same `grid_world.py` from Session 10. Kids
  should still have their version (with their solved
  puzzles) on their machines.
- Pre-built versions of each feature option (gems,
  facing direction, ice tiles, multi-character) for
  reference if a kid wants to compare implementations.
- The base grid_world.py source open for reference.

**Prep time:** ~30-45 minutes — mostly building one or
two of the feature-option implementations to demo.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 10.
  Today: extending.
- **Part A — add a puzzle** (~30 min). Show the
  pattern, kids design + add their own. Buddy testing.
- **Break** (~5 min).
- **Part B — pick a feature** (~40 min). Walk through
  the four options. Kids pick one. Implement.
- **Wrap-up + show-and-tell** (~10 min).

If running short, **all of Part B can be cut.** The
base goal — "kid adds a puzzle" — is the priority.

### Teaching Part A — adding puzzles

#### "Puzzles are data"

The framing:

> "Each puzzle is just a dictionary. A start, a goal,
> some walls. Five lines of data. To add a puzzle, you
> add another dictionary to the list. *That's it.* No
> code change.
>
> This is a real software design choice — separating
> *data* from *code*. The grid_world *engine* doesn't
> change when you add puzzles. Only the data does."

This is a teachable moment. Worth pausing on.

#### Sketch first

Push every kid to **draw their puzzle on paper** before
typing it. Without this:

- Walls placed wherever — puzzle unsolvable.
- Goal in same cell as a wall.
- Path completely trivial (no challenge).

Sketching forces design thinking.

#### Buddy testing is the design payoff

Once a kid has a puzzle working, immediately have a
buddy try to solve it without help. The reactions are
revealing:

- "Oh, I forgot to put a wall there."
- "It's too easy."
- "It's impossible — let me check."

This iterative design loop is *real puzzle-game design.*

#### Encourage themed puzzle packs

A kid who finishes one puzzle quickly can make 3-5 more
with a theme — "the spiral series," "wall of doom,"
"pickup hell." This is a great stretch.

### Teaching Part B — features

#### Don't try to teach all four

Walk through *one* feature in depth on the projector.
The other three are described in the handout for kids
to attempt on their own.

**Recommended pick: gems.** It's the cleanest extension,
it doesn't require new movement primitives, and it
adds real puzzle design (the path now has to detour).

#### Walking through gems

Show the changes step by step. Each step runs:

1. Add `gems` to puzzles (data change).
2. Track collected gems (state).
3. Detect collection on move.
4. Check at goal whether all gems are collected.
5. Draw uncollected gems.

Each step builds. Kids should see the feature *grow* on
screen.

#### Common stuck points by feature

**Gems:**
- Forgot to draw them. They exist in data but invisible.
- Forgot the "all collected" check at goal — solving
  works without picking up gems.

**Facing direction:**
- Direction list rotation math is error-prone. Use
  `directions = ["up", "right", "down", "left"]` and
  modular arithmetic.
- Forgot to draw the facing arrow.
- Forgot to update `facing` when turning.

**Ice tiles:**
- Slide direction unclear (need to track *previous*
  move, not current).
- Slide can push character into walls — need
  collision check.
- Slide can push character off the grid — need
  bounds check.

**Multi-character:**
- Confusing which set of move functions controls which
  character.
- Forgetting to track two positions, two states.

Encourage kids to pick the *one* feature most
appealing, not try multiple.

### Common stumbles

- **Edited the wrong file.** Some kids made a copy
  but kept editing the original. Walk through "save
  as" / file naming.
- **Puzzle index off by one.** Added puzzle 6, but
  pressed 5. Or vice versa.
- **Puzzle unsolvable.** Walls block all paths. Solve
  it on paper first.
- **Walls in wrong cells.** `(2, 5)` confused with
  `(5, 2)`. Coordinate convention: x first, y second.
- **`solve()` from puzzle 1 doesn't work for puzzle
  2.** Each puzzle needs its own solution code. Or use
  buddy as the solver.
- **Modified the framework, broke something.** Walk
  through git: did they save a checkpoint? If not,
  this becomes a debugging exercise.
- **JSON-style errors with dict syntax.** Forgot
  comma between dict entries. Forgot `:` between key
  and value.
- **Feature added but doesn't run.** Ran the wrong
  file, or didn't save, or syntax error. Walk through.

### Differentiation

- **Younger kids (9-10):** Goal is one new puzzle.
  Stop there. Designing a puzzle is real creative
  work.
- **Older kids (12+):** Add 2-3 puzzles, attempt one
  feature option (gems is the cleanest).
- **Advanced (any age):** Push for multiple features,
  or:
  - A puzzle editor UI
  - Save/load puzzles to JSON file
  - Animation polish
  - Push the modified grid-world to GitHub
- **Struggling:** A kid stuck on adding a puzzle is
  the kid you focus on. Most common cause: edited
  wrong place, didn't save, or the puzzle data
  isn't quite right.

### What to watch for

- **The "I made a puzzle!" reaction.** Same satisfaction
  as a designer making a level. Visible.
- **Buddies trading puzzles.** Encourage. Real
  multiplayer-design moment.
- **Kids tempted to design over-elaborate puzzles.**
  Big wall mazes that take 30 moves to solve. Fine if
  they want, but redirect if it's eating session time.
- **Kids combining puzzle design with feature additions
  prematurely.** Encourage finishing puzzle first, then
  feature.
- **Frustration with feature implementation.** Some
  features (especially facing direction) have fiddly
  state. Reassure — this is what real game development
  feels like.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 12 (game state).** Today's "puzzle solved!"
  is a tiny scene transition. Session 12 makes scenes
  proper.
- **Sessions 13-14 (milestone).** A kid could absolutely
  build a "grid-world variant" as their milestone — a
  themed puzzle game with their own character, art, and
  rules. Encourage.
- **Phase 7 (web).** Browser-based puzzle games use the
  same patterns (puzzle data, render, check win state).
- **Career-long callback:** "Read the source, add a
  feature" is exactly how every professional programmer
  works on every team they join. Real practice.
- **Peanut butter callback opportunity:** the puzzle
  unsolvable / wall-in-wrong-cell debugging is a
  precision moment. Designed exactly what was intended,
  but the result wasn't playable.

### Materials checklist

- [ ] Demo machine with grid_world.py
- [ ] Pre-built example of at least one feature
      (gems recommended)
- [ ] Optional: pre-built examples of all four features
- [ ] Graph paper for puzzle sketching
- [ ] Projector
- [ ] Class roster
