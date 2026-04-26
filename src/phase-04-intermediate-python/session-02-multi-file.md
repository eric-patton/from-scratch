## Session 2: Multi-file programs and your own modules

*Phase 4 — Intermediate Python · Session 2 of 9*

### What we're learning today

Until now, every program you've written has lived in **one
file.** Real programs don't work that way — they're spread
across many files, each one focused on a specific job.
Today you'll learn how to split your code across files and
how to **import your own files** the same way you've been
importing `random` or `turtle`. By the end of class, you'll
have a multi-file program with its parts cleanly separated.

### You'll need to remember from last time

- **The terminal** — `cd`, `ls`, `python script.py`.
- **`import`** — used in Phase 2 (`import turtle`) and Phase
  3 (`import random`). Today we use the same syntax with our
  own files.
- **Functions** and **classes** (we'll add classes in Session
  4 — for now, functions are enough).

---

### Part A: Splitting a program in two

Open Thonny and start a new folder for today. Create a folder
on your desktop called `today_session`. Inside it, create two
empty Python files:

- `tools.py`
- `main.py`

(Use Thonny: File → New, save as `tools.py`. Repeat for
`main.py`. Or create the files in a file manager. Either
works.)

#### The motivation

Suppose you wanted to build a small program that does math:
add, subtract, multiply, divide. You could put it all in one
file:

```python
# all_in_one.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(add(x, y))
elif op == "-":
    print(subtract(x, y))
elif op == "*":
    print(multiply(x, y))
elif op == "/":
    print(divide(x, y))
```

This works. But the math functions could be useful in *other*
programs too — a budget tracker, a grade calculator, anywhere
you need math. Why not put them in their own file?

#### Step 1: Put the math functions in `tools.py`

Open `tools.py` in Thonny. Type:

```python
# tools.py — math helper functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

Save. That's it. No `input`, no `print`, no main code. Just
function definitions. This file is now a **module** — a file
of reusable code.

#### Step 2: Use the module from `main.py`

Open `main.py`. Type:

```python
# main.py — the calculator program
import tools

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(tools.add(x, y))
elif op == "-":
    print(tools.subtract(x, y))
elif op == "*":
    print(tools.multiply(x, y))
elif op == "/":
    print(tools.divide(x, y))
```

Save.

Now run it from the terminal. Open a terminal, navigate to
your folder, and run `main.py`:

```
$ cd Desktop/today_session
$ python main.py
Enter first number: 5
Enter second number: 3
Operation (+, -, *, /): +
8
```

It works! And the math functions live in their own file.

#### What's happening

`import tools` tells Python to load the `tools.py` file. After
that, you access its functions with `tools.add(...)` — the
file name (without `.py`), then a dot, then the function
name.

This is the same pattern as `import random` then
`random.randint(1, 100)`. Same syntax. Just our own file
this time instead of a built-in module.

#### `from ... import ...`

There's a shorter way to import:

```python
from tools import add, subtract, multiply, divide
```

Now you can call them by their plain names — no `tools.`
prefix needed:

```python
print(add(x, y))    # not tools.add
```

Both styles work. The `from ... import ...` style is cleaner
when you only use a few specific things from a module. The
plain `import tools` is cleaner when you use lots of things
from it (or when you want it to be obvious in your code where
something came from).

**Pick one style and use it consistently in any one file.**
Mixing them is confusing.

#### Why split files matters

A few reasons:

- **Reuse.** The math functions in `tools.py` can now be
  imported into ANY program. Not just this calculator —
  anything that needs math.
- **Organization.** A single file with 500 lines is hard to
  navigate. A folder with five files of 100 lines each is
  much easier.
- **Working with others.** When you have a project with
  many people, each person can work on different files
  without stepping on each other.
- **Testing.** Tests (Session 7) are usually in a separate
  file from the code they test.

This is one of those moves that doesn't *change what you can
build* — but it changes how *manageable* big programs are.
Phase 4's projects from here on will be multi-file.

**Checkpoint:** *You have two files (`tools.py` and
`main.py`) where `main.py` imports and uses functions from
`tools.py`, and you've run `main.py` from the terminal.*
**This is the natural stop point if class is cut short.**

---

### Part B: A multi-file project

Now build something more substantial.

#### What you're building

A small program with **three files** working together — a
journal that tracks daily entries with a quote-of-the-day
feature.

#### Plan it out

Three files:

- `quotes.py` — has a list of quotes and a function
  `random_quote()` that returns one
- `journal.py` — has functions to read and write journal
  entries
- `main.py` — the user-facing program that uses both

Each file is small and focused. The main file is the *only*
one with input/output and the program flow.

#### Build `quotes.py`

```python
# quotes.py
import random

QUOTES = [
    "The journey of a thousand miles begins with a single step.",
    "Be the change you wish to see.",
    "Patience is bitter, but its fruit is sweet.",
    "He who has a why can endure any how.",
    "The only way out is through.",
]

def random_quote():
    return random.choice(QUOTES)
```

Save.

(Capitalized variable names like `QUOTES` are a Python
convention for **constants** — values that aren't expected
to change while the program runs. It's a hint to readers,
not a Python rule.)

#### Build `journal.py`

```python
# journal.py
JOURNAL_FILE = "journal.txt"

def add_entry(text):
    with open(JOURNAL_FILE, "a") as f:
        f.write(text + "\n")

