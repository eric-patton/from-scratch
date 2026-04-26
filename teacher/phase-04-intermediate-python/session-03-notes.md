## Session 3 — Teacher Notes

*Phase 4, Intermediate Python · Session 3 of 9 · Title:
Standard library modules*

### Purpose of this session

The standard library is one of Python's biggest selling points
— so much functionality "in the box." Today is a tour, not
deep dives. Five jobs, in priority order:

1. **Land "the standard library exists and is huge."** Just
   knowing what's there changes how kids think about
   problems. "Oh, I can probably import something for that."
2. **Land `sys.argv` for command-line arguments.** Combined
   with last week's CLI workflow, this is how kids start
   writing real CLI tools.
3. **Land `datetime` and `pathlib` as the modern Python
   defaults.** Both come up in almost every real program.
4. **Build a real CLI tool.** The journal program is small but
   feels like a real utility — runs from terminal, takes
   arguments, has subcommands.
5. **Set up Session 4 (classes).** Today's `Path`, `datetime`
   are classes. Foreshadow lightly — "next week we'll build
   our own."

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with terminal open.
- Pre-built complete journal CLI for destination preview.
- Make sure all stdlib modules import (they always do — but
  sanity check on Linux Mint).

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was multi-file.
  Anyone build a multi-file program at home?
- **Part A: tour** (~40 min) — datetime ~10 min, pathlib ~10
  min, sys.argv ~10 min, os briefly ~5 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: journal CLI** (~35 min) — base ~15 min,
  subcommand stretch ~10 min, view-specific-day extension ~5
  min, list extension ~5 min.
- **Wrap-up** (~5 min).

If running short, **the extensions can be cut.** The base
journal CLI is the goal.

### Teaching Part A

#### datetime

The `datetime.now()` returns a datetime object. The
`strftime` method formats it. Walk through the format codes:

| Code | Meaning |
|---|---|
| `%Y` | 4-digit year (2026) |
| `%m` | 2-digit month (04) |
| `%d` | 2-digit day (25) |
| `%H` | 2-digit hour (24-hour) |
| `%M` | 2-digit minute |
| `%S` | 2-digit second |
| `%A` | full weekday name (Wednesday) |
| `%B` | full month name (April) |

Don't memorize. Look up when needed.

The `timedelta` for date math is genuinely useful:

> "Want to know what date is 30 days from now? `now +
> timedelta(days=30)`. Want to know what date was a year
> ago? `now - timedelta(days=365)`. The math just works."

This is one of those "Python is great" moments.

#### pathlib

The `Path` class is the modern way. Walk through:

```python
from pathlib import Path
home = Path.home()
notes = home / "notes.txt"
```

The `/` operator for joining paths is genuinely surprising:

> "The slash isn't division here — it's joining. `Path.home()
> / 'notes.txt'` builds the full path. This works on Windows
> too, even though Windows uses backslashes for paths. `Path`
> handles the platform difference."

This is one of pathlib's killer features.

`.exists()`, `.is_file()`, `.is_dir()`, `.mkdir()` are
mechanical. Show as needed.

#### sys.argv

The new big one for today. Walk through:

> "When you run `python script.py one two three` in the
> terminal, `sys.argv` is `['script.py', 'one', 'two',
> 'three']`. The script name is always first. Then each
> argument the user typed."

Demo at the projector by running:

```
$ python tour.py hello world
```

And showing the output. The "wait, my program can take
arguments?" moment.

The `sys.exit(1)` is also new. Mention briefly:

> "`sys.exit(N)` ends the program with status code N. Zero
> means success; non-zero means error. Programs that run
> from scripts use this convention to signal what
> happened."

#### os

Quick mention. `os.environ` for environment variables;
`os.listdir` for directory listing. Most os.path stuff has
been replaced by pathlib but the module still has useful
bits.

> "`os` is older. Most of what `os.path` does, `pathlib`
> does better. But `os.environ` for environment variables
> and `os` for some lower-level stuff are still common."

Don't dwell.

### Teaching Part B

#### The journal CLI

Walk through the structure before any code:

> "We're building a real CLI tool. The user runs `python
> journal.py 'some text'` and we save the text to today's
> file with a timestamp. Three modules in one program:
> `sys` for the argument, `datetime` for today's date,
> `pathlib` for the file path."

Build at the projector. The new patterns:

- `Path.home() / "journals"` — build a path
- `.mkdir(exist_ok=True)` — make if not exists
- `len(sys.argv) < 2` and `sys.exit(1)` — usage check
- `" ".join(sys.argv[1:])` — joining all args after the
  script name
- `datetime.now().strftime("%Y-%m-%d")` — today's date

The `" ".join(sys.argv[1:])` is worth pausing on:

> "Each space-separated word becomes a separate argument.
> So `python journal.py Today I learned` gives us
> `['journal.py', 'Today', 'I', 'learned']`. We slice off
> the script name with `[1:]` and join the rest back
> together with spaces. That gives us back the original
> sentence."

Most kids will quote their multi-word arguments after seeing
this:

```
$ python journal.py "Today I learned"
```

That works too — it's one quoted argument that includes
spaces. Both ways work. Mention.

The `with open(filename, "a") as f:` is Phase 3 callback —
append mode, doesn't erase what's there.

#### Run it

Walk through running it from the terminal. Multiple times to
show entries accumulating. Then look at the file:

```
$ cat /home/student/journals/2026-04-25.txt
[14:32] First entry
[14:45] Second entry
```

The "I built a real CLI tool" satisfaction is the lesson
landing.

#### Stretch — subcommands

The "view" subcommand introduces the *subcommand pattern*.
Worth naming explicitly:

> "Real CLI tools work this way. `git` is one command but
> has lots of subcommands: `git commit`, `git push`, `git
> status`. We're doing the same — `journal.py view` and
> `journal.py 'some text'` do different things."

Walk through how the code distinguishes them:

```python
if sys.argv[1] == "view":
    # show entries
