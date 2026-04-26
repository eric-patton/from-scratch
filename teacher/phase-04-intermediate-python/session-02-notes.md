## Session 2 — Teacher Notes

*Phase 4, Intermediate Python · Session 2 of 9 · Title: Multi-
file programs and your own modules*

### Purpose of this session

Multi-file programs are the #1 organizational tool in real
Python. Five jobs, in priority order:

1. **Land "files can import each other."** The mental shift
   from "one file = one program" to "many files cooperating"
   is the lesson.
2. **Land `import yourfile`.** Same syntax as `import
   random` — but for student-written modules. Students will
   get the "wait, I can do that?" reaction.
3. **Land code organization principles.** Code in one file,
   data in another (callback to hangman words.txt and
   adventure rooms.json from Phase 3). The journal/quotes/
   main split today is the cleanest example yet.
4. **Introduce Python conventions.** UPPERCASE for constants,
   `_` prefix for private, `def main()` pattern. These aren't
   syntactic rules but every Python programmer follows them.
5. **Set up Sessions 3-7.** Multi-file is the structural
   foundation for Phase 4. Stdlib modules (Session 3),
   classes (Session 4), Git tracking files (Sessions 5-6),
   and tests in their own files (Session 7) all build on
   multi-file.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny + terminal open.
- Optional: pre-built three-file journal program for the
  destination preview.
- Verify Python finds modules in the same folder when run
  from the terminal. Should "just work" but worth confirming.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was the CLI.
  Anyone use it at home?
- **Part A: split a program** (~40 min) — create folder and
  files ~5 min, motivation ~5 min, build tools.py ~5 min,
  build main.py ~10 min, run from terminal ~5 min,
  from/import variation ~5 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: three-file journal** (~35 min) — quotes.py ~5
  min, journal.py ~10 min, main.py ~10 min, run + test ~5
  min, stretch (search) ~5 min.
- **Wrap-up** (~5 min).

If running short, **the search stretch and the quotes-from-
file extension can be cut.** The base journal program is the
goal.

### Teaching Part A

#### Folder + files

Have students create a fresh folder and two empty files
(`tools.py`, `main.py`) before the lesson properly starts.
This is mechanical setup; getting it out of the way first
keeps the conceptual flow clean.

Walk through using Thonny's File → New → Save As to create
each file in the same folder. Or use a file manager. Either
works.

#### The motivation

Show the all-in-one calculator at the projector. Then talk
through the issue:

> "This works. But the four math functions could be useful
> in *other* programs too. Why are they trapped here? What
> if we want to use them in a budget app? In a grade
> calculator? We'd have to copy them every time. There's a
> better way."

This sets up "split into files" as the answer.

#### Build tools.py

Functions only, no main code. Worth pointing out:

> "This file is a *module* — a file of reusable code. It
> has no `input`, no `print`, no main program flow. Just
> definitions. Other files can import and use it."

#### Build main.py

The `import tools` line is the new thing. Walk through:

> "`import tools` tells Python to load the file `tools.py`
> from this folder. After that, we use the functions with
> `tools.add(...)` — the filename (without `.py`), dot,
> function name. Same syntax as `random.randint(...)` —
> just our own file this time."

This is the connection moment. Several kids should get the
"oh, I've been doing this all along, just with built-in
modules" insight.

#### Run from the terminal

The `cd` to the folder, then `python main.py`. Critical: it
must be run *from the folder containing both files.* If you
run from another folder, Python won't find `tools.py`.

> "Python looks for imports in the current folder. So you
> have to be IN the folder when you run. `cd` there first."

This is the only mechanical gotcha of the session. Drill it.

#### `from tools import add, subtract, ...`

Show the alternate syntax:

```python
from tools import add, subtract, multiply, divide
```

Then `add(x, y)` directly — no prefix.

> "Two styles. `import tools` then `tools.add(...)` keeps
> the source visible. `from tools import add` then `add(...)`
> is shorter but loses the source. Pick one style per file
> and stick with it."

The choice is real. Don't be too prescriptive. Both have
merits.

### Teaching Part B

#### The plan

Walk through the three-file plan at the projector:

> "Quotes is its own file because random quotes are a
> standalone thing. Journal is its own file because file
> reading and writing is its own concern. Main pulls them
> together for the user. Each file has one job."

Naming the principle helps:

> "This is called *separation of concerns* — each piece of
> code handles one thing. Real programs are organized this
> way."

#### Build quotes.py

Mechanical. Worth pointing out the convention:

> "`QUOTES` in capitals is a Python convention for a
> *constant* — a value that doesn't change while the program
> runs. It's not enforced; it's just a hint to readers."

#### Build journal.py

The `try / except FileNotFoundError` is the Session 13
pattern returning. Worth a callback:

> "Same pattern as Session 13 — if the file doesn't exist
> on the first run, we don't crash, we just return an empty
> list."

The list comprehension is new syntax:

```python
[line.strip() for line in f if line.strip()]
```

Walk through what it does:

