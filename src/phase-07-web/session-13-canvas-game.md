## Session 13: Canvas mini-game

*Phase 7 — Web · Session 13 of 17*

### What we're learning today

Last week you drew on a canvas. Today you make it
**move and respond.** You'll learn the browser's
**frame loop** (`requestAnimationFrame`), handle
**keyboard input**, and build a complete mini-game —
a falling-things catcher (just like Phase 6 Session
5, but in the browser). By the end, you'll have a
playable game in HTML that anyone with a browser can
load. Save high scores with localStorage (Session 11
callback).

### You'll need to remember from last time

- **Canvas + ctx** (Session 12).
- **`addEventListener`** (Session 9).
- **`localStorage`** for the high score (Session 11).
- **Phase 6 Sessions 1, 4, 5** — frame loop,
  keyboard input, collision. **All directly
  transfers.**

---

### Part A: The browser's frame loop

#### `requestAnimationFrame`

In Pygame, you used a `while running:` loop with
`clock.tick(60)`. The browser has a different
mechanism: **`requestAnimationFrame`**.

The pattern:

```javascript
function gameLoop() {
    // 1. Update state
    // 2. Clear and redraw
    
    requestAnimationFrame(gameLoop);    // schedule the next frame
}

requestAnimationFrame(gameLoop);    // start the loop
```

`requestAnimationFrame(fn)` says "run `fn` on the
next animation frame" — typically about 60 times per
second. The function recursively schedules itself,
keeping the loop going.

It's smarter than a `while` loop:

- **Synced to the screen refresh** (usually 60 Hz).
- **Pauses when the tab is hidden** (saves battery).
- **Doesn't block the page** (other JS can run).

Compare to Pygame:

```python
# Pygame
while running:
    # update
    # draw
    clock.tick(60)
```

```javascript
// Browser
function gameLoop() {
    // update
    // draw
    requestAnimationFrame(gameLoop);
}
gameLoop();
```

Same shape, different mechanism.

#### A bouncing rectangle

Open Thonny. Save a new file as `bouncing.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bouncing</title>
    <style>
        body { margin: 0; background: #1a1a2e; }
        canvas { display: block; margin: 20px auto; background: #0f3460; }
    </style>
</head>
<body>
    <canvas id="game" width="600" height="400"></canvas>
    
    <script>
        const canvas = document.querySelector("#game");
        const ctx = canvas.getContext("2d");
        
        // State
        let x = 100;
        let y = 100;
        let dx = 3;
        let dy = 2;
        const SIZE = 40;
        
        function gameLoop() {
            // Update
            x += dx;
            y += dy;
            
            if (x < 0 || x > 600 - SIZE) dx = -dx;
            if (y < 0 || y > 400 - SIZE) dy = -dy;
            
            // Draw
            ctx.fillStyle = "#0f3460";
            ctx.fillRect(0, 0, 600, 400);    // clear (paint background)
            
            ctx.fillStyle = "#e94560";
            ctx.fillRect(x, y, SIZE, SIZE);
            
            requestAnimationFrame(gameLoop);
        }
        
        gameLoop();
    </script>
</body>
</html>
```

Save. Open in browser. **A pink box bounces around
the canvas.**

What's happening:

- Same as Phase 6 Session 1's bouncing rect, but in
  JavaScript.
- Update: change x and y, flip direction at edges.
- Draw: fill the canvas (clear), draw the box.
- `requestAnimationFrame(gameLoop)` schedules the
  next frame.

The pattern is **identical** to Pygame. If you got
through Phase 6, this is muscle memory.

#### Keyboard input

For continuous (held-key) input, track key state in
an object:

```javascript
const keys = {};

document.addEventListener("keydown", (event) => {
    keys[event.key] = true;
});

document.addEventListener("keyup", (event) => {
    keys[event.key] = false;
});
```

Then in your update:

```javascript
if (keys["ArrowLeft"]) x -= 5;
if (keys["ArrowRight"]) x += 5;
```

`event.key` is the name of the key pressed:
`"ArrowLeft"`, `"ArrowRight"`, `"ArrowUp"`,
`"ArrowDown"`, `" "` (space), `"a"`, `"b"`, etc.

(In Pygame this was `pygame.key.get_pressed()`.
Browser is more manual but the model is the same.)

#### Build it — a tiny controllable square

Replace the bouncing logic with player controls:

