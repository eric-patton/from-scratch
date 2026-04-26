## Session 11: Reading and writing files

*Phase 3 — Python basics · Session 11 of 16*

### What we're learning today

So far, every program you've written **forgets everything** the
moment it ends. Type some favorites, close the program, gone.
Today we fix that. We'll learn how to **write** information to a
file on your computer and **read** it back later. By the end of
class, your contact book (or any program with a list) can
remember information *between runs.*

### You'll need to remember from last time

- **Lists** and **dictionaries** — the things we'll save and
  load.
- **`for` loops** for iterating through collections.
- **`while True:` and `break`** for input loops.
- **`.strip()`** from Session 3 — useful for cleaning up text
  from files.
- **String concatenation and f-strings** for building text to
  write.

---

### Part A: Writing a file

Open Thonny and start a new file. Save it as `files.py`.

#### `with open(...)` — the safe way

To work with a file, Python uses the `open()` function. The
modern, safe way to use it is with a `with` block:

```python
with open("hello.txt", "w") as f:
    f.write("Hello, file!\n")
```

Save and run.

Then look in the same folder where `files.py` is saved. There
should be a new file: `hello.txt`. Open it (in Thonny, or any
text editor). It contains:

```
Hello, file!
```

You just wrote a file. Walk through the code:

- `with open("hello.txt", "w") as f:` — opens a file. The `"w"`
  means **write mode** (creates the file if it doesn't exist;
  *replaces* it if it does). The file is given the temporary
  name `f` inside the block.
- `f.write("Hello, file!\n")` — writes a string to the file.
  The `\n` at the end is a newline (line break), so the next
  thing written goes on a new line.
- The `with` block automatically **closes the file** when it
  ends. That's the magic of `with` — you don't have to remember
  to clean up.

#### Three modes

The second argument to `open()` is the mode:

| Mode | What it does |
|---|---|
| `"r"` | **read** — file must exist; you can read but not write |
| `"w"` | **write** — replaces the file (or creates it) |
| `"a"` | **append** — adds to the end of an existing file |

Use `"w"` carefully — it *erases* whatever was there. `"a"` is
safer if you want to add to a file without losing what's there.

#### Writing multiple lines

Each `.write()` writes exactly what you give it. Newlines
(`\n`) are how you separate lines:

```python
with open("favorites.txt", "w") as f:
    f.write("pizza\n")
    f.write("soccer\n")
    f.write("blue\n")
```

Run. Open `favorites.txt`. Three lines.

You can also use a loop to write a whole list:

```python
favorites = ["pizza", "soccer", "blue", "books"]

with open("favorites.txt", "w") as f:
    for fav in favorites:
        f.write(fav + "\n")
```

Same result, but driven by a list. This is the standard pattern
for saving a list to a file.

**Checkpoint:** *You've written at least one file using
`with open(..., "w") as f:` and `.write(...)`.* **This is the
natural stop point if class is cut short.**

---

### Part B: Reading a file (and a real project)

Now let's **read** the file back.

#### Reading line by line

The most common pattern: loop through the lines.

```python
with open("favorites.txt", "r") as f:
    for line in f:
        print(line)
```

Run.

```
pizza

soccer

blue

books

```

Notice the **extra blank lines.** That's because each line in
the file ends with `\n`, AND `print` adds another `\n` at the
end. Two newlines = blank line.

Fix it with `.strip()`:

```python
with open("favorites.txt", "r") as f:
    for line in f:
        clean = line.strip()
        print(clean)
```

`.strip()` removes whitespace (including newlines) from the
start and end of a string. Now the print adds the only
newline, and the output looks right.

This is one of the most common file-reading patterns: open,
loop with `for line in f:`, strip each line.

#### Reading into a list

Sometimes you want all the lines in a list (so you can shuffle
them, sort them, etc.):

```python
with open("favorites.txt", "r") as f:
    favorites = []
    for line in f:
        favorites.append(line.strip())

print(favorites)
print(f"You have {len(favorites)} favorites.")
```

Now `favorites` is a list of strings, ready to use just like
any other list.

#### A persistent notes program

Build something that uses both reading AND writing. A simple
notes-keeper that remembers your notes between runs:

