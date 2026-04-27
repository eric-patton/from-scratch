## Session 12 — Teacher Notes

*Phase 7, Web · Session 12 of 17 · Title: Canvas —
drawing in JavaScript*

### Purpose of this session

The "canvas is browser-Pygame" session. Five jobs, in
priority order:

1. **Land the canvas + ctx pattern.** The two-step
   setup: get canvas, get context. Then ctx for
   everything.
2. **Land "Pygame patterns transfer directly."**
   Same coordinates, same shapes, same logic.
   Different language, that's all.
3. **Land the path/fill pattern for arcs and
   polygons.** `beginPath` / `arc` or `lineTo` /
   `fill` or `stroke`. New mechanic.
4. **Practice creative drawing.** Same kind of
   exercise as Phase 6 Session 2 (scene building) —
   prove the transfer.
5. **Set up Session 13 (game).** Today: static
   drawing. Next: animation + input.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built scene example (the house from Part A).
- Pre-built mouse-draw demo.
- Optional: side-by-side with Phase 6 Session 2's
  Pygame scene for direct comparison.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 11
  (localStorage). Today: drawing.
- **Part A: canvas + ctx + first shapes** (~20 min).
- **Part A: arcs + polygons + the scene** (~25 min).
- **Break** (~5 min).
- **Part B: build your own scene** (~30 min).
- **Wrap-up** (~5 min).

If running short, **drop the mouse-draw stretch and
gradients.** The scene-building goal is the priority.

### Teaching Part A

#### "Pygame in the browser"

Open with the framing:

> "You spent 14 sessions in Phase 6 with Pygame.
> Drawing rectangles, circles, lines. Coordinates
> with (0,0) at the top-left. Animation with frame
> loops.
>
> Today you do *the same things* in the browser.
> Different language — JavaScript instead of Python.
> Different surface — `<canvas>` instead of `screen`.
> But the *patterns* are identical. If you survived
> Pygame, you'll glide through canvas."

Drive this point home. It's empowering — kids realize
they have a 14-session head start.

#### `width`/`height` in HTML, not CSS

This is a real precision moment:

> "Set the canvas size in *HTML attributes*, not
> CSS. CSS scales the canvas — which works visually
> but blurs everything (like resizing a JPG). The
> attribute sets the actual pixel resolution."

Demo: set `canvas { width: 800px; }` in CSS — see
the canvas stretch and blur. Bad. Set `width="800"`
in HTML — clean.

#### `ctx` is your handle

Every draw method is on `ctx`:

```javascript
ctx.fillStyle = "...";
ctx.fillRect(...);
ctx.beginPath();
ctx.arc(...);
ctx.fill();
```

Frame:

> "Once you have `ctx`, *everything* is `ctx.something`.
> Memorize this — `const ctx = canvas.getContext('2d')`
> at the top, then `ctx` everywhere."

#### Side-by-side with Pygame

Show the Pygame and canvas code for the same scene
on the projector. Point at the parallels:

```python
# Pygame
screen.fill((135, 206, 235))
pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))
pygame.draw.circle(screen, (255, 235, 59), (500, 80), 40)
```

```javascript
// Canvas
ctx.fillStyle = "#87ceeb";
ctx.fillRect(0, 0, 600, 400);
ctx.fillStyle = "red";
ctx.fillRect(50, 50, 100, 100);
ctx.fillStyle = "#ffeb3b";
ctx.beginPath();
ctx.arc(500, 80, 40, 0, Math.PI * 2);
ctx.fill();
```

Almost line-for-line. Just different syntax.

#### The path/fill pattern

For circles and polygons, canvas uses a *path*
pattern that's different from Pygame:

```javascript
ctx.beginPath();    // start a new path
ctx.arc(x, y, r, 0, Math.PI * 2);    // describe the shape
ctx.fill();         // OR ctx.stroke();
```

Frame:

> "For complex shapes — circles, triangles, custom
> polygons — canvas uses *paths*. Tell it you're
> starting (`beginPath`), describe the shape
> (`arc(...)` or `moveTo`/`lineTo`), then either
> `fill()` or `stroke()` to actually draw it.
>
> Rectangles skip this — `fillRect` and `strokeRect`
> draw immediately."

The two-step (path + fill) catches kids by surprise.
Drill it.

#### `Math.PI * 2` for full circles

Briefly:

> "JavaScript uses radians, not degrees. A full circle
> is `2 × π`. So `0` to `Math.PI * 2` = full circle.
>
> If you wanted half (semicircle), it's `0` to
> `Math.PI`. A quarter is `0` to `Math.PI / 2`."

