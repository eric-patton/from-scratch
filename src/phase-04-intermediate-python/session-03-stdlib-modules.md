## Session 3: Standard library modules

*Phase 4 — Intermediate Python · Session 3 of 9*

### What we're learning today

Python comes with a huge collection of pre-written code called
the **standard library** — modules for working with dates,
files, paths, web pages, and dozens of other things. You've
already met two (`random` and `turtle`). Today we tour several
more useful ones and use them to build a real CLI tool: a
**daily journal** you run from the terminal.

### You'll need to remember from last time

- **`import yourfile`** — same syntax for stdlib modules.
- **The terminal** — running scripts with `python script.py`.
- **File I/O** from Phase 3 — `open(...)`, append mode `"a"`.
- **f-strings** for formatting output.

---

### Part A: A tour of useful modules

Open Thonny and start a new file. Save it as `tour.py`.

#### `datetime` — dates and times

The `datetime` module handles dates, times, and date math.

```python
from datetime import datetime

now = datetime.now()
print(now)

today = now.strftime("%Y-%m-%d")
print(today)

time = now.strftime("%H:%M")
print(time)
```

Run.

```
2026-04-25 14:32:18.123456
2026-04-25
14:32
```

`datetime.now()` returns the current date and time. `.strftime(...)`
formats it as a string. The `%Y-%m-%d` and `%H:%M` are
**format codes** — `%Y` means 4-digit year, `%m` is 2-digit
month, etc. There are dozens of format codes; look them up
when you need them.

You can also do date math:

```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(days=7)

print(f"Now: {now.strftime('%Y-%m-%d')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"Last week: {last_week.strftime('%Y-%m-%d')}")
```

`timedelta(days=1)` represents a day. Add or subtract from a
datetime to get a different date. Useful for "calculate the
date 30 days from now" type problems.

#### `pathlib` — modern file paths

`pathlib` is the modern way to handle file paths in Python.
Cleaner than the older `os.path` style.

```python
from pathlib import Path

home = Path.home()
print(f"Home: {home}")

current = Path.cwd()
print(f"Current: {current}")

# build a path
notes_file = home / "notes.txt"
print(f"Path: {notes_file}")

# check if it exists
print(f"Exists? {notes_file.exists()}")
```

Walk through:

- `Path.home()` — your home directory.
- `Path.cwd()` — the current working directory (where you're
  running from).
- `home / "notes.txt"` — uses `/` to combine paths. Way
  cleaner than string concatenation.
- `.exists()` — does this file or folder actually exist?

`Path` also has methods like `.is_file()`, `.is_dir()`,
`.mkdir()`, and many others.

#### `sys` — command-line arguments

Remember how the terminal lets you pass extra arguments to
commands? Like `cp source destination` or `mkdir new_folder`?
Your Python scripts can take arguments too.

```python
import sys

print(f"Number of arguments: {len(sys.argv)}")
print(f"All arguments: {sys.argv}")

if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")
```

`sys.argv` is a list. The first item (`sys.argv[0]`) is
always the script name. The rest are whatever the user
typed after.

Run from the terminal:

```
$ python tour.py hello world
Number of arguments: 3
All arguments: ['tour.py', 'hello', 'world']
First argument: hello
```

This is how real CLI tools work — `git commit "message"`,
`python script.py argument`, etc. Each space-separated word
becomes an item in `argv`.

> **About different machines:** the class machines run
> Linux, where `python tour.py hello world` works exactly as
> shown. If you try this from a Windows home laptop and `python`
> isn't found, try `py tour.py hello world` instead. Same
> behavior — `sys.argv` works on every operating system once
> you can launch the script.

#### `os` — operating system stuff

`os` has lots of functions for interacting with the operating
system:

```python
import os

# environment variables
home = os.environ.get("HOME", "unknown")
print(f"Home from env: {home}")

# list files in a directory
files = os.listdir(".")
print(f"Files here: {files}")
```

We mostly use `pathlib` instead of `os.path` these days, but
`os` still has useful environment-variable and process stuff.

**Checkpoint:** *You've used `datetime`, `pathlib`, and `sys`
in at least one program each.* **This is the natural stop
point if class is cut short.**

---

### Part B: A daily journal CLI

Time to build something real that uses these modules.

#### What you're building

A command-line journal. Each day gets its own file. You
add entries by running:

```
$ python journal.py "Today I learned about modules"
Saved to /home/sam/journals/2026-04-25.txt
```

The script:
1. Takes the entry text from `sys.argv`.
2. Uses `datetime` to figure out today's date.
3. Uses `pathlib` to build the filename.
4. Appends the entry (with a timestamp) to today's file.

Real CLI tool — runs from the terminal, takes an argument,
does its job, exits.

#### Build it

```python
# journal.py
import sys
from datetime import datetime
from pathlib import Path

JOURNAL_DIR = Path.home() / "journals"
JOURNAL_DIR.mkdir(exist_ok=True)

if len(sys.argv) < 2:
    print("Usage: python journal.py <entry text>")
    sys.exit(1)

# get the entry text (everything after the script name)
entry_text = " ".join(sys.argv[1:])

# build today's filename
today = datetime.now().strftime("%Y-%m-%d")
filename = JOURNAL_DIR / f"{today}.txt"

# append the entry with a timestamp
timestamp = datetime.now().strftime("%H:%M")
with open(filename, "a") as f:
    f.write(f"[{timestamp}] {entry_text}\n")

print(f"Saved to {filename}")
```

