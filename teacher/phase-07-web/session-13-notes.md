## Session 13 — Teacher Notes

*Phase 7, Web · Session 13 of 17 · Title: Canvas
mini-game*

### Purpose of this session

Browser games are real. Five jobs, in priority order:

1. **Land `requestAnimationFrame`.** Browser's
   answer to Pygame's `clock.tick(60)`. Different
   syntax, same model.
2. **Land keyboard state with `keys` object.**
   Manual but flexible. The standard JS pattern.
3. **Land DOM + canvas mixing.** Canvas for game
   graphics, DOM (e.g., a `<p>`) for UI text.
   Real architecture.
4. **Build a complete mini-game.** Same shape as
   Phase 6 Session 5's fruit catcher. Direct
   transfer.
5. **Set up Sessions 14-17.** Today: a real
   shareable game. Push to GitHub Pages and the
   world can play.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built bouncing rect (Part A).
- Pre-built controllable square.
- Pre-built complete catcher (Part B end-state).
- Pre-built version with bombs and high score
  (stretches).
- Optional: side-by-side with Phase 6 Session 5's
  Pygame fruit catcher for comparison.

**Prep time:** ~30 minutes. Build the catcher
once before class, tune speeds.

### Timing and flow

Total: ~90 min — possibly tight given the breadth.

- **Welcome and recap** (~5 min). Recap Session 12
  (canvas drawing).
- **Part A: requestAnimationFrame + bouncing
  rect** (~15 min).
- **Part A: keyboard input + controllable
  square** (~20 min).
- **Break** (~5 min).
- **Part B: catcher game** (~35 min). Type
  together.
- **Stretches** (~5 min).
- **Wrap-up** (~5 min).

If running short, **drop the high-score
persistence and bombs.** The base catcher (paddle +
falling blocks + score + lives + game over) is the
priority.

### Teaching Part A

#### "Pygame moves to the browser"

Open with the framing:

> "Last session was canvas drawing — like Pygame's
> draw functions. Today: animation and input —
> like Pygame's frame loop and `key.get_pressed`.
> Real browser games. Same model as Phase 6,
> different language."

#### `requestAnimationFrame` is *the* browser way

Don't introduce `setInterval` (the older approach).
Frame:

> "`requestAnimationFrame(yourFunction)` says 'run
> this function on the next animation frame.' It
> recursively calls itself, keeping the loop
> running.
>
> Why not `while (true)`? The browser would freeze.
> rAF (`requestAnimationFrame`) cooperates with the
> browser — runs at the screen's refresh rate
> (~60 fps), pauses when the tab isn't visible,
> doesn't block other JS."

The recursive self-call pattern feels weird at first.
Walk through it slowly:

```javascript
function loop() {
    // do stuff
    requestAnimationFrame(loop);    // schedule next call
}
loop();    // first call
```

> "We call it once. It runs. At the end, it asks
> the browser to call it again. The browser does.
> It runs again, asks again, runs again... 60 times
> a second."

#### Keyboard state pattern

Two listeners, one object:

```javascript
const keys = {};
document.addEventListener("keydown", (e) => keys[e.key] = true);
document.addEventListener("keyup", (e) => keys[e.key] = false);
```

Frame:

> "Browsers don't have `key.get_pressed()` like
> Pygame. We *make* it ourselves. Two listeners
> track which keys are currently down. Then we
> check `keys['ArrowLeft']` in our update — same
> shape as Pygame.
>
> *This pattern goes at the top of every browser
> game.* Memorize it."

#### `event.key` strings

Brief reference:

```
"ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"
"a", "b", ... "z"  (lowercase)
" "  (space)
"Enter", "Escape", "Tab"
```

`event.key` is the *symbol* of the key. So Shift+a
is `"A"` (capital), not `"a"`.

(There's also `event.code` which is the *physical*
key location — `"KeyA"`, `"Space"` — usually less
useful.)

#### The bouncing rect demo

Walk through the bouncing rect from Part A on the
projector. After typing it:

> "Compare to Phase 6 Session 1. Same code structure
> — variables for x, y, dx, dy. Update them. Bounce
> at edges. Draw. Loop. *Same game programming
> pattern in a different language.*"

### Teaching Part B

#### The catcher

Type the catcher line by line. Pause to discuss:

- **`for (let i = blocks.length - 1; i >= 0; i--)`**
  — backward iteration when removing.
- **The four-comparison rect collision** — same as
  Pygame.
- **`blocks.splice(i, 1)`** — remove one item.
- **`status.textContent = ...`** — DOM update from
  inside the canvas game loop. Mix is fine.

