## Session 6: Build Pong together

*Phase 6 — Pygame · Session 6 of 14*

### What we're learning today

Today we build **Pong** — the first commercial video game,
released in 1972, and still a perfect example of game
design. Two paddles, one ball, a score. We'll build it
together in **six steps,** each one running and playable
before we move on. By the end of class, you'll have a
complete two-player game.

This is the first big build of Phase 6 — combining the
frame loop, drawing, input, and collision into one
working game.

### You'll need to remember from last time

- **The frame loop** (Session 1).
- **`pygame.draw.rect`** and `circle` (Session 2).
- **The Rect class** (Session 3) — `x`, `y`, `width`,
  `height`, `center`, `move_ip`, `clamp_ip`.
- **`get_pressed`** for held keys (Session 4).
- **`rect.colliderect`** (Session 5).
- **`f"text {variable}"`** strings.

---

### Part A: Build Pong, step by step

Open Thonny. Save a new file as `pong.py`.

We'll build in six steps. **Run after every step.**
Don't skip — each step builds on the one before.

#### Step 1 — The window and the loop

Standard Pygame setup:

```python
import pygame

pygame.init()
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. A black window with the title "Pong."

What's slightly new:

- **`WIDTH, HEIGHT = 700, 500`** — Python tuple unpacking
  on a single line. Two variables in one assignment.
- **`WHITE`, `BLACK` constants** — uppercase signals
  "named value, won't change." Easier to read than raw
  RGB tuples scattered everywhere.

#### Step 2 — Two paddles

Two paddles, one on each side. Just rectangles drawn with
`pygame.draw.rect`.

Above the loop:

```python
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 80

