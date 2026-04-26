## Session 9: Sprite classes and groups

*Phase 6 — Pygame · Session 9 of 14*

### What we're learning today

Your games have a lot of objects. Each fruit was a `[rect,
speed]` pair in a list. Each enemy too. As games get
bigger, this gets messy fast. Today we use Pygame's
**`Sprite`** class — one Python class per kind of
object — and **`Group`** containers that update and draw
many sprites at once. By the end you'll have refactored
the fruit catcher into a much cleaner shape, and you'll
have the production pattern that real Pygame projects
use.

This is where Phase 4's classes really pay off.

### You'll need to remember from last time

- **Classes** — Phase 4 Session 4. `class Pet:`,
  `__init__`, `self`, methods.
- **The fruit catcher** from Session 5 — basket and a list
  of falling fruit.
- **Pygame Rect** (Session 3) — `image`, `rect`, `blit`.
- **`colliderect`** (Session 5).
- **Frame loop** — input, update, draw.

---

### Part A: Your first Sprite

#### What's a Sprite?

Pygame's `pygame.sprite.Sprite` is a base class. You
create your own classes that *inherit* from it. Each
sprite holds:

- An `image` (its picture, usually a `Surface`).
- A `rect` (its position).
- An `update()` method (what it does each frame).

Then `pygame.sprite.Group` is a container. You stuff
sprites into it. The group has:

- `group.update()` — calls `update()` on every sprite.
- `group.draw(screen)` — draws every sprite to the
  screen.
- `pygame.sprite.spritecollide(sprite, group, dokill)`
  — finds collisions between a sprite and a group.

The win: instead of looping over a list and calling
update + draw + collision check yourself, **the group
does it all.**

#### Build a Player class

Open Thonny. Save a new file as `sprite_basics.py`. Type:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sprite class")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())


# Create one player and put it in a group
all_sprites = pygame.sprite.Group()
player = Player(300, 200)
all_sprites.add(player)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    
    screen.fill((100, 150, 100))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. WASD or arrows to move the player.

What's new:

- **`class Player(pygame.sprite.Sprite):`** — Player
  *inherits* from Sprite. (Phase 4 Session 4 didn't
  cover inheritance — this is a small new step. The
  parentheses say "based on this other class.")
- **`super().__init__()`** — call the parent class's
  init. Required when you inherit. Phase 4 didn't show
  this; it's a one-liner you always add.
- **`self.image`** and **`self.rect`** — the two
  attributes Pygame's Group expects. Names matter —
  Group looks for these specifically.
- **`update(self)` method** — Pygame Group calls this
  on every sprite each frame.
- **`pygame.sprite.Group()`** — make an empty group.
- **`all_sprites.add(player)`** — add a sprite to the
  group.
- **`all_sprites.update()`** — calls each sprite's
  `update()`.
- **`all_sprites.draw(screen)`** — blits each sprite.

Look at the loop. **Three lines of game logic:** event,
update, draw. The Player class holds all the *details.*

This is the production pattern.

#### Add a Coin class

```python
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect(center=(x, y))
    
    def update(self):
        pass    # coins don't move
```

Then create a few:

```python
import random

coins = pygame.sprite.Group()
for _ in range(8):
    cx = random.randint(50, 550)
    cy = random.randint(50, 350)
    coin = Coin(cx, cy)
    coins.add(coin)
    all_sprites.add(coin)    # also add to all_sprites for drawing
```

Two groups: `coins` (just the coins, for collision
checking) and `all_sprites` (everything, for drawing).

In the draw section, `all_sprites.draw(screen)` already
draws everything. No change needed there.

#### Group-based collision

Replace your old loop-based collision with:

```python
hit_coins = pygame.sprite.spritecollide(player, coins, True)
score += len(hit_coins)
```

`spritecollide(player, coins, True)`:

- Check `player` against every sprite in `coins`.
- Returns a list of the coin sprites that the player is
  touching.
- The `True` means "kill collided sprites" — they're
  removed from *all* their groups automatically.

Add a `score` variable above the loop, and a font/text
to display it (Session 5 pattern).

Save. Run. Walk over the coins. They disappear. Score
goes up. **Same game as Session 5, much less code.**

**Checkpoint:** *You have a sprite-class-based game with
a Player, multiple Coins, and group collision.* **This
is the natural stop point if class is cut short.**

---

### Part B: Refactor the fruit catcher

The Session 5 fruit catcher used lists of `[rect, speed]`
pairs. Today we re-do it with proper sprite classes.

#### Build it