```javascript
let x = 280;
let y = 350;
const SPEED = 6;

const keys = {};
document.addEventListener("keydown", (e) => keys[e.key] = true);
document.addEventListener("keyup", (e) => keys[e.key] = false);

function gameLoop() {
    if (keys["ArrowLeft"] || keys["a"]) x -= SPEED;
    if (keys["ArrowRight"] || keys["d"]) x += SPEED;
    if (keys["ArrowUp"] || keys["w"]) y -= SPEED;
    if (keys["ArrowDown"] || keys["s"]) y += SPEED;
    
    // Stay on screen
    if (x < 0) x = 0;
    if (x > 600 - 40) x = 600 - 40;
    if (y < 0) y = 0;
    if (y > 400 - 40) y = 400 - 40;
    
    // Draw
    ctx.fillStyle = "#0f3460";
    ctx.fillRect(0, 0, 600, 400);
    ctx.fillStyle = "#e94560";
    ctx.fillRect(x, y, 40, 40);
    
    requestAnimationFrame(gameLoop);
}

gameLoop();
```

Save. Reload. **Use arrow keys (or WASD) to move the
square around.** It stays on screen. Real
controllable character.

**Checkpoint:** *You have a canvas with a player
sprite that responds to keyboard input.* **This is
the natural stop point if class is cut short.**

---

### Part B: A falling-things catcher

Time to build a complete game. You built one in
Phase 6 Session 5 (fruit catcher). Today's is the
same idea, in browser.

#### Build it

Save a new file as `catcher.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Catcher</title>
    <style>
        body {
            margin: 0;
            background: #1a1a2e;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        canvas {
            display: block;
            margin: 20px auto;
            background: #0f3460;
        }
        h1 { margin-top: 20px; }
        #status { font-size: 24px; }
    </style>
</head>
<body>
    <h1>Catch the falling boxes</h1>
    <p id="status">Score: 0  •  Lives: 3</p>
    <canvas id="game" width="600" height="500"></canvas>
    
    <script src="catcher.js"></script>
</body>
</html>
```

`catcher.js`:

```javascript
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
const status = document.querySelector("#status");

const WIDTH = 600;
const HEIGHT = 500;
const PADDLE_W = 80;
const PADDLE_H = 16;
const BLOCK_SIZE = 30;
const SPEED = 7;

let paddleX = WIDTH / 2 - PADDLE_W / 2;
let blocks = [];
let score = 0;
let lives = 3;
let gameOver = false;

const keys = {};
document.addEventListener("keydown", (e) => keys[e.key] = true);
document.addEventListener("keyup", (e) => keys[e.key] = false);

let spawnTimer = 0;
const SPAWN_INTERVAL = 60;    // frames

function update() {
    if (gameOver) return;
    
    // Move paddle
    if (keys["ArrowLeft"] || keys["a"]) paddleX -= SPEED;
    if (keys["ArrowRight"] || keys["d"]) paddleX += SPEED;
    if (paddleX < 0) paddleX = 0;
    if (paddleX > WIDTH - PADDLE_W) paddleX = WIDTH - PADDLE_W;
    
    // Spawn blocks
    spawnTimer++;
    if (spawnTimer >= SPAWN_INTERVAL) {
        spawnTimer = 0;
        blocks.push({
            x: Math.random() * (WIDTH - BLOCK_SIZE),
            y: -BLOCK_SIZE,
            speed: 2 + Math.random() * 3
        });
    }
    
    // Move blocks + check catches/misses
    for (let i = blocks.length - 1; i >= 0; i--) {
        const b = blocks[i];
        b.y += b.speed;
        
        // Check catch (rect collision)
        if (
            b.y + BLOCK_SIZE >= HEIGHT - PADDLE_H &&
            b.y <= HEIGHT &&
            b.x + BLOCK_SIZE >= paddleX &&
            b.x <= paddleX + PADDLE_W
        ) {
            blocks.splice(i, 1);
            score++;
        } else if (b.y > HEIGHT) {
            blocks.splice(i, 1);
            lives--;
            if (lives <= 0) {
                gameOver = true;
            }
        }
    }
    
    status.textContent = `Score: ${score}  •  Lives: ${lives}`;
}

function draw() {
    // Clear
    ctx.fillStyle = "#0f3460";
    ctx.fillRect(0, 0, WIDTH, HEIGHT);
    
    // Paddle
    ctx.fillStyle = "#e94560";
    ctx.fillRect(paddleX, HEIGHT - PADDLE_H, PADDLE_W, PADDLE_H);
    
    // Blocks
    ctx.fillStyle = "#f9d56e";
    for (const b of blocks) {
        ctx.fillRect(b.x, b.y, BLOCK_SIZE, BLOCK_SIZE);
    }
    
    // Game over text
    if (gameOver) {
        ctx.fillStyle = "white";
        ctx.font = "60px Arial";
        ctx.textAlign = "center";
        ctx.fillText("GAME OVER", WIDTH / 2, HEIGHT / 2);
        ctx.font = "24px Arial";
        ctx.fillText("Reload to play again", WIDTH / 2, HEIGHT / 2 + 50);
    }
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

gameLoop();
```

Save. Reload. **Use arrows (or A/D) to move the
paddle.** Catch the falling blocks. Don't let too
many fall off — you only have 3 lives.

**You built a complete browser game.** The exact
same shape as Phase 6's fruit catcher, in JavaScript
+ Canvas.

