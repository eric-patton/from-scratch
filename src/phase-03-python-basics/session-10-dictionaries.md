## Session 10: Dictionaries — key-value pairs

*Phase 3 — Python basics · Session 10 of 16*

### What we're learning today

Lists hold values in **order**: the first one, the second one,
the third. Sometimes you need a different kind of organization
— "this name has this phone number," "this country has this
capital," "this word has this definition." That's a
**dictionary**, the second-most-important data structure in
Python after lists. By the end of class, you'll have built a
contact book that stores names with phone numbers and lets you
look them up.

### You'll need to remember from last time

- **Lists** — `[1, 2, 3]`, indexing, iteration.
- **`enumerate`** for looping with index.
- **`max`, `min`, `sum`** for stats.
- **`while True:` and `break`** for "until done" loops.
- **The `in` operator** — `"red" in colors` returns True/False.

---

### Part A: What dictionaries are and how to use them

Open Thonny and start a new file. Save it as `dicts.py`.

#### The motivation

Remember Session 8's "favorites with categories" extension?
We had two parallel lists:

```python
favorites = ["pizza", "soccer", "blue"]
categories = ["food", "activity", "color"]
```

Items at the same index belong together. Item 0 was "pizza"
which is a "food". This works but it's awkward — if you remove
something from one list, you have to remember to remove from
the other too. The lists can get out of sync.

A **dictionary** solves this. Instead of two lists with matching
indexes, you have ONE structure where each value has a *name*
attached:

```python
favorites = {
    "pizza": "food",
    "soccer": "activity",
    "blue": "color"
}
```

The names ("pizza", "soccer", "blue") are called **keys.** The
things they point to ("food", "activity", "color") are called
**values.** Together they're **key-value pairs.**

You look up a value by its key:

```python
print(favorites["pizza"])     # food
print(favorites["soccer"])    # activity
```

Same `[ ]` syntax as lists — but instead of a number for the
index, you use the key.

#### Making a dictionary

The syntax uses **curly braces** with `key: value` pairs:

```python
person = {
    "name": "Sam",
    "age": 12,
    "color": "blue"
}
```

Three keys (`"name"`, `"age"`, `"color"`), three values. The
curly braces and the colons are required.

You can also start with an empty dictionary and add to it:

```python
person = {}
person["name"] = "Sam"
person["age"] = 12
print(person)    # {'name': 'Sam', 'age': 12}
```

