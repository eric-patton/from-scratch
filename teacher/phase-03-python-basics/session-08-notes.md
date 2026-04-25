## Session 8 — Teacher Notes

*Phase 3, Python basics · Session 8 of 16 · Title: Lists —
collections of values*

### Purpose of this session

Lists are the most-used data structure in Python. Today is the
introduction; Session 9 deepens. Five jobs, in priority order:

1. **Land "a list is one variable holding many values."** This
   is a real conceptual shift — until now, variables held one
   thing.
2. **Land the basic operations: `[index]`, `len()`, `.append()`,
   `for ... in ...`.** Together these cover ~80% of what
   students will do with lists. Drill.
3. **Connect to strings.** The `[index]` syntax and the `for X
   in Y:` syntax are *identical* between strings and lists.
   Strings are basically lists of characters. Make this
   connection explicit.
4. **Build something real.** The favorites collector is a
   complete interactive program structured around a list. It's
   small but it works.
5. **Set up Session 9.** Today covers the basics; Session 9 adds
   slicing, more methods, common patterns. Don't try to cover
   everything today.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: pre-built favorites collector for destination
  preview.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was the guessing
  game. Anyone hit a 1-try win at home?
- **Part A: lists basics** (~40 min) — making lists ~5 min,
  indexing ~5 min, len ~3 min, append ~10 min, for loop ~10
  min, changing items ~3 min, checkpoint ~4 min.
- **Break** (~5 min).
- **Part B: favorites collector** (~35 min) — base ~15 min,
  numbered stretch ~5 min, extensions ~15 min.
- **Wrap-up** (~5 min).

If running short, **the parallel-lists extension can be cut.**
The basic favorites collector is the goal.

### Teaching Part A

#### Making a list

The square-brackets-with-commas syntax is mechanical. Show:

```python
colors = ["red", "blue", "green", "yellow"]
print(colors)
```

The output (`['red', 'blue', 'green', 'yellow']`) shows the
list visually. The brackets are part of the list syntax;
they're how Python indicates "this is a list."

Show the variations:
- list of numbers
- list of mixed types (works but unusual; mention briefly)
- empty list (`[]`) — the most useful starting point

#### Indexing

This is the bridge from Session 3 (string indexing). Make the
connection explicit:

> "Remember when we did `name[0]` to get the first character of
> a string? Lists work *exactly* the same way. `colors[0]` is
> the first item. `colors[-1]` is the last."

Some kids will get this immediately because they've seen the
syntax. Affirm.

#### `.append()`

The most-used list method. Walk through:

```python
colors = ["red", "blue"]
colors.append("green")
print(colors)
```

The list went from 2 items to 3. `.append()` modifies the list
*in place* — it doesn't return a new list (unlike string
methods which return new strings).

> "This is different from strings. When you did `name.upper()`
> in Session 3, it returned a *new* string and didn't change
> the original. `.append()` *changes the list itself.* Lists
> are *mutable* — they can be modified."

This is one of the more important Python distinctions. Worth
calling out, even if kids don't internalize it yet.

#### `for` loop over a list

The familiar `for X in Y:` syntax. Show:

```python
for color in colors:
    print(f"I like {color}.")
```

Make the connection to Session 3:

> "Same as `for letter in name:` — Python knows how to walk
> through any *collection*. Strings are collections of
> characters. Lists are collections of values. Same loop
> works for both."

This is a profound insight that unlocks a lot of Python. Make
sure it lands.

#### Changing items

```python
colors[1] = "purple"
```

