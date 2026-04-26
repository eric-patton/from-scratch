## Session 4: Movement and the keyboard

*Phase 6 — Pygame · Session 4 of 14*

### What we're learning today

You can put a sprite on screen. Today we make it
**listen.** Specifically, to the keyboard. By the end you
can move a sprite around with WASD or arrow keys — and
you'll understand the two ways Pygame handles input
(events and continuous polling) and when to use each.
This is the foundation for almost every game with a
playable character.

### You'll need to remember from last time

- **Sprites** — `pygame.image.load`, `screen.blit`, the
  `Rect` class.
- **`get_rect(center=(x, y))`** to position by center.
- **`rect.move_ip(dx, dy)`** to move a rect.
- **The frame loop** — read input, update, draw.
- **Conditionals** — `if`, `elif`, `else`.

---

### Part A: Two ways to read the keyboard

Pygame gives you **two different APIs** for the keyboard,
and they're for different jobs. Knowing when to use each
saves real bugs.

#### Way 1: Events — for moments

Last sessions you used:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

The `for event in pygame.event.get()` loop reads every
event that happened *since the last frame.* The user
clicked? Event. User pressed a key? Event. User released
a key? Event.

Use events when you care about a **moment** — the instant
something happened. Examples:

- "When the user presses **space**, fire a bullet."
  (One bullet per press, not 60 per second.)
- "When the user presses **escape**, pause the game."
- "When the user clicks the mouse, drop a marker."

Add to the event loop:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Space was just pressed!")
        if event.key == pygame.K_ESCAPE:
            running = False
```

`KEYDOWN` is the moment a key starts being pressed.
`KEYUP` is the moment it's released. `event.key` tells
you *which* key.

The constants are `pygame.K_a`, `pygame.K_b`, ...
`pygame.K_SPACE`, `pygame.K_ESCAPE`, `pygame.K_LEFT`,
`pygame.K_RIGHT`, `pygame.K_UP`, `pygame.K_DOWN`,
`pygame.K_RETURN` (enter), and so on.

#### Way 2: Polling — for "is it down right now?"

For **continuous** actions like "move while the key is
held," events don't work cleanly. (Holding a key only
sends one KEYDOWN, plus repeats much later.)

Instead, **poll** the keyboard each frame:

```python
keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:
    player_rect.move_ip(-5, 0)
if keys[pygame.K_RIGHT]:
    player_rect.move_ip(5, 0)
```

`pygame.key.get_pressed()` returns a special dict-like
object. Index into it with a key constant — get `True`
(currently pressed) or `False` (not pressed).

This runs **every frame.** Hold the left arrow → 60
moves per second. Release → stop.

#### Rule of thumb

- **One-shot action?** Use event. (Fire, pause, jump.)
- **Continuous action?** Use `get_pressed`. (Move, hold,
  charge.)

#### Build it — a movable sprite

Open Thonny. Save a new file as `movement.py`. Type:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Move me!")
clock = pygame.time.Clock()

player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect(center=(300, 200))
SPEED = 5

running = True
while running:
    # 1. Read input — events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # 2. Read input — held keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += SPEED
    
    # 3. Draw
    screen.fill((100, 150, 100))
    screen.blit(player_image, player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Replace `"player.png"` with your sprite filename.

Save. Run. **Press the arrow keys or WASD.** The sprite
moves. Press escape to quit.

What's new:

- Both **WASD and arrows** work — `if keys[A] or keys[B]`.
  Real games support multiple control schemes.
- **`SPEED = 5`** at the top. A constant — uppercase
  signals "this is a value I might tune." Easy to find
  and change.
- **Negative y for up.** Remember y goes *down*; subtract
  to move up.
- **`player_rect.x -= SPEED`** is shorthand for
  `player_rect.x = player_rect.x - SPEED`.

#### Stay on screen

Right now you can walk off the edge and disappear. Add
boundary checks:

```python
# After all the movement code, before draw:
if player_rect.left < 0:
    player_rect.left = 0
if player_rect.right > 600:
    player_rect.right = 600
if player_rect.top < 0:
    player_rect.top = 0
if player_rect.bottom > 400:
    player_rect.bottom = 400
```

Notice we use `left`, `right`, `top`, `bottom` — Rect
properties from Session 3. Setting `left = 0` snaps the
rect's left edge to 0.

Save. Run. The sprite stops at the edges. **Stays on
screen, no matter how long you hold the key.**

**Checkpoint:** *You have a sprite that moves with WASD
or arrow keys, stays on screen, and quits with escape.*
**This is the natural stop point if class is cut short.**

---

### Part B: A small game — collect the items

Time to combine sprites + keyboard + lists into a tiny
game. The base goal: a player you control, a few items
scattered on screen, and a way to know if you "got" one
(by walking on top of it).

We'll do the *touching* part properly next session
(collision detection). For today, we'll fake it with a
simple distance check.

#### Build it

```python
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Collector")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

player_image = pygame.image.load("player.png")
coin_image = pygame.image.load("coin.png")
SPEED = 5

player_rect = player_image.get_rect(center=(50, 200))

# Make 8 coins at random positions
coins = []
for i in range(8):
    cx = random.randint(50, 550)
    cy = random.randint(50, 350)
    coin_rect = coin_image.get_rect(center=(cx, cy))
    coins.append(coin_rect)

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += SPEED
    
    # Stay on screen
    player_rect.clamp_ip(screen.get_rect())
    
    # Check for "collection" — distance check
    for coin_rect in coins[:]:    # iterate over a copy
        dx = player_rect.centerx - coin_rect.centerx
        dy = player_rect.centery - coin_rect.centery
        if dx * dx + dy * dy < 40 * 40:    # within 40 pixels
            coins.remove(coin_rect)
            score += 1
    
    # Draw
    screen.fill((100, 150, 100))
    for coin_rect in coins:
        screen.blit(coin_image, coin_rect)
    screen.blit(player_image, player_rect)
    
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))
    
    if len(coins) == 0:
        win_surface = font.render("You got them all!", True, (255, 255, 0))
        screen.blit(win_surface, (200, 200))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. Walk around and collect all the coins. Score
