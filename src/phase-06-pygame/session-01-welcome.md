## Session 1: Welcome to Pygame — the frame loop

*Phase 6 — Pygame · Session 1 of 14*

### What we're learning today

A Pygame program is different from anything you've built
so far. It runs a **frame loop** — about 60 times every
second, the program reads input, updates the world, and
redraws the screen. Today you'll see your first Pygame
window, learn the heartbeat that drives every game ever
made, and make a colored rectangle bounce around inside
it.

### You'll need to remember from last time

- **Importing modules** — Phase 4 Session 3.
- **Lists, variables, conditionals, functions** — Phase 3.
- **The event loop** from customtkinter (Phase 5) — Pygame
  has something similar but very different. We'll compare.
- **Running Python from a file** — `python game.py` from
  the terminal, or hit Run in Thonny.

---

### Part A: Your first Pygame window

#### What's a frame loop?

Open a video game on your phone. The screen is being
**redrawn** about 60 times every second. You don't see
those redraws because they happen so fast — your eye
sees smooth animation.

Each "redraw" is a **frame.** A 60-frame-per-second
(60 FPS) game runs the same loop 60 times a second:

1. **Read input.** What keys are pressed? What did the
   mouse just do?
2. **Update the world.** Move characters, check collisions,
   advance the score.
3. **Draw the screen.** Clear it, then draw everything in
   its new position.

That loop is the heartbeat of every video game. Mario,
Minecraft, Fortnite — all of them. The art is fancier;
the loop is the same.

Compare to Phase 5 customtkinter:

| customtkinter | Pygame |
|---|---|
| Sits and **waits** for the user | Runs **constantly** at 60 FPS |
| Calls a function when something happens | Reads input every frame |
| You don't draw — widgets draw themselves | You draw everything yourself, every frame |

Same Python, very different mental model.

#### The minimum Pygame program

Open Thonny. Save a new file as `game.py`. Type this:

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My first Pygame")

clock = pygame.time.Clock()
running = True

while running:
    # 1. Read input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 2. Update the world
    # (nothing yet)
    
    # 3. Draw the screen
    screen.fill((30, 30, 40))    # dark blue-grey
    
    pygame.display.flip()         # show what we drew
    clock.tick(60)                # cap at 60 FPS

pygame.quit()
```

Save. Run. A window appears with a dark blue-grey
background. Click the X to close it.

That's it. **You have a running game.** It's empty, but
the heartbeat is there.

What every line does:

- **`import pygame`** — bring in the Pygame library.
- **`pygame.init()`** — start up Pygame. Always at the top.
- **`screen = pygame.display.set_mode((600, 400))`** —
  create a 600-wide-by-400-tall window. The `screen` is
  what we'll draw on.
- **`pygame.display.set_caption(...)`** — sets the window
  title bar.
- **`clock = pygame.time.Clock()`** — keeps time so we can
  cap the frame rate.
- **`while running:`** — the frame loop. Each pass is one
  frame.
- **`for event in pygame.event.get():`** — pulls all input
  events that happened since last frame (key presses,
  clicks, the close-window X).
- **`if event.type == pygame.QUIT:`** — the user clicked
  the X. Stop looping.
- **`screen.fill((30, 30, 40))`** — paint the whole screen
  this color (RGB). Always do this first — it erases the
  previous frame so we can draw fresh.
- **`pygame.display.flip()`** — show what we drew. Without
  this, you'd see nothing.
- **`clock.tick(60)`** — wait just long enough so we run
  at 60 frames per second, no faster.
- **`pygame.quit()`** — clean up when the loop ends.

Memorize this shape. Every Pygame program has it.

#### Add a rectangle

Inside the loop, after `screen.fill(...)` but before
`pygame.display.flip()`, add:

```python
pygame.draw.rect(screen, (255, 100, 50), (250, 150, 100, 100))
```

Save. Run. An orange-red square appears in the middle.

The arguments:

- **`screen`** — what to draw on.
- **`(255, 100, 50)`** — color, RGB. (Red 255, green 100,
  blue 50.) We'll talk about colors next session.
- **`(250, 150, 100, 100)`** — the rectangle: x, y, width,
  height. So at position (250, 150), 100 wide and 100 tall.

That last group `(x, y, w, h)` is a **`Rect`** — Pygame's
basic shape. You'll use these constantly.

#### A quick word on coordinates

Pygame's coordinate system isn't quite what you might
expect:

- **`(0, 0)` is the top-left corner.**
- **x increases to the right.**
- **y increases *downward.***

So `(250, 150)` is 250 pixels right of the left edge and
150 pixels *down* from the top edge.

This is different from the math class graphs you've seen
(where y goes up). It's the same as Phase 1's Scratch was,
roughly — most computer graphics do it this way.

#### Make it move

Now the heartbeat starts to matter. Replace the hardcoded
`250` with a variable that changes every frame.

Above the loop, add:

```python
x = 250
```

In the **update** part of the loop (right after the event
handling, before the draw), add:

```python
x = x + 2
```

In the draw, change the rect to use `x`:

```python
pygame.draw.rect(screen, (255, 100, 50), (x, 150, 100, 100))
```

Save. Run. The rectangle slides right across the screen,
off the edge, gone forever.

Why? Each frame, `x` grows by 2. After about 5 seconds at
60 FPS, the rectangle is way past the right edge.

#### Make it bounce

Add another variable for x-velocity:

```python
x = 250
dx = 2    # how much to move x each frame
```

In the update step:

```python
x = x + dx

