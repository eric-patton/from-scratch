## Session 4 — Teacher Notes

*Phase 6, Pygame · Session 4 of 14 · Title: Movement and
the keyboard*

### Purpose of this session

The keyboard input session — and the first "small game."
Five jobs, in priority order:

1. **Land the events vs polling distinction.** This is
   the conceptual hook of the session. Events for moments,
   polling for held keys. Wrong choice = bugs that "feel"
   broken (jump only fires on the first frame; movement
   only happens once per press).
2. **Land WASD/arrow control.** The standard control
   scheme of every PC game. Make it real.
3. **Land the `Rect.clamp_ip(screen.get_rect())` pattern**
   for keeping things on screen. Clean and reusable.
4. **Build a tiny complete game.** Player + items + score
   + win condition is *a real game.* The first one in
   Phase 6.
5. **Set up Session 5 (collision).** Today we faked
   collision with distance. Next we use it properly.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame + sprite assets.
- Pre-built movable-player example.
- Pre-built collector game.
- Pre-built collector with enemies (the stretch).

**Prep time:** ~20 minutes. The collector game is real
code; build and play it once before class.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Sessions 1-3.
  Today: input.
- **Part A: events vs polling** (~10 min). Conceptual
  framing on the board.
- **Part A: build movable player** (~20 min). Type
  together, run, test WASD + arrows + boundaries.
- **Break** (~5 min).
- **Part B: collector game** (~35 min). Type together,
  walk through the new pieces (clamp_ip, list-while-
  modifying, distance check).
- **Part B: stretches** (~10 min). Enemies, diagonal
  fix.
- **Wrap-up** (~5 min).

If running short, **the diagonal speed fix can be cut.**
The complete collector game is the priority.

### Teaching Part A

#### Events vs polling — frame it on the board

Draw two columns:

```
EVENTS                          POLLING
"Did X just happen?"            "Is X happening RIGHT NOW?"
                                
Use for:                        Use for:
  Fire bullet                     Move character
  Pause/unpause                   Aim turret
  Jump (one jump per press)       Charge weapon (hold to charge)
  Click button                    Hold to crouch

How it works:                   How it works:
  pygame.event.get()              pygame.key.get_pressed()
  -> list of events that          -> dict-like, True/False
     happened this frame             for each key right now
```

This is the conceptual peg. Drill it.

#### The held-key trap

If you don't have this conceptual model, kids try to use
KEYDOWN events for movement:

```python
# WRONG:
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        player_rect.x -= 5
```

This moves the player **once per press.** Hold the key
— player still moves once. Release and re-press to move
again.

When a kid does this (and several will), use it as the
teaching moment. "Right — events fire once per press.
You want the key to *keep working* while held. Use
`get_pressed`."

#### Why support both WASD and arrows

Two reasons:

1. Real games do. Players have preferences.
2. Demonstrates `if X or Y` — a real Boolean pattern.

Mention briefly; don't dwell.

#### `clamp_ip` — the elegant boundary check

The four-`if` boundary check is fine but verbose. The
one-liner:

```python
player_rect.clamp_ip(screen.get_rect())
```

`clamp_ip` clamps a rect to fit inside another rect. The
"in place" suffix means it modifies the rect directly.
`screen.get_rect()` returns a rect for the whole screen
(starts at 0,0, size = screen size).

Show both versions. Let kids prefer whichever reads
better to them. The four-`if` is more explicit about
what's happening; `clamp_ip` is shorter.

### Teaching Part B

#### The collector game is the heart

