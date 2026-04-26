## Session 5: Collision detection

*Phase 6 — Pygame · Session 5 of 14*

### What we're learning today

Last week you faked "touching" with a distance check.
Today you'll do it **properly**: Pygame's built-in
collision methods. Two rects either overlap or they
don't — `rect.colliderect(other)` answers in one line.
You'll use this to build a "falling fruit catcher" mini
game with real collisions, scoring, and lives. By the end
of class you'll be ready for Session 6 — Pong.

### You'll need to remember from last time

- **Sprites and rects** (Session 3).
- **Keyboard input** (Session 4) — events vs polling.
- **Lists of rects** (Session 3) — many of the same
  thing.
- **The frame loop**.

---

### Part A: Real collision detection

#### `rect.colliderect(other_rect)`

The simplest collision check in Pygame:

```python
if player_rect.colliderect(coin_rect):
    print("Touching!")
```

Returns `True` if the two rectangles overlap, `False`
otherwise. That's it.

This is **rectangle vs rectangle.** Pygame compares the
boxes — not the actual pixels. If your sprite has empty
space inside its rect (most do), the rect catches it
before the visible pixel does. That's normal and fine for
most games.

For pixel-perfect collision you'd need `pygame.mask` —
which we won't cover. Rect collision is what most games
use.

#### Two rectangles, one collision

Open Thonny. Save a new file as `collision.py`. Type:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Collision test")
clock = pygame.time.Clock()

player_image = pygame.image.load("player.png")
coin_image = pygame.image.load("coin.png")