# bounce off left and right edges
if x < 0 or x > 500:    # 600 - 100 (width of rect)
    dx = -dx
```

Save. Run. The rectangle now bounces back and forth.

Each frame:

1. Move `x` by `dx` (which is 2, then maybe -2, then 2...).
2. If `x` is off either edge, flip the direction (negate
   `dx`).

That's an animation. You wrote it. **You're a game
developer now.**

**Checkpoint:** *You have a Pygame window with a bouncing
rectangle.* **This is the natural stop point if class is
cut short.**

---

### Part B: Make it your own

The base goal: tweak the bouncing rectangle so it does
something noticeably *yours*. Pick one or more:

#### Stretch — bounce vertically too

Add `y` and `dy`. Update both each frame. Bounce off top
and bottom too.

```python
x = 250
y = 150
dx = 2
dy = 1.5
```

In update:

```python
x = x + dx
y = y + dy

if x < 0 or x > 500:
    dx = -dx
if y < 0 or y > 300:    # 400 - 100
    dy = -dy
```

Now the rectangle bounces around the whole window
diagonally. Looks like the old DVD player screensaver.

#### Stretch — change color on bounce

Above the loop, add a list of colors:

```python
colors = [(255, 100, 50), (50, 255, 100), (100, 50, 255), (255, 255, 100)]
color = colors[0]
import random
```

When bouncing, pick a new color:

```python
if x < 0 or x > 500:
    dx = -dx
    color = random.choice(colors)
```

Then draw with the variable: `pygame.draw.rect(screen, color, ...)`.

#### Stretch — multiple bouncing rectangles

Use a list of `[x, y, dx, dy, color]` lists. Loop through
them in update and draw.

#### Extension — speed up over time

Each bounce, slightly increase `dx` and `dy` (multiply by
1.05 or so). Watch it accelerate. Add a "max speed" cap.

#### Extension — change with the keyboard

Below the QUIT check (still inside the for-event loop),
add:

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        dx = -dx
        dy = -dy
```

Now pressing **space** reverses direction.

(We'll go deeper into keyboard input in Session 4.)

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your bouncing rectangle.
- Did you tweak it? What did you change?
- Does the "60 frames per second" feel make sense?
  Anyone notice that the motion looks smooth?

Today you wrote your first frame loop. The heartbeat of
every video game. **Read input, update the world, draw
the screen.** You'll see this shape in every Pygame
program for the rest of the phase.

You also learned:

- `pygame.init()`, `set_mode`, `Clock`, the `while running`
  loop, `pygame.display.flip()`.
- The Pygame coordinate system (`(0, 0)` top-left).
- `pygame.draw.rect` and the `(x, y, w, h)` shape.
- Animation = changing values across frames.
- Bouncing = flipping a velocity when you hit a boundary.

Keep this `game.py`. We'll use it as a starting point in
later sessions.

### If you missed this session

Open Thonny. Then:

1. Type out the minimum Pygame program. Run it. See the
   blank window.

2. Add the orange rectangle. Run it. See the rectangle.

3. Make it move (`x = x + 2`). Run it. See it slide off
   the screen.

4. Make it bounce (add `dx`, flip on edges). Run it.

If you don't have Pygame at home, install it from a
terminal:
```
$ pip install pygame
```

About 30-45 minutes. By the end you should have a
bouncing rectangle.

### Stretch and extension ideas

- **Bounce in 2D.** Both x and y, with `dx` and `dy`.
- **Color changes.** New random color on each bounce.
- **Many rectangles.** A list of them, all bouncing.
- **Different shapes.** `pygame.draw.circle(screen, color,
  (cx, cy), radius)` and `pygame.draw.line(...)`. Try
  drawing a bouncing circle instead.
- **Trail effect.** Don't fully clear the screen — fill
  with a translucent color. Use
  `pygame.Surface((600, 400), pygame.SRCALPHA)` then
  `surface.fill((30, 30, 40, 20))` and blit. Advanced.
- **Different background.** Try `screen.fill((255, 255, 255))`
  for white, or any other RGB.
- **Slow motion.** Change `clock.tick(60)` to `clock.tick(10)`.
  Watch the rectangle move in slow, choppy hops.

### What's next

Next week is **drawing on the screen** — circles, lines,
polygons, all the colors. We'll build a small scene by
combining shapes (a face, a house, a landscape — your
pick).