Save. Then in the terminal:

```
$ cd Desktop/today
$ python journal.py "First entry of the day"
Saved to /home/sam/journals/2026-04-25.txt
```

Walk through what's happening:

- `JOURNAL_DIR = Path.home() / "journals"` — build a path to
  a `journals` folder in the home directory.
- `.mkdir(exist_ok=True)` — make the folder if it doesn't
  exist. The `exist_ok=True` means "no error if it already
  exists."
- `len(sys.argv) < 2` — check that the user provided at
  least one argument. If not, print usage and exit.
- `sys.exit(1)` — exit the program with status code 1
  (meaning "error"). Any non-zero status code is conventional
  for "something went wrong."
- `" ".join(sys.argv[1:])` — slice off the script name (the
  `[1:]`), then join the rest with spaces. So if the user
  typed `python journal.py hello world`, you get `"hello
  world"` as a single string.
- The rest is familiar — file path with `pathlib`, append
  with `"a"` mode.

Try it a few times. Each entry gets appended to today's
file. Tomorrow's entries will go to a different file
automatically.

That's the **base goal.**

#### Stretch — a "view" subcommand

Allow the user to view today's entries. Detect the special
case of `view` as the argument:

```python
# journal.py
import sys
from datetime import datetime
from pathlib import Path

JOURNAL_DIR = Path.home() / "journals"
JOURNAL_DIR.mkdir(exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
today_file = JOURNAL_DIR / f"{today}.txt"

if len(sys.argv) < 2:
    print("Usage: python journal.py <entry text>")
    print("       python journal.py view")
    sys.exit(1)

if sys.argv[1] == "view":
    if today_file.exists():
        print(f"\n=== {today} ===")
        with open(today_file, "r") as f:
            print(f.read())
    else:
        print(f"No entries yet for {today}.")
else:
    # add a new entry
    entry_text = " ".join(sys.argv[1:])
    timestamp = datetime.now().strftime("%H:%M")
    with open(today_file, "a") as f:
        f.write(f"[{timestamp}] {entry_text}\n")
    print(f"Saved to {today_file}")
```

Now:

```
$ python journal.py view
=== 2026-04-25 ===
[14:32] First entry of the day
[14:45] Made the journal a real CLI tool

$ python journal.py "Adding a third entry"
Saved to /home/sam/journals/2026-04-25.txt
```

Two ways to use the same script — *subcommands.* Real CLI
tools (Git, Docker, etc.) work this way: `git commit`, `git
push`, `git status` — different verbs, same `git` command.

#### Extension — view a specific day

```python
if sys.argv[1] == "view":
    if len(sys.argv) >= 3:
        # view a specific date
        date_arg = sys.argv[2]
        target_file = JOURNAL_DIR / f"{date_arg}.txt"
    else:
        # view today
        target_file = today_file
    
    if target_file.exists():
        with open(target_file, "r") as f:
            print(f.read())
    else:
        print(f"No entries for that date.")
```

Now `python journal.py view 2026-04-20` shows entries from
that date.

#### Extension — list all journals

```python
if sys.argv[1] == "list":
    files = sorted(JOURNAL_DIR.glob("*.txt"))
    for f in files:
        print(f.stem)   # filename without extension
```

`.glob("*.txt")` returns all `.txt` files in the directory.
`.stem` is the filename without the extension (so
`2026-04-25.txt` → `2026-04-25`).

Add this to your subcommand check. Now you have three
commands: add (default), view, list. Real CLI app.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the base journal — does it feel
  weird to run it from the terminal with arguments?
- For the stretch — was the subcommand pattern clean?
- For the extension — anyone build a `delete` command or a
  `count` command?

You learned today how to use Python's **standard library** to
build real, useful CLI tools. The patterns you saw — `sys.argv`
for arguments, `datetime` for now-aware programs, `pathlib`
for file paths — are *exactly* how professional Python
scripts are built.

You also learned **subcommands** — the way real CLI tools
expose multiple actions through one entry point. `git`, `npm`,
`docker`, `kubectl` — they all work this way. Today's journal
is a tiny version of the same shape.

### If you missed this session

Open Thonny. Then:

1. Try the `datetime` examples from Part A — print today's
   date and the time.
2. Try the `pathlib` examples — print your home directory.
3. Try `sys.argv` — pass a few arguments when you run the
   script and print them.
4. Build the journal CLI from Part B base.

Run from the terminal each time. About 30-40 minutes.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- **`json`** — read and write JSON files. Useful for saving
  structured data. `json.dump(data, f)` to save; `json.load(f)`
  to load.
- **`csv`** — read and write CSV files (spreadsheet format).
  `import csv`.
- **`shutil`** — file operations like copy, move, delete
  whole directories.
- **`subprocess`** — run other programs from your Python
  script. `subprocess.run(["ls", "-la"])`.
- **`urllib.request`** — fetch content from URLs (basic web
  requests).

Browse [the standard library docs](https://docs.python.org/3/library/)
when you're curious — there's a whole world to explore.

### What's next

Next week we add **classes** to your toolkit — a way to bundle
data and the functions that work on that data into a single
unit. Classes are how `Path` and `datetime` are built — and
how almost all "object-oriented" Python is structured.
