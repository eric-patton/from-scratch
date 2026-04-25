## Session 8: Lists — collections of values

*Phase 3 — Python basics · Session 8 of 16*

### What we're learning today

Until now, every variable has held *one* thing — one number,
one string, one True/False. Today you'll learn how to hold
**many** things in a single variable. That's a **list**, and
it's arguably the most important data type in all of Python.
By the end of class, you'll have built a "favorites collector"
program that lets the user enter as many things as they want
and then shows them all back.

### You'll need to remember from last time

- **Variables** can hold a value (number, string, boolean).
- **`for` loops** — `for i in range(N):`.
- **`while True:` and `break`** for "loop until something
  happens" patterns.
- **`input(...)`** for getting input from the user.
- **f-strings** for formatting output.

---

### Part A: What lists are and how to use them

Open Thonny and start a new file. Save it as `lists.py`.

#### Making a list

A **list** is a value that holds multiple other values, in
order. You make one with **square brackets**:

```python
colors = ["red", "blue", "green", "yellow"]
print(colors)
```

Save. Run.

```
['red', 'blue', 'green', 'yellow']
```

The variable `colors` holds *four* strings, all in one list.

A list can hold any kind of value — strings, numbers, even
booleans:

```python
ages = [12, 14, 9, 16]
mixed = ["Alex", 12, True]
empty = []
```

The last one (`[]`) is an *empty list* — a list with nothing in
it yet. Useful when you want to fill it up gradually.

#### Getting items by index

Lists use the same `[index]` syntax you learned for strings in
Session 3. The first item is at index `0`:

```python
colors = ["red", "blue", "green", "yellow"]
print(colors[0])    # red
print(colors[1])    # blue
print(colors[-1])   # yellow (last)
```

Same indexing rules. Negative numbers count from the end.

#### How long is the list?

`len()` works on lists too:

```python
colors = ["red", "blue", "green", "yellow"]
print(len(colors))    # 4
```

#### Adding to a list

The most common list operation: **adding an item.** Use the
`.append()` method:

```python
colors = ["red", "blue"]
colors.append("green")
colors.append("yellow")

print(colors)    # ['red', 'blue', 'green', 'yellow']
```

Each `.append()` adds one item to the end of the list.

#### Looping through a list

You can iterate through a list with `for`, just like you did
with strings:

```python
colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(f"I like the color {color}.")
```

Output:
```
I like the color red.
I like the color blue.
I like the color green.
I like the color yellow.
```

The loop runs once for each item. Each iteration, `color` (the
loop variable) holds the next item from the list.

This is *the same syntax* as `for letter in name:` from Session
3. Strings and lists both work with `for ... in ...`.

#### Changing items

You can replace an item by assigning to its index:

```python
colors = ["red", "blue", "green"]
colors[1] = "purple"
print(colors)    # ['red', 'purple', 'green']
```