> "This is a *list comprehension* — a compact way to build
> a list. It's the same as a for-loop with an if-check
> inside, all on one line. We haven't formally taught it
> yet but it's worth recognizing — Python uses it
> constantly. The longer version is in the handout."

Don't formally teach. Just show.

#### Build main.py

The `def main(): ...; main()` pattern is new and worth
naming:

> "This is the *main function pattern.* Wrap your program's
> main code in a function called `main`, then call it at
> the bottom. It looks slightly weird at first but it's a
> Python convention worth adopting. Two reasons: it makes
> the file importable without running everything, and it
> makes the main flow easy to find."

#### Run it

The first run shows "no entries yet"; second run shows the
entry from before. The persistence-between-runs callback
to Session 11 lands again.

#### Stretch — search

The search function adds a third feature to `journal.py`.
The menu in `main.py` grows. Worth pointing out:

> "Notice — when we wanted to add a feature, we added it
> to `journal.py` (where journal stuff lives) and called it
> from `main.py`. Each file's job stayed clean. *That's the
> point* of multi-file."

#### Extension — quotes from file

Pulls QUOTES out of `quotes.py` and into `quotes.txt`. Same
code-vs-data separation pattern as Session 12 (hangman) and
Session 14 (text adventure). Reinforces.

The `_load_quotes` with a leading underscore introduces:

> "The underscore in `_load_quotes` means 'this is meant to
> be private — only used inside this file.' Python doesn't
> enforce it; it's a hint. Other modules shouldn't call
> `_load_quotes` directly; they should use `random_quote`."

### Common stumbles

- **`ModuleNotFoundError: No module named 'tools'`.** Almost
  always: run from a different folder than where `tools.py`
  is. Use `pwd` to check. `cd` to the right place.
- **Imported the wrong name.** `from tools import addd`
  (typo) — `ImportError: cannot import name 'addd'`.
- **`tools.add` instead of `tools.add(x, y)`.** Without
  parens, it's the function object, not the result of
  calling it. Common.
- **`import tools.py`** (with the .py extension). Don't
  include `.py` in imports.
- **Edited the imported file but didn't see the change.**
  Each `python` run loads fresh; should be fine. But if
  using interactive shell or auto-reload, may need to
  re-import.
- **`def main()` defined but never called.** The function
  exists but the program does nothing. Add `main()` at
  the bottom (no indent).
- **Forgot to save the imported file.** Edited `tools.py`
  in Thonny but didn't save. The terminal still sees the
  old version.

### Differentiation

- **Younger kids (9-10):** May find the multi-file structure
  confusing. Lean on the "each file has one job" framing.
  Walk through navigating between files in Thonny (file
  tabs at the top).
- **Older kids (12+):** Will pick up multi-file fast. Push
  them to the journal stretch and the quotes-from-file
  extension.
- **Advanced (any age):** Suggest:
  - Subfolders for modules (with `__init__.py`)
  - `import tools as t` — renaming on import
  - The `__name__ == "__main__"` idiom (Phase 4+ topic)
  - Building a small "library" of utilities to reuse across
    later projects
- **Struggling:** A kid who can't get the basic two-file
  import working in Part A is the kid you focus on. Most
  common cause: ran from wrong folder, or wrong filename.
  Walk through `pwd`, `ls`, then `python main.py`.

### What to watch for

- **The "wait, I can import my own files?" reaction.**
  Several kids will visibly process this. Affirm — it's
  the same pattern as `import random`.
- **The "this feels organized" reaction** to the three-file
  journal. Several kids will prefer it to a single big
  file once they see it.
- **Buddies trading file-organization ideas.** "What if I
  put X in its own file?" — encourage. This is real
  software design conversation.
- **Kids who keep all the code in `main.py`.** Push them to
  split. The whole point of today is that splitting is
  *better.* If they're not splitting, the lesson didn't
  land.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 3 (next week, stdlib).** Today's `import` from
  your own files is the same syntax as importing from
  Python's standard library. Today's foundation lets us
  explore the whole library next week.
- **Sessions 5-6 (Git).** Multi-file projects are exactly
  what Git tracks well. Foreshadow.
- **Session 7 (testing).** Tests live in their own file —
  e.g., `test_tools.py` next to `tools.py`. Multi-file is
  the prerequisite.
- **Sessions 8-9 (milestone).** The milestone project should
  use multi-file structure from day one.
- **Phase 5 (customtkinter).** GUI apps split widgets into
  their own modules. Today's pattern scales up.
- **Phase 6 (Pygame).** Game state in one module, sprites
  in another, level data in another. Same idea.
- **Phase 8 (Flask).** Routes in one file, models in another,
  templates in their own folder. Again, same idea.
- **Peanut butter callback opportunity:** the
  ModuleNotFoundError when running from the wrong folder is
  a precision moment. Python looked exactly where it was
  supposed to look (the current directory); the file wasn't
  there.

### Materials checklist

- [ ] Demo machine with Thonny + terminal
- [ ] Optional: pre-built journal program for the
      destination preview
- [ ] Projector (helpful for the multi-file walkthrough)
- [ ] Class roster