After it works: **play it as a class.** Take turns.
Highlight what works (paddle response feels good)
and what could be better (block speed varies a lot).

#### Backwards iteration

Worth its own moment:

> "When you remove items from an array while looping
> *forward*, indices shift and you skip items. When
> looping *backward*, removing item N doesn't affect
> items N-1, N-2, etc. — you've already seen them.
> Safe.
>
> JavaScript doesn't have Python's `for x in
> blocks[:]` slice trick. Backward loop is the
> standard JS approach."

#### High score with localStorage

Quick. Three lines on save, two on load. Practice
applying Session 11 to a real game.

> "Anywhere you have state worth keeping, persist
> it. High scores, settings, drafts, game progress
> — all the same `setItem`/`getItem` pattern."

#### Restart on R (stretch)

The reset pattern:

```javascript
score = 0;
lives = 3;
blocks = [];
gameOver = false;
```

Don't reset `paddleX` (player can leave it where it
was). Don't reset `highScore` (we want it to
persist).

### Common stumbles

- **`requestAnimationFrame` not called.** Loop
  runs once and stops. Forgot the recursive call.
- **Both keydown and keyup attached to wrong
  element.** Try `document` (catches all keys).
- **Game freezes after first key press.** Browser
  default behavior — Space scrolls the page,
  Tab moves focus. Add `event.preventDefault()`
  in the keydown handler if needed:
  ```javascript
  if (e.key === " ") e.preventDefault();
  ```
- **Forward iteration with splice.** Items
  skipped, mysterious bugs. Use backward.
- **Rect collision math wrong.** The four
  comparisons are easy to invert. Walk through
  with paper.
- **Spawn rate too high.** 60 blocks per second =
  unplayable chaos. Use a timer.
- **Block speeds inconsistent.** Some too fast.
  Cap with `2 + Math.random() * 3` (range 2-5).
- **Game keeps running after game over.**
  `if (gameOver) return;` at start of update.
- **Status DOM not updating.** Forgot to set
  `textContent`.
- **Canvas blurry from CSS sizing.** Same
  Session 12 issue. Use HTML attributes.

### Differentiation

- **Younger kids (9-10):** Goal is the bouncing
  rect + controllable square. Catcher game is a
  stretch.
- **Older kids (12+):** Push for the full catcher
  + high score.
- **Advanced (any age):** Suggest:
  - Bombs + bombs avoidance
  - Speed-up over time
  - Sound effects (`new Audio(...).play()`)
  - Pause/resume with P
  - Mobile/touch controls
  - Save game state across sessions
  - Multi-game (different paddles, different
    block types)
- **Struggling:** A kid who can't get the
  bouncing rect working is the kid you focus on.
  Most common cause: forgot the recursive
  `requestAnimationFrame` call, or canvas not
  set up.

### What to watch for

- **The "I made a browser game!" reaction.** Real
  moment. Many kids will be visibly impressed
  with themselves.
- **Buddies playing each other's games.**
  Encourage. The browser-as-distribution thing is
  going to land.
- **Excitement about high score.** "It saved!"
  Pause for it.
- **Kids running into key-conflict issues** (Space
  scrolls page, Tab leaves focus). Walk through
  `preventDefault`.
- **Comparison to Phase 6.** "This is way fewer
  classes than Pygame!" Yes — JS has classes too,
  but for a small game, plain functions are
  fine. Reaffirm.
- **Kids deploying their game** (jumping to
  Session 15 mentally). Encourage but redirect to
  finishing the base game first.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 14 (fetch).** Could load high scores
  from a server.
- **Session 15 (GitHub Pages).** Their browser
  game becomes shareable as a URL. Real
  audience.
- **Sessions 16-17 (milestone).** Many kids will
  build canvas games for their milestone.
- **Phase 8 (Flask).** Backend could store
  high scores across users.
- **Career-long callback:** browser games are a
  real industry — Phaser, Three.js, even larger
  frameworks all use canvas under the hood.
- **Peanut butter callback opportunity:** the
  forward-vs-backward iteration with splice
  bug is a precision moment. Code does what you
  wrote, but the result is wrong if iterating
  forward.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built bouncing rect
- [ ] Pre-built controllable square
- [ ] Pre-built catcher (complete)
- [ ] Pre-built catcher with stretches (bombs,
      high score)
- [ ] Optional: Phase 6 Session 5 fruit catcher
      open for comparison
- [ ] Projector
- [ ] Class roster