This is the first "real game" in Phase 6 (and arguably
the first since Phase 3's Hangman). Give it the time it
deserves. Type it together on the projector. Pause to
discuss the new pieces:

#### `coins[:]` — list copy for safe iteration

This is a real Python idiom. Frame it:

> "We're looping over `coins` and *removing* items as we
> go. That confuses Python — the list is changing under
> the loop. The fix: loop over a *copy* (`coins[:]`),
> remove from the original."

Some kids will ask why. Real answer:

> "Lists are like an ordered container. As you remove
> items, the indexes shift. The loop's index gets out of
> sync. Easier to loop over a copy."

#### Distance check as collision-substitute

The Pythagorean check (`dx*dx + dy*dy < r*r`) is **circle
collision** — sprites are treated as circles. Works fine
for round-ish things. Square things (rectangles) need
real rect collision (next session).

Frame it:

> "We're treating the player and coin as *circles* —
> within 40 pixels = touching. Real game-developer trick.
> Next session we'll do *rectangle* collision, which is
> what most 2D games actually use."

Why no `math.sqrt`? Square root is slow. Comparing the
*squares* of distances gives the same answer faster.
Mention briefly; advanced kids will appreciate.

#### Win condition

The "You got them all!" text is the simplest possible win
state. Real games have title screens, game-over screens,
restart logic — that's Session 12.

### Common stumbles

- **Movement only fires once per press.** Used KEYDOWN
  events instead of `get_pressed`. Walk through the
  difference.
- **Player gets stuck off-screen.** Clamp not applied,
  or applied at wrong spot in loop. Apply *after*
  movement, *before* draw.
- **Coins don't disappear when "collected".** Forgot to
  call `coins.remove(coin_rect)`. Or removed from a copy
  by accident.
- **`RuntimeError: dictionary changed size during
  iteration`** (or similar). Modifying a list while
  looping over it without the `[:]` copy trick. Add the
  `[:]`.
- **Diagonal feels too fast.** Real bug — that's what the
  diagonal stretch addresses.
- **Sprite goes through walls.** Boundary check missing.
  Add it.
- **`pygame.K_LEFT` doesn't work.** Used uppercase wrong
  (`pygame.K_left`) or forgot the `pygame.` prefix. Walk
  through.
- **Score starts at 0 then jumps to many** — likely the
  collision is firing every frame the player overlaps,
  not just once. The `coins.remove(coin_rect)` *also*
  prevents the loop from re-counting; check that's
  happening.
- **`UnboundLocalError`-style issues** if they extracted
  enemy data wrong. Walk through tuple unpacking
  patiently.

### Differentiation

- **Younger kids (9-10):** Goal is the basic movable
  player + boundary clamping. Collector game is a
  stretch.
- **Older kids (12+):** Push for the full collector game
  + enemies. The "lose state" feels real to them.
- **Advanced (any age):** Suggest:
  - Enemies that *chase* the player (compute direction
    each frame)
  - Power-ups that grant temporary speed boost
  - Multiple item types with different point values
  - Animation — sprite alternates between two poses while
    moving
  - Two-player mode (different keys for each player)
- **Struggling:** A kid stuck on the basic movable player
  is the kid you focus on. Most common cause: confused
  events vs polling, or wrong key constant.

### What to watch for

- **The "I made a game" reaction.** When a kid finishes
  the collector and beats their own coin field. Real
  game-feel.
- **Buddies playing each other's games.** Encourage. Let
  them rate each other's coin field difficulty.
- **Excessive speed values.** Some kids set `SPEED = 50`
  and the player teleports. Suggest 5-10 as a sane range.
- **The "wait, why does diagonal feel weird?" reaction.**
  Some kids notice it. Acknowledge — that's a real thing.
  Show them the fix.
- **Buddies trading control schemes.** Some kids prefer
  arrows, others WASD. Both work. Real player preference.
- **Frustration with the events-vs-polling distinction.**
  Some kids will conflate them for a while. Patient
  re-explanation.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 5 (collision).** Today's distance check is
  approximate. Real `rect.colliderect` is precise.
- **Session 6 (Pong).** Pong = two paddles (today's
  movement, but constrained to one axis), one ball, one
  score (today's pattern), one win condition. Today gets
  us 70% there.
- **Session 9 (sprite classes).** The collector's
  pattern (player rect, coin rects, enemy data) wraps
  into Sprite classes.
- **Phase 7 (web).** Browser keyboard events have a
  similar two-API split (`keydown`/`keyup` events vs.
  tracking pressed keys yourself). Today's mental model
  transfers.
- **Peanut butter callback opportunity:** the events-vs-
  polling confusion is *the* precision moment of Phase 6.
  Wrong API = "broken" game that's actually doing exactly
  what was asked.

### Materials checklist

- [ ] Demo machine with Pygame + sprite assets
- [ ] Pre-built movable player demo
- [ ] Pre-built collector game
- [ ] Pre-built collector with enemies (stretch)
- [ ] Optional: handout / whiteboard with the events-vs-
      polling table
- [ ] Projector
- [ ] Class roster
