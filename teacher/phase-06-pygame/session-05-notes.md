## Session 5 — Teacher Notes

*Phase 6, Pygame · Session 5 of 14 · Title: Collision
detection*

### Purpose of this session

Pong prep. Five jobs, in priority order:

1. **Land `rect.colliderect`.** The simplest collision
   API; the foundation for everything in Sessions 6-14.
2. **Land "rectangle collision is approximate but fine."**
   Pixel-perfect collision is a rabbit hole; for almost
   every kid game, rect collision is correct.
3. **Land game state — lives, score, game over.** This
   is the conceptual frame for "the game ends" and
   "the player can lose."
4. **Land frame-timer spawning.** Counting frames to
   trigger spawn events. Foundation for any game with
   waves, projectiles, or timed events.
5. **Set up Session 6 (Pong).** Today's fruit catcher is
   one paddle + falling things. Pong is two paddles + a
   bouncing ball + scoring. Same primitives, different
   shape.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame + sprite assets.
- Pre-built collision test (Part A).
- Pre-built fruit catcher game.
- Pre-built variant with bombs (stretch).

**Prep time:** ~25 minutes. Build and play the fruit
catcher; tune SPEED and SPAWN_INTERVAL so it feels right.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap distance check
  vs real collision.
- **Part A: `colliderect`** (~20 min). Build the collision
  test, run, verify.
- **Break** (~5 min).
- **Part B: fruit catcher** (~50 min). Type together,
  walk through new pieces. Roam and debug.
- **Part B: stretches** (~5 min). Bombs, restart for
  fast finishers.
- **Wrap-up** (~5 min).

If running short, **the stretch goals can be cut.** The
fruit catcher itself is the priority — it's both the
session goal and a Pong rehearsal.

### Teaching Part A

#### `colliderect` is one line

Don't oversell. It's:

```python
if a_rect.colliderect(b_rect):
    # they're touching
```

Frame as:

> "Last week we faked it with distance. Pygame has the
> real thing built in. One method on a rect: 'do you
> touch this other rect?' Returns True or False."

#### Rectangle collision is "good enough"

Some kid will ask "but what if the sprite shape is
weird? What if the rect has empty corners?"

Honest answer:

> "Yes. The rect catches it before the visible pixel
> would. For most games this doesn't matter — players
> don't notice. For games where it does matter (a
> precision platformer), there's `pygame.mask` for pixel-
> perfect collision. Rect collision is what most games
> use. Cheaper, fast, almost always good enough."

Show the visualization: outline both rects (3rd arg to
`pygame.draw.rect` for outline-only). Kids can *see*
when the rects overlap.

```python
pygame.draw.rect(screen, (255, 255, 0), player_rect, 2)
pygame.draw.rect(screen, (255, 255, 0), coin_rect, 2)
```

Drop these in for a kid who's confused. Helps a lot.

#### `collidelist` and `collidelistall`

Mention briefly if asked:

- `rect.collidelist([rect1, rect2, rect3])` returns the
  *index* of the first collision (or `-1`).
- `rect.collidelistall(list)` returns *all* indexes.

For the curriculum, the for-loop pattern is more
flexible. Don't drill these.

### Teaching Part B

#### The fruit catcher is the heart

This is a real game with all the pieces: input,
movement, collision, scoring, lives, spawning, game
state. Treat it as such — type it together, run it
together, play it together.

#### Walk through `make_fruit()` carefully

This is a function. Phase 3-4 covered functions, but
some kids haven't reached for them in Pygame yet. Frame:

> "We need to spawn a fruit at a random place. We could
> inline that — random x, get rect, append. But we'll do
> it many times. Wrapping it in a function makes the
> spawn logic *one place to fix.* Real game code does
> this everywhere."

#### `spawn_timer` — frame-counting timers

The pattern is canonical:

```python
spawn_timer += 1
if spawn_timer >= SPAWN_INTERVAL:
    do_thing()
    spawn_timer = 0
```

Explain the math:

> "60 frames per second. SPAWN_INTERVAL of 60 = one spawn
> per second. SPAWN_INTERVAL of 30 = two per second
> (faster). Lower number = more frequent spawns."

Show what happens with SPAWN_INTERVAL = 10. Madness.

There are real Pygame timer APIs (`pygame.time.set_timer`)
but the frame-counter version is simpler and more flexible.
We'll stick with this.

#### `if lives > 0:` gating the update

Important pattern for game state:

