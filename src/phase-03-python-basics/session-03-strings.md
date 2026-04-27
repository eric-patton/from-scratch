## Session 3: Strings — text in Python

*Phase 3 — Python basics · Session 3 of 16*

### What we're learning today

Last week's age calculator had a bunch of awkward
`+ str(...) +` mess every time we wanted to put a number into a
sentence. Today we fix that with a tool called **f-strings**, and
we learn how to do useful things with text — change its case,
find pieces of it, count letters, even reverse it. By the end of
class, you'll have built a "name analyzer" that takes a name and
reports five different facts about it.

### You'll need to remember from last time

- **Three types** — int, float, str.
- **Type conversion** — `int(...)`, `float(...)`, `str(...)`.
- **`input(...)`** always returns a string.
- **String concatenation** — `"Hello, " + name + "!"` (the
  awkward way we did it last week).

---

### Part A: f-strings (the good way)

Open Thonny and start a new file. Save it as `strings.py`.

Remember last week's age calculator? It looked like this:

```python
print("In " + str(years) + " years, you'll be " + str(future_age) + ".")
```

Notice the `+` and `str()` everywhere. Annoying.

Here's the better way:

```python
print(f"In {years} years, you'll be {future_age}.")
```

Same output. Way cleaner. That's an **f-string.**

#### What's an f-string

An f-string is a string with an `f` in front of the opening
quote. Inside, you can put **variables in curly braces** and
they get inserted automatically.

```python
name = "Sam"
age = 12
print(f"My name is {name} and I'm {age} years old.")
```

Output: `My name is Sam and I'm 12 years old.`

The `{name}` and `{age}` get replaced with whatever's in those
variables. **No `str()` needed** — Python figures out how to
turn each variable into text for you.

You can also put **whole expressions** in the curly braces:

```python
age = 12
print(f"Next year you'll be {age + 1}.")
print(f"In ten years you'll be {age + 10}.")
```

Output:
```
Next year you'll be 13.
In ten years you'll be 22.
```

The math runs first; the result goes into the string.

#### Try it

Build a file with your own f-string demos:

```python
name = "Sam"
age = 12
favorite_color = "blue"

print(f"Hi, my name is {name}.")
print(f"I am {age} years old.")
print(f"My favorite color is {favorite_color}.")
print(f"In 7 years I'll be {age + 7}.")
```

Save. Run.

That's the entire f-string thing. Three rules:

1. Put `f` in front of the opening quote.
2. Put variables in `{curly braces}`.
3. Done.

> "From now on, **always use f-strings** when building strings
> with variables in them. The old `+ str(...) +` way still
> works, but f-strings are easier to read and easier to write."

#### Useful string methods

A **method** is a function that belongs to a value. You call it
with a `.` after the value:

| Method | What it does |
|---|---|
| `s.upper()` | returns the string in UPPERCASE |
| `s.lower()` | returns the string in lowercase |
| `s.strip()` | removes whitespace from the start and end |
| `s.replace("old", "new")` | replaces parts of the string |
| `s.split(" ")` | splits the string into a list at each space |

Try these:

```python
name = "Sam"
print(name.upper())
print(name.lower())
print(name.replace("a", "X"))
```

Output:
```
SAM
sam
SXm
```

These methods don't *change* the variable — they return a new
string. So `name` is still `"Sam"` after `name.upper()`.

If you want to change `name` itself, you'd assign back to it:

```python
name = name.upper()
```

#### `.strip()` — clean up `input()` (do this *every time*)

There's a quiet bug that gets people for years: `input()` and
file reading often hand you strings with **invisible whitespace
on the ends.** A trailing space. A leftover newline character.
That whitespace makes string comparisons silently fail:

```python
guess = input("Guess: ")
if guess == "yes":
    print("You got it!")
```

If the kid types `yes` and hits enter, this works fine — but if
their input has a trailing space (easy to hit by accident), the
comparison breaks. The string `"yes "` is *not* equal to
`"yes"`.

**Fix:** call `.strip()` on every `input()` you ever do.

```python
guess = input("Guess: ").strip()
```

Now `"yes "`, `"yes"`, and `"  yes  "` all become `"yes"`. The
comparison works.

> **From now on, every `input()` in the curriculum gets
> `.strip()` chained on it.** It's one of those "always do this"
> habits — like wearing a seatbelt. Free protection.

#### `.split()` — break a string into a list of pieces

If a string has multiple words separated by spaces, `.split(" ")`
breaks it into a **list** of those words. (Lists are coming in
Session 8 — for now, just know it gives you back several pieces
you can use.)

```python
sentence = "the quick brown fox"
words = sentence.split(" ")
print(words)
# Output: ['the', 'quick', 'brown', 'fox']
```

You can split on any character, not just spaces. `s.split(",")`
splits on commas. Useful when input comes in as a list of things
the user typed: `"red,blue,green".split(",")` gives you each
color separately.

We'll use `.split()` heavily once we hit lists. For now, just
know it exists and what it does.

#### How long is a string?

`len(s)` tells you how many characters are in a string:

