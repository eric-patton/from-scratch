## Session 9: More lists — patterns and slicing

*Phase 3 — Python basics · Session 9 of 16*

### What we're learning today

Last week you learned the basics of lists. Today we go deeper:
**slicing** (taking pieces of a list, just like with strings),
more useful list **methods** (sort, reverse, remove, pop), the
**`enumerate`** function (a cleaner way to loop with indexes),
and built-in functions like **`max`**, **`min`**, and **`sum`**
that work on any list. By the end of class, you'll have built a
score tracker that does real statistics on a list of numbers.

### You'll need to remember from last time

- **Lists** — `[1, 2, 3]`, indexing with `[0]`, `len()`,
  `.append()`.
- **Looping** — `for item in colors:`.
- **String slicing** from Session 3 — `name[0:3]` for the
  first three characters.

---

### Part A: New ways to use lists

Open Thonny and start a new file. Save it as `more_lists.py`.

#### Slicing

Lists slice the same way strings do — same `[start:end]`
syntax:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:3])    # [10, 20, 30]
print(numbers[2:])     # [30, 40, 50, 60]
print(numbers[:3])     # [10, 20, 30]
print(numbers[-2:])    # [50, 60] — last two
print(numbers[::-1])   # [60, 50, 40, 30, 20, 10] — reversed
```

Same rules as string slicing: includes `start`, excludes
`end`. Negative numbers count from the end. `[::-1]` reverses.

The slice returns a *new* list — the original is unchanged.

#### `enumerate` — looping with indexes

Last week we used `range(len(...))` to loop with index numbers:

```python
for i in range(len(favorites)):
    print(f"{i + 1}. {favorites[i]}")
```

That works, but Python has a cleaner way: `enumerate`.

```python
for i, item in enumerate(favorites):
    print(f"{i + 1}. {item}")
```

`enumerate` walks through a list and gives you both the **index
and the item** at the same time. Two variables (`i` and `item`)
both get values from each iteration.

This is shorter, cleaner, and what most Python programmers use.

#### `max`, `min`, `sum`

Some built-in functions work directly on lists of numbers:

```python
scores = [85, 92, 78, 95, 88, 70]

print(max(scores))     # 95
print(min(scores))     # 70
print(sum(scores))     # 508
print(len(scores))     # 6
print(sum(scores) / len(scores))   # 84.66... (the average)
```

`max` returns the largest. `min` returns the smallest. `sum`
adds them all up. `len` you already know.

These are *huge* time-savers. Without them, you'd write a loop
with a tracking variable and a conditional. With them — one
function call.

#### More list methods

Beyond `.append()`, lists have several useful methods:

| Method | What it does |
|---|---|
| `.sort()` | sorts the list in place (smallest to largest) |
| `.reverse()` | reverses the list in place |
| `.remove(x)` | removes the first occurrence of `x` |
| `.pop()` | removes and returns the last item |
| `.pop(i)` | removes and returns the item at index `i` |
| `.insert(i, x)` | inserts `x` at index `i` (existing items shift right) |
| `.count(x)` | counts how many times `x` appears |
| `.index(x)` | returns the index of the first occurrence of `x` |

Try a few:

```python
colors = ["red", "blue", "green", "blue"]

print(colors.count("blue"))    # 2
print(colors.index("green"))   # 2

colors.sort()
print(colors)    # ['blue', 'blue', 'green', 'red']

colors.reverse()
print(colors)    # ['red', 'green', 'blue', 'blue']

colors.remove("blue")
print(colors)    # ['red', 'green', 'blue']  (only first removed)

last = colors.pop()
print(last)      # 'blue'
print(colors)    # ['red', 'green']

colors.insert(0, "purple")
print(colors)    # ['purple', 'red', 'green']
```

Don't memorize all of these. Refer back when you need one.

**Checkpoint:** *You've used at least three of the new list
operations from this section (slicing, enumerate, or one of the
built-ins / methods).* **This is the natural stop point if class
is cut short.**

---

### Part B: A score tracker

Time to build something that uses many of these together.

#### What you're building

A program that asks the user to enter a series of test scores,
then reports statistics: how many, the highest, the lowest, the
average, and a sorted listing.

#### Base goal

```python
print("Score Tracker")
print("Enter scores one at a time. Type 'done' when finished.")

scores = []

while True:
    entry = input("Score: ")
    if entry == "done":
        break
    scores.append(int(entry))

if len(scores) == 0:
    print("No scores entered.")
else:
    print(f"\nYou entered {len(scores)} scores:")
    for i, score in enumerate(scores):
        print(f"  {i + 1}. {score}")
    
    print(f"\nHighest: {max(scores)}")
    print(f"Lowest:  {min(scores)}")
    print(f"Total:   {sum(scores)}")
    print(f"Average: {sum(scores) / len(scores):.1f}")