goes up. When you collect the last one, "You got them
all!" appears.

Quite a bit going on:

- **`player_rect.clamp_ip(screen.get_rect())`** — keeps
  the player rect inside the screen rect. Cleaner than
  the four `if` boundaries from Part A.
- **`coins[:]`** — `[:]` makes a copy of the list. We
  loop over the copy because we're *removing from the
  original* inside the loop. Modifying a list while
  looping over it directly causes weird bugs.
- **Distance check:** `dx*dx + dy*dy < 40*40` is the
  Pythagorean-without-square-root version of "within 40
  pixels." Faster than calling `math.sqrt`.
- **`f"Score: {score}"`** — f-string from Phase 3, drawn
  with `font.render`.
- **Win text** when no coins remain.

You just built a tiny game with a player, items, scoring,
and a win condition. **You're a game designer.**

#### Stretch — add enemies

Add a few enemy sprites that move on their own. If the
player gets too close, **lose**.

```python
enemy_image = pygame.image.load("enemy.png")
enemies = []
for i in range(3):
    ex = random.randint(100, 500)
    ey = random.randint(100, 300)
    enemy_rect = enemy_image.get_rect(center=(ex, ey))
    enemies.append([enemy_rect, random.choice([-2, 2]), random.choice([-2, 2])])

# Inside the loop, in update:
for enemy in enemies:
    enemy_rect, edx, edy = enemy
    enemy_rect.x += edx
    enemy_rect.y += edy
    if enemy_rect.left < 0 or enemy_rect.right > 600:
        enemy[1] = -edx
    if enemy_rect.top < 0 or enemy_rect.bottom > 400:
        enemy[2] = -edy
    
    # Did the enemy catch the player?
    dx = player_rect.centerx - enemy_rect.centerx
    dy = player_rect.centery - enemy_rect.centery
    if dx*dx + dy*dy < 40*40:
        running = False
        print("You lose!")

# Draw enemies in the draw section:
for enemy_rect, _, _ in enemies:
    screen.blit(enemy_image, enemy_rect)
```

Now you have a game with **risk and reward.**

#### Stretch — diagonal speed fix

If you press left + up at the same time, the player moves
faster diagonally than horizontally. (Think Pythagoras —
moving 5 in x AND 5 in y is moving ~7 along the diagonal.)

A simple fix: normalize the diagonal speed.

```python
import math

dx, dy = 0, 0
if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    dx -= 1
if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    dx += 1
if keys[pygame.K_UP] or keys[pygame.K_w]:
    dy -= 1
if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    dy += 1

# Normalize diagonal
if dx != 0 and dy != 0:
    dx *= 0.707    # 1 / sqrt(2)
    dy *= 0.707

player_rect.x += dx * SPEED
player_rect.y += dy * SPEED
```

Now diagonal movement is the same speed as straight.

#### Extension — restart on win

When all coins are collected, refill them and reset the
score. Endless mode!

```python
if len(coins) == 0:
    for i in range(8):
        cx = random.randint(50, 550)
        cy = random.randint(50, 350)
        coin_rect = coin_image.get_rect(center=(cx, cy))
        coins.append(coin_rect)
    # could also: SPEED += 1  to make it harder each round
```

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your collector. How many coins did
  you set?
- For the kids who added enemies — was it harder? Did you
  lose to your own enemies?
- Anyone notice the diagonal-speed bug?
- Did the **events vs polling** distinction make sense?
  Can anyone name a one-shot action vs a continuous one?

Today you learned:

- **Two input APIs:** events (for moments) and
  `get_pressed` (for held keys).
- **Key constants** — `pygame.K_LEFT`, `pygame.K_a`, etc.
- **WASD or arrows** as alternate controls.
- **Boundary clamping** with `Rect.clamp_ip`.
- **Distance checks** as a stand-in for collision (real
  collision is next session).
- **List-while-modifying** trick: `for x in coins[:]:`.
- **A complete tiny game** — player, items, score, win
  condition.

Next week we make collisions *proper* — `rect.colliderect`
— and that opens up Pong, our first big game build.

### If you missed this session

Open Thonny. You'll need a player sprite and a coin
sprite (or any two PNGs).

1. Build the basic movable-player example from Part A
   first. WASD or arrows. Make sure boundary clamping
   works.

2. Build the collector game from Part B. Adjust number
   of coins, position, and SPEED to taste.

3. (Stretch) Add enemies.

About 45-60 minutes. By the end you should have a working
collector game.

### Stretch and extension ideas

- **Enemies that chase the player.** Compute direction
  from enemy to player each frame, move the enemy
  slightly in that direction.
- **Multiple players** — WASD for player 1, arrows for
  player 2, two players, two scores.
- **Sprite faces direction.** When moving left, flip the
  player image. (`pygame.transform.flip`.)
- **Sound effect on collection.** (We'll do sound
  properly in Session 8.)
- **Speed-up over time** — each second, increase SPEED.
- **Random spawn timing** — coins appear over time, not
  all at once.
- **Pause menu** — press P to pause; the game state
  freezes until P is pressed again.

### What's next

Next week: **collision detection.** The proper way for
sprites to know they've touched. Then we use it to build
Pong.