def read_entries():
    try:
        with open(JOURNAL_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []
```

Save.

The `[line.strip() for line in f if line.strip()]` is a
**list comprehension** — a compact way to build a list. It's
equivalent to:

```python
result = []
for line in f:
    cleaned = line.strip()
    if cleaned:
        result.append(cleaned)
return result
```

Just shorter. List comprehensions are common Python; we
haven't formally taught them but they're worth recognizing.

#### Build `main.py`

```python
# main.py
import quotes
import journal

def main():
    print("Welcome to your journal!")
    print(f"\nQuote of the day: {quotes.random_quote()}\n")
    
    print("Past entries:")
    entries = journal.read_entries()
    if len(entries) == 0:
        print("  (none yet)")
    else:
        for i, entry in enumerate(entries):
            print(f"  {i + 1}. {entry}")
    
    print("\nAdd a new entry (or press Enter to skip):")
    new_entry = input("> ").strip()
    
    if new_entry:
        journal.add_entry(new_entry)
        print("Saved!")

main()
```

Save.

The `def main()` and `main()` at the bottom is a **common
Python pattern.** Wrap the program's main code in a function
called `main`, then call it at the bottom. It makes things
easier to read and is a habit you'll thank yourself for later.

#### Run it

```
$ cd Desktop/today_session
$ python main.py
Welcome to your journal!

Quote of the day: The only way out is through.

Past entries:
  (none yet)

Add a new entry (or press Enter to skip):
> Today I learned about multi-file programs.
Saved!
```

Run it again. Your entry from before is now in the "past
entries" section. The quote changes each run. It works.

That's the **base goal** — three files, each focused, all
working together.

#### Stretch — add a "search" feature

Add a function to `journal.py`:

```python
def search_entries(keyword):
    entries = read_entries()
    results = []
    for entry in entries:
        if keyword.lower() in entry.lower():
            results.append(entry)
    return results
```

In `main.py`, add a menu option to search:

```python
def main():
    print("Welcome to your journal!")
    
    while True:
        print("\nWhat do you want to do?")
        print("  1. Show quote of the day")
        print("  2. Show past entries")
        print("  3. Add new entry")
        print("  4. Search entries")
        print("  5. Quit")
        
        choice = input("> ")
        
        if choice == "1":
            print(f"\n{quotes.random_quote()}")
        elif choice == "2":
            entries = journal.read_entries()
            for i, entry in enumerate(entries):
                print(f"  {i + 1}. {entry}")
        elif choice == "3":
            text = input("Entry: ")
            journal.add_entry(text)
            print("Saved!")
        elif choice == "4":
            keyword = input("Search for: ")
            results = journal.search_entries(keyword)
            if len(results) == 0:
                print("No matches.")
            else:
                for entry in results:
                    print(f"  - {entry}")
        elif choice == "5":
            break

main()
```

Now you have a real journal app — multi-file, menu-driven,
search-capable.

#### Extension — load quotes from a file

Pull the quotes out of `quotes.py` and into `quotes.txt`:

```
The journey of a thousand miles begins with a single step.
Be the change you wish to see.
Patience is bitter, but its fruit is sweet.
```

Then `quotes.py` reads from the file:

```python
# quotes.py
import random

QUOTES_FILE = "quotes.txt"

def _load_quotes():
    with open(QUOTES_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def random_quote():
    return random.choice(_load_quotes())
```

The leading underscore on `_load_quotes` is a Python
convention meaning "this function is *private* — meant only
for use inside this module." Readers know not to use it from
elsewhere.

Now you can edit `quotes.txt` to add or change quotes,
without touching the Python code. **Code and data, separated
again.**

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the journal — does multi-file feel
  cleaner than one big file?
- For the kids who added the search feature — was it easy to
  add to `journal.py` without touching `main.py`?
- Did anyone get an `ImportError` or `ModuleNotFoundError`?
  What fixed it?

You learned today the most important *organizational* idea in
real programming. **Real codebases are dozens or hundreds of
files**, each focused on one thing, all importing from each
other. Today's three-file journal is the prototype for every
project from here on.

You also met a few Python conventions: `UPPERCASE_NAMES` for
constants, `_underscore_prefix` for private helpers, and the
`def main(): ...; main()` pattern for the program's main code.
These conventions aren't rules — Python doesn't enforce them
— but every Python programmer follows them, so your code
looks like real Python.

### If you missed this session

Open Thonny and create a folder. Inside it:

1. Create `tools.py` with a few simple functions like `add`
   and `subtract`.

2. Create `main.py` that does `import tools` and uses
   `tools.add(2, 3)`.

3. Open a terminal, `cd` into your folder, run
   `python main.py`.

4. Build the three-file journal from Part B.

About 40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- **Subfolders for modules.** Put related modules in a
  subfolder. To make it work as a package, add an empty
  `__init__.py` file in the subfolder. Then `import
  myfolder.mymodule`.
- **Renaming on import.** `import really_long_module_name as
  mod` — now you call it `mod.something()` for short.
- **`from module import *`** — imports everything. Don't do
  this; it pollutes your namespace and confuses readers.
  Mention only as a "what not to do."
- **Circular imports.** When file A imports B and B imports
  A. Confusing and error-prone. Mention only if a kid hits
  it.

### What's next

Next week we explore Python's **standard library** — the huge
collection of modules that come with Python. You've already
used a few (`random`, `turtle`). There are dozens more for
working with dates, files, paths, web pages, and more. We'll
tour the most useful ones.