```python
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Fruit catcher (sprites)")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)


class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("basket.png")
        self.rect = self.image.get_rect(midbottom=(300, 490))
        self.speed = 7
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fruit.png")
        x = random.randint(20, 580)
        self.rect = self.image.get_rect(center=(x, -20))
        self.speed = random.randint(3, 6)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 500:
            self.kill()    # remove from all groups
            global lives
            lives -= 1


# Setup
all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()

basket = Basket()
all_sprites.add(basket)

score = 0
lives = 3
spawn_timer = 0
SPAWN_INTERVAL = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if lives > 0:
        all_sprites.update()
        
        # Catch — collision check
        caught = pygame.sprite.spritecollide(basket, fruits, True)
        score += len(caught)
        
        # Spawn
        spawn_timer += 1
        if spawn_timer >= SPAWN_INTERVAL:
            new_fruit = Fruit()
            all_sprites.add(new_fruit)
            fruits.add(new_fruit)
            spawn_timer = 0
    
    # Draw
    screen.fill((180, 220, 255))
    all_sprites.draw(screen)
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (180, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (480, 10))
    
    if lives <= 0:
        over_text = font.render("GAME OVER", True, (200, 0, 0))
        rect = over_text.get_rect(center=(300, 250))
        screen.blit(over_text, rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. Same fruit catcher as Session 5 — same
gameplay, different shape inside.

What changed:

- The `Basket` class holds *both* its image AND its
  movement logic.
- The `Fruit` class holds its image AND its falling
  logic AND its "I went off-screen" handling.
- The main loop is much smaller. Three lines of update
  logic, plus spawn and collision. Compare to Session 5.
- **`self.kill()`** — a Sprite removes itself from all
  its groups. No more `coins.remove(coin_rect)`.
- **`global lives`** in `Fruit.update()` — the sprite
  modifies the outer `lives` variable. Not pretty, but
  works. (Real games would pass a game-state object to
  the sprite. We'll skip that.)

The biggest win: **adding a new fruit type is now a new
class.** No special-case handling in the main loop.

#### Stretch — add bombs as a subclass

```python
class Bomb(Fruit):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bomb.png")
        # rect is already set by parent's __init__
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 500:
            self.kill()    # bombs that fall through don't lose lives


# In spawn:
if random.random() < 0.2:    # 20% chance
    new_thing = Bomb()
else:
    new_thing = Fruit()
all_sprites.add(new_thing)
fruits.add(new_thing)
```

Bombs *inherit* from Fruit. Same falling behavior, but
different image and different "fall through" handling
(no life lost — bombs are *good* to miss).

For the catch logic, bombs should **lose a life** when
caught. Update collision:

```python
caught = pygame.sprite.spritecollide(basket, fruits, True)
for thing in caught:
    if isinstance(thing, Bomb):
        lives -= 1
    else:
        score += 1
```

`isinstance(thing, Bomb)` checks the type. Bombs lose a
life on catch; fruits add to score on catch.

#### Stretch — sprite that moves on its own

Add a class for an enemy that bounces around the screen
on its own:

```python
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect(center=(100, 100))
        self.dx = random.choice([-3, 3])
        self.dy = random.choice([-3, 3])
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0 or self.rect.right > 600:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > 500:
            self.dy = -self.dy
```

Add some to the game. The basket should avoid them.

#### Extension — refactor your Pong

Pong has three sprites — two paddles, one ball. Refactor
it:

```python
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, up_key, down_key):
        super().__init__()
        self.image = pygame.Surface((12, 80))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, 250))
        self.up_key = up_key
        self.down_key = down_key
        self.speed = 6
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[self.down_key] and self.rect.bottom < 500:
            self.rect.y += self.speed


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(350, 250))
        self.dx = 5
        self.dy = 4
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.top < 0 or self.rect.bottom > 500:
            self.dy = -self.dy
```

Notice: `pygame.Surface((12, 80))` — make a Surface of
that size (no image file needed). `.fill((255,255,255))`
paints it. Drawing-from-shapes built into the sprite.

The two paddles only differ by their position and which
keys they use — passed as constructor arguments. **One
class, two instances.** That's the win.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your refactored fruit catcher.
  Does the code feel cleaner?
- For kids who added Bomb — does inheritance feel useful?
- For kids who refactored Pong — same gameplay, same
  result?
- Does the main game loop feel smaller now?

Today you learned:

- **`pygame.sprite.Sprite`** — the base class for every
  game object.
- **`pygame.sprite.Group`** — container for many sprites.
- **`group.update()`** and **`group.draw(screen)`** —
  one call updates/draws all sprites.
- **`pygame.sprite.spritecollide(sprite, group, kill)`**
  — collision against a group.
- **`self.kill()`** — sprite removes itself.
- **Inheritance** — `class Bomb(Fruit):` makes Bomb a
  *kind of* Fruit with overrides.
- **`pygame.Surface(size)`** — a blank surface for
  drawing on (no image file needed).

The main loop **shrinks** when you use sprite classes.
That's not just style — it's how production game code
stays manageable as games grow. Tomorrow's bigger games
will use this pattern by default.

Next week: **the grid-world.** Mr. Eric's coding-puzzle
game — built on Pygame, controlled by Python code you
write. You'll play it as a user first. Week after, you'll
extend it.

### If you missed this session

Open Thonny. Then:

1. Build the basic Player + Coins example from Part A.
   Walk over the coins. Watch them disappear.

2. Refactor your fruit catcher with sprite classes (Part
   B). Same gameplay, cleaner code.

3. (Stretch) Add a Bomb class that inherits from Fruit.

About 60-90 minutes — this is a meaty session.

### Stretch and extension ideas

- **Refactor Pong** with sprite classes (above).
- **Bombs** in fruit catcher (above).
- **Bouncing enemies** that the basket must avoid.
- **Multiple fruit types** — Cherry, Apple, Banana — each
  worth different points.
- **Sprite groups for visual layering** — a `background`
  group drawn first, then `mid`, then `top`. Order
  matters.
- **A `Game` class that holds everything.** All your
  sprites and state become attributes of one Game
  instance.
- **`pygame.sprite.groupcollide(group_a, group_b, kill_a,
  kill_b)`** — two groups vs each other. Useful for "all
  bullets vs all enemies."

### What's next

Next week: **the grid-world.** Mr. Eric built a
coding-puzzle game where you control a character on a
grid by writing Python. You'll play through some
puzzles and see how the game works. The week after,
you'll extend it — add new puzzles, new abilities,
make it yours.