```python
NOTES_FILE = "notes.txt"

# Load existing notes
notes = []
try:
    with open(NOTES_FILE, "r") as f:
        for line in f:
            notes.append(line.strip())
except FileNotFoundError:
    pass   # no file yet, that's fine — empty list

print(f"You have {len(notes)} notes.")
for i, note in enumerate(notes):
    print(f"  {i + 1}. {note}")

# Add new notes
print("\nAdd more notes (or 'done' to save and exit):")
while True:
    note = input("Note: ")
    if note == "done":
        break
    notes.append(note)

# Save everything back
with open(NOTES_FILE, "w") as f:
    for note in notes:
        f.write(note + "\n")

print(f"\nSaved {len(notes)} notes to {NOTES_FILE}.")
```

Save. Run. Add a few notes. Quit. Run *again* — your previous
notes should still be there. Add more. Quit. Run a third time
— all your notes from all three runs are there.

Walk through what's new:

- `NOTES_FILE = "notes.txt"` — the filename in a constant at
  the top. Easy to change in one place.
- `try: ... except FileNotFoundError: pass` — try to load the
  file, but if it doesn't exist (first run), just skip the
  loading step. (This is a sneak peek of error handling — full
  treatment in Session 13.)
- The rest is patterns from Sessions 8-10 (lists, append,
  enumerate, while loop) plus today's file I/O.

That's the **base goal** — a real persistent program.

#### Stretch — append mode

The base version overwrites the file every time. That works,
but you read everything into memory and write it all back. For
large files this is wasteful.

Append mode (`"a"`) just adds to the end:

```python
with open("log.txt", "a") as f:
    f.write("Program ran on Wednesday.\n")
```

Each run appends a new line, without touching what was already
there. Useful for logs.

Try writing a "diary" program that asks for one entry and
appends it to a `diary.txt` file with a timestamp. Each run
adds one more entry; the file grows over time.

#### Extension — a file processor

Take a real file and process it. If your machine has a `.txt`
file with some content already (a story, your notes, anything),
write a program that reads it and reports:

- Total number of lines
- Total number of words
- Total number of characters
- The longest line (and how long)

```python
filename = input("Filename: ")

with open(filename, "r") as f:
    lines = []
    for line in f:
        lines.append(line.strip())

print(f"\nFile: {filename}")
print(f"Lines: {len(lines)}")

total_words = 0
total_chars = 0
longest_line = ""

for line in lines:
    words = line.split()
    total_words = total_words + len(words)
    total_chars = total_chars + len(line)
    if len(line) > len(longest_line):
        longest_line = line

print(f"Words: {total_words}")
print(f"Characters: {total_chars}")
print(f"Longest line ({len(longest_line)} chars): {longest_line[:60]}...")
```

This pulls together file I/O, lists, iteration, max-tracking,
slicing, f-strings — basically all of Phase 3 so far in one
program.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the notes program — does it actually
  remember between runs? (Run it, add a note, quit. Run it
  again. Note still there.)
- For the kids who tried append mode — what's the difference
  between writing each time vs appending?
- What other programs would benefit from saving to a file?
  (High scores in a game! Settings! Saved progress!)

You learned today how to make a program *remember* between
runs. **This is a huge step.** Until today, your programs lived
only while they ran. Now they can persist — store data, load it
back, modify it over time. Almost every real program does this:
documents save to files, games save progress to files, settings
save to files.

You also got a taste of `try/except` for the case where the
file doesn't exist yet. Next week we'll cover error handling
properly.

### If you missed this session

Open Thonny and start a new file. Save as `files.py`. Then:

1. Write a file:
   ```python
   with open("hello.txt", "w") as f:
       f.write("Hello, file!\n")
   ```
   Save, run. Look for `hello.txt` in the same folder.

2. Read it back:
   ```python
   with open("hello.txt", "r") as f:
       for line in f:
           print(line.strip())
   ```

3. Build the persistent notes program from Part B.

About 35-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- `f.read()` reads the *entire file* as one string. Useful for
  small files where you want the whole thing at once.
- `f.readlines()` reads all lines into a list (with the `\n`
  still attached to each — usually you `.strip()` after).
- **CSV files** — comma-separated values, the format of
  spreadsheets. Python has a `csv` module. We'll touch this in
  Session 14.
- **Different file locations** — by default, `open("name.txt")`
  uses the current folder. You can also use absolute paths
  like `"/home/sam/notes.txt"` (on Linux) or relative paths
  like `"data/notes.txt"`.

### What's next

Next week is **hangman** — your biggest Phase 3 project so far.
You'll build a complete word-guessing game using lists,
dictionaries, loops, conditionals, functions, AND today's file
I/O (the word list comes from a file). It pulls together
everything you've learned.