The same `[key] = value` syntax adds new entries (if the key
doesn't exist) or updates existing ones (if it does).

#### Looking up values

Two ways:

```python
person = {"name": "Sam", "age": 12}

print(person["name"])    # Sam
```

Direct lookup with `[key]`. Simple, but if the key doesn't
exist, you get a `KeyError`:

```python
print(person["color"])   # KeyError: 'color'
```

Safer way: check first with `in`:

```python
if "color" in person:
    print(person["color"])
else:
    print("No color set.")
```

The `in` operator returns True/False — same `in` you've used
with strings and lists, just checking if a key exists.

#### Iterating

Two common ways to loop through a dictionary:

```python
person = {"name": "Sam", "age": 12, "color": "blue"}

# loop through keys
for key in person:
    print(key)              # name, age, color (one per line)

# loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

The first form gives you each key in turn (one variable). The
second uses `.items()` and gives you both key AND value at
the same time (two variables, like `enumerate` from Session 9).

The second form is what you'll use most often.

#### How big is the dictionary?

`len()` works on dicts too — it tells you how many key-value
pairs:

```python
person = {"name": "Sam", "age": 12}
print(len(person))    # 2
```

**Checkpoint:** *You've created a dictionary, looked up at least
one value by key, used `in` to check whether a key exists, and
iterated through it with `.items()`.* **This is the natural
stop point if class is cut short.**

---

### Part B: A contact book

Time to use dictionaries for something practical.

#### What you're building

A program that stores phone numbers by name. The user can add
contacts, look up a name, and view all contacts.

#### Base goal

```python
print("Contact Book")

contacts = {}

while True:
    print("\nWhat do you want to do?")
    print("  1. Add a contact")
    print("  2. Look up a contact")
    print("  3. Show all contacts")
    print("  4. Quit")
    
    choice = input("Choice: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print(f"Added {name}.")
    elif choice == "2":
        name = input("Name to look up: ")
        if name in contacts:
            print(f"{name}'s phone: {contacts[name]}")
        else:
            print(f"{name} is not in your contacts.")
    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts yet.")
        else:
            print(f"\nYour {len(contacts)} contacts:")
            for name, phone in contacts.items():
                print(f"  {name}: {phone}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
```

Save. Run. Add a few contacts. Look one up. Show all. Quit.

Walk through what's happening:

- `contacts = {}` — empty dict to start.
- Menu loop (similar to last week's score tracker).
- **Add**: `contacts[name] = phone` adds a new pair (or
  updates an existing one).
- **Look up**: `if name in contacts:` checks for the key first
  (avoids KeyError); then `contacts[name]` gets the phone.
- **Show all**: `contacts.items()` for iterating both keys and
  values together.

That's the **base goal.** A working contact book using all the
dictionary basics.

#### Stretch — remove contact

Add an option to delete a contact:

```python
elif choice == "5":
    name = input("Name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}.")
    else:
        print(f"{name} is not in your contacts.")
```

(Add `print("  5. Delete a contact")` to the menu, of course.)

The `del` keyword removes a key (and its value) from the dict.
`del contacts[name]` removes the entry for that name.

#### Extension — a word counter

Different application of dicts: counting how many times each
word appears in a sentence.

```python
print("Word Counter")
sentence = input("Enter a sentence: ")
words = sentence.lower().split()

counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(f"\nWord counts:")
for word, count in counts.items():
    print(f"  {word}: {count}")
```

What's new:

- `sentence.lower().split()` — convert to lowercase, then split
  into a list of words. (`.split()` with no argument splits on
  whitespace.)
- The `for word in words:` loop checks each word.
- If the word is already in `counts`, add 1 to its current
  count. Otherwise, set it to 1 (first time we've seen it).

Try it with a sentence like "the quick brown fox jumps over
the lazy dog the fox sees the dog" — you should see "the"
appear 4 times, "fox" 2 times, "dog" 2 times, and most other
words 1 time.

This pattern (counting things into a dict) is one of the most
common Python idioms. Once you have the shape, you can count
anything: characters in a string, scores in a list, items in
any collection.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the contact book — did the menu feel
  natural?
- For the kids who did the word counter — did anything in your
  sentence appear more often than you expected?
- Can anyone think of another situation where a dictionary
  would be useful? *(Examples: a quiz program with
  question-answer pairs, a translation tool with
  word→translation, a game with player→score, etc.)*

You learned today the second-most-important Python data
structure. **Dictionaries are everywhere** in real programs —
configuration files, JSON data from web APIs, database results,
HTTP request data. Anywhere there's "this thing has this value"
information, dictionaries are the tool.

You also learned a key Python pattern: **count-into-a-dict.**
Walk through a collection, increment the count for each item.
This pattern shows up in word frequency, vote counting, error
counting, anywhere you need to tally things by category.

### If you missed this session

Open Thonny and start a new file. Save as `dicts.py`. Then:

1. Make a dictionary and look up values:
   ```python
   person = {"name": "Sam", "age": 12}
   print(person["name"])
   print(person["age"])
   ```

2. Add and update keys:
   ```python
   person["color"] = "blue"
   person["age"] = 13   # update
   print(person)
   ```

3. Iterate:
   ```python
   for key, value in person.items():
       print(f"{key}: {value}")
   ```

4. Build the contact book from Part B (menu + add + look up +
   show all).

About 30-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- `dict.keys()` returns a view of just the keys; `dict.values()`
  returns just the values. Useful in different situations.
- `dict.get(key, default)` — like `dict[key]` but returns
  `default` if the key isn't there (instead of raising
  KeyError). For example: `counts.get("hello", 0)` returns 0
  if "hello" isn't a key.
- **Nested dicts** — values can be dicts themselves. `people =
  {"sam": {"age": 12, "color": "blue"}}`. Useful for more
  complex data.
- **Dict comprehensions** — like list comprehensions but for
  dicts. `squares = {n: n*n for n in range(5)}`. Concise but
  more advanced; try if curious.

### What's next

Next week we learn how to **read data from files** — your
contact book that disappears when you close the program is
about to become one that *remembers* contacts between sessions.
That's `open()` and file reading, the first step toward
programs that work with real-world data.