```

Save. Run. Type a few scores like `85`, `92`, `78`, `95`. Type
`done`. The program reports the statistics.

Walk through what's happening:

- `scores = []` — empty list.
- `while True:` loop with `break` on "done" — same pattern as
  the favorites collector.
- `int(entry)` converts the input string to a number before
  appending. Without this, the `max`/`min`/`sum` functions
  would either fail or behave weirdly with strings.
- `if len(scores) == 0:` handles the case where the user typed
  "done" immediately. (Always a good idea to check for empty
  data.)
- `enumerate(scores)` for numbered output.
- `max`, `min`, `sum`, `len` for the statistics.
- `:.1f` in the f-string for one decimal place on the average.

That's the **base goal.** A complete program with input,
processing, and statistics.

#### Stretch — show top three

Sort the scores and show the top three:

```python
sorted_scores = sorted(scores, reverse=True)
print(f"\nTop three:")
for i, score in enumerate(sorted_scores[:3]):
    print(f"  {i + 1}. {score}")
```

What's new:

- `sorted(scores, reverse=True)` returns a new sorted list,
  highest to lowest. (Compare to `scores.sort()` which sorts
  in place.)
- `sorted_scores[:3]` slices the first three.
- `enumerate` numbers them.

If you have fewer than 3 scores, the slice just returns
whatever you have. (Lists tolerate slices that go past the
end.)

#### Extension — a menu

Build a more interactive version with a menu:

```python
print("Score Tracker")
scores = []

while True:
    print("\nWhat would you like to do?")
    print("  1. Add a score")
    print("  2. Show all scores")
    print("  3. Show statistics")
    print("  4. Quit")
    
    choice = input("Choice: ")
    
    if choice == "1":
        score = int(input("Score: "))
        scores.append(score)
        print(f"Added. You now have {len(scores)} scores.")
    elif choice == "2":
        if len(scores) == 0:
            print("No scores yet.")
        else:
            for i, score in enumerate(scores):
                print(f"  {i + 1}. {score}")
    elif choice == "3":
        if len(scores) == 0:
            print("No scores yet.")
        else:
            print(f"  Highest: {max(scores)}")
            print(f"  Lowest:  {min(scores)}")
            print(f"  Average: {sum(scores) / len(scores):.1f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
```

Now the user can add scores incrementally, view them, see
statistics, and quit when they want. This is a **menu-driven
program** — a common shape for command-line tools (which is
exactly what Phase 4 is about).

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the base — what scores did you enter?
  Did the average make sense?
- For the kids who did the menu version — does adding the
  menu make the program feel more like an *app*?
- Was anyone surprised by how much `max`, `min`, and `sum`
  shortened the code?

You learned today the patterns that show up in **every Python
program that handles data.** Lists, iteration, slicing,
statistics functions, and the menu structure — these are the
shapes that real programs are built from. Phase 4's CLI tools
will use all of them; Phase 8's web apps will use them too.

You also met `sorted(...)` (returns a new sorted list) vs
`scores.sort()` (sorts in place). The choice between "modify
the original" and "give me a new one" comes up a lot in Python
— for lists, dicts, and other data types. Knowing the
difference saves real bugs.

### If you missed this session

Open Thonny and start a new file. Save as `more_lists.py`.
Then:

1. Try slicing on a list:
   ```python
   numbers = [10, 20, 30, 40, 50]
   print(numbers[0:3])
   print(numbers[::-1])
   ```

2. Use `enumerate`:
   ```python
   colors = ["red", "blue", "green"]
   for i, color in enumerate(colors):
       print(f"{i}: {color}")
   ```

3. Try `max`, `min`, `sum`:
   ```python
   scores = [85, 92, 78, 95]
   print(max(scores))
   print(sum(scores) / len(scores))
   ```

4. Build the score tracker base from Part B.

About 30-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- `sum(scores) / len(scores)` is the average, but Python's
  `statistics` module has `statistics.mean(scores)` —
  `import statistics` and try it.
- `sorted(scores)` gives ascending; `sorted(scores,
  reverse=True)` gives descending. Same for `.sort(reverse=True)`.
- **List comprehensions** — Python's slick way to build a list
  from another. `doubled = [x * 2 for x in scores]` makes a new
  list with every score doubled. We won't formally cover; try
  it if you're curious.
- **Nested lists** — a list of lists. `grid = [[1, 2, 3], [4,
  5, 6]]`. Access with `grid[0][1]` (returns 2). Useful for
  2D data like game boards.

### What's next

Next week we meet **dictionaries** — like lists, but instead of
positions (0, 1, 2...) you use **names** to look up values
(name → phone number, country → capital, word → definition).
Dictionaries solve the parallel-lists problem from Session 8
and unlock a whole new class of programs.
