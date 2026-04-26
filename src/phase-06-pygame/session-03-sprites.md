## Session 3: Sprites and images

*Phase 6 — Pygame · Session 3 of 14*

### What we're learning today

You can draw shapes. That's enough for prototypes — but
real games use **images**. A character isn't a rectangle;
it's a *picture*. Today you'll load a PNG file into your
program, paste it on the screen, and move it around. By
the end you'll have your first **sprite** — a moving
image with a position. This is the building block of
every game with characters, enemies, items, and
projectiles.

### You'll need to remember from last time

- **The frame loop** (Session 1).
- **Drawing shapes** (Session 2).
- **The coordinate system** — `(0, 0)` top-left, y goes
  down.
- **Variables that change each frame = animation**.
- **Lists** (Phase 3 Session 8) — for groups of sprites.

---

### Part A: Loading and drawing an image

#### Get an image

In class today, you've been given some sprite PNGs in a
folder named `images/`. If you're working at home, find
or make a small PNG (you can draw one in any image
editor, or download a free game sprite).

A good starter sprite is **transparent** — the background
isn't a solid color. PNGs support transparency; JPGs
don't. Stick with PNGs.

Put the image file in the **same folder as your Python
file**.

#### A program to display it

Open Thonny. Save a new file as `sprite.py` in the same
folder as your image. Type:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My first sprite")
clock = pygame.time.Clock()

