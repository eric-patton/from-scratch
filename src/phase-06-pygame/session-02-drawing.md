## Session 2: Drawing on the screen

*Phase 6 — Pygame · Session 2 of 14*

### What we're learning today

Last week you drew **rectangles**. Today we add the rest
of Pygame's drawing toolkit: **circles, lines, polygons,
text**, and **all the colors.** By the end of class you'll
have built a small *scene* — a face, a house, a landscape,
or whatever you want — by combining shapes.

### You'll need to remember from last time

- **The frame loop** — read input, update, draw, repeat.
- **`pygame.draw.rect(screen, color, (x, y, w, h))`**.
- **The coordinate system** — `(0, 0)` is top-left, y goes
  *down*.
- **`screen.fill(color)`** to clear the screen each frame.
- **`pygame.display.flip()`** to show what we drew.

---

### Part A: Shapes and colors

#### Start fresh

Open Thonny. Save a new file as `scene.py`. Type the same
minimum Pygame program as last week:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My Scene")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((180, 220, 255))    # light blue (sky?)
    
    # ← we'll draw shapes here
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. Window with a light blue background.

#### Colors are RGB triples

Every color in Pygame is **(red, green, blue)** — three
numbers from 0 to 255.

- `(0, 0, 0)` — black (no light)
- `(255, 255, 255)` — white (all light)
- `(255, 0, 0)` — pure red
- `(0, 255, 0)` — pure green
- `(0, 0, 255)` — pure blue
- `(255, 255, 0)` — yellow (red + green)
- `(255, 0, 255)` — magenta (red + blue)
- `(0, 255, 255)` — cyan (green + blue)
- `(128, 128, 128)` — middle grey
- `(180, 220, 255)` — pale sky blue (what we used above)

Mix the three values to get any color. Want orange? More
red, some green, no blue: `(255, 165, 0)`. Want forest
green? Less green, a little red and blue:
`(34, 100, 30)`. Want pink? Lots of red, some green and
blue: `(255, 180, 200)`.

If you want to look up specific colors, search "RGB
picker" — every browser has one online.

You can also use a 4th value for **transparency** (alpha)
— but that requires `Surface` tricks. We'll skip it for
now.

#### Rectangles (review)

```python
pygame.draw.rect(screen, color, (x, y, width, height))
```

The position `(x, y)` is the **top-left corner.** Width
and height go right and down from there.

```python
pygame.draw.rect(screen, (200, 100, 50), (250, 250, 100, 100))
```

That's a brown 100×100 square with its top-left at
(250, 250).

To draw an **outline only** (not filled), add a fifth
argument — the line width:

```python
pygame.draw.rect(screen, (255, 255, 255), (100, 100, 80, 80), 3)
```

That's a white square outline, 3 pixels thick, hollow
inside.

#### Circles

```python
pygame.draw.circle(screen, color, (center_x, center_y), radius)
```

The position is the **center** (not the top-left like
rects). The radius is the size.

```python
pygame.draw.circle(screen, (255, 220, 0), (300, 100), 40)
```

A yellow circle of radius 40, centered at (300, 100).
Think: a sun.

Outline-only also works:

```python
pygame.draw.circle(screen, (0, 0, 0), (300, 100), 40, 2)
```

#### Lines

```python
pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)
```

Draws a line from `(x1, y1)` to `(x2, y2)`.

```python
pygame.draw.line(screen, (50, 50, 50), (0, 350), (600, 350), 4)
```

A dark grey line, 4 pixels thick, from the left edge to
the right edge at y=350. Think: the ground.

#### Polygons

For triangles or other shapes, use polygons — a list of
points:

```python
pygame.draw.polygon(screen, color, [point1, point2, point3, ...])
```

Each point is `(x, y)`. The polygon connects them in
order and closes the shape.

```python
pygame.draw.polygon(screen, (200, 50, 50), [(250, 200), (350, 200), (300, 150)])
```

A red triangle (a roof, maybe?) with corners at three
specific points.

#### Try it together — a tiny scene

Replace your "we'll draw shapes here" comment with:

```python
# ground
pygame.draw.line(screen, (50, 100, 50), (0, 350), (600, 350), 6)
# house body
pygame.draw.rect(screen, (200, 150, 100), (250, 250, 100, 100))
# house roof
pygame.draw.polygon(screen, (150, 50, 50), [(240, 250), (360, 250), (300, 180)])
# door
pygame.draw.rect(screen, (80, 50, 30), (290, 300, 20, 50))
# sun
pygame.draw.circle(screen, (255, 220, 0), (500, 80), 35)
```

Save. Run. A tiny house in a meadow under a sun.