> "When lives reach 0, we want everything to *stop* —
> the basket can't move, fruit can't fall, no new spawns.
> But the GAME OVER text needs to show. So: gate the
> update behind `if lives > 0:`. The draw still runs
> always."

This is the simplest version of game states (next:
title screen → playing → game over in Session 12).

#### Distinguish caught-vs-missed

Two outcomes for a fruit:

- **Caught**: collides with basket → score++, remove.
- **Missed**: falls past bottom → lives--, remove.

The `elif` ordering matters:

```python
if basket_rect.colliderect(fruit_rect):
    fruits.remove(fruit)
    score += 1
elif fruit_rect.top > 500:
    fruits.remove(fruit)
    lives -= 1
```

Caught is checked first. If the fruit is *both* off-screen
AND somehow colliding (shouldn't happen, but), caught
wins.

### Common stumbles

- **Forgot `[:]`** for the loop-while-removing. Fruits
  get skipped or repeated.
- **Removed twice.** `fruits.remove(fruit)` in both
  branches by accident, then the `elif` removes a
  non-existent item. Walk through control flow.
- **`midbottom` confusion.** Thought it was `(midx, midy)`
  — it's actually `(midx, bottom_y)`. Show the difference.
- **Lives go negative.** Forgot the `if lives > 0:` gate;
  more fruit falls past after game over and lives
  decrement past zero. Add the gate.
- **Game over text doesn't appear.** Forgot to check
  `if lives <= 0:` in the draw. Or it draws but is
  hidden behind something else.
- **Player can move *during* game over.** Forgot the
  movement is inside `if lives > 0:`.
- **Fruit speed too fast.** `random.randint(3, 6)` is
  usually fine. If it feels too fast, reduce to `(2, 4)`.
- **Fruit spawns visible at top.** `center=(x, -20)`
  starts the fruit *above* the screen so it scrolls in.
  If a kid uses `(x, 0)`, the fruit appears mid-screen.
- **`KeyError` on dict access.** Maybe a kid tried
  `keys[K_LEFT]` (without `pygame.`). Walk through the
  prefix.
- **Spawn interval too small.** 1 fruit per frame =
  60 fruits per second = chaos. Suggest starting with
  60 and tuning down.

### Differentiation

- **Younger kids (9-10):** Goal is the basic collision
  test (Part A) and a simplified fruit catcher (no
  lives, just score). Skip the lives logic if it's too
  much.
- **Older kids (12+):** Push for the full fruit catcher.
  Add bombs as the stretch.
- **Advanced (any age):** Suggest:
  - Acceleration: each catch slightly increases all
    fruits' fall speed
  - Combo multiplier (3 in a row = 2x score)
  - Multiple fruit types with different point values
  - Particle effects on catch
  - High score saved to file
- **Struggling:** A kid who can't get collision working
  is the kid you focus on. Most common cause: forgot
  `colliderect`, or rects positioned wrong.

### What to watch for

- **The "I caught one!" reaction.** First successful
  catch in Part B. Real game-feel.
- **Kids playing each other's games.** Encourage. Some
  kids tune the difficulty differently — comparing is
  fun.
- **Excessive tuning.** Some kids spend 20 minutes
  tweaking SPEED. Gentle: "It's good. Add bombs?"
- **Buddies pair-debugging the spawn logic.** This is
  the trickiest piece. Encourage helping.
- **Kids who add extras the wrong way** (modify list
  while iterating without `[:]`). Catch these and walk
  through.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 6 (Pong).** Today's fruit catcher → Pong:
  - Basket → two paddles
  - Fruit → one bouncing ball
  - "Caught" → ball hits paddle, bounce
  - "Missed" → ball off-screen, point for opponent
- **Session 9 (sprite classes).** The fruit catcher's
  fruit list (rects + speeds) becomes a Group of Sprite
  instances.
- **Session 12 (game state).** Today's `if lives > 0:`
  gate becomes a proper state machine with title /
  playing / game over.
- **Phase 7 (web).** Browser games use the same
  collision concepts (bounding-box collision in canvas
  games). Today's mental model transfers.
- **Peanut butter callback opportunity:** the iterate-
  while-modifying bug is a precision moment. Computer
  did exactly what you said.

### Materials checklist

- [ ] Demo machine with Pygame + sprite assets
- [ ] Pre-built collision test (Part A)
- [ ] Pre-built fruit catcher game
- [ ] Pre-built fruit catcher with bombs (stretch)
- [ ] Projector
- [ ] Class roster
