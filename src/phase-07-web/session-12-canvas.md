## Session 12: Canvas — drawing in JavaScript

*Phase 7 — Web · Session 12 of 17*

### What we're learning today

You can draw in **Pygame.** Today you draw in **the
browser** — using the `<canvas>` element and JavaScript.
The drawing API looks *very* similar to Pygame's: same
shapes, same coordinate system (top-left = 0,0, y goes
down), same logic. The mental model from Phase 6
**transfers directly.** By the end of class you'll have
a small scene drawn in the browser. Next session: a
mini-game.

### You'll need to remember from last time

- **JavaScript syntax** (Session 8).
- **`document.querySelector`** (Session 9).
- **Phase 6 Sessions 1-2** — Pygame's `pygame.draw.rect`,
  `circle`, `line`, the coordinate system. **All of
  that mental model applies today.**

---

### Part A: The canvas element

#### What's a canvas?

The `<canvas>` element is a **rectangular drawing
surface** in HTML. It looks like nothing on its own —
just a blank rectangle. You use **JavaScript** to draw
on it.

```html
<canvas id="myCanvas" width="600" height="400"></canvas>
```

The `width` and `height` set the canvas's pixel
dimensions. (Always set them in HTML, not CSS — CSS
just *scales* the canvas, which can blur it.)

#### Get the drawing context

To draw, you need the **2D drawing context:**

```javascript
const canvas = document.querySelector("#myCanvas");
const ctx = canvas.getContext("2d");
```

`ctx` (short for "context") is your drawing handle.
Almost every canvas method is called on `ctx`.

(There's also `getContext("webgl")` for 3D — way out
of scope.)

#### Try it — your first canvas

Open Thonny. Save a new file as `canvas-test.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Canvas test</title>
    <style>
        canvas {
            border: 1px solid #999;
            display: block;
            margin: 20px auto;
        }
    </style>
</head>
<body>
    <canvas id="myCanvas" width="600" height="400"></canvas>

    <script>
        const canvas = document.querySelector("#myCanvas");
        const ctx = canvas.getContext("2d");

        // Background
        ctx.fillStyle = "#87ceeb";
        ctx.fillRect(0, 0, 600, 400);

        // A red box
        ctx.fillStyle = "red";
        ctx.fillRect(50, 50, 100, 100);
    </script>
</body>
</html>
```

Save. Open in browser. **A canvas with a sky-blue
background and a red square in the corner.**

What's happening:

- **`ctx.fillStyle = "..."`** sets the *color* for
  any shape we draw next.
- **`ctx.fillRect(x, y, width, height)`** draws a
  filled rectangle.

Compare to Pygame:

```python
# Pygame
screen.fill((135, 206, 235))
pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))
```

```javascript
// Canvas
ctx.fillStyle = "#87ceeb";
ctx.fillRect(0, 0, 600, 400);
ctx.fillStyle = "red";
ctx.fillRect(50, 50, 100, 100);
```

**Almost identical.** Different language, same model.

#### The coordinate system

Same as Pygame. Same as Phase 7's HTML positions.

- `(0, 0)` is the **top-left corner.**
- `x` increases to the **right.**
- `y` increases **downward.**

If you remember Phase 6, this is automatic.

#### Filled vs outlined shapes

```javascript
// Filled — interior color
ctx.fillStyle = "blue";
ctx.fillRect(200, 50, 80, 80);

// Outlined — border color
ctx.strokeStyle = "blue";
ctx.lineWidth = 4;
ctx.strokeRect(300, 50, 80, 80);
```

`fillRect` and `strokeRect` (filled and outlined,
respectively).
`fillStyle` and `strokeStyle` (the two color
properties).
`lineWidth` (border thickness).

#### Circles (with `arc`)

Canvas doesn't have `drawCircle`. It has **`arc`**,
which draws part of a circle (or all of it, if you
go full 360°).

The pattern for a full circle:

