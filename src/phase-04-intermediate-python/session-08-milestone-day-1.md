## Session 8: Milestone project work day 1

*Phase 4 — Intermediate Python · Session 8 of 9*

### What we're learning today

Today is *your* day. You'll plan a Python project that uses
the Phase 4 toolkit — multi-file structure, Git tracking,
maybe classes, maybe tests — and start building it. Next
week you'll finish it and demo it to the class.

### You'll need to remember from last time

- **Multi-file programs** (Session 2) — split your code
  across files.
- **Stdlib modules** (Session 3) — `datetime`, `pathlib`,
  `sys`, `os`, etc.
- **Classes** (Session 4) — bundle data and methods.
- **Git** (Sessions 5-6) — `init`, `add`, `commit`, `log`,
  branches.
- **Tests** (Session 7) — `assert` statements that catch
  bugs.

---

### Part A: Plan your project

Same shape as previous milestones, with new requirements
specific to Phase 4.

#### The plan

Take a piece of paper or open a blank text file. Answer
these six questions:

1. **What's the program?** *(One sentence.)*

2. **What does the user do?** *(How do they interact?
   Input? Subcommands? Menu?)*

3. **What files will you have?** *(Brainstorm. At least
   two — one for the main program, one for a module.
   Could be more. Examples: `main.py`, `data.py`,
   `widgets.py`.)*

4. **Will you use classes?** *(Optional. If yes, what are
   they?)*

5. **What's the simplest version?** *(Build this FIRST.)*

6. **What will you test?** *(At least one or two `assert`
   tests for the important pieces.)*

#### If you don't have an idea

Pick one and modify:

- **A multi-file CLI tool** — extended journal, todo list,
  budget tracker, contact book. Use `sys.argv` for
  subcommands.
- **A class-based simulation** — extended Pet game with
  multiple Pet types; a small bank with multiple accounts;
  a mini RPG with players and enemies.
- **A tested utility library** — a module of useful
  functions (string utilities, math helpers, date
  utilities) with thorough tests.
- **A multi-file game** — text adventure with rooms in their
  own file, items in another, game logic in main.
- **A "learning tool"** — flashcards, quiz, a math
  practice app, anything educational.

Pick one. Spend two minutes. Don't overthink.

#### Show Mr. Eric

When your plan is ready, show it to Mr. Eric. He'll either
say "go build it" or ask one question.

#### Set up the project — with Git from day one

Create a folder for your project. In a terminal:

```
$ cd ~                          # or wherever you keep projects
$ mkdir my_project              # use your project's name
$ cd my_project
$ git init                      # start tracking immediately
```

Make your first file (probably `main.py`). Commit it before
writing much:

```
$ git status
$ git add main.py
$ git commit -m "Initial project setup"
```

**Commit early, commit often.** Every meaningful change
gets its own commit. Don't wait until the end.

#### Build the simplest version first

Look at your answer to question 5. Build that *first.*
Iterate from there.

For each significant change:

1. Make the change.
2. Test it (run the code, make sure it works).
3. Commit (`git add ...; git commit -m "..."`).
4. Move to the next thing.

If something feels risky (a big change you might want to
undo), make a branch:

```
$ git checkout -b try-new-thing
# ... experiment ...
$ git checkout main
$ git merge try-new-thing    # if it worked
# OR
$ git branch -D try-new-thing  # if it didn't
```

This is real software engineering practice.

### Wrap-up

Last 5 minutes: each of you, in one sentence, tell the
room **one thing you got working today**.

Bring your project (just the folder — Git carries the
history) next week. We'll finish, then demo.

### If you missed this session

Open a terminal. Then:

1. Spend 10-15 minutes answering the six planning questions.

2. Create a folder for your project. `git init` in it.
   Create your first file. Commit.

3. Build the simplest version. Commit as you go (every few
   meaningful changes).

About 50 minutes total — planning + significant build time.

If you don't have an idea, the seed list above is a starting
point. Pick one and modify.

### Stretch and extension ideas

If your base project is working and you want to add more:

- **Add tests** for your core functions/methods (Session 7).
- **Use a branch** to try a risky feature without breaking
  main (Session 6).
- **Read configuration from a file** instead of hardcoding
  (Session 11 of Phase 3).
- **Add CLI subcommands** (Session 3 — git/journal pattern).
- **Use a class** to organize state (Session 4).
- **Use a stdlib module** you haven't used yet (`json`,
  `csv`, `datetime`).

Whatever you add, **commit each change.** Future you wants
to see the journey.

### What's next

Next week you'll have time to finish, polish, and **demo
your project** to the class. Each person gets 3-5 minutes.
Bring a working project, your enthusiasm, and your Git log
— part of the demo will be showing the *journey* of how
your project came together.
