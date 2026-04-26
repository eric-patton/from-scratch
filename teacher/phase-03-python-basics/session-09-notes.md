## Session 9 — Teacher Notes

*Phase 3, Python basics · Session 9 of 16 · Title: More lists
— patterns and slicing*

### Purpose of this session

Lists deepen. Five jobs, in priority order:

1. **Land slicing on lists.** Same syntax as strings (Session 3)
   — make the connection explicit so kids realize the patterns
   are general.
2. **Land `enumerate` as the upgrade from `range(len(...))`.**
   Cleaner Python; what real programmers use. Worth introducing
   today rather than letting kids form the habit of the awkward
   version.
3. **Land `max`, `min`, `sum` as built-in functions.** These
   are huge time-savers and they're idiomatic. They also work
   on more than just lists (any "iterable") — a hint of how
   general Python's tools are.
4. **Show the menu-driven program shape.** This is one of the
   canonical CLI patterns (think `git`, `npm`, etc.). Phase 4
   is built around this shape; today previews it.
5. **Set up Session 10 (dictionaries).** Today's score tracker
   doesn't need dictionaries (just numbers). But the favorites
   collector with categories from Session 8 — and the contact
   book in Session 10 — both make dictionaries clearly useful.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: pre-built menu-driven score tracker as destination
  preview.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was lists basics.
  Anyone build their favorites collector at home?
- **Part A: new operations** (~40 min) — slicing ~10 min,
  enumerate ~10 min, max/min/sum ~10 min, methods table ~5
  min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: score tracker** (~35 min) — base ~15 min, sorted
  top-3 stretch ~10 min, menu extension ~10 min.
- **Wrap-up** (~5 min).

If running short, **the menu extension can be cut.** The base
score tracker with statistics is the goal.

### Teaching Part A

#### Slicing

Open with the explicit Session 3 callback:

> "Remember slicing strings? `name[0:3]`? Lists work the same
> way — same syntax, same rules. Includes start, excludes end,
> negative numbers count from the end, and `[::-1]` reverses."

Demo a few:

```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:3])    # [10, 20, 30]
print(numbers[::-1])   # reversed
```

The "lists slice exactly like strings" insight is the
generalization moment. Make it explicit.

#### `enumerate`

The motivation is the awkward `range(len(...))` from Session 8.
Show side by side:

```python
# the long way
for i in range(len(favorites)):
    print(f"{i + 1}. {favorites[i]}")

# the better way
for i, item in enumerate(favorites):
    print(f"{i + 1}. {item}")
```

The "two variables in the for-loop" syntax is the new bit.
Walk through:

> "`enumerate` gives you back two things each iteration: the
> index AND the item. We use two variable names — `i, item` —
> separated by a comma. Each iteration both get values."

Some kids will find this immediately cleaner; some will need
to see it a few times. Both are fine.

#### `max`, `min`, `sum`

Mechanical. Walk through:

```python
scores = [85, 92, 78, 95, 88, 70]
print(max(scores))     # 95
print(sum(scores))     # 508
```

> "Without these, you'd write a loop with a tracking variable.
> `max_so_far = scores[0]`, then `for ...` — that's a lot of
> code for one number. `max(scores)` is one function call."

If a kid asks how `max` works internally — that's exactly the
loop they're avoiding. Mention briefly: "it loops through and
keeps track of the biggest. We're just using the built-in
version of that."

The average pattern (`sum(scores) / len(scores)`) is worth
naming as a common idiom. Many Python programs compute averages
this way.

The `:.1f` formatting for the average decimal places is a quick
mention; introduced in Session 6, here used again.

#### List methods table

The table is a reference. Don't drill — kids will refer back
when they need them.

Worth noting: **`.sort()` modifies in place; `sorted()` returns
new.** This distinction comes up in Part B's stretch. Mention
explicitly:

> "Two ways to sort: `scores.sort()` changes the list itself;
> `sorted(scores)` gives you a new sorted list and leaves the
> original alone. Pick whichever fits."

### Teaching Part B

#### Base — score tracker

Walk through the structure once at the projector. The pattern is
familiar from Session 8 (favorites collector) but with int
conversion and statistics at the end.

Note the empty-list check (`if len(scores) == 0:`) — defensive
programming. Ask kids what happens if the user types "done"
immediately without entering any scores. Without the check,
`max([])` errors. With the check, the program handles it
gracefully.

This is a real engineering practice — handling edge cases.
Worth naming.

#### Stretch — top three

The `sorted(scores, reverse=True)[:3]` is a new compact pattern.
Walk through:

- `sorted(scores, reverse=True)` returns a new list, biggest first.
- `[:3]` slices the first three.
- `enumerate` numbers them.