This is one of the things lists can do that strings can't —
strings are immutable (you can't change their characters), but
lists are mutable (you can).

**Checkpoint:** *You've created a list, accessed items by
index, used `.append()` to add to it, and used a `for` loop to
print all the items.* **This is the natural stop point if class
is cut short.**

---

### Part B: A favorites collector

Time to use lists for something real.

#### What you're building

A program that asks the user to enter their favorite things,
one at a time. They keep entering until they type "done." Then
the program shows back the complete list.

#### Base goal

```python
print("Favorites Collector!")
print("Enter your favorite things, one at a time. Type 'done' when finished.")

favorites = []

while True:
    item = input("Favorite: ")
    if item == "done":
        break
    favorites.append(item)

print(f"\nYou have {len(favorites)} favorites:")
for fav in favorites:
    print(f"  - {fav}")
```

Save. Run. Type a few favorites (pizza, soccer, blue, whatever).
Type "done" when finished. The program shows the list.

Walk through what's happening:

- `favorites = []` — start with an empty list.
- The `while True:` loop keeps asking forever.
- If the user types "done", we `break` out of the loop.
- Otherwise, we `.append()` what they typed to the list.
- After the loop ends, `len(favorites)` and a `for` loop show
  the complete list.

That's the **base goal** — a complete interactive program built
around a list.

#### Stretch — number them

Right now the list shows:
```
- pizza
- soccer
- blue
```

Numbered would be nicer:
```
1. pizza
2. soccer
3. blue
```

Use `range(len(favorites))` to get the indexes:

```python
print(f"\nYou have {len(favorites)} favorites:")
for i in range(len(favorites)):
    print(f"  {i + 1}. {favorites[i]}")
```

The loop variable `i` goes 0, 1, 2... but we add 1 to display
"1, 2, 3..." (humans number from 1).

`favorites[i]` looks up the item at index `i`. Same
square-bracket syntax as accessing a single item.

#### Extension — categorize

Ask the user to categorize each favorite — food, color,
activity, etc. Store both:

```python
favorites = []
categories = []

while True:
    item = input("Favorite (or 'done'): ")
    if item == "done":
        break
    cat = input("What category? ")
    favorites.append(item)
    categories.append(cat)

print(f"\nYou have {len(favorites)} favorites:")
for i in range(len(favorites)):
    print(f"  {i + 1}. {favorites[i]} ({categories[i]})")
```

Two parallel lists. The favorite at index 0 has the category at
index 0. They stay in sync because we always append to both at
the same time.

(There are *better* ways to do this in Python — using a list of
*pairs*, or a dictionary, or a list of dictionaries. We'll get
to dictionaries in Session 10. For now, two lists is fine.)

#### Extension — sorted output

Sort the list before showing it:

```python
favorites.sort()
print(f"\nYour {len(favorites)} favorites (alphabetical):")
for fav in favorites:
    print(f"  - {fav}")
```

`.sort()` is a list method that sorts the list *in place* (it
changes the list itself). Strings sort alphabetically; numbers
sort numerically.

---

### Wrap-up

Before we leave, share with the room:

- What's in your favorites list? Anything funny?
- For the kids who built the categorized version — did the two
  parallel lists stay in sync?
- For the kids who used `.sort()` — did the order surprise you?
  (Capital letters sort before lowercase letters.)

You learned today the most-used data structure in all of Python.
**Lists are everywhere.** Files are read as lists of lines.
Spreadsheet rows are lists of cells. Webpages are lists of
elements. Programs that handle data, programs that handle
collections of anything — they all use lists.

You also learned that **a `for` loop knows how to walk through
a list** (or a string). Same `for X in Y:` syntax, different
collections. From here on out, that pattern is your default
for "do something with each item."

### If you missed this session

Open Thonny and start a new file. Save as `lists.py`. Then:

1. Make a list and try basic operations:
   ```python
   colors = ["red", "blue", "green"]
   print(colors[0])     # red
   print(len(colors))   # 3
   colors.append("yellow")
   print(colors)
   ```

2. Loop through it:
   ```python
   for color in colors:
       print(f"I like {color}.")
   ```

3. Build the favorites collector from Part B:
   - Empty list
   - while True loop
   - input, check for "done", append
   - Print all at the end with a for loop

About 30-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- **`.remove(item)`** — removes the first occurrence of an item
  from the list. `colors.remove("red")` deletes "red".
- **`.pop()`** — removes and returns the last item. `colors.pop()`
  takes off the last one.
- **`in`** for membership — `"red" in colors` returns True/False.
  Same `in` you used for `if letter in "aeiou":` in Session 3.
- **`+` between lists** — `[1, 2, 3] + [4, 5]` is `[1, 2, 3, 4,
  5]`. Combines two lists.
- **`*` between lists and ints** — `["a"] * 5` is `["a", "a",
  "a", "a", "a"]`. Useful for initialization.

### What's next

Next week we go *deeper* into lists — more methods, more
patterns, slicing (the `[start:end]` syntax you saw with
strings). After that, **dictionaries** — lists' cousin that
holds *named* pairs instead of just ordered values.