player_rect = player_image.get_rect(center=(300, 200))
coin_rect = coin_image.get_rect(center=(450, 200))
SPEED = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += SPEED
    player_rect.clamp_ip(screen.get_rect())
    
    # Check collision
    touching = player_rect.colliderect(coin_rect)
    
    # Draw
    screen.fill((30, 30, 50) if not touching else (80, 50, 50))
    screen.blit(coin_image, coin_rect)
    screen.blit(player_image, player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. Move the player onto the coin. The
**background turns red** when you're touching. Move off —
back to dark blue.

That's collision. One line: `player_rect.colliderect(coin_rect)`.

#### Many things — `colliderect` in a list

For a list of objects (like the coins from last
session), loop through and check each:

```python
for coin_rect in coins[:]:    # copy because we modify
    if player_rect.colliderect(coin_rect):
        coins.remove(coin_rect)
        score += 1
```

There's also a built-in: `rect.collidelist(list_of_rects)`
returns the *index* of the first rect in the list that
collides, or `-1` if none. Useful sometimes. The for-loop
version is more flexible (you can react per-collision).

**Checkpoint:** *You have a sprite that moves and reacts
when it touches another sprite.* **This is the natural
stop point if class is cut short.**

---

### Part B: Falling fruit catcher

A small game. Fruit falls from the top. You move a basket
left and right at the bottom. Catch the fruit (collide) —
score goes up. Miss — lose a life. Lose 3 lives — game
over.

#### Build it

```python
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Fruit catcher")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

basket_image = pygame.image.load("basket.png")    # or any sprite
fruit_image = pygame.image.load("fruit.png")      # or any sprite

basket_rect = basket_image.get_rect(midbottom=(300, 490))
SPEED = 7

# Each fruit: a rect + falling speed
fruits = []

def make_fruit():
    x = random.randint(20, 580)
    fruit_rect = fruit_image.get_rect(center=(x, -20))
    speed = random.randint(3, 6)
    return [fruit_rect, speed]

# Spawn first fruit
fruits.append(make_fruit())

score = 0
lives = 3
spawn_timer = 0
SPAWN_INTERVAL = 60    # frames between spawns (1 second)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if lives > 0:
        # Move basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            basket_rect.x -= SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            basket_rect.x += SPEED
        basket_rect.clamp_ip(screen.get_rect())
        
        # Move fruits down + check catches/misses
        for fruit in fruits[:]:
            fruit_rect, speed = fruit
            fruit_rect.y += speed
            
            if basket_rect.colliderect(fruit_rect):
                fruits.remove(fruit)
                score += 1
            elif fruit_rect.top > 500:
                fruits.remove(fruit)
                lives -= 1
        
        # Spawn new fruits
        spawn_timer += 1
        if spawn_timer >= SPAWN_INTERVAL:
            fruits.append(make_fruit())
            spawn_timer = 0
    
    # Draw
    screen.fill((180, 220, 255))
    for fruit_rect, _ in fruits:
        screen.blit(fruit_image, fruit_rect)
    screen.blit(basket_image, basket_rect)
    
    score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_surface = font.render(f"Lives: {lives}", True, (180, 0, 0))
    screen.blit(score_surface, (10, 10))
    screen.blit(lives_surface, (480, 10))
    
    if lives <= 0:
        over_surface = font.render("GAME OVER", True, (200, 0, 0))
        rect = over_surface.get_rect(center=(300, 250))
        screen.blit(over_surface, rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. Catch fruit with the basket. Don't lose all
your lives.

What's new since last session:

- **`get_rect(midbottom=(300, 490))`** — positions the
  rect's bottom-middle at that point. Useful for "stand
  on the floor" placement.
- **List of `[rect, speed]` pairs** — each fruit has its
  own falling speed.
- **`make_fruit()` function** — encapsulates fruit
  spawning. Cleaner than inlining the random logic.
- **`spawn_timer`** — counts frames between spawns.
  Triggers `make_fruit()` every `SPAWN_INTERVAL` frames.
  This is a **timer**, the game-dev pattern for "do
  something every N seconds."
- **Lives countdown** — fruit that falls past the bottom
  costs a life.
- **`if lives > 0:` around the update logic** — when
  lives = 0, the game freezes (no movement, no spawning).
  Only the draw still runs (so we can show GAME OVER).
- **Two text labels** — score on the left, lives on the
  right.

You just built a complete arcade-style game with
collision, scoring, lives, spawning, and a game-over
state. **This is a real game.**

#### Stretch — restart on game over

When game over, press R to restart:

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_r and lives <= 0:
        # Reset state
        lives = 3
        score = 0
        fruits = []
        spawn_timer = 0
```

#### Stretch — different fruit types

Use a list of images. Random choice each spawn:

```python
fruit_images = [
    pygame.image.load("apple.png"),
    pygame.image.load("banana.png"),
    pygame.image.load("cherry.png"),
]

def make_fruit():
    image = random.choice(fruit_images)
    x = random.randint(20, 580)
    fruit_rect = image.get_rect(center=(x, -20))
    speed = random.randint(3, 6)
    return [image, fruit_rect, speed]
```

Update the loop to handle the extra `image` value in each
fruit entry, and blit the fruit's own image instead of a
shared `fruit_image`.

#### Stretch — bombs!

Some falling things are **bombs** — catching one costs a
life. Different sprite (a black circle, a red X). When
the player catches one, lose a life instead of gaining
score.

#### Extension — speed up over time

Every 10 score, increase fall speed slightly. Or make
SPAWN_INTERVAL shorter. The game gets harder as you go
— classic arcade design.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — what's your high score?
- Did the GAME OVER feel real? You *lose* something now.
- For the kids who added bombs — was it harder or
  easier than catching?
- Anyone notice that you can move the basket while a
  fruit is mid-fall? That's the frame loop in action —
  every frame, the basket moves AND the fruit falls AND
  collisions are checked.

Today you learned:

- **`rect.colliderect(other_rect)`** — the standard
  collision check in Pygame.
- **Looping over a list to check collisions** — the
  pattern for many objects.
- **`midbottom`, `topleft`, etc.** — positioning by edges
  and corners.
- **Spawning over time** — frame timers + `random` for
  procedural content.
- **Game state** — `lives` and `score` as state
  variables; `if lives > 0:` to gate the update.
- **A complete arcade game** — collision, lives, scoring,
  game over.

Today is the conceptual peak of Phase 6 fundamentals.
You now have the four core ingredients of any 2D game:
**draw, move, input, collide.** Combine them in
different shapes and you get any genre.

### If you missed this session

Open Thonny. You'll need a basket sprite and a fruit
sprite (or any two PNGs).

1. Build the basic collision example from Part A. Verify
   the background changes when you touch the coin.

2. Build the fruit catcher from Part B. Adjust SPEED,
   SPAWN_INTERVAL, and starting lives to taste.

3. (Stretch) Add bombs or different fruit types.

About 45-60 minutes. By the end you should have a working
fruit catcher.

### Stretch and extension ideas

- **Bombs** that cost lives.
- **Power-ups** — a "double points" fruit that grants 2
  score for one catch.
- **Combo system** — catching 3 in a row gives bonus
  points.
- **Background music** — Session 8 covers this properly,
  but you can sneak-preview it.
- **Particle effect on catch** — small dots appear at the
  catch position for half a second.
- **High score saved to file** — `with open("highscore.txt",
  "w") as f: f.write(str(score))`. Load on startup.
  Persistence callback to Phase 5 Session 6.
- **Two players** — two baskets, two scores, two lives.
  WASD vs arrows.
- **Falling enemies that target the basket** — they steer
  toward you while falling.

### What's next

Next week is the big one: **Pong, built together.** Two
paddles, one ball, a score. We'll combine everything
from Sessions 1-5 into one complete classic game. Bring
your enthusiasm.
