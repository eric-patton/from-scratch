## Session 12: Game state — title screens and game over

*Phase 6 — Pygame · Session 12 of 14*

### What we're learning today

Real games aren't just one screen. They have a **title
screen** when you launch them, **gameplay** when you
press start, and a **game over** screen when you lose.
Maybe a pause screen, a settings menu, a level-select.
Today you learn the pattern that makes this work — a
**state variable** that controls which screen the game
is showing — and add proper title and game-over screens
to one of your games.

This is the difference between "a single-screen toy"
and "a real game."

### You'll need to remember from last time

- **Sprite classes and groups** — Session 9.
- **One of your previous games** — Pong, fruit catcher,
  collector. Bring whichever you want to upgrade.
- **The frame loop** — input, update, draw.
- **Conditionals** — `if`, `elif`, `else`.

---

### Part A: A state variable

#### What "state" means here

A **state** is "what mode is the game in right now?"
Title? Playing? Paused? Game over? Each state has
**different things drawn** and **different rules for
input.**

The simplest implementation: a string variable that says
which state we're in. The main loop checks the variable
and dispatches.

#### A tiny example — title and play

Open Thonny. Save a new file as `state_demo.py`. Type:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("State demo")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
big_font = pygame.font.SysFont("Arial", 72)

state = "title"