else:
    # add an entry
```

Same script, different behavior. The user picks via the
first argument.

#### Extensions

Both extensions add more subcommands. The `view <date>`
takes an additional argument; the `list` uses `Path.glob`
for pattern matching.

The `Path.glob("*.txt")` is new and useful. Mention briefly:

> "`Path.glob` finds all files matching a pattern. `*.txt`
> means 'any name ending in .txt'. Returns the matching
> files."

### Common stumbles

- **`IndexError: list index out of range` when accessing
  sys.argv[1]`.** Forgot the usage check. Always check
  `len(sys.argv)` before indexing past 0.
- **`TypeError` when concatenating `Path` and string.** Use
  the `/` operator: `home / "notes.txt"`, not
  `home + "/notes.txt"`.
- **Wrong format codes in strftime.** Look them up. `%Y`
  vs `%y` (4-digit vs 2-digit year). `%m` vs `%M` (month vs
  minute — common confusion).
- **Path doesn't exist when expected.** Use `.exists()`
  before opening.
- **`sys.exit(1)` exits silently.** Add a `print(...)`
  before it explaining the error.
- **Subcommand check happens after the file write.** If the
  view check is in the wrong place, the script writes
  "view" as an entry. Walk through the if/else flow.
- **Multi-word arguments without quotes.** `python journal.py
  Today I learned` works (joined with " ".join), but
  `python journal.py 'Today I learned'` is also valid (one
  quoted arg). Both work; both are correct in context.

### Differentiation

- **Younger kids (9-10):** Tour Part A briefly; focus on the
  base journal in Part B. The subcommand stretch is
  optional.
- **Older kids (12+):** Will pick up the modules fast. Push
  them through both stretches and extensions.
- **Advanced (any age):** Suggest:
  - `argparse` — Python's "real" CLI argument parser
    (handles flags, types, help text). Significantly more
    complex than `sys.argv` but much more capable.
  - `json` for saving structured data
  - `csv` for spreadsheet-style data
  - The full Python docs at python.org/3/library/
- **Struggling:** A kid who can't get the basic journal
  working is the kid you focus on. Most common cause:
  Path arithmetic typos, sys.argv index errors, or wrong
  filename.

### What to watch for

- **The "I can pass arguments to my Python script!" reaction.**
  The CLI tool moment lands here.
- **The "subcommands are cool" reaction** when kids see git
  /journal pattern recognition.
- **Buddies trying out each other's CLI tools.** Encourage
  — the journal can have entries from both buddies.
- **Kids exploring the docs.** Some will go deep on the
  stdlib docs. Encourage. The "this is huge" realization is
  valuable.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 4 (next week, classes).** `Path` and `datetime`
  are classes. Today's use is the consumer side; next week
  is the producer side ("how do we make our own?").
- **Sessions 5-6 (Git).** Git is a CLI tool with
  subcommands. Today's subcommand pattern preps kids for
  understanding Git's design.
- **Session 7 (testing).** Tests run from the command line
  too. Today's CLI muscle memory transfers.
- **Phase 5 (customtkinter).** Many GUI apps still use CLI
  arguments at startup (e.g., `app.py --debug`). Today's
  `sys.argv` is the foundation.
- **Phase 8 (Flask).** `python app.py` to run a server.
  Today's CLI knowledge.
- **Peanut butter callback opportunity:** the IndexError on
  sys.argv[1] without the length check is a precision
  moment. The computer accessed exactly what was asked; the
  list was too short; that's an error.

### Materials checklist

- [ ] Demo machine with Thonny + terminal
- [ ] Pre-built journal CLI for destination preview
- [ ] Projector (helpful for the CLI demos)
- [ ] Class roster