A few details:

- **Loop blocks backwards** when removing
  (`for (let i = blocks.length - 1; i >= 0; i--)`)
  — modifying an array while iterating forwards
  causes index issues. Same gotcha as Phase 6.
- **`blocks.splice(i, 1)`** removes the item at
  index `i` (one item).
- **Rect collision** — the four `>=`/`<=` checks
  are the standard "do these two rectangles
  overlap" test.
- **Status updated in the DOM** every frame —
  outside the canvas, the score lives in a regular
  `<p>` tag. **Mix DOM and canvas** for game UI.

#### Add a high score with localStorage

Add to the top of `catcher.js`:

```javascript
let highScore = parseInt(localStorage.getItem("catcherHigh") || "0");
```

Then in `update`, when game over:

```javascript
if (lives <= 0) {
    gameOver = true;
    if (score > highScore) {
        highScore = score;
        localStorage.setItem("catcherHigh", highScore);
    }
}
```

Update the status display:

```javascript
status.textContent = `Score: ${score}  •  Lives: ${lives}  •  Best: ${highScore}`;
```

Save. Reload. Play. Lose. **Your high score is
saved.** Reload. The high score is still there.

`parseInt(localStorage.getItem(...) || "0")` — load
as integer. `|| "0"` defaults to "0" if no saved
score yet.

#### Stretch — restart on R

Add to your event listeners:

```javascript
document.addEventListener("keydown", (event) => {
    if (event.key === "r" && gameOver) {
        // Reset everything
        score = 0;
        lives = 3;
        blocks = [];
        gameOver = false;
    }
});
```

Press R after game over to restart. No reload
needed.

#### Stretch — bombs

Some falling things should be **bombs** — catching
one costs a life:

```javascript
// In spawn:
const isBomb = Math.random() < 0.2;    // 20% chance
blocks.push({
    x: Math.random() * (WIDTH - BLOCK_SIZE),
    y: -BLOCK_SIZE,
    speed: 2 + Math.random() * 3,
    isBomb: isBomb
});

// In catch handling:
if (catch logic) {
    if (b.isBomb) {
        lives--;
    } else {
        score++;
    }
    blocks.splice(i, 1);
}

// In draw:
ctx.fillStyle = b.isBomb ? "#000000" : "#f9d56e";
ctx.fillRect(b.x, b.y, BLOCK_SIZE, BLOCK_SIZE);
```

Now you have to *avoid* catching bombs. Real
gameplay tension.

#### Extension — speed up over time

Increase fall speed each catch:

```javascript
// On catch:
score++;
// Slightly increase difficulty
// (would need to modify SPAWN_INTERVAL or speeds globally)
```

Or shorten SPAWN_INTERVAL:

```javascript
let spawnInterval = 60;
// On catch:
spawnInterval = Math.max(20, spawnInterval - 1);
```

(Use `spawnInterval` as a variable instead of a
const.)

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your catcher. What's your
  high score?
- Did the Pygame patterns transfer cleanly? Any
  surprises?
- Did seeing the high score persist after a reload
  feel satisfying?
- For the kids who added bombs — how did the gameplay
  change?

Today you learned:

- **`requestAnimationFrame`** — the browser's frame
  loop.
- **Tracking key state** with `keydown`/`keyup`
  listeners + a `keys` object.
- **Rect collision** with the four-comparison
  pattern.
- **Backwards iteration** when removing from arrays.
- **DOM + canvas** working together (canvas for
  game graphics, DOM for UI text).
- **High score persistence** with localStorage.

You built **a real browser game.** Open it in any
browser, on any computer with internet. Anyone can
play. **That's the web's superpower.**

Next week: **fetch + JSON** — talking to APIs
across the internet. Then GitHub Pages. Then your
milestone.

### If you missed this session

Open Thonny.

1. Build the bouncing rectangle from Part A. See it
   bounce.

2. Add keyboard control. Move the square with
   arrows.

3. Build the catcher game from Part B.

4. (Stretch) Add high score persistence.

About 60-90 minutes — this is a substantial
session.

### Stretch and extension ideas

- **Restart on R** — reset state, no reload needed.
- **Bombs** that lose a life on catch.
- **Speed up over time.**
- **Multiple block types** — different colors, point
  values, sizes.
- **Particle effects** — small explosion when a
  block is caught.
- **Sound** — `new Audio("...mp3").play()` on catch.
- **Mobile controls** — touch events for tablets/
  phones.
- **Pause** with P or Escape.
- **Save the game state** to localStorage so you can
  resume after a reload (advanced).
- **Push to GitHub** — your game becomes a public
  repo.

### What's next

Next week: **fetch and JSON** — JavaScript talking to
the internet. We hit a public API, get data back as
JSON, and display it on the page. Random dog photos,
random jokes, random *whatever* an API offers.
