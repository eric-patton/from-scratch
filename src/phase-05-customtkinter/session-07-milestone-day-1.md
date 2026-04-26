## Session 7: Milestone project work day 1

*Phase 5 — customtkinter · Session 7 of 8*

### What we're learning today

Today is *your* day. You'll plan a desktop app of your own
design — your idea, your widgets, your behavior — and start
building it. Next week you'll finish it and demo it to the
class.

### You'll need to remember from last time

- **The widget toolbox** — labels, buttons, entries,
  checkboxes, radios, dropdowns, frames.
- **`pack` and `grid`** for layout.
- **Callbacks** with `command=`.
- **The redraw pattern** — state + a refresh function.
- **Persistence with JSON** (Session 6 stretch).
- **Git** (Phase 4 Sessions 5-6) — commit as you go.

---

### Part A: Plan your app

Same shape as previous milestones, with new requirements
specific to Phase 5.

#### The plan

Take a piece of paper or open a blank text file. Answer
these six questions:

1. **What's the app?** *(One sentence. "A flashcard
   quiz." "A budget tracker." "A drawing pad.")*

2. **What does the user do with it?** *(How do they
   interact? What do they click? What do they type?)*

3. **What widgets will it have?** *(Labels, entries,
   buttons, lists, checkboxes? Sketch the window on
   paper if it helps.)*

4. **What state does it track?** *(A list of items? A
   single value? A dictionary?)*

5. **What's the simplest version?** *(Build this FIRST.
   No persistence, no fancy features — just the core.)*

6. **Will it save data to a file?** *(Optional but
   recommended. JSON for lists/dicts, plain text for
   single values.)*

#### If you don't have an idea

Pick one and modify:

- **A flashcard app** — load questions from a file, show
  one at a time, click to reveal the answer, next button.
- **A budget tracker** — add expenses with category and
  amount, show running totals, save to JSON.
- **A drawing pad** — `CTkCanvas` (similar to Phase 2
  turtle world), click and drag to draw lines.
- **A timer / pomodoro app** — set a duration, click
  start, watch the countdown.
- **A dice roller for tabletop games** — pick number of
  dice, click roll, show results.
- **A unit converter** — pick from/to units, type a
  value, see the result.
- **A simple text editor** — `CTkTextbox`, save/load
  buttons, file path entry.
- **A character sheet for a game** — name, stats, items
  (extension of Session 4's character builder, with save).
- **A quiz game** — multiple choice questions, score
  tracking, end screen.
- **A music player UI** — list of songs, play/pause/skip
  buttons. (The buttons can fake it — print to console
  instead of actually playing audio.)
- **A memory match game** — grid of buttons that flip
  to reveal images or letters; match pairs.

Pick one. Spend two minutes. Don't overthink.

#### Show Mr. Eric

When your plan is ready, show it to Mr. Eric. He'll either
say "go build it" or ask one question.

#### Set up the project

Create a folder for your project. Open a terminal:

```
$ cd ~                          # or wherever you keep projects
$ mkdir my_app                  # use your project's name
$ cd my_app
$ git init
```

Create your main file (probably `main.py` or `app.py`) and
commit it before writing much:

```
$ git add main.py
$ git commit -m "Initial project setup"
```

**Commit early, commit often.** Each meaningful change
gets its own commit.

#### Build the simplest version first

Look at your answer to question 5. Build *that* first.
Get a window on screen. Get the most important widget
working. Wire up one callback. Then iterate.

For each significant change:

1. Make the change.
2. Run it. Make sure it works.
3. Commit (`git add ...; git commit -m "..."`).
4. Move to the next thing.

If your widgets are getting unwieldy and there are lots of
top-level globals, **wrap your code in a class** (like
Session 6's class refactor). Real apps tend to grow into
classes.

If something feels risky (a big change you might want to
undo), make a branch:

```
$ git checkout -b try-new-thing
# ... experiment ...
$ git checkout main
$ git merge try-new-thing       # if it worked
# OR
$ git branch -D try-new-thing   # if it didn't
```

### Wrap-up

Last 5 minutes: each of you, in one sentence, tell the
room **one thing you got working today.** Bonus points
for showing a screenshot.

Bring your project (the folder — Git carries the history)
next week. We'll finish, then demo.

### If you missed this session

Open Thonny and a terminal. Then:

1. Spend 10-15 minutes answering the six planning
   questions.

2. Create a folder for your project. `git init` in it.
   Create your first file. Commit.

3. Build the simplest version. Commit as you go (every
   few meaningful changes).

About 60-75 minutes total — planning + a substantial first
build. If you can show your buddy a window with at least
one working button next week, you're ready for Day 2.

If you don't have an idea, the seed list above is a
starting point. Pick one and modify.

### Stretch and extension ideas

If your base project is working and you want to add more:

- **Add JSON persistence** so state survives between runs
  (Session 6 pattern).
- **Refactor to a class** if you started with globals
  (Session 6 stretch).
- **Add a Settings dialog** with `CTkToplevel` — a
  separate window for app preferences.
- **Style it** — try `ctk.set_appearance_mode("dark")`
  and `ctk.set_default_color_theme("green")` near the top.
- **Use a branch** to try a feature without breaking
  main. Merge if it works.
- **Add a menu bar** with File / Edit / View options
  (advanced — `tkinter.Menu`).
- **Make it resizable nicely** — use `grid` weights so
  things scale with the window.
- **Add icons** — buttons can have images via `image=`.

Whatever you add, **commit each change.** Future you
wants to see the journey.

### What's next

Next week is the **last session of Phase 5.** You'll have
time to finish, polish, and **demo your app** to the
class. Each person gets 3-5 minutes. Bring a working app,
your enthusiasm, and your Git log — part of the demo will
be showing the *journey* of how your app came together.
