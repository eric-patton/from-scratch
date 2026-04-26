## Session 11 — Teacher Notes

*Phase 3, Python basics · Session 11 of 16 · Title: Reading and
writing files*

### Purpose of this session

File I/O makes programs *persistent.* Five jobs, in priority
order:

1. **Land the `with open(...) as f:` pattern.** This is the
   modern, safe way to handle files in Python. Resource cleanup
   is automatic. Worth establishing as the default.
2. **Land the three modes (r, w, a).** Mechanical but important.
   `"w"` *erases* the file — easy to lose data if not careful.
3. **Land the `for line in f:` + `.strip()` pattern.** The most
   common way to read text files. Combined with lists/dicts
   from prior weeks, opens up real data processing.
4. **Demonstrate persistence.** The notes program literally
   remembers things between runs. The "wow, I quit and the data
   was still there" moment is the lesson landing.
5. **Sneak preview of `try/except`.** The
   `try: ... except FileNotFoundError:` pattern is needed for
   any program that loads a possibly-missing file. Today's
   intro is informal; Session 13 makes it formal.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Verify file write/read works on Linux Mint (it does; sanity
  check).
- Optional: have a sample text file ready (a public-domain
  short text, a passage, anything ~20 lines) for the file
  processor extension.
- Verify Thonny saves files to a known folder (usually the
  same folder as the .py file). Worth noting at the projector.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was dictionaries.
  Anyone build a dictionary-based program at home?
- **Part A: writing files** (~35 min) — the `with open` pattern
  ~10 min, the modes ~5 min, multi-line writing ~10 min,
  loop-driven writing ~5 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: reading + persistent notes** (~40 min) — basic
  reading ~10 min, the strip pattern ~5 min, persistent notes
  build ~20 min, stretch/extension ~5 min.
- **Wrap-up** (~5 min).

If running short, **the file processor extension can be cut.**
The persistent notes program is the goal.

### Teaching Part A

#### Why `with`

The naive way to open a file is:

```python
f = open("hello.txt", "w")
f.write("hi")
f.close()
```

This works but has a problem: if your code errors between
`open()` and `close()`, the file might never get closed
properly, leading to data loss or locks. The `with` statement
handles this automatically.

> "We use `with open(...) as f:` because it always cleans up,
> even if something goes wrong. It's the modern Python way and
> what real code does."

Don't dwell on context managers — just establish the habit.

#### Walking through `with open(...)`

Demo at the projector:

```python
with open("hello.txt", "w") as f:
    f.write("Hello, file!\n")
```

Step through:
- `open("hello.txt", "w")` — open the file for writing
- `as f` — give it the temporary name `f` inside this block
- The indented body uses `f` to write
- When the body ends, the file auto-closes

The file appears in the same folder as the `.py` file. Show
this at the projector — open the file manager, find the
folder, see the file appear after the run.

> "When you write a file from a Python program, it goes to the
> same folder as your `.py` file by default. You can find it,
> open it in any text editor, see what's there."

This is genuinely magical for kids. Their program created a
real file they can see and open with other apps.

#### The modes

`"w"` is the default for the lesson. Mention `"a"` (append)
and `"r"` (read) briefly.

> "`'w'` always erases what was there before. If you have data
> you don't want to lose, use `'a'` to add to the end instead.
> Or read first, modify in memory, then write."

This will save real student work later.

#### `\n` for newlines

Each `.write()` writes exactly what you give it. To go to a
new line, you have to include `\n`.

> "If you write 'pizza' and then 'soccer' without `\n`, the
> file says 'pizzasoccer' — all on one line. The newline
> character `\n` is what makes the next thing appear on a new
> line."

Demo without `\n` first, then with. The visible difference
sticks.

### Teaching Part B

#### Basic reading

```python
with open("favorites.txt", "r") as f:
    for line in f:
        print(line)
```

Run. Show the extra blank lines. Walk through:

> "The file has each line ending with `\n`. `print` adds its
> *own* `\n` at the end. So we end up with two newlines per
> line, which prints blank lines between."

Then `.strip()` to fix:

```python
print(line.strip())
```

> "`.strip()` removes whitespace from the start and end of a
> string — including newlines. Now `print` only adds one
> newline, and we get clean output."

This pattern (`for line in f: print(line.strip())`) is
extremely common. Drill it.

#### Persistent notes program

This is the integration moment. Walk through the structure
before any code:

> "Three parts: load existing notes from the file (if any),
> ask the user for new notes, then save everything back."

