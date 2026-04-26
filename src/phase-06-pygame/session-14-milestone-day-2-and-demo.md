## Session 14: Milestone project work day 2 + demo day

*Phase 6 — Pygame · Session 14 of 14*

### What we're learning today

Today is the **last session of Phase 6 — and the
midpoint of the entire curriculum.** First half: finish
your game. Second half: **demo to the class.** By the
end, you'll have shipped your sixth milestone project,
pushed it to GitHub, and you're halfway through the
journey from "no programming experience" to "shipping
real software."

### You'll need to remember from last time

- **Your project plan** from last week.
- **Whatever you got working** last week.
- **Your buddy** for testing.
- **Git** — commit your final changes today.
- **GitHub** — push the final version.
- **Everything from Sessions 1-12** — you have all the
  tools.

---

### Part A: Final polish

You have about 35 minutes to finish.

#### What "finished" means

Same three rules as always:

1. **It runs without crashing** under normal use.
2. **It does what your plan said it would do** — at
   least the simplest version.
3. **You can explain how it works.**

If your game doesn't meet all three, focus on getting
there before adding anything new.

#### Polish ideas (Phase 6 specific)

- **Add a title screen** if you don't have one.
  (Session 12 pattern.)
- **Add a game-over screen** with restart instructions.
- **Add at least one sound** — bounce, hit, score,
  death. (Session 8.)
- **Background music** that loops.
- **Use sprite classes** for your game objects (Session
  9). If you started with raw rect lists, refactor.
- **Reset on restart** — make sure score, lives,
  positions reset properly between rounds.
- **Window title and size.** `pygame.display.set_caption(
  "...")` and `set_mode((W, H))`.
- **Add a README.md** with controls and how to run.
  Push it to your repo.
- **Take a screenshot** for the README.
- **All commits clean.** `git status` should show
  "working tree clean" before the demo.

#### Buddy test

About 15 min in, **swap with your buddy.** They play
your game; you play theirs. Notice things they get
wrong (control confusion, unclear win condition).
Those are real UX bugs.

For Pygame games especially: hand the keyboard to your
buddy *with no instructions.* Watch what they try.
Their first instinct = your game's controls need to
match.

#### Push to GitHub

If you haven't already: push. Today is your demo day,
and your demo includes showing your repo URL.

```
$ git status
$ git add .
$ git commit -m "Final polish before demo"
$ git push
```

If your repo doesn't have a README, add one now:

```markdown
# My Game

A Pygame game built in From Scratch Programming Class,
Phase 6.

## How to play

- **Move:** WASD or arrows
- **Action:** Space
- **Quit:** Esc

## How to run

```
pip install pygame
python main.py
```
```

Push it.

**Checkpoint:** *Your game runs the basic version of
what you planned, your `git log` shows the journey, and
your repo is on GitHub.* **This is the natural stop point
if class is cut short — but today, demo time is next.**

---

### Part B: Demo day

Each person gets **3-5 minutes**.

#### How a demo works

When it's your turn:

1. **Show your title screen.** That first frame is
   the impression. Walk us through the controls if
   needed.
2. **Play the game.** Let us see it actually working.
3. **Hand the keyboard to a classmate** if there's
   time. Real users, real reactions.
4. **Show your GitHub repo.** Open the URL in a
   browser. Show your `git log --oneline`.
5. **Tell us one thing that was hard.** Bug stories,
   design decisions, things that took longer than
   expected. Maybe one thing that surprised you.
6. **Take one question.**

#### What we're celebrating

This is **Phase 6's demo** — and the midpoint of the
entire curriculum. Halfway through. You've shipped:

- A Scratch project (Phase 1).
- A Python turtle scene (Phase 2).
- A Python program (Phase 3).
- A multi-file CLI tool (Phase 4).
- A desktop app (Phase 5).
- A game (Phase 6, today).

**Six.** Most adults have shipped *zero.* You're at
six.

#### After everyone demos

Mr. Eric will say a few specific things about each
project. Then we celebrate Phase 6 completion. Then
we frame Phase 7.

### What you accomplished

- **Sixth milestone project.** Shipped.
- **Sprite classes** — you wrote production-style
  Pygame code.
- **Game state machine** — your game has real screens.
- **Public GitHub repo** with a real README and (likely)
  a screenshot.
- **Animation, input, collision, sound** — all of it
  working together.
- **You finished Phase 6.** Half the curriculum is
  yours.

### What's next: Phase 7 — HTML, CSS, JavaScript

Phase 7 moves to the **web.** You learn to build things
that run in **a browser** — anyone with internet can
visit and use, no install required.

What's different:

- **HTML** for structure, **CSS** for style,
  **JavaScript** for behavior. Three new languages
  (well, technically — they're all friendly).
- **The browser is your runtime.** No `pip install`,
  no Python. Just a `.html` file and a browser.
- **Designing for *anyone*.** Your work is shareable as
  a URL. Friends, family, anyone in the world can use
  it from their phone or laptop.
- **Visual design.** CSS lets you make things look the
  way you want — colors, fonts, layouts, animations.
- **JavaScript ≠ Python.** Different syntax. Same ideas
  (variables, functions, loops, classes). The mental
  model from Phase 3 still applies.

You'll build:

- Static pages.
- Interactive single-page apps.
- A canvas-based mini-game (yes, browser games — the
  Pygame patterns transfer).
- A milestone web project of your design, hosted on
  GitHub Pages so anyone can use it.

Phase 7 is longer than Phase 6 (about 17 sessions). It
introduces the most languages of any phase. But you've
got a strong foundation — every concept (loops,
functions, classes, state machines) you've already met.

Bring your machine and your enthusiasm. See you in
Phase 7.

### If you missed this session

Two cases:

**Missed only the demo half:** Show your game to Mr.
Eric at the start of next week's class. Same kind of
feedback you'd have gotten in the demo.

**Missed the whole session:** No big deal. Finish your
game at home using your Session 13 plan, and bring it
next week. Or just join us in Phase 7 — you've already
shipped enough this phase to be proud.

### Stretch and extension ideas

If you have time after demos, or want to keep building
at home:

- **Polish more.** Add features, more sound, better
  art, smoother animation.
- **Share your game.** Send the GitHub URL to a friend
  or family member. Have them play.
- **Build a release.** Tools like PyInstaller can turn
  your game into a standalone `.exe` or `.app`.
  Advanced — ask Mr. Eric.
- **Add controller support.** Pygame supports gamepads
  via `pygame.joystick`.
- **Open source someone else's Pygame project.** Find
  one on GitHub, clone it, run it, modify it.
- **Save a copy of every milestone project.** They're
  yours. Six so far.
- **Read a Pygame tutorial outside our curriculum.**
  Real Python, free YouTube series, official Pygame
  docs. Different teachers explain differently.

### What's next

Phase 7 — the web. See you there.
