## Session 13: Error handling — `try` and `except`

*Phase 3 — Python basics · Session 13 of 16*

### What we're learning today

When something goes wrong in your program — the user types
"hello" when you wanted a number, a file doesn't exist, you
divide by zero — Python **crashes** by default. Today we
learn to **catch** those errors and handle them gracefully
with `try` and `except`. By the end of class, you'll be able
to write programs that don't crash on bad input — they ask
again instead.

### You'll need to remember from last time

- **`int(input(...))`** — converts user input to a number,
  but crashes if it's not numeric.
- **`open(...)`** — fails if the file doesn't exist.
- **Function definitions** — Sessions 4 and 6.
- **`while True:` and `break`** — for "keep trying" loops.

---

### Part A: `try` and `except`

Open Thonny and start a new file. Save it as `try_except.py`.

#### The problem

Try this:

```python
age = int(input("How old are you? "))
print(f"In ten years you'll be {age + 10}.")
```

Run. Type your age. Works fine.

Now run again. This time, type "hello" instead of a number.

```
ValueError: invalid literal for int() with base 10: 'hello'
```

Crash. Your program ends. The user — who maybe just made a
typo — sees an error message that looks scary and confusing.

Real programs don't do that. They handle the error and ask
again.

#### `try` and `except`

Here's how you handle it:

```python
try:
    age = int(input("How old are you? "))
    print(f"In ten years you'll be {age + 10}.")
except ValueError:
    print("That's not a number!")
```

Save and run. Type "hello." Now you get:

```
That's not a number!
```

No crash. No scary message. The program ends cleanly with a
friendly note.

Walk through:

- **`try:`** — start a block of code that *might* fail.
- The code inside the `try` runs as normal.
- **If an error happens**, Python jumps to the **`except`**
  block matching the error type.
- If no error, the `except` block is skipped.

The error type after `except` (`ValueError` here) tells Python
which kinds of errors to catch. `ValueError` is the error
`int()` raises when its input can't be converted to a number.

#### Common exception types

Python has many built-in exception types. Some common ones:

| Exception | When it happens |
|---|---|
| `ValueError` | bad value given to a function (`int("hello")`) |
| `ZeroDivisionError` | dividing by zero |
| `FileNotFoundError` | trying to open a file that doesn't exist |
| `KeyError` | dict lookup with a missing key |
| `IndexError` | list lookup with an out-of-range index |
| `TypeError` | wrong type passed (`"5" + 3`) |
| `NameError` | using a variable that doesn't exist |

Try a few:

```python
# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Can't divide by zero!")

# KeyError
person = {"name": "Sam"}
try:
    print(person["age"])
except KeyError:
    print("No age stored.")
```

Each `try` runs the risky code; each matching `except`
catches the specific failure.

#### Why catch specific exceptions

You *can* catch any error with a bare `except:` — but this is
usually a bad idea:

```python
try:
    age = int(input("Age? "))
except:
    print("Something went wrong.")   # what went wrong??
```

This catches *everything* — including bugs in your own code,
which you probably wanted to know about. Always catch the
specific exception you're handling:

```python
try:
    age = int(input("Age? "))
except ValueError:
    print("That's not a number!")
```

Now the only error caught is the one you expected. Other bugs
still crash, which is what you want during development.

#### Try-again loop

The most common pattern: ask the user, try to convert, if it
fails ask again:

```python
while True:
    try:
        age = int(input("How old are you? "))
        break    # success — exit the loop
    except ValueError:
        print("That's not a number. Try again.")

print(f"You're {age} years old.")
```

Walk through:
- `while True:` — loop forever (until break).
- Inside the `try`: ask, convert, if successful `break` out.
- Inside the `except`: print error, loop continues.

The `break` is *inside* the `try` because we want to break
only on success. If the `int()` fails, the break is skipped
and the except block runs instead.

This is a very common Python pattern. Memorize the shape.

**Checkpoint:** *You've used `try / except` to catch at least
one specific exception, and you've written a try-again loop
that keeps asking until the user provides valid input.* **This
is the natural stop point if class is cut short.**

---

### Part B: A robust input function

Time to use what you learned to make your previous programs
better.

#### The function

Build a reusable function that asks for a number and won't
take no for an answer:

```python
def ask_for_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a number. Try again.")
```

Walk through:

- A function with a parameter (`prompt`).
- Infinite loop.
- Try to convert; if successful, **return** the number
  immediately (which exits the function and the loop).