Don't drill radians. Just give them the recipe.

#### `lineTo` and polygons

```javascript
ctx.beginPath();
ctx.moveTo(210, 200);    // pen down here
ctx.lineTo(390, 200);    // line to here
ctx.lineTo(300, 130);    // line to here
ctx.closePath();          // back to start
ctx.fill();
```

Frame as drawing with a pen:

> "Pen up. Move to a point. Pen down. Line to next
> point. Line to next. Close back to the start.
> *Then* fill or stroke. Each `lineTo` is one edge."

### Teaching Part B

#### Free-form scene

Same exercise as Phase 6 Session 2, in browser. Push
kids to:

- Pick a subject before coding.
- Use at least 6 shapes.
- Use color.
- Maybe loops for repeated elements.

#### Loops feel natural here

Generating 50 random stars with a `for` loop is
satisfying. Show it on the projector. Encourage
kids to try.

#### Mouse drawing is the magic stretch

The 10-line paint program is genuinely fun. Push
fast finishers toward it.

The `getBoundingClientRect()` business is fiddly.
Walk through:

> "The mouse `clientX`/`clientY` are relative to
> the *page*. We need it relative to the *canvas*.
> Subtract the canvas's top-left position. That's
> what `getBoundingClientRect()` gives us."

Don't drill — give the recipe.

### Common stumbles

- **Canvas blurry / stretched.** Set width/height in
  CSS instead of HTML. Move to attributes.
- **Drew without `beginPath`.** Path "remembers"
  previous shapes. Stale path issues.
- **Forgot `fill()` or `stroke()`.** `arc(...)`
  alone draws nothing — needs the fill or stroke
  call.
- **Wrong angle units.** `arc(x, y, r, 0, 360)` —
  expecting degrees. Use radians: `Math.PI * 2`.
- **Circle is an ellipse.** Maybe canvas is being
  scaled by CSS. Same blurry-canvas issue.
- **Color string typo.** `"#abcdgh"` — invalid hex.
  Browser uses default (black) silently.
- **Drawn in wrong order.** Sky on top of house.
  Drawing order matters: back to front.
- **`moveTo` skipped.** First `lineTo` doesn't know
  where to start from. Path issues.
- **`closePath` missing.** Polygon is open. Looks
  weird with stroke; usually fine with fill.
- **Mouse coordinates wrong.** Forgot
  `getBoundingClientRect`. Drawn in wrong place.

### Differentiation

- **Younger kids (9-10):** Goal is the basic scene
  with rectangles and one circle. Skip polygons
  and stretches.
- **Older kids (12+):** Push for the full scene +
  one stretch (loops or mouse).
- **Advanced (any age):** Suggest:
  - Gradients (linear, radial)
  - Multiple polygons (a star, a snowflake)
  - Mouse drawing with color picker + brush size
  - Save canvas as image
  - Animated single shape (preview Session 13)
- **Struggling:** A kid who can't get the first
  rectangle on canvas is the kid you focus on.
  Most common cause: HTML canvas not sized,
  forgot `getContext`, or syntax error in
  selector.

### What to watch for

- **The "Pygame transferred!" reaction.** Some kids
  realize at minute 5 that this is familiar. Pause
  for them.
- **Buddies trading scene ideas.** Encourage.
- **Kids drawing entire game graphics** (Pong,
  Snake) just to see if they can. Some will
  preview Session 13 entirely. Encourage but
  redirect to Part B if they haven't done a scene.
- **Mouse drawing addiction.** A few kids will
  spend the rest of the session drawing. Let them.
- **Excitement about "save as image".** Real moment
  for some kids.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 13 (canvas game).** Today's drawing +
  animation + input = mini-game.
- **Session 15 (GitHub Pages).** Their canvas demo
  could be deployed as a public page.
- **Sessions 16-17 (milestone).** Many kids will
  build canvas-based projects — drawing apps,
  games, visualizations.
- **Phase 8 (Flask).** Backend can serve dynamic
  data; front-end can render with canvas.
- **Career-long callback:** Canvas powers most
  browser games and many visualizations. Real
  industry tool.
- **Peanut butter callback opportunity:** the
  HTML-vs-CSS sizing precision moment. Set in
  attribute or it blurs.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built scene example
- [ ] Pre-built mouse-draw demo
- [ ] Optional: Phase 6 Session 2 Pygame scene for
      side-by-side comparison
- [ ] Projector
- [ ] Class roster
