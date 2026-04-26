## Session 13: Milestone project work day 1

*Phase 6 — Pygame · Session 13 of 14*

### What we're learning today

Today is *your* day. You'll plan a Pygame game — your
design, your art, your gameplay — and start building it.
Next week you'll finish it and demo it to the class.

This is your **sixth milestone project.** You have every
tool you need.

### You'll need to remember from last time

- **The frame loop** (Session 1) — input, update, draw.
- **Drawing and sprites** (Sessions 2-3).
- **Input** (Session 4) — events vs polling.
- **Collision** (Session 5).
- **Sound** (Session 8) — `mixer.Sound`, `mixer.music`.
- **Sprite classes and groups** (Session 9).
- **Game state** (Session 12) — title, playing,
  game-over.
- **Git + GitHub** — commit as you go; push to a repo
  by the end.

---

### Part A: Plan your game

Same shape as previous milestones, with new requirements
specific to Phase 6.

#### The plan

Take a piece of paper or open a blank text file. Answer
these seven questions:

1. **What's the game?** *(One sentence. "Snake but with
   power-ups." "A two-player tank battle." "A puzzle
   where you arrange tiles.")*

2. **What does the player do?** *(Move with arrows?
   Click to shoot? Type a word?)*

3. **What's the goal? What's the lose condition?**
   *(Reach a score? Survive 60 seconds? Clear all
   levels?)*

4. **What sprites are in it?** *(Player? Enemies?
   Items? Backgrounds? Sketch the screen.)*

5. **What states does it have?** *(Title, playing,
   game-over at minimum. Maybe more.)*

6. **What's the simplest version?** *(Build this
   FIRST. No art polish, no sound, no fancy features.
   Just core gameplay.)*

7. **What's one stretch feature?** *(After core works:
   sound? high score? AI opponent? more levels?)*

#### Phase 6 requirements

Your milestone must have:

- **At least one sprite class** (Session 9).
- **At least three game states** — title, playing,
  game-over (Session 12).
- **Pushed to GitHub** by the demo (Session 7).
- **Run without crashing** under normal use.
- **Be fun for at least 30 seconds.** Subjective but
  real. If your buddy can't enjoy it for 30 seconds,
  iterate.

#### If you don't have an idea

Pick one and modify:

- **Snake** — classic. Player snake grows when eating
  apples; lose if you hit yourself or the wall.
- **Brick Breaker** — Pong with a wall of bricks at the
  top. Hit the ball to break bricks. Win when all
  bricks are broken.
- **Space Invaders simple** — a ship at the bottom,
  enemies advancing from the top. Shoot bullets up;
  enemies shoot down.
- **Frogger** — guide a frog across a road / river of
  moving obstacles. Don't get hit.
- **A puzzle game** — Sokoban-style boxes-and-floors,
  match-3, sliding tiles. (The grid-world from
  Sessions 10-11 was this kind!)
- **A two-player game** — tank battle, sumo (push each
  other off), maze-chase, anything that needs two
  controllers (WASD vs arrows).
- **A reaction game** — circles appear and disappear;
  click them before they vanish. Faster as you go.
- **A flappy-bird-style game** — gravity pulls a bird
  down; tap to flap; avoid pipes.
- **A rhythm game** — notes scroll; press the right key
  at the right time.
- **A platformer** (small) — single screen, jump on
  platforms, reach the goal. Don't fall.
- **Asteroids variant** — ship in the middle, asteroids
  fly around. Shoot them. Don't get hit.
- **A shoot-em-up bullet hell** — enemies come from
  above; you dodge bullets, return fire.
- **A grid-world variant** — start with `grid_world.py`,
  but make it about *your* theme (maze for a wizard,
  delivery routes for a robot, etc.).

Pick one. Spend two minutes. Don't overthink.

#### Show Mr. Eric

When your plan is ready, show it to Mr. Eric. He'll
either say "go build it" or ask one question.

#### Set up the project

Create a folder for your project:

```
$ cd ~                          # or wherever you keep projects
$ mkdir my_game
$ cd my_game
$ git init
$ touch main.py                 # create empty file
$ git add main.py
$ git commit -m "Initial project setup"
```

#### Build the simplest version first

Look at your answer to question 6. Build *that* first.
Get a window. Get a player on screen. Get one core
mechanic working. Iterate from there.

For each significant change:

1. Make the change.
2. Run it. Make sure it works.
3. Commit.
4. Move to the next thing.

If something feels risky, make a branch:

```
$ git checkout -b try-new-thing
# experiment
$ git checkout main
$ git merge try-new-thing       # if it worked
# OR
$ git branch -D try-new-thing   # if not
```

#### Use what you've learned

- **Sprite classes** for any game object that has
  position + behavior (player, enemies, items, bullets).
- **Groups** for collections (`enemies = pygame.sprite.Group()`).
- **`spritecollide`** for collisions.
- **State variable** for screens.
- **Sound** for at least one event (Session 8) — even
  one sound makes the game feel alive.

The complete list of patterns is in Sessions 1-12.
Skim them when stuck.

### Wrap-up

Last 5 minutes: each of you, in one sentence, tell the
room **one thing you got working today.**

Bring your project (the folder — Git carries the
history) next week. We'll finish, then demo.

If you got far, **push to GitHub** before next week.
You can also keep iterating at home if you have Pygame
installed.

### If you missed this session

Open Thonny and a terminal.

1. Spend 10-15 minutes answering the seven planning
   questions.

2. Create a folder for your project. `git init` in it.
   Create `main.py`. Commit.

3. Build the simplest version (question 6). Commit as
   you go.

About 60-90 minutes total. By next week you should have:

- A window with at least the player on it.
- One core mechanic working (player can move, or one
  collision happens, or one rule is enforced).
- Several Git commits.

If you don't have an idea, pick from the seed list and
modify.

### Stretch and extension ideas

If your base game is working and you want to add more:

- **Sprite classes** for everything — player, enemies,
  items.
- **Sound effects** for at least three events.
- **Background music** that loops.
- **All three states** — title, playing, game over.
- **High score persistence** to a file.
- **Push to GitHub** — your game becomes a public repo.
- **README.md** with controls and how to run.
- **Polish** — better art, smoother animations, juicier
  feedback.
- **Pause state.**
- **Difficulty progression** — gets harder over time.

### What's next

Next week you'll have time to **finish, polish, and
demo your game** to the class. Each person gets 3-5
minutes. Bring a working game, your enthusiasm, and your
GitHub URL — part of the demo will be showing the
*journey* of how your game came together.