x = 300
y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and state == "title":
                state = "playing"
            if event.key == pygame.K_ESCAPE and state == "playing":
                state = "title"
    
    # Update and draw based on state
    screen.fill((30, 30, 50))
    
    if state == "title":
        title = big_font.render("MY GAME", True, (255, 255, 255))
        sub = font.render("Press Enter to play", True, (180, 180, 180))
        screen.blit(title, title.get_rect(center=(300, 150)))
        screen.blit(sub, sub.get_rect(center=(300, 250)))
    
    elif state == "playing":
        # Update — move the box
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: x -= 5
        if keys[pygame.K_RIGHT]: x += 5
        if keys[pygame.K_UP]: y -= 5
        if keys[pygame.K_DOWN]: y += 5
        
        # Draw — show the box
        pygame.draw.rect(screen, (255, 100, 50), (x, y, 50, 50))
        hint = font.render("Esc = back to title", True, (180, 180, 180))
        screen.blit(hint, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Save. Run. You see a title screen with "MY GAME" and
"Press Enter to play."

Press **Enter.** State flips to `"playing"`. The orange
box appears. Use arrow keys to move it.

Press **Esc.** State flips back to `"title"`. The title
screen returns.

That's it. That's the whole pattern.

#### What's happening

- **`state = "title"`** — a variable that holds the
  current state name (a string).
- **`if state == "title": ...`** — when in title state,
  do title things (draw the title, check for Enter).
- **`elif state == "playing": ...`** — when in playing
  state, do game things (move the box, draw the box).
- **State transitions** happen in the input handling —
  Enter sends you from title to playing; Esc sends you
  back.

It's that simple. A string. An `if/elif`. Transitions
on input.

#### Add a third state — game over

```python
# At the top, add:
score = 0

# Inside event handling, add:
if event.key == pygame.K_RETURN and state == "game_over":
    # restart
    state = "title"
    score = 0

# Inside the playing state's update, add a way to lose:
if x < 0 or x > 550 or y < 0 or y > 350:
    state = "game_over"

# Add the game_over branch to your dispatcher:
elif state == "game_over":
    over = big_font.render("GAME OVER", True, (255, 50, 50))
    sub = font.render("Press Enter to restart", True, (180, 180, 180))
    screen.blit(over, over.get_rect(center=(300, 150)))
    screen.blit(sub, sub.get_rect(center=(300, 250)))
```

Save. Run. Move the box off-screen → game over screen.
Press Enter → back to title. Replay.

You now have a **complete game flow:**

```
title → playing → game_over → title → ...
```

Three states. Three transitions. Looks like a real game.

**Checkpoint:** *You have a program with three states
and you can transition between them all.* **This is the
natural stop point if class is cut short.**

---

### Part B: Add states to a real game

Pick one of your games — Pong, fruit catcher, the
collector — and add a title screen and game-over
screen. Open the file. Make a copy first if you want.

#### Adding a title to Pong

Above the loop:

```python
state = "title"
font = pygame.font.SysFont("Arial", 36)
big_font = pygame.font.SysFont("Arial", 80)
```

Convert your existing main loop logic into an
`elif state == "playing":` block. Add a title state in
front and (likely) a game-over state at the end.

Sketch:

```python
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and state == "title":
                state = "playing"
                # reset whatever needs resetting (scores, ball position)
            if event.key == pygame.K_RETURN and state == "game_over":
                state = "title"
    
    screen.fill(BLACK)
    
    if state == "title":
        title = big_font.render("PONG", True, WHITE)
        sub = font.render("Press Enter to play", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
        screen.blit(sub, sub.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))
    
    elif state == "playing":
        # ALL your existing Pong code goes here:
        # paddle movement, ball update, collision, score draw, ...
        
        # Check for game over
        if left_score >= 10:
            state = "game_over"
            winner = "Left player"
        elif right_score >= 10:
            state = "game_over"
            winner = "Right player"
    
    elif state == "game_over":
        text = big_font.render(f"{winner} wins!", True, WHITE)
        sub = font.render("Press Enter to restart", True, WHITE)
        screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
        screen.blit(sub, sub.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))
    
    pygame.display.flip()
    clock.tick(60)
```

Save. Run. Title screen → press Enter → play → first to
10 → game over → press Enter → title.

**Your Pong now feels like a real game.**

#### Resetting state on transitions

A common bug: you transition to `"playing"` but the
score from the last game carries over. Or the ball is
still in the position from when you lost.

Solution: do the **reset** as part of the transition.

```python
if event.key == pygame.K_RETURN and state == "title":
    state = "playing"
    left_score = 0
    right_score = 0
    ball_rect.center = (WIDTH//2, HEIGHT//2)
    # ... reset whatever else
```

A cleaner approach: write a `reset_game()` function and
call it. When the game grows, you'll thank yourself.

```python
def reset_game():
    global left_score, right_score
    left_score = 0
    right_score = 0
    ball_rect.center = (WIDTH//2, HEIGHT//2)
    # ... etc
```

Then `reset_game()` on transition.

#### Stretch — add a pause state

A fourth state: paused. Press P to pause; press P to
resume.

```python
# In event handling:
if event.key == pygame.K_p:
    if state == "playing":
        state = "paused"
    elif state == "paused":
        state = "playing"

# Add the dispatcher branch:
elif state == "paused":
    # Draw the game frozen (snapshot from last frame stays on screen)
    # Then draw "PAUSED" overlay
    text = big_font.render("PAUSED", True, WHITE)
    screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
    # Notice: no game updates happen this frame
```

Pause = "skip the update; just keep drawing."

#### Stretch — high score display on title

Save the high score to a file (Phase 5 callback). Show
it on the title screen.

```python
import os

def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt") as f:
            return int(f.read())
    return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# At startup:
high_score = load_high_score()

# When game ends:
if score > high_score:
    high_score = score
    save_high_score(high_score)

# On title screen, display:
hs_text = font.render(f"High score: {high_score}", True, WHITE)
screen.blit(hs_text, hs_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100)))
```

Now your game **persists** between runs. The high score
follows you.

#### Stretch — class-based scenes

For bigger games, the if/elif dispatcher gets unwieldy.
Real production games use **scene classes** — each scene
is a class with `update()` and `draw()` methods, and
the main loop calls the *current* scene's methods.

```python
class TitleScene:
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return PlayingScene()
        return self
    
    def draw(self, screen):
        title = big_font.render("PONG", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//2)))


class PlayingScene:
    def __init__(self):
        # set up sprites, scores, etc.
        ...
    
    def update(self, events):
        # game logic
        if won:
            return GameOverScene()
        return self
    
    def draw(self, screen):
        # draw sprites
        ...


# In the main loop:
current_scene = TitleScene()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    current_scene = current_scene.update(events)
    
    screen.fill(BLACK)
    current_scene.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
```

The trick: each scene's `update()` returns either
`self` (stay in this scene) or a *new scene* (transition
to that one).

This pattern scales much better. For a 3-state game,
the if/elif version is fine. For a game with title,
level-select, playing, paused, game-over, victory,
credits... use scene classes.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your game with a title screen.
  Did it feel different to launch?
- For the kids who added pause — pause feels weirdly
  satisfying, doesn't it?
- For the kids who saved a high score — show closing
  the game and reopening to see the score persist.
- Anyone try the scene-class pattern?

Today you learned:

- **A state variable** controls which screen the game
  is showing.
- **`if/elif` dispatch** on the state variable.
- **State transitions** happen on input or game events
  (and may also reset state).
- **Resetting state** is part of the transition.
- (Stretch) **Scene classes** — scalable pattern for
  bigger games.

You also turned at least one previous game from "single
screen toy" into "real game with proper screens." That's
the polish that makes a game *feel* finished.

Next two weeks are **your milestone game.** You have
every tool you need:

- Sprites, classes, groups (Session 9)
- Input + collision (Sessions 4-5)
- Sound (Session 8)
- Game state (today)
- Git + GitHub (Session 7)

Bring an idea. Or come without one — we'll have a seed
list ready.

### If you missed this session

Open Thonny.

1. Build the basic `state_demo.py` from Part A. Get the
   title → playing → game_over flow working.

2. Pick one of your games and add a title screen and
   game-over screen.

3. (Stretch) Add a pause state.

4. (Stretch) Save a high score to a file.

About 60-90 minutes — this is meaty.

### Stretch and extension ideas

- **Pause state** with a translucent overlay over the
  paused gameplay.
- **High score persistence** to a file.
- **Settings screen** with options (volume, color
  scheme, difficulty).
- **Level select screen** between title and playing.
- **Credits screen** accessible from the title.
- **Animated transitions** between scenes — fade out
  the old, fade in the new.
- **Scene classes** for any game with 4+ states.
- **Push your improved game to GitHub.** A second commit
  on the same repo. Real iteration history.

### What's next

Next week is **milestone planning + work day 1.** You
plan and start *your* Pygame game — your design, your
art, your gameplay. Week after, you finish, polish, and
**demo** to the class.

Bring an idea or two. Or come empty-handed — we have a
seed list ready.