The `try/except FileNotFoundError` is the only new mechanic.
Frame it informally:

> "If the file doesn't exist (first time running the program),
> Python errors. The `try / except FileNotFoundError: pass`
> says 'try to open it; if it's not there, just skip and
> move on.' We'll cover this `try/except` thing properly
> next week."

Don't over-teach. Today's intro is enough.

The "save everything back" part uses `"w"` mode — erases the
file and rewrites the whole list. This is fine for small
files; for huge files you'd be more careful. Mention
briefly.

#### The persistence demo

After kids build it, **make them run it twice.** First run:
add some notes, quit. Look at the file (open it in a text
editor). Second run: notes are still there!

This is the lesson landing. The "my program remembered!"
moment.

#### Stretch — append mode

Append mode for things you only add to (logs, diary
entries). Mechanical addition.

#### Extension — file processor

Pulls together file I/O, lists, iteration, len, max-tracking,
slicing. Real Phase 3 integration.

If a kid wants a sample file to process: provide one (a
short story or text passage), or have them save one of their
own programs (.py is also text).

### Common stumbles

- **Forgot the `\n`** — file becomes one giant line. Add `\n`
  to each `.write()`.
- **Used `"w"` and lost data.** `"w"` erases. If kid had
  written a list to a file and then ran a different program
  that opened the same file in `"w"` mode, gone. Lesson:
  use `"a"` for adding; only `"w"` when you're rewriting
  the entire file.
- **`with` block indentation.** Code that should be inside
  the `with` block isn't indented; the file closes too early.
  Walk through the indentation.
- **Reading a file that doesn't exist.** `FileNotFoundError`.
  Handle with try/except (foreshadow), or check first with
  `os.path.exists` (we won't formally teach `os`).
- **Writing strings without converting.** `f.write(5)` errors
  because `5` is an int. Convert: `f.write(str(5))` or use an
  f-string.
- **Newlines in unexpected places.** When reading, each line
  has `\n` at the end. Forgot `.strip()` → comparisons fail
  ("apple" != "apple\n"). Always `.strip()` lines from files.
- **Wrong working directory.** If Thonny saves the .py file in
  one folder but the kid runs it elsewhere, `open("name.txt")`
  uses the current dir, which may not be the .py folder.
  Confusing. Easiest fix: save and run from the same folder.

### Differentiation

- **Younger kids (9-10):** May find file I/O abstract. Lean on
  the visible payoff — they can SEE the file in the file
  manager. Make this concrete.
- **Older kids (12+):** Will pick this up fast. Push them to
  the file processor extension or to add features to the notes
  program (delete a note, search for a note, etc.).
- **Advanced (any age):** Suggest:
  - JSON for structured data (`import json; json.dump(...)`,
    `json.load(...)`)
  - Reading binary files (`"rb"` mode)
  - Writing CSV with the `csv` module
  - Pickle for saving any Python object (`import pickle`)
- **Struggling:** A kid who can't get the basic write working
  is the kid you focus on. Most common cause: file permission
  issues (rare on Linux), or wrong working directory. Help
  them find their file in the file manager.

### What to watch for

- **The "I made a real file" reaction** when they see their
  file appear in the folder. Affirm.
- **The "wait, my notes are still there!" reaction** on the
  second run of the persistent notes program. The
  persistence-between-runs is genuinely surprising the first
  time.
- **Buddies sharing files.** "Hey, save your notes to a file
  and let me read them" — encourage. Real-world workflow.
- **Frustration with the `\n` and `.strip()` interaction.**
  Both come up. Walk through patiently.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 12 (next week, hangman).** Word list for hangman
  comes from a file (`words.txt`). Today's reading patterns
  used directly.
- **Session 13 (try/except).** Today's `try/except
  FileNotFoundError` is the informal preview; next week
  formalizes the pattern.
- **Session 14 (text adventure or CSV reader).** Reading
  structured data from files. CSV is just a slight extension
  of today's text reading.
- **Phase 4 (intermediate Python).** Modules and packages —
  including `os`, `pathlib`, `json`, `csv` — let you do much
  more with files. Today is the foundation.
- **Phase 8 (Flask).** Web apps often read configuration from
  files, save uploads as files, etc. Same `with open` pattern.
- **The peanut butter callback opportunity:** the
  `forgot \n, file is all one line` bug is a precision moment.
  The computer wrote exactly what was given; you didn't include
  newlines, so there are no newlines.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: sample .txt file for the file processor
      extension
- [ ] File manager open at the projector for showing files
      appearing
- [ ] Class roster
