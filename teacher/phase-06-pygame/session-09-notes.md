## Session 9 — Teacher Notes

*Phase 6, Pygame · Session 9 of 14 · Title: Sprite
classes and groups*

### Purpose of this session

The "production refactor" session. Five jobs, in priority
order:

1. **Land `pygame.sprite.Sprite` as the standard.**
   This is how real Pygame projects organize game
   objects. After this session, kids should default to
   sprite classes for new games.
2. **Land `Group` for management.** Update many sprites
   in one call. Draw many in one call. Collide many in
   one call. The win.
3. **Land inheritance.** `class Bomb(Fruit):` is most
   kids' first time using inheritance for real. Pay it
   off properly.
4. **Show the main-loop shrink.** Compare Session 5 and
   Session 9 versions of fruit catcher side by side.
   Sprites push detail into classes; main loop becomes
   simple.
5. **Set up Sessions 10-11 (grid-world).** The grid-world
   uses sprite classes for everything (the character,
   tiles, items). Fluency needed.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame + sprite assets.
- Pre-built sprite-classes Player + Coins example.
- Pre-built sprite-classes fruit catcher (Part B
  end-state).
- Pre-built sprite-classes Pong (the stretch refactor),
  for the "look how clean it is" demo.
- Optional: side-by-side comparison of Session 5 fruit
  catcher and Session 9 sprite version. The line-count
  difference is striking.

**Prep time:** ~25 minutes. Build all three demo programs
and run them.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 8 sound.
  Today: refactor.
- **Part A: first sprite class** (~30 min). Walk through
  Player class line by line. Add Coin class. Group
  collision. Build live.
- **Break** (~5 min).
- **Part B: refactor fruit catcher** (~35 min). Type
  together. Compare to Session 5.
- **Part B stretches** (~10 min). Bomb subclass for fast
  finishers; Pong refactor for advanced.
- **Wrap-up** (~5 min).

If running short, **the Bomb subclass and Pong refactor
can be cut.** The fruit catcher refactor is the priority.

### Teaching Part A

#### Inheritance — go slow

This is most kids' first real use of inheritance. Phase
4 Session 4 introduced classes but didn't dwell on
inheritance.

Walk through carefully:

> "`class Player(pygame.sprite.Sprite):` means our Player
> is a *kind of* Sprite. It gets all the things Sprite
> already knows how to do, *plus* whatever we add.
>
> `super().__init__()` calls the Sprite's `__init__` —
> some Sprite setup we need. Always include this when
> inheriting."

Don't go deeper than this. Inheritance is a deep topic;
the recipe is what they need.

#### `self.image` and `self.rect` are *required* names

Pygame's Group looks for these specific attributes. If
you call them `self.picture` and `self.box`, draw won't
work.

> "Two attribute names *Pygame requires*: `self.image`
> and `self.rect`. Group uses them to draw and check
> collision. Anything else you can name however you want
> — but those two are fixed."

#### `update()` is the per-frame method

Frame:

> "When you call `group.update()`, it goes through every
> sprite and calls *its* `update()` method. So put
> per-frame logic for the sprite *in* its `update()`."

The Player puts movement code in `update()`. Coin's
`update()` is empty (`pass`) because coins don't move.

#### `pygame.sprite.spritecollide` is the killer feature

Walk through the signature:

```python
hits = pygame.sprite.spritecollide(player, coins, dokill=True)
```

- First arg: a single sprite (the "thing checking").
- Second: a group of sprites to check against.
- Third: `dokill` — if True, collided sprites are
  removed from all their groups automatically.
- Returns: a list of the collided sprites.

Show the comparison to Session 5's loop:

```python
# Session 5:
for coin in coins[:]:
    if player.colliderect(coin):
        coins.remove(coin)
        score += 1

# Session 9:
hits = pygame.sprite.spritecollide(player, coins, True)
score += len(hits)
```

Two lines vs five. **Cleaner.**

### Teaching Part B

#### Walk through Basket and Fruit classes carefully

These are real, full-featured sprite classes. Each one
has:

- `__init__` with positioning and parameters.
- `update()` with the per-frame behavior.
- (For Fruit) self-removal via `kill()` when off-screen.

Type together. After each class, run the program at that
state. Iterate.

#### `self.kill()` is the cleanup move

```python
if self.rect.top > 500:
    self.kill()
```

Frame:

> "When a sprite is *done*, it removes itself. `kill()`
> takes it out of every group it belongs to. Cleanup
> done. Garbage collected by Python. Real."

This is way cleaner than tracking which sprites to remove
in the main loop.

#### `global lives` — call out the smell

The `global` keyword is genuinely awkward. Mention:

> "We're using `global lives` so the Fruit can decrement
> the outer `lives` variable. This is *not* the prettiest
> pattern. Real games would put `lives` (and `score`,
> `level`, etc.) on a `Game` class — every sprite gets a
> reference to the game and reads/writes through it.
>
> For today, `global` is fine. We've kept the example
> small. Just know there's a cleaner pattern for bigger
> games."