# Load the image — once, before the loop
player_image = pygame.image.load("player.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((100, 150, 100))    # green background
    
    # Draw the image at position (300, 200)
    screen.blit(player_image, (300, 200))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Replace `"player.png"` with the actual filename of your
image.

Save. Run. Your image appears at position (300, 200).

What's new:

- **`pygame.image.load("player.png")`** — reads the file
  from disk and creates a `Surface` (Pygame's word for
  "image you can draw").
- **`screen.blit(image, (x, y))`** — pastes the image
  onto the screen at position `(x, y)`. The position is
  the **top-left corner** of the image (just like rects).

`blit` (rhymes with "fit") is short for "block transfer."
It's how you paste *one image* onto *another*. The screen
is also a Surface, so we blit images onto it.

#### Load images once, draw them every frame

Notice `pygame.image.load` is **before** the loop, but
`blit` is **inside** it.

This is important. Loading an image from disk is *slow*
— if you reloaded it every frame, your game would crawl.
Load once, blit many times.

Same with the `screen` itself, the `clock`, and any other
setup. Set up once, use every frame.

#### Move the sprite

Same trick as the bouncing rectangle. Add variables for
position, change them each frame.

Add above the loop:

```python
x = 300
y = 200
```

Change the blit:

```python
screen.blit(player_image, (x, y))
```

In the update part of the loop:

```python
x = x + 2
```

Save. Run. The sprite moves right, off the edge.

#### The Rect — Pygame's box

Every image (and shape) in Pygame has a **`Rect`** —
a rectangle that describes its position and size. Rects
make collision detection (next session) easy and they
keep position bookkeeping clean.

Get a Rect from an image:

```python
player_rect = player_image.get_rect()
print(player_rect)    # Rect(0, 0, width, height)
```

The default Rect has its top-left at `(0, 0)` and the
size of the image. You can move it:

```python
player_rect = player_image.get_rect()
player_rect.x = 300
player_rect.y = 200
```

Then blit using the rect:

```python
screen.blit(player_image, player_rect)
```

`blit` accepts either a `(x, y)` tuple or a Rect. Same
result — but with the Rect, you have a bunch of useful
properties:

- `player_rect.x` and `player_rect.y` — top-left
- `player_rect.width` and `player_rect.height` — size
- `player_rect.right` — `x + width`
- `player_rect.bottom` — `y + height`
- `player_rect.center` — `(cx, cy)` of the rect
- `player_rect.centerx`, `player_rect.centery`
- `player_rect.move_ip(dx, dy)` — move "in place" by
  `(dx, dy)`

Try changing `player_rect.x = ...` to:

```python
player_rect.center = (300, 200)
```

Now the image is **centered** at (300, 200) instead of
having its top-left there. Often what you want.

#### Update with the Rect

Move the rect each frame instead of separate variables:

```python
player_rect.x = player_rect.x + 2
```

Or, more idiomatic:

```python
player_rect.move_ip(2, 0)
```

`move_ip` moves the rect "in place" — modifies it
directly. Same effect, less typing.

**Checkpoint:** *You have a sprite (image) on the screen
that you can move with a Rect.* **This is the natural stop
point if class is cut short.**

---

### Part B: Many sprites and a small scene

Time to build a small game scene with multiple sprites.

#### Multiple sprites

Each sprite needs its own image *and* its own Rect.

```python
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")
coin_image = pygame.image.load("coin.png")

player_rect = player_image.get_rect(center=(100, 200))
enemy_rect = enemy_image.get_rect(center=(500, 200))
coin_rect = coin_image.get_rect(center=(300, 200))
```

Note the trick: `get_rect(center=(100, 200))` immediately
positions the rect with that center. Saves two lines.

In the draw section:

```python
screen.blit(player_image, player_rect)
screen.blit(enemy_image, enemy_rect)
screen.blit(coin_image, coin_rect)
```

#### A list of sprites — for groups

When you have many of the same kind of thing (10 enemies,
20 coins, 100 stars), use a list of rects:

```python
import random

# Make 10 random coin positions
coins = []
for i in range(10):
    cx = random.randint(0, 600)
    cy = random.randint(0, 400)
    coin_rect = coin_image.get_rect(center=(cx, cy))
    coins.append(coin_rect)
```

Then in the draw section:

```python
for coin_rect in coins:
    screen.blit(coin_image, coin_rect)
```

One image, many rects, drawn in a loop. **This is how
real games handle many objects.**

#### Animate the player

Combine everything. Use mouse position to move the
player:

```python
# inside the loop, in update:
mouse_x, mouse_y = pygame.mouse.get_pos()
player_rect.center = (mouse_x, mouse_y)
```

Now the sprite follows your mouse around. Move over the
coins. Notice they don't react yet — collision detection
is next session.

#### Stretch — scaling and rotating

Pygame can resize and rotate images:

```python
# Make the player twice as big
player_image = pygame.transform.scale(player_image, (128, 128))

# Rotate 45 degrees (counter-clockwise)
rotated = pygame.transform.rotate(player_image, 45)
```

`scale` takes `(width, height)`. `rotate` takes degrees
(positive = counter-clockwise).

Note: rotated images often change size (the box around the
rotated image is bigger). You may need to recompute the
rect.

#### Stretch — flipping

```python
flipped_image = pygame.transform.flip(player_image, True, False)
```

The two booleans are `(flip_x, flip_y)`. Useful for making
your sprite face left vs right when moving.

#### Extension — sprite trail

Don't update `player_rect.center = ...` directly. Instead,
keep a list of recent positions and draw the sprite at
each one with decreasing transparency. Advanced — requires
`Surface` alpha.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your sprite. Did you use the one
  from class, or did you bring your own?
- For the kids who built the multi-sprite scene — show
  it.
- For the kids who tried scaling/rotating — does it look
  cool?
- Anyone notice the coins don't react when the player
  touches them? (Foreshadowing.)

Today you learned:

- **`pygame.image.load(filename)`** to read PNGs.
- **`screen.blit(image, position)`** to paste an image.
- **Load once, blit every frame.**
- **`image.get_rect()`** to get a Rect for an image.
- **Rect properties** — `x`, `y`, `width`, `height`,
  `center`, `right`, `bottom`, etc.
- **`get_rect(center=(x, y))`** to position by center.
- **Lists of sprites** — one image, many rects.
- (Stretch) **`pygame.transform.scale`, `rotate`, `flip`**.

You've gone from "shapes drawn from code" to "real game
art on screen." The visual gap from Session 2 to today is
huge. Next week we make these sprites respond to keys.

### If you missed this session

Open Thonny. Get a PNG image (any small one — a dot, a
square, anything from the internet). Then:

1. Type the minimum Pygame program. Add the `image.load`
   and `blit` lines to display your image.

2. Switch to using a Rect (`get_rect()`, `screen.blit(img,
   rect)`).

3. Move the sprite — try `mouse.get_pos()` to follow the
   mouse.

4. Add a second sprite (different image or same image).

About 30-45 minutes. By the end you should have multiple
sprites on screen.

### Stretch and extension ideas

- **Scale, rotate, flip** images.
- **Mouse-controlled sprite.**
- **Random sprite placement** — a starfield, scattered
  coins, falling snowflakes.
- **Background image** — load a big PNG, blit it at
  `(0, 0)` first. Background scenery.
- **Sprite trail** (advanced — alpha surfaces).
- **Animated sprite** — load multiple images of the same
  character in different poses, switch between them each
  few frames. Walking animation.
- **Resize while running** — make the sprite grow when you
  press space (modify the `scale` call).

### What's next

Next week we add **input** — keyboard controls. You'll
make the player sprite move with WASD or the arrow keys,
which is the foundation for almost any game with a
playable character.