That's it — that's how you make scenes in Pygame. Each
line is one shape. Order matters: things drawn later
appear *on top* of things drawn earlier. (Notice the door
is drawn after the house body — that's why you see it.)

**Checkpoint:** *You have a scene with at least three
different shapes and three different colors.* **This is
the natural stop point if class is cut short.**

---

### Part B: Build your own scene

Time to make something yours. **Pick a subject** and
build it out of shapes:

- A **face** (circle for head, smaller circles for eyes,
  rectangle or polygon for mouth, lines for eyebrows)
- A **house** (extend the example with windows, chimney,
  trees, clouds)
- A **landscape** (mountains as polygons, sun, river,
  trees)
- A **rocket ship** (rectangles, triangles, circles for
  windows)
- A **robot** (rectangles for body and head, circles for
  eyes, lines for antennas)
- A **cat** (circles, triangles, lines for whiskers)
- A **city skyline** (rectangles of varying heights)
- An **abstract pattern** (circles in a grid, color
  gradients)

Spend at least 20 minutes. Use **at least 6 shapes.** Use
**at least 3 colors.** Make it look like *something* —
even a recognizable smiley face beats a pile of random
shapes.

#### Stretch — write text on the screen

Pygame can draw text. The setup is fiddlier than for
shapes:

```python
# above the loop, once:
font = pygame.font.SysFont("Arial", 36)

# inside the loop, in the draw section:
text_surface = font.render("Hello!", True, (0, 0, 0))
screen.blit(text_surface, (50, 50))
```

What that does:

- `pygame.font.SysFont("Arial", 36)` — get the system
  Arial font at size 36.
- `font.render("Hello!", True, (0, 0, 0))` — render the
  text. `True` means anti-aliased (smooth edges). The
  color is RGB.
- `screen.blit(text_surface, (50, 50))` — paste the
  rendered text at position (50, 50). `blit` is "draw
  this image onto the screen."

Add a title or label to your scene. Try different fonts:
`"Times New Roman"`, `"Courier"`, `"Comic Sans MS"`.

#### Stretch — animate one thing

Last week you bounced a rectangle. This week, animate one
piece of your scene:

- A bird (small triangle) flying across.
- A sun moving across the sky.
- A car (rectangle on rectangle wheels) driving past.
- A bouncing ball.

Use the same pattern: a variable that changes each frame,
used in the position when you draw.

#### Extension — interactive scene

Make the scene respond to the mouse:

```python
# inside the loop:
mouse_x, mouse_y = pygame.mouse.get_pos()
pygame.draw.circle(screen, (255, 100, 100), (mouse_x, mouse_y), 20)
```

Now a red circle follows your cursor. Add it to your
scene — a "you are here" pointer.

#### Extension — gradient background

A real sky has a gradient (lighter at the horizon, darker
above). Loop through y-values, drawing a thin horizontal
line of a slightly different color at each row:

```python
for y in range(400):
    blue = 255 - y // 4    # 255 at top, decreasing
    pygame.draw.line(screen, (180, 200, blue), (0, y), (600, y))
```

Replace your `screen.fill(...)` with that.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your scene. What did you build?
- For the kids who animated something — does it look
  alive?
- Anyone find a particularly satisfying color combo?
- Did you discover the rule about draw order? (Things
  drawn later appear on top.)

Today you learned the **drawing toolkit:**

- **Rectangles** with `pygame.draw.rect`.
- **Circles** with `pygame.draw.circle`.
- **Lines** with `pygame.draw.line`.
- **Polygons** with `pygame.draw.polygon`.
- **Text** with `font.render` + `screen.blit` (stretch).
- **Colors** as `(r, g, b)` triples.
- **Draw order** — later shapes go on top.

Combined with last week's frame loop, you can now make
any visual you can imagine. The only limit is shapes and
colors — which means the limit is your imagination.

### If you missed this session

Open Thonny. Then:

1. Type the minimum Pygame program. Run it.

2. Draw a rectangle, a circle, a line, and a polygon. Run
   after each to make sure it appears.

3. Pick a subject (house, face, robot, etc.) and build a
   small scene with at least 6 shapes.

About 30-45 minutes. By the end you should have a scene
made of shapes.

### Stretch and extension ideas

- **Text labels** for parts of your scene.
- **Animate one piece.**
- **Mouse-following shape.**
- **Gradient background.**
- **More shape types** — `pygame.draw.ellipse(screen,
  color, rect)` (oval inside a rect),
  `pygame.draw.arc(...)` (partial circle),
  `pygame.draw.aaline(...)` (smoother lines).
- **Save your scene as an image:**
  `pygame.image.save(screen, "scene.png")` writes a PNG
  file. Add this where you want a snapshot — maybe on a
  keypress.
- **Random scenes:** use `random.randint(...)` to pick
  positions and colors. Each run is a different artwork.

### What's next

Next week we move from *drawing shapes* to *loading
images.* You'll bring in a PNG file, slap it on the
screen, and use it as a sprite — the building block of
every game with characters, enemies, and items.