The `[1]` accesses *and* assigns. Different from strings (which
don't allow this).

Don't dwell on mutability theory. Just show that lists let you
change individual items.

### Teaching Part B

#### The favorites collector

This is the integration project. Walk through the structure
before any code:

> "We need: an empty list to hold favorites. A loop that asks
> until the user is done. A way to add each item to the list.
> A way to print them all at the end."

Then build at the projector:

```python
favorites = []        # empty list to start

while True:
    item = input("Favorite: ")
    if item == "done":
        break
    favorites.append(item)

print(f"\nYou have {len(favorites)} favorites:")
for fav in favorites:
    print(f"  - {fav}")
```

The structure mirrors the number-guessing game from Session 7
— `while True:` with `break`, with input handling and a list
operation in the middle.

Worth pointing out: `\n` in an f-string is a *newline*. Causes
the output to skip a line. Useful for spacing.

#### Numbered stretch

The `for i in range(len(favorites)):` pattern is a slight new
thing — looping by index instead of by item. Walk through:

> "When we just want each item, we use `for fav in favorites:`.
> When we need the *index too* — for numbering, for example —
> we use `for i in range(len(favorites))` to get 0, 1, 2,
> ..., then `favorites[i]` to get the item at that index."

Then the `i + 1` to convert from zero-indexed to human-numbered.

If a kid asks "is there a better way?": yes — `enumerate`. But
defer; today's range/index is enough.

#### Parallel lists extension

Two lists kept in sync. Walk through the principle:

> "We append to both lists in the same iteration. So if
> `favorites[0]` is 'pizza', then `categories[0]` is the
> category for 'pizza'. The indexes line up."

This is a *kind of* data structure. It's clunky compared to
dictionaries (Session 10) or list-of-pairs (which we won't
formally cover). But it works and it teaches the "things at
the same index belong together" pattern.

If a kid notices this is awkward: yes, that's why dictionaries
exist. We'll see them in Session 10.

#### Sort extension

`.sort()` is mechanical. Note that it sorts *in place* —
modifies the list, doesn't return a new sorted list:

```python
favorites.sort()           # modifies favorites
sorted_list = sorted(favorites)   # alternative — returns new
```

Don't introduce `sorted()` as a separate function unless asked
— it confuses the in-place vs return-new distinction.

The "uppercase sorts before lowercase" gotcha will surprise
some kids. ASCII order is the reason; don't dwell. If asked:
"computers compare letters by their internal codes; uppercase
codes come before lowercase. To make case-insensitive sort,
use `.sort(key=str.lower)` — but that's beyond today."

### Common stumbles

- **`for color in colors[0]:`** — tried to iterate the first
  item instead of the list itself. Symptom: iterates through
  characters of the first string. Walk through.
- **`colors.append("a", "b")`** — `.append()` only takes one
  argument. To add multiple, use `.append("a")` then
  `.append("b")`, or `.extend(["a", "b"])`.
- **`colors[5]`** when list has 4 items. IndexError. Mention:
  `len(colors)` tells you how many items; valid indexes are
  0 through `len-1`.
- **Modifying list while iterating.** `for color in colors:
  colors.remove(color)` — broken, skips items. Don't worry
  about this today; mention in passing if a kid hits it.
- **Confusing list creation `[]` with indexing `[]`.**
  `colors = []` (empty list) vs `colors[0]` (first item). Same
  symbol, two contexts. Walk through.
- **`colors = "red, blue"` instead of `["red", "blue"]`.** A
  string with commas is just a string, not a list. The
  brackets matter.
- **The favorites loop never breaks.** User types `Done` (capital
  D), but the check is `if item == "done":`. Add `.lower()` or
  use the alternative spelling.

### Differentiation

- **Younger kids (9-10):** May find the "list as a thing that
  holds things" abstraction tricky. Lean on the visual: print
  the list and *see* it. The `for` loop is familiar; lean on
  the connection to Session 3.
- **Older kids (12+):** Will pick up lists fast. Push them to
  the parallel-lists extension and the sort extension. If they
  finish: ask them to find the longest favorite using a loop.
- **Advanced (any age):** May know lists from prior experience.
  Push them to:
  - `enumerate(favorites)` for numbered output
  - List comprehensions: `[fav.upper() for fav in favorites]`
  - List slicing: `favorites[0:3]`
- **Struggling:** A kid who can't get a basic list created and
  iterated in Part A is the kid you focus on. Most common
  cause: confused brackets and parens, or forgot to use
  `.append()` vs assignment.

### What to watch for

- **The "wait, this is just like a string" insight.** When
  kids see `for fav in favorites:` and recognize the pattern
  from Session 3. Affirm explicitly.
- **The "I want to track [some interesting thing]" creativity.**
  Favorites is generic; some kids will personalize. Hymns,
  YouTube channels, drinks at the church potluck, anything.
  Encourage.
- **Buddies trading list-building strategies.** Encourage. The
  empty-list-plus-loop-plus-append pattern is a major Python
  idiom; seeing different applications cements it.
- **Kids who finish base + stretch + extension and still have
  time.** They're ready for Session 9's deeper material.
  Foreshadow: "next week we go deeper into lists — slicing,
  more methods, building bigger programs around them."

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 9 (next week, more lists).** Today's basics; next
  week's depth. Slicing, more methods, common idioms.
- **Session 10 (dictionaries).** The parallel-lists extension
  today is *exactly* what dictionaries solve more elegantly.
  Foreshadow: "we'll learn a better way to do this next week."
- **Session 11 (file I/O).** Reading a file gives you a list of
  lines. Direct application of today's iteration patterns.
- **Session 12 (hangman).** Heavy use of lists — list of valid
  letters, list of guessed letters, list of word characters.
- **Phase 4 (intermediate Python).** Lists of objects (custom
  classes), nested lists (lists of lists), more sophisticated
  patterns.
- **Phase 6 (Pygame).** Lists of game objects (sprites,
  enemies, projectiles). Today's iteration pattern scales to
  game development directly.
- **Peanut butter callback opportunity:** the
  `Done`-vs-`done` capital letter bug is a precision moment.
  The computer compared exactly what was typed; "Done" is not
  equal to "done"; therefore the check failed.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built favorites collector
- [ ] Projector (helpful for the for-loop walkthrough)
- [ ] Class roster
