# Phase 6 — Pygame (2D games)

You can write desktop apps. You can save versions of your
work and (soon) push them to the world. Now we make
**games** — animated, interactive, with graphics and
sound and the kind of "one more try" pull that real games
have.

## What this phase is

About fourteen sessions on building 2D games with
**Pygame**. You'll learn the *frame loop* — the heartbeat
of every video game ever made — and use it to build
classic games together (Pong is the big one), then design
and ship your own game for the milestone.

This phase is the longest one yet because games are bigger
than apps. There's more to remember, more moving parts,
and more chances to get something wrong in a really
visible way (sprites flying off-screen, characters
walking through walls). That's also what makes it fun.

## What you'll learn

| Session | Idea | What's new |
|---|---|---|
| 1 | Welcome to Pygame — the frame loop | The 60-frames-per-second mental model |
| 2 | Drawing on the screen | `pygame.draw`, colors, shapes, the coordinate system |
| 3 | Sprites and images | Loading PNGs, `blit`, the `Rect` class |
| 4 | Movement and the keyboard | Key events + `Clock` for smooth motion |
| 5 | Collision detection | `Rect.colliderect`, simple physics |
| 6 | Build Pong together | Your first complete game |
| 7 | GitHub — push to the world | `git push`, repos as portfolios |
| 8 | Sound and music | `pygame.mixer`, sound effects, background music |
| 9 | Sprite classes and groups | The `Sprite` class, organizing many things |
| 10 | The grid-world (intro) | Mr. Eric's coding-puzzle game — play it |
| 11 | The grid-world (extending) | Build your own puzzles, add features |
| 12 | Title screens and game over | Game state, scenes |
| 13 | Milestone day 1 | Plan + start your game |
| 14 | Milestone day 2 + demo | Finish + showcase |

The Python skills here build on Phase 4's classes
(sprites are classes), Phase 4's Git (you'll push your
first repo), and Phase 5's event-driven thinking
(rethought as the frame loop).

## What you'll build

- **Sessions 1-5:** small experiments — moving shapes,
  sprites you can control, things that bounce.
- **Session 6:** **Pong** — a complete game we build as
  a class.
- **Sessions 9-12:** the **grid-world** (a programmable
  character on a grid solving puzzles), plus polish like
  title screens.
- **Sessions 13-14:** *your* milestone game — your idea,
  your art, your gameplay.

## What you'll need

- Same machine as before. **Pygame** is pre-installed on
  the class machine.
- For working at home, install with:
  ```
  $ pip install pygame
  ```
- Thonny still works as your editor.
- A **GitHub account** (we'll set this up together in
  Session 7 — bring an email address you use).

## How sessions work

Same shape as before:

- **Part A** introduces a new game-building concept with
  a guided exercise.
- **Part B** is open practice or a project.
- **Wrap-up** to share what you did.

## A note about games

Games are different from anything you've built so far.

A Pygame program runs a **frame loop** — about 60 times
every second, the program:

1. Reads input (keys, mouse).
2. Updates state (move things, check collisions).
3. Draws everything to the screen.

That's the heartbeat. Every game you've ever played —
Mario, Minecraft, Fortnite — runs this same loop. The
art is more elaborate, the physics are more complex, but
the structure is the same.

You're learning the actual mental model that real game
developers use, just with simpler graphics.

## A note about sprites and classes

Phase 4 introduced classes. Phase 5 used them as a
production-style refactor. **Phase 6 makes them
essential.** Every moving thing in your game — the
player, each enemy, each bullet, each particle — will be
a sprite *instance*. Sprite groups let you update or draw
hundreds of them at once.

If classes felt abstract before, they will not by the end
of this phase.

## A note about the difficulty curve

Sessions 1-5 are individual mechanics — drawing, moving,
collisions. Each one stands alone. **Session 6 (Pong)
is the first big jump** — combining all five into one
game. Expect that to feel hard. That's normal.

After Pong, the curve flattens. Sound, classes, the
grid-world — each one adds a new tool but the *shape*
of a game program is now familiar.

## Where to start

[Session 1: Welcome to Pygame](session-01-welcome.md)
opens your first window — but this time, the window has
a heartbeat.

When you're stuck, the [Getting unstuck](../appendices/getting-unstuck.md)
appendix is the first place to go. The
[Glossary](../appendices/glossary.md) will grow as Phase
6 introduces game-specific terms.

Welcome to game development. Let's go.