The Game-class approach is a stretch goal in the handout.

#### The main loop shrinks dramatically

After typing both, scroll through the new main loop:

```python
all_sprites.update()
caught = pygame.sprite.spritecollide(basket, fruits, True)
score += len(caught)
spawn_timer += 1
if spawn_timer >= SPAWN_INTERVAL:
    new_fruit = Fruit()
    all_sprites.add(new_fruit)
    fruits.add(new_fruit)
    spawn_timer = 0
```

That's the entire game logic. **Compare to Session 5.**
Show side-by-side if you can.

> "The main loop is now about *coordinating* the game.
> The classes hold the *details.* This is how real game
> code stays manageable as games get bigger."

#### Inheritance with Bomb

```python
class Bomb(Fruit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bomb.png")
```

Frame:

> "Bomb is a *kind of* Fruit. It gets Fruit's `__init__`
> (which sets the rect and speed). Then we change the
> image. That's it — Bomb falls just like Fruit because
> it inherits Fruit's update."

Then `isinstance(thing, Bomb)` for the catch logic. This
is real polymorphism; don't dwell on the word.

### Common stumbles

- **Forgot `super().__init__()`.** Sprite doesn't behave
  right; mysterious errors. Add it.
- **Renamed `self.image` to `self.picture`.** Group
  can't draw it. Reset to `image`.
- **Renamed `self.rect` similarly.** Same problem.
- **Sprite added to wrong group.** Sprite doesn't appear
  (forgot `all_sprites.add(...)`). Or doesn't get checked
  for collision.
- **`spritecollide` arguments wrong order.** First is
  the sprite, second is the group. Flipping causes
  errors.
- **`dokill=True` misunderstood.** Sprites disappear on
  first frame because the kid put it in two groups and
  `dokill` removed it. Or kept `dokill=False` and
  expected sprites to disappear.
- **Forgot `global lives`.** `UnboundLocalError`. Walk
  through.
- **`update()` not being called.** Forgot
  `all_sprites.update()` in the main loop.
- **Stale references.** Stored a sprite reference
  somewhere; sprite got `.kill()`'d; later code crashes.
  Discuss only if it comes up.
- **`isinstance(x, ClassName)`** — don't quote the class
  name. `isinstance(thing, "Bomb")` errors.

### Differentiation

- **Younger kids (9-10):** Goal is the basic Player +
  Coins example (Part A). Refactor of fruit catcher is
  a stretch. Focus on understanding `update` is called
  every frame.
- **Older kids (12+):** Push for the full fruit catcher
  refactor. Bomb subclass as stretch.
- **Advanced (any age):** Push to refactor Pong with
  sprite classes. Suggest:
  - A `Game` class that holds all sprites + state
  - Multiple sprite groups for layering (background,
    actors, UI)
  - A common base class for "things the player can
    catch" with subclasses
  - Particle effects as a sprite group
- **Struggling:** A kid who can't get the inheritance
  syntax right is the kid you focus on. Most common
  cause: forgot `super().__init__()`, or wrong attribute
  name (`self.image` vs `self.img`).

### What to watch for

- **The "wait, the main loop is so small" reaction.**
  When kids see the size difference, the win clicks.
- **Inheritance confusion.** Some kids will try to call
  parent methods directly (`Fruit.__init__(self)`)
  instead of `super().__init__()`. Both work; super is
  cleaner.
- **The "I don't see why this is better" reaction.** For
  small games, sprite classes are *more* code than the
  list-based version. Reassure: the win shows up at
  scale.
- **Buddies pair-debugging the inheritance.** Encourage.
- **Kids tempted to refactor every prior game.** Let
  them — it's good practice. Just keep one buddy on the
  shared work.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sessions 10-11 (grid-world).** Grid-world is built
  with sprite classes. Today's pattern fluent = those
  sessions land cleaner.
- **Session 12 (game state).** State machines work
  cleanly with sprites — different sprite groups per
  state.
- **Sessions 13-14 (milestone).** Their milestone games
  should default to sprite classes.
- **Phase 7 (web).** JavaScript classes have similar
  shape (`class Foo extends Bar`). Today's mental model
  transfers.
- **Real game engines.** Unity's GameObject + Component,
  Godot's Node + Script — same pattern at larger scale.
- **Peanut butter callback opportunity:** the
  `self.image` / `self.rect` *required attribute names*
  is a precision moment. Pygame literally checks for
  those names. Other names = silent failure.

### Materials checklist

- [ ] Demo machine with Pygame + sprite assets
- [ ] Pre-built Player + Coins demo
- [ ] Pre-built sprite-class fruit catcher
- [ ] Pre-built sprite-class Pong
- [ ] Optional: Session 5 fruit catcher open in another
      tab for line-count comparison
- [ ] Projector
- [ ] Class roster