```python
name = "Caleb"
print(len(name))   # 5
```

`len` is a function (not a method), so the syntax is `len(name)`,
not `name.len()`.

**Checkpoint:** *You've built a Python file that uses an f-string
with at least two variables, and you've called `.upper()` (or
`.lower()`) on a string and printed the result.* **This is the
natural stop point if class is cut short.**

---

### Part B: Indexing, slicing, and a name analyzer

Strings are made of characters in order. Python lets you grab
specific characters or pieces of a string by *position*.

#### Indexing

A string is like a row of boxes, numbered starting from **0**:

```
"Caleb"
 C a l e b
 0 1 2 3 4
```

To get one character, use square brackets:

```python
name = "Caleb"
print(name[0])    # C
print(name[1])    # a
print(name[4])    # b
```

You can also count from the *end* using negative numbers:

```python
print(name[-1])   # b (last character)
print(name[-2])   # e (second-to-last)
```

#### Slicing

To get a *piece* of a string, use `[start:end]`. The slice
includes `start` but stops *before* `end`:

```python
name = "Caleb"
print(name[0:3])    # Cal (characters 0, 1, 2 — not 3)
print(name[1:4])    # ale (characters 1, 2, 3)
print(name[2:])     # leb (from 2 to the end)
print(name[:3])     # Cal (from the start to 3)
```

You can also slice with a *step*. The most useful step trick:
**reverse a string with `[::-1]`:**

```python
print(name[::-1])   # belaC
```

The double colon means "take every step character" — and `-1`
means "step backward." Don't memorize the syntax; just remember
`[::-1]` reverses a string.

#### Build a name analyzer

Combine everything from Part A and Part B:

```python
name = input("What's your name? ").strip()

print(f"Your name is {name}.")
print(f"It has {len(name)} characters.")
print(f"It starts with '{name[0]}' and ends with '{name[-1]}'.")
print(f"In all caps: {name.upper()}")
print(f"Reversed: {name[::-1]}")
```

Save. Run. Type your name.

(Notice `.strip()` on the `input()` — that's the new habit.)

The shell shows five facts about your name, all using f-strings.

That's the **base goal** for today.

#### Stretch — vowel counter

Count how many vowels are in the name. Use `in` to check if a
character is in a string:

```python
name = input("What's your name? ").lower()
vowel_count = 0

for letter in name:
    if letter in "aeiou":
        vowel_count = vowel_count + 1

print(f"{name} has {vowel_count} vowels.")
```

This combines:
- `.lower()` to make the comparison case-insensitive
- `for letter in name:` — a loop that goes through each letter
  of the string
- `if letter in "aeiou":` — checks if the letter is one of the
  vowels
- A counter variable that increases when we find a vowel
- An f-string for the result

The `for letter in name:` syntax is new but easy: it's a `for`
loop that visits each character of the string in order. We'll
see this pattern a lot more once we get to lists.

#### Extension — palindrome checker

A **palindrome** is a word that reads the same forwards and
backwards. "Mom" is a palindrome. "Racecar" is a palindrome.
"Caleb" is not.

Build a palindrome checker:

```python
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
```

Try it with `mom`, `racecar`, `taco`, `level`, `wasitacaroracatisaw`.

The `.lower()` makes the comparison case-insensitive (so "Mom"
and "mom" both work). The `word[::-1]` reverses the string. If
the original equals the reverse, it's a palindrome.

---

### Wrap-up

Before we leave, share with the room:

- What did you put into the name analyzer? Anything funny?
- For the kids who did the vowel counter — does your name have
  more vowels than you expected?
- For the kids who did the palindrome checker — what's the
  longest palindrome you found?

You learned today the most-used string operations in real
Python: f-strings (for output), indexing (for getting one
character), slicing (for getting pieces), and a few methods
(for transforming).

**F-strings will be in almost every program you write from now
on.** They're that common. The old `+ str(...) +` mess is
officially retired.

### If you missed this session

Open Thonny and start a new file. Save as `strings.py`. Then:

1. Build an f-string demo:
   ```python
   name = "Sam"
   age = 12
   print(f"My name is {name} and I'm {age} years old.")
   print(f"Next year I'll be {age + 1}.")
   ```

2. Try `.upper()`, `.lower()`, `len()` on a string. Print the
   results.

3. Try indexing: `name[0]`, `name[-1]`, `name[1:3]`.

4. Build the name analyzer from Part B base goal.

About 30-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- F-string formatting: `f"{age:>5}"` right-justifies in 5
  spaces. `f"{price:.2f}"` shows 2 decimal places. There are
  many — try them and see.
- `s.startswith("hello")` and `s.endswith("!")` return
  True/False. Useful in conditionals.
- `s.find("substring")` returns the position where a substring
  first appears (or `-1` if it's not in the string).
- Multi-line strings: `"""Hello\nWorld"""` (triple quotes for
  strings that span lines).

### What's next

Next week we deepen **conditionals** — combining multiple
conditions with `and`, `or`, and `not`. Combined with f-strings,
you'll be able to write programs that respond to multiple things
at once and tell the user clearly what they decided.