```javascript
ctx.beginPath();
ctx.arc(300, 200, 50, 0, Math.PI * 2);    // x, y, radius, startAngle, endAngle
ctx.fillStyle = "yellow";
ctx.fill();
```

`arc(x, y, radius, startAngle, endAngle)` draws an
arc:

- `(x, y)` — the center.
- `radius` — size.
- `startAngle` — where to start (in radians).
- `endAngle` — where to end (in radians).

`Math.PI * 2` is a full 360° circle.

The `beginPath()` / `fill()` pair is required for
arcs. Frame:

> "Arcs are drawn as a *path*. Tell canvas you're
> starting a new path (`beginPath`), describe the
> shape (`arc(...)`), then either `fill()` or
> `stroke()` to actually draw it."

Lines work the same way (we'll see in a moment).

#### A complete scene

Replace your script with:

```javascript
const canvas = document.querySelector("#myCanvas");
const ctx = canvas.getContext("2d");

// Sky background
ctx.fillStyle = "#87ceeb";
ctx.fillRect(0, 0, 600, 400);

// Ground
ctx.fillStyle = "#3a7d3a";
ctx.fillRect(0, 300, 600, 100);

// Sun
ctx.fillStyle = "#ffeb3b";
ctx.beginPath();
ctx.arc(500, 80, 40, 0, Math.PI * 2);
ctx.fill();

// House body
ctx.fillStyle = "#c69876";
ctx.fillRect(220, 200, 160, 100);

// Roof — using lineTo
ctx.fillStyle = "#8b3030";
ctx.beginPath();
ctx.moveTo(210, 200);
ctx.lineTo(390, 200);
ctx.lineTo(300, 130);
ctx.closePath();
ctx.fill();

// Door
ctx.fillStyle = "#5a3a1a";
ctx.fillRect(280, 250, 40, 50);
```

Save. Reload. **A scene** — sky, ground, sun, house,
door.

What's new:

- **`moveTo(x, y)`** — move the "pen" to that point
  without drawing.
- **`lineTo(x, y)`** — draw a line from the pen's
  position to that point.
- **`closePath()`** — close the path back to where
  it started.

This is how you draw triangles, polygons, and any
custom shape. Phase 6 had `pygame.draw.polygon` —
this is the canvas equivalent.

#### Text

```javascript
ctx.font = "30px Arial";
ctx.fillStyle = "white";
ctx.fillText("Hello!", 100, 100);
```

`fillText(text, x, y)` draws text at a position.
The `font` property is a CSS-style font string.

For text alignment:

```javascript
ctx.textAlign = "center";    // or "left" (default), "right"
ctx.fillText("Centered", 300, 200);
```

#### Where else does this look like CSS?

A few canvas properties take CSS-like values:

- `ctx.fillStyle = "red"` or `"#ff0000"` or
  `"rgba(255, 0, 0, 0.5)"`
- `ctx.font = "30px Arial"`
- `ctx.lineWidth = 4`

Familiar territory. The web is unified.

**Checkpoint:** *Your canvas has at least 4 different
shapes (rectangle, circle, polygon, text), in
different colors.* **This is the natural stop point if
class is cut short.**

---

### Part B: Build a scene

Time to make something yours.

#### Pick a subject

Same kind of exercise as Phase 6 Session 2 (the
shape-drawing scene). Pick:

- A **face** — circles for head and eyes, lines for
  smile.
- A **landscape** — mountains as triangles, sky, sun,
  trees.
- A **rocket ship** — rectangles + triangles + circle
  windows.
- A **city skyline** — rectangles of varying heights.
- A **bouncing logo** screensaver (like the old DVD
  player).
- An **abstract pattern** — circles in a grid, color
  gradients.

#### Use loops

JavaScript loops work in canvas too. A row of stars:

```javascript
for (let i = 0; i < 50; i++) {
    const x = Math.random() * 600;
    const y = Math.random() * 200;
    const r = Math.random() * 3 + 1;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fillStyle = "white";
    ctx.fill();
}
```

50 random stars at random positions and sizes. The
power of loops + drawing.

#### Stretch — gradients

```javascript
const gradient = ctx.createLinearGradient(0, 0, 0, 400);
gradient.addColorStop(0, "#ff7e5f");
gradient.addColorStop(1, "#feb47b");
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, 600, 400);
```

A vertical sunset gradient (orange to peach).

`createLinearGradient(x1, y1, x2, y2)` makes a
gradient from one point to another. `addColorStop(t,
color)` places a color at position `t` (0 to 1).
Then use the gradient as a `fillStyle`.

#### Stretch — drawing with the mouse

You can draw with mouse events. Add to your script:

```javascript
let drawing = false;

canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => drawing = false);

canvas.addEventListener("mousemove", (event) => {
    if (!drawing) return;
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, Math.PI * 2);
    ctx.fillStyle = "black";
    ctx.fill();
});
```

Click and drag on the canvas. **You're drawing.** A
tiny paint program in 10 lines.

The `getBoundingClientRect()` business is needed
because the mouse position is relative to the *page*,
not the canvas. Subtract the canvas's left/top to get
the canvas-relative position.

#### Stretch — clear the canvas

```javascript
ctx.clearRect(0, 0, canvas.width, canvas.height);
```

Erases everything. Useful for animations (next
session).

Add a button to clear:

```html
<button id="clearBtn">Clear</button>

<script>
    document.querySelector("#clearBtn").addEventListener("click", () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });
</script>
```

#### Extension — save as image

```javascript
const dataURL = canvas.toDataURL("image/png");
// Open in new tab:
window.open(dataURL);
```

`toDataURL()` returns the canvas as an encoded image.
Visit the URL in a new tab to download. Real "save
my drawing" feature.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your scene. What did you
  build?
- For the kids who used loops — what did you
  generate?
- Anyone try the mouse drawing? Did it feel like a
  real paint program?
- Did the Pygame mental model transfer cleanly?

Today you learned:

- **`<canvas>`** — drawing surface in HTML.
- **`getContext("2d")`** — your drawing handle (`ctx`).
- **`ctx.fillRect`, `strokeRect`** — rectangles.
- **`ctx.arc`** — circles (and other arcs).
- **`ctx.moveTo` + `lineTo`** — lines and polygons.
- **`ctx.beginPath` / `fill` / `stroke`** — the path
  pattern.
- **`ctx.fillStyle`, `strokeStyle`, `lineWidth`,
  `font`** — visual properties.
- **`ctx.fillText`** — text on canvas.
- **Mouse coordinates** with
  `getBoundingClientRect`.

The Pygame mental model **directly transfers.**
Different language, same drawing primitives, same
coordinates. If you survived Phase 6, you can canvas.

Next week: **canvas + animation + input** = a real
game in the browser.

### If you missed this session

Open Thonny.

1. Build the canvas-test.html with the basic
   rectangle and circle.

2. Build the scene from Part A — sky, ground, sun,
   house.

3. Build your own scene — pick a subject from the
   list, use at least 6 shapes.

4. (Stretch) Try the mouse-draw feature.

About 30-45 minutes. By the end you should have a
canvas scene of your own.

### Stretch and extension ideas

- **Gradients** — linear and radial.
- **Mouse drawing** — paint program.
- **Fill style with patterns or images.**
- **Shadow effects** — `ctx.shadowBlur`,
  `shadowColor`.
- **Save as image** with `toDataURL`.
- **Clear button** to wipe and start over.
- **Color picker** — let user choose color.
- **Brush size** — slider for the pen size.
- **Read MDN's Canvas tutorial** for the full API.

### What's next

Next week: **animation + input** = a real
mini-game in the browser. We use
`requestAnimationFrame` for the frame loop, listen
for keyboard events, and build something playable.
The Pygame patterns from Phase 6 transfer directly.