- If conversion fails, print the message and loop back.

Now use it:

```python
def ask_for_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a number. Try again.")

age = ask_for_number("How old are you? ")
years = ask_for_number("How many years from now? ")

future_age = age + years
print(f"In {years} years, you'll be {future_age}.")
```

Run. Type bad input. The function asks again. Type good input.
Continue.

This pattern — wrap risky input in a function with try-again
logic — is one of the most useful tools you'll have.

That's the **base goal.**

#### Stretch — bounded numbers

Often you want a number *in a range.* Modify the function:

```python
def ask_for_number(prompt, min_value, max_value):
    while True:
        try:
            n = int(input(prompt))
            if n < min_value or n > max_value:
                print(f"Number must be between {min_value} and {max_value}.")
                continue
            return n
        except ValueError:
            print("That's not a number. Try again.")

# usage:
age = ask_for_number("How old are you? ", 0, 120)
```

Now the function rejects out-of-range numbers too. The
`continue` skips the `return` and goes back to the top of the
loop.

#### Extension — apply to your hangman game

Open last week's hangman game (or rebuild it). Add error
handling for these cases:

- User types nothing (just Enter): say "Please type a letter."
- User types more than one character: say "One letter at a
  time."
- User types something that isn't a letter (a number, a
  symbol): say "Letters only."

This doesn't strictly need `try/except` — most of these are
just `if` checks. But the *spirit* is the same: don't crash;
ask again.

```python
def ask_for_letter():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 0:
            print("Please type a letter.")
        elif len(guess) > 1:
            print("One letter at a time.")
        elif not guess.isalpha():
            print("Letters only.")
        else:
            return guess
```

`guess.isalpha()` returns True if the string is all letters.
Useful string method, similar to the `.lower()`/`.upper()` etc.
from Session 3.

Replace the `input("Guess a letter: ").lower()` line in your
hangman with `guess = ask_for_letter()`. Now your game is
much more robust.

#### Extension — file-not-found

Update your persistent notes program from Session 11 to use
a proper `try/except`:

```python
notes = []
try:
    with open(NOTES_FILE, "r") as f:
        for line in f:
            notes.append(line.strip())
except FileNotFoundError:
    print("No notes file yet — starting fresh.")
```

Same pattern, different exception type. Now the program tells
the user explicitly what's happening on first run, instead of
silently doing nothing.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built `ask_for_number` — does it feel
  satisfying to type bad input and have the program just ask
  again?
- For the kids who used it in hangman — what edge cases did
  you handle?
- Think back to all the programs you've written this phase.
  Which ones would have benefited from `try/except`? *(Most of
  them.)*

You learned today how to write programs that **don't crash on
bad input.** This is the difference between code that
*technically works* and code that's *actually usable*. Real
software handles errors everywhere — invalid user input, missing
files, network failures, bad data, you name it. Today is your
introduction to a habit you'll use for the rest of your
programming life.

You also learned the **try-again loop pattern** —
`while True: try: ... return ... except: print error`. This is
the canonical Python idiom for "keep asking until the user
gives me what I need." You'll use it constantly.

### If you missed this session

Open Thonny and start a new file. Save as `try_except.py`.
Then:

1. Try the basic try/except:
   ```python
   try:
       age = int(input("Age? "))
       print(f"You're {age}.")
   except ValueError:
       print("That's not a number.")
   ```
   Run, try good input. Run again, try bad input. See the
   difference.

2. Build the try-again loop pattern from Part A.

3. Build the `ask_for_number` function from Part B and use it
   in a small program.

About 30-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- `else` clause — `try / except / else:`. The `else` runs only
  if no exception happened. Useful for separating "the risky
  code" from "the code that depends on it succeeding."
- `finally` clause — `try / except / finally:`. The `finally`
  always runs, regardless of exceptions. Useful for cleanup.
- Catching multiple exception types: `except (ValueError,
  TypeError):` — catches either.
- Catching the exception itself: `except ValueError as e:` —
  `e` is the exception object, with details about what went
  wrong.
- `raise ValueError("custom message")` — make your *own*
  errors when something is wrong in your code's logic.

### What's next

Next week is the **biggest integration project of Phase 3** —
either a **text adventure game** (multiple rooms, choices that
change the story) or a **CSV reader** (a real-world data tool).
You'll use *everything* you've learned, including today's
error handling, to build something genuinely impressive.