The `reverse=True` keyword argument is the new piece. Worth
mentioning that some functions accept named arguments; you're
about to see more of these.

#### Extension — menu version

The menu structure is canonical for CLI programs:

1. Print the menu.
2. Ask the user for a choice.
3. Branch on the choice.
4. Loop until they choose to quit.

Walk through the structure at the projector:

```python
while True:
    # show menu
    choice = input(...)
    if choice == "1":
        ...
    elif choice == "2":
        ...
    ...
    elif choice == "4":
        break
    else:
        print("invalid")
```

This shape will return in Phase 4. The "menu-driven CLI" is
how a lot of real programs work (think any text-based admin
tool).

### Common stumbles

- **Forgot `int(entry)` before append.** `scores` ends up as a
  list of strings. `max(scores)` then sorts alphabetically
  (which gives wrong answers — `"100"` is "less than" `"99"`
  alphabetically because `"1"` < `"9"`).
- **Average of empty list.** `sum([]) / len([])` is
  `ZeroDivisionError`. Hence the empty-list check.
- **`enumerate` syntax confusion.** `for i, item in enumerate(list)`:
  - one variable: `for x in enumerate(list):` works but `x` is
    a tuple `(0, 'red')` etc.
  - two variables: `for i, item in enumerate(list)` unpacks
    the tuple.
  Don't try to teach tuples; just show the two-variable form.
- **`sorted()` vs `.sort()` confusion.** Mistake: writing
  `sorted_list = scores.sort()` and finding `sorted_list` is
  `None`. Reason: `.sort()` returns nothing because it modifies
  in place. Fix: use `sorted(scores)` or call `.sort()` then
  use `scores`.
- **Menu choice as int instead of string.** Mistake: `choice
  = int(input(...))` then `if choice == "1":`. The `int()`
  conversion makes choice a number, but the comparison is
  against a string. Use `if choice == 1:` (no quotes) or
  remove the `int()`.
- **Slice with negative start, no end.** `scores[-3:]` returns
  the last 3. `scores[:-3]` returns all *except* the last 3.
  Surprises kids; mention.

### Differentiation

- **Younger kids (9-10):** Will probably get the basics but
  might struggle with the menu extension. Focus on the base +
  stretch.
- **Older kids (12+):** Will pick this up fast. Push them to
  the menu extension and beyond. If they finish: ask them to
  add a "remove score" option using `.remove()`.
- **Advanced (any age):** Suggest list comprehensions:
  `top_5 = sorted(scores, reverse=True)[:5]` then `doubled =
  [s * 2 for s in top_5]`. Or have them write a function
  `compute_stats(scores)` that returns multiple values
  (name them via a dict — foreshadows Session 10).
- **Struggling:** A kid who can't get the score tracker base
  working is the kid you focus on. Most common cause: forgot
  `int()`, or indentation in the if/while structure. Use the
  debugger to walk through.

### What to watch for

- **The "wait, this is the same as strings" recognition** for
  slicing. Several kids will visibly process this.
- **The "max() does my whole loop" reaction** for the built-in
  functions. Several kids will laugh.
- **Buddies arguing about menu order or wording.** Encourage —
  this is UI design and it matters.
- **The "I want to keep playing with this" moment.** The score
  tracker is genuinely useful. Encourage taking it home and
  customizing.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 10 (next week, dictionaries).** Today's parallel-
  lists problem from Session 8 (favorites + categories) gets a
  cleaner solution with dicts. Frame: "lists hold many of one
  thing; dicts hold one thing per name."
- **Session 11 (file I/O).** A file is read as a list of
  lines. All today's iteration patterns apply.
- **Session 12 (hangman).** The valid-letters list, the
  guessed-letters list, the word-letters list — heavy list use.
  `in` for "did they guess this letter."
- **Session 14 (text adventure or CSV reader).** A text
  adventure has a list of rooms; a CSV reader splits a line
  into a list of cells. Today's slicing and iteration patterns
  scale up.
- **Phase 4 (CLI tools).** Menu-driven programs are the
  canonical shape. Today's menu extension is the prototype.
- **Phase 6 (Pygame).** Lists of game objects (enemies,
  bullets, particles). Today's iteration patterns become game
  loops.
- **The peanut butter callback opportunity:** the
  `forgot int() so max sorts alphabetically` bug is a precision
  moment. The computer compared what you gave it (strings); you
  meant numbers; the computer sorted alphabetically because
  that's what string comparison does.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built menu version of score tracker
- [ ] Projector (helpful for the enumerate side-by-side)
- [ ] Class roster