left_paddle = pygame.Rect(40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
```

In the draw section:

```python
pygame.draw.rect(screen, WHITE, left_paddle)
pygame.draw.rect(screen, WHITE, right_paddle)
```

Save. Run. Two white paddles, one on each side, vertically
centered.

What's new:

- **`pygame.Rect(x, y, w, h)`** — create a Rect directly,
  not from an image. We'll use it for the paddle's shape
  AND its collision box.
- **`HEIGHT // 2 - PADDLE_HEIGHT // 2`** — the math to
  center vertically. `//` is integer division (whole
  numbers). 500 // 2 = 250, 80 // 2 = 40, so paddle starts
  at y = 210 (center on the screen's middle).

#### Step 3 — Move the paddles

Left paddle: W (up) and S (down).
Right paddle: ↑ (up) and ↓ (down).

In the loop, after the event handling:

```python
PADDLE_SPEED = 6

keys = pygame.key.get_pressed()
if keys[pygame.K_w] and left_paddle.top > 0:
    left_paddle.y -= PADDLE_SPEED
if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
    left_paddle.y += PADDLE_SPEED
if keys[pygame.K_UP] and right_paddle.top > 0:
    right_paddle.y -= PADDLE_SPEED
if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
    right_paddle.y += PADDLE_SPEED
```

Save. Run. Hold W or S — left paddle moves. Hold ↑ or ↓ —
right paddle moves. Both stay on screen because of the
`top > 0` and `bottom < HEIGHT` checks.

#### Step 4 — The ball

A bouncing ball — like Session 1, but for a circle.

Above the loop:

```python
BALL_RADIUS = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5
ball_dy = 4
```

In update (after paddle movement):

```python
ball_x += ball_dx
ball_y += ball_dy

# Bounce off top and bottom
if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
    ball_dy = -ball_dy
```

In draw:

```python
pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
```

Save. Run. The ball flies across, bounces off the top and
bottom, and disappears off the right edge. (We'll deal
with that in Step 6.)

#### Step 5 — Bounce off paddles

Now collision. The ball needs a `Rect` to collide with.

Replace your ball position with a Rect-based version:

Above the loop, change to:

```python
BALL_SIZE = 20
ball_rect = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)
ball_rect.center = (WIDTH // 2, HEIGHT // 2)
ball_dx = 5
ball_dy = 4
```

In update, replace the position math with rect math:

```python
ball_rect.x += ball_dx
ball_rect.y += ball_dy

# Bounce off top and bottom
if ball_rect.top < 0 or ball_rect.bottom > HEIGHT:
    ball_dy = -ball_dy

# Bounce off paddles
if ball_rect.colliderect(left_paddle) or ball_rect.colliderect(right_paddle):
    ball_dx = -ball_dx
```

In draw, change the circle to a rect (or keep it as a
circle drawn at the rect's center — your choice):

```python
pygame.draw.rect(screen, WHITE, ball_rect)
# OR
# pygame.draw.circle(screen, WHITE, ball_rect.center, BALL_SIZE // 2)
```

Save. Run. The ball now **bounces off the paddles!**
Move the paddles to intercept. This is starting to feel
like a real game.

There's a subtle bug here that real Pong programs deal
with: if the ball is moving fast and the paddle is
positioned just so, the ball can get *stuck* inside the
paddle (the bounce flips direction every frame, and the
ball can't escape). We'll ignore this for now — it's rare
at low speeds. Real Pong does extra logic to push the
ball back out of the paddle when this happens.

#### Step 6 — Score

When the ball goes off the left edge, **right player
scores.** When it goes off the right, **left player
scores.** Then reset the ball to the middle.

Above the loop:

```python
left_score = 0
right_score = 0
font = pygame.font.SysFont("Arial", 60)

def reset_ball():
    ball_rect.center = (WIDTH // 2, HEIGHT // 2)
```

In update, after the paddle bounce check:

```python
# Score: ball off the left or right edge
if ball_rect.right < 0:
    right_score += 1
    reset_ball()
    ball_dx = abs(ball_dx)    # send it right (toward the loser)
if ball_rect.left > WIDTH:
    left_score += 1
    reset_ball()
    ball_dx = -abs(ball_dx)
```

In draw, after the paddles and ball:

```python
left_text = font.render(str(left_score), True, WHITE)
right_text = font.render(str(right_score), True, WHITE)
screen.blit(left_text, (WIDTH // 4, 20))
screen.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width(), 20))
```

Save. Run. **You have Pong.** Score appears at the top.
Ball resets when someone scores. Two players can play
against each other.

A few details:

- **`abs(ball_dx)`** = absolute value (always positive).
  After resetting, send the ball *toward* the loser
  (positive dx = right, negative = left).
- **Centered scores** with two different alignment tricks
  — left score positioned by left edge, right score
  positioned by right edge.

**Checkpoint:** *You have a working two-player Pong game
with paddles, a bouncing ball, and a score.* **This is
the natural stop point if class is cut short. (Today's
goal.)**

---

### Part B: Make Pong yours

Time to add polish. Pick any of these — or invent your
own.

#### Stretch — speed up over time

Each paddle bounce, slightly increase ball speed:

```python
if ball_rect.colliderect(left_paddle) or ball_rect.colliderect(right_paddle):
    ball_dx = -ball_dx
    # Speed up
    if ball_dx > 0:
        ball_dx += 0.5
    else:
        ball_dx -= 0.5
    if ball_dy > 0:
        ball_dy += 0.3
    else:
        ball_dy -= 0.3
```

(Note: with floats now, `ball_rect.x` will quietly round.
Fine for this game.)

Reset speed in `reset_ball()` so a new round starts at
normal speed.

#### Stretch — ball direction depends on where it hit

In real Pong, hitting the ball with the *top* of the
paddle sends it up; the *bottom* sends it down. Better
gameplay:

```python
if ball_rect.colliderect(left_paddle):
    ball_dx = abs(ball_dx)    # always go right after left paddle
    # vertical based on where it hit
    relative = (ball_rect.centery - left_paddle.centery) / (left_paddle.height / 2)
    ball_dy = relative * 8

if ball_rect.colliderect(right_paddle):
    ball_dx = -abs(ball_dx)
    relative = (ball_rect.centery - right_paddle.centery) / (right_paddle.height / 2)
    ball_dy = relative * 8
```

The math: `relative` is between -1 (top of paddle) and +1
(bottom). Multiplied by 8 = ball y-speed between -8 and
+8.

#### Stretch — center line

A dashed line down the middle (cosmetic):

```python
for y in range(0, HEIGHT, 30):
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, y, 4, 15))
```

Add to draw section. Looks like real Pong.

#### Stretch — winning the game

Game ends at 10 points. Show a win screen.

Above the loop:

```python
WIN_SCORE = 10
game_over = False
winner = ""
```

After scoring:

```python
if left_score >= WIN_SCORE:
    game_over = True
    winner = "Left"
if right_score >= WIN_SCORE:
    game_over = True
    winner = "Right"
```

Wrap movement and ball update in `if not game_over:`.

In draw, after everything else:

```python
if game_over:
    big_font = pygame.font.SysFont("Arial", 50)
    text = big_font.render(f"{winner} wins! Press R to restart", True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
```

Add R-to-restart in the event handling.

#### Extension — single player vs computer

Replace the right paddle with **AI**: each frame, move
the right paddle toward the ball.

```python
# Replace the right_paddle keyboard checks with:
if right_paddle.centery < ball_rect.centery and right_paddle.bottom < HEIGHT:
    right_paddle.y += PADDLE_SPEED - 2    # AI is slightly slower
if right_paddle.centery > ball_rect.centery and right_paddle.top > 0:
    right_paddle.y -= PADDLE_SPEED - 2
```

Now it's one player vs the computer. The "minus 2" makes
the AI beatable; without it, the AI is perfect.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your Pong. Did you and your buddy
  play a round?
- For the kids who added the angle-by-position bounce —
  does it feel more like real Pong?
- For the kids who built single-player AI — can you beat
  it?
- What's the highest score you saw?

Today you built **a complete classic game from scratch.**
Pong is a perfect example because it's *minimal* — six
sessions of skills add up to a real, playable, fun game.

You used **everything from Sessions 1-5:**

- The frame loop (Session 1)
- Drawing rectangles + the screen size (Session 2)
- The Rect class (Session 3)
- Polled keyboard input (Session 4)
- `colliderect` (Session 5)

Plus one new piece — `pygame.Rect(x, y, w, h)` to make a
Rect directly, without an image.

Next week we put your Pong **on the internet** — push it
to GitHub, where the world can see it. After that:
sound. Then sprite classes (so we can refactor games
with many objects). Then Mr. Eric's grid-world.

### If you missed this session

Open Thonny. Then:

1. Build Pong step by step. Don't skip steps. Run after
   each.

2. By the end you should have two paddles, a bouncing
   ball, and a score.

3. (Stretch) Add at least one polish item — speed-up,
   angle-by-position, center line, or win screen.

About 60-90 minutes total — this is a long session.

### Stretch and extension ideas

- **All the stretches above** — speed-up, angle bounce,
  center line, win screen, AI opponent.
- **Sound effects** — Session 8 will cover the proper
  way. For now, you can sneak-preview:
  ```python
  bounce_sound = pygame.mixer.Sound("bounce.wav")
  # then bounce_sound.play() on collision
  ```
- **Multi-color ball** — change ball color each bounce.
- **Trail effect** — instead of `screen.fill(BLACK)`,
  fill with a translucent black using `pygame.Surface`
  alpha. Ball leaves a fading trail.
- **Powerups** — random items appear on the field. Catch
  with the ball: bigger paddle, faster ball, freeze
  opponent.
- **Touch-up the visuals** — fancier scoreboard, chamfered
  paddles (rounded corners), pixel-art ball.
- **Save your high score** to a file (Phase 5 callback).

### What's next

Next week: **GitHub.** You'll create a GitHub account,
push your Pong to the internet, and have a real public
repo with your name on it. By the end of class, you can
share a link to your game with anyone.
