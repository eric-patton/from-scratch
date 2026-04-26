## Session 12 — Teacher Notes

*Phase 6, Pygame · Session 12 of 14 · Title: Game state
— title screens and game over*

### Purpose of this session

The "real game polish" session. Five jobs, in priority
order:

1. **Land the state-variable + dispatch pattern.** A
   string + `if/elif` covers 95% of indie games. Drill
   it.
2. **Land that game state matters for *feel*.** A title
   screen makes a game feel like a *game*, not a toy.
   Same for game over. Real polish.
3. **Land the reset-on-transition trick.** Most common
   bug in this pattern: forgetting to clear scores or
   reset positions when leaving game-over to title.
4. **Set up the milestone.** Title → playing →
   game-over is the *minimum* shape every milestone
   should have. Frame this as a base requirement.
5. **(Stretch) Show the scene-class pattern.** For kids
   who are ready, scene classes are the production
   version. Mention; don't drill.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame.
- Pre-built `state_demo.py` (Part A).
- Pre-built version of Pong with title + game-over
  (Part B). Use *the* Pong from Session 6 as the base.
- Optional: pre-built scene-class version for advanced
  demo.

**Prep time:** ~20 minutes. Build the demos, run them.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 11.
  Today: scenes.
- **Part A: state_demo** (~25 min). Walk through the
  three-state pattern. Type live.
- **Break** (~5 min).
- **Part B: add states to a game** (~45 min). Each kid
  picks a game and adds title + game-over. Roam and
  debug.
- **Stretches** (~10 min). Pause + high score for fast
  finishers. Scene classes for advanced.
- **Wrap-up + milestone framing** (~5 min).

If running short, **stretches can be cut.** The base
goal — "kid's game has a title screen and game-over
screen" — is the priority.

### Teaching Part A

#### Frame "state" plainly

Don't use the words "finite state machine" or get into
formal CS theory. Frame:

> "What screen is the game showing right now? Title?
> Playing? Game over? Each one is a *state*. We have
> a variable that holds which state we're in. Then the
> game does different things based on the state."

A simple analogy:

> "Think of a vending machine. State 1: 'waiting for
> coins.' State 2: 'showing item options.' State 3:
> 'dispensing.' State 4: 'returning change.' Each state,
> the machine does different things. Inputs (coin
> inserted, button pressed) trigger transitions."

#### Walk through the dispatcher slowly

```python
if state == "title":
    # title things
elif state == "playing":
    # playing things
```

The conceptual move: **same main loop, different
behavior per state.** The loop runs 60 times a second
regardless. The state determines what happens *inside*
each frame.

#### Where transitions happen

Transitions belong in **input handling** (Enter pressed,
Esc pressed) or in **game logic** (score reached 10,
lives at 0).

Show both:

```python
# Input transition
if event.key == pygame.K_RETURN and state == "title":
    state = "playing"

# Game-logic transition
if score >= 10:
    state = "game_over"
```

Either way, "state changes" is one line.

#### The `state == "X"` guard on input

Notice the input handling is *guarded by state*:

```python
if event.key == pygame.K_RETURN and state == "title":
    state = "playing"
```

Why? Because pressing Enter during *play* shouldn't do
anything (or should do something different). The state
guard says "this transition only happens when in this
state."

For complex games, the input handling itself becomes
state-dependent. Mention briefly.

### Teaching Part B

#### Pick one game

Don't have kids try to refactor *all* their games. Pick
one (Pong is the most common, fruit catcher is
next-easiest). Encourage:

> "Pick the game you most want to feel polished. We're
> only adding screens to one. Future games can copy
> this pattern."

#### The "wrap existing code in `elif state == 'playing':`" move

The key refactor:

> "Take all your existing game logic — paddle movement,
> ball update, collision, score draw, the whole thing.
> Indent it under `elif state == 'playing':`. That's
> the bulk of the change."

This is mechanical but easy to mess up — one stray
unindented line and Python errors.

#### The reset-on-transition trick

This is the single most common bug in state-based
games. Walk through:

> "When you transition from game_over back to title (or
> from title to playing), you need to *reset* the game.
> Score back to 0. Ball back to center. Lives back to
> 3. Whatever the game tracks.
>
> The cleanest way: write a `reset_game()` function.
> Call it on transition. One place to update if you
> change game state."

#### The "currently-empty branches" pattern

When kids first add three states, the title and
game_over branches are tiny — just text. The playing
branch has all the logic. **That's correct.** Don't
let kids feel they need to "balance" the branches.

### Teaching the stretches

#### Pause is delightful

Pause is conceptually the simplest stretch. Two
transitions (P from playing → paused; P from paused →
playing). The "drawing while paused" trick — keep the
game's last frame visible, draw "PAUSED" overlay. No
update happens during pause.

Show how skipping the update freezes the game in time.
Kids who haven't seen this before find it slightly
magical.

#### High score is the persistence callback

References Phase 5 Session 6 (JSON save/load) and Phase
3 Session 11 (file I/O). The pattern reappears at every
phase. Drill it gently.

#### Scene classes — show, don't drill

For advanced kids only. Walk through the class structure
on the projector. Show the cleaner main loop.

The teaching frame:

> "When games get big — like, 5+ states with their own
> state inside — the if/elif dispatcher gets ugly. Real
> games use scene *classes*. Each scene is its own
> class with `update()` and `draw()`. The main loop
> just calls the current scene's methods."

Do not drill. The kids who get it will use it; the kids
who don't can stay with if/elif.

### Common stumbles

- **Indentation wrong on the wrap.** Existing code not
  consistently indented under `elif state == 'playing':`.
  Walk through.
- **State doesn't actually transition.** Forgot the
  `state = "..."` assignment.
- **Game logic still runs in title screen.** Forgot to
  put the logic *inside* the playing branch. (Or
  duplicated it outside.)
- **Score/lives/positions don't reset.** No reset on
  transition. Walk through `reset_game()`.
- **Pressing Enter on title transitions to playing
  AND triggers something in playing.** Event handling
  bleeds across states. Add state guards.
- **`elif` confused with `if`.** Two `if`s in a row
  may both run, causing bugs. Use `elif` for
  mutually-exclusive branches.
- **Game over triggers but doesn't show.** The
  game_over branch has no draw code, or the draw runs
  but is hidden behind something.
- **Pause "doesn't pause" — game still updates.** Forgot
  to skip the update in the paused branch. Or kept
  the update outside the dispatcher.
- **Highscore file format.** Wrote a number, tried to
  read as int. Make sure to wrap in `int(f.read())`.

### Differentiation

- **Younger kids (9-10):** Goal is the basic three-state
  flow on one game. Pause + high score are stretches.
- **Older kids (12+):** Push for pause + high score.
  Polished game.
- **Advanced (any age):** Push for scene classes.
  Suggest:
  - A settings screen with volume controls
  - A level-select screen
  - Animated transitions (fade in/out)
  - A "best time" or "fastest score" tracker
- **Struggling:** A kid who can't get the three-state
  flow working is the kid you focus on. Most common
  cause: indentation, or forgot to assign state on
  transition.

### What to watch for

- **The "wait, my Pong has a title screen?" moment.**
  Genuine "now it feels like a game" reaction.
- **Comparing games before and after.** Buddies
  showing each other their old vs new. Encourage.
- **Kids who try to refactor too many games at once.**
  Redirect: "Pick one. Get it perfect. Polish for the
  others later."
- **Kids who add too many states.** Title, splash,
  intro, level select, playing, paused, dialogs,
  game over, victory, credits... too much. Redirect
  to the basic three.
- **Buddies trying each other's title screens.** First
  impressions matter. Some title screens are great;
  others are minimal. Both are fine.
- **Excitement about the milestone.** The "next two
  weeks are *yours*" framing should land. Some kids
  already start sketching ideas.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sessions 13-14 (milestone).** Today's three-state
  pattern is the *minimum* shape every milestone game
  should have. Frame this as a base requirement when
  planning milestones.
- **Phase 7 (web).** Single-page web apps use a similar
  pattern (different "views" depending on state).
- **Phase 8 (Flask).** URL routes are a dispatcher of
  the same flavor — different state, different render.
- **Real game engines.** Unity's scenes, Godot's scene
  tree — formalized versions of today's pattern.
- **Career-long callback:** state machines are
  everywhere — UIs, network protocols, anything that has
  modes. Today's intuition matters for years.
- **Peanut butter callback opportunity:** the
  "transition without reset → broken state on next round"
  bug is a precision moment. Code did exactly what was
  written; just missed the cleanup.

### Materials checklist

- [ ] Demo machine with Pygame
- [ ] Pre-built state_demo.py
- [ ] Pre-built Pong with title + game-over
- [ ] Optional: scene-class version for advanced demo
- [ ] Projector
- [ ] Class roster
