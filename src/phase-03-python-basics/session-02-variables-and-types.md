## Session 2: Variables and types

*Phase 3 — Python basics · Session 2 of 16*

### What we're learning today

You've been using variables for a while now (Phase 1 Session 6,
Phase 2 Session 5). Today we get specific about **what kinds of
values** variables can hold — numbers, decimals, text, and what
happens when you mix them up. By the end of class, you'll have
written a program that does math with answers from the user, and
you'll know why `"5" + "3"` is `"53"` instead of `8`.

### You'll need to remember from last time

- **`print(...)`** — Python tells you something.
- **`input(...)`** — Python asks you something. Returns whatever
  the user typed.
- **`+`** — sticks two strings together (concatenation).
- **Variables** — `name = "Sam"`.

---

### Part A: Three kinds of values

Open Thonny and start a new file. Save it as `types.py`.

A **type** is a category of value. Python has lots of types, but
three matter for almost everything you'll do:

| Type | What it is | Examples |
|---|---|---|
| `int` | a whole number (integer) | `5`, `42`, `-3`, `0` |
| `float` | a decimal number | `3.14`, `5.0`, `-0.5` |
| `str` | text (string) | `"Hello"`, `"Sam"`, `"42"` |

Notice that `5` and `5.0` look almost the same but are different
types — one is an int, one is a float. And `"42"` (with quotes)
is a *string* even though it looks like a number.

#### See the type with `type()`

Python has a built-in function called `type()` that tells you
what type a value is. Try this:

```python
print(type(5))
print(type(5.0))
print(type("Hello"))
print(type("5"))
```

Save. Run.

The shell shows:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'str'>
```

Notice the last two: `5.0` is a float, but `"5.0"` (with quotes)
is a string. The quotes change everything.

#### Why types matter

Try this:

```python
print(5 + 3)
print("5" + "3")
```

Run. The shell shows:

```
8
53
```

Two completely different answers. Same-looking values; different
types; different behavior.

- `5 + 3` is **number addition.** Five plus three is eight.
- `"5" + "3"` is **string concatenation.** "5" stuck together
  with "3" is "53".

Python `+` does *different things* depending on what it's
between. With numbers, math. With strings, sticking together.

This matters because **`input()` always returns a string** —
even if the user typed a number. Try:

```python
age = input("How old are you? ")
print(type(age))
print(age + 1)
```

Save. Run. Type your age and press Enter.

You get an error:

```
TypeError: can only concatenate str (not "int") to str
```

Translation: "I can't add a number to a string. They're
different types."

The fix: convert the string to a number before doing math with
it.

#### Type conversion

Python has functions for converting between types:

| Function | Converts to | Example |
|---|---|---|
| `int(x)` | integer | `int("5")` is `5` |
| `float(x)` | decimal | `float("3.14")` is `3.14` |
| `str(x)` | string | `str(5)` is `"5"` |

Fix the previous program:

```python
age = int(input("How old are you? "))
print(type(age))
print(age + 1)
```

The `int(input(...))` does two things: gets the user's input
(as a string), then converts it to an integer.

Save. Run. Type your age. Now you see:

```
<class 'int'>
[your age plus 1]
```

The error is gone because `age` is now an int, and you can add
1 to an int.

This is one of the most common patterns in Python: **convert
input to the type you actually want to work with.**

#### One more conversion

You might also need `str()` to go the other direction. Try this
without conversion:

```python
score = 100
print("Your score is " + score + " points!")
```

Run. Error: `TypeError: can only concatenate str (not "int")`.

Fix it with `str()`:

```python
score = 100
print("Your score is " + str(score) + " points!")
```

Now the int `100` becomes the string `"100"`, which can be
concatenated with the rest of the message.

(There's a *much* nicer way to do this in Python called
*f-strings* — coming next week.)

**Checkpoint:** *You've used `type()` to check the type of at
least three different values, you've seen the difference between
`5 + 3` and `"5" + "3"`, and you've used `int()` to convert input
to a number for math.* **This is the natural stop point if class
is cut short.**

---

### Part B: A real program with math

Now let's build something useful with input + types.

#### Base goal — age in years

Build this:

```python
print("Welcome to the Age Calculator!")
age = int(input("How old are you? "))
years = int(input("How many years from now? "))

future_age = age + years
print("In " + str(years) + " years, you'll be " + str(future_age) + ".")
```

Run. Type your age (e.g., 12). Type a number of years (e.g., 8).
The shell tells you what age you'll be then.

Walk through what's new:

- **Two `int(input(...))` calls** to get two numbers.
- **Math on variables**: `age + years` adds them.
- **`str()` on the way out** so we can concatenate the numbers
  into the output string.

Tedious but it works. You'll see why f-strings are nicer next
week.

#### Stretch — decimals

What if you want fractional answers? Use `float`:

```python
print("Average calculator!")
a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))

average = (a + b + c) / 3
print("The average is " + str(average))
```

Now the user can type decimals (like `4.5` or `7.25`) and the
result handles fractional averages.

The parentheses in `(a + b + c) / 3` matter — they make sure
the addition happens first, then the division. Math order of
operations applies in Python just like math class.

#### Extension — multi-step calculator

Build a tip calculator. Or a "how many minutes until..." program.
Or "convert miles to feet." Or anything that asks the user for
numbers, does some math, and reports the result.

For example, a savings calculator:

```python
print("Savings Calculator")
weekly_save = float(input("How much do you save each week? $"))
weeks = int(input("How many weeks? "))

total = weekly_save * weeks
print("In " + str(weeks) + " weeks, you'll save $" + str(total))
```

Or a unit converter:

```python
miles = float(input("How many miles? "))
feet = miles * 5280
print(str(miles) + " miles is " + str(feet) + " feet.")
```

Pick something you'd want to know an answer to, and write the
program to compute it.

---

### Wrap-up

Before we leave, share with the room:

- What did your calculator compute?
- Did anyone hit a `TypeError` they had to fix?
- For the kids who built the savings or unit conversion — does
  the answer look right?

You learned today how Python tells different *kinds of values*
apart, and how to convert between them. **Types are one of the
fundamental ideas in programming.** Every value has a type.
Operations behave differently depending on type. Errors happen
when types don't match.

In Phase 2 you got away with not thinking about types because
turtle commands took numbers and you typed numbers. Now that
input() is in the mix, type conversion becomes part of every
interactive program.

### If you missed this session

Open Thonny and start a new file. Save as `types.py`. Then:

1. Try `print(type(5))`, `print(type(5.0))`, `print(type("hi"))`.
   See the three types: int, float, str.

2. Try `print(5 + 3)` and `print("5" + "3")`. Notice the
   different answers.

3. Build the age calculator from Part B base:
   ```python
   age = int(input("How old are you? "))
   years = int(input("How many years from now? "))
   future_age = age + years
   print("In " + str(years) + " years, you'll be " + str(future_age) + ".")
   ```

4. Customize: build a calculator that asks for numbers and
   reports something useful (savings, conversion, average).

About 30 minutes. If you get stuck, ask your buddy at the start
of next class.

### Stretch and extension ideas

- What does `int("5.7")` do? What does `int(5.7)` do? Try both
  and see.
- What does `float("hello")` do? Run it and read the error
  message.
- What does `str(5) + str(3)` return? Why?
- What does `int("5") + int("3")` return? Why?
- Try `5 + 5.0` — what type is the result? (Hint: it'll be a
  float. When you mix int and float, Python promotes to float.)

### What's next

Next week we dig deeper into **strings** — text is the most
common kind of data in real programs (names, addresses,
sentences, file contents). We'll learn how to slice strings,
search them, change their case, and — most importantly — use
**f-strings** to format text without all the `+ str(...) +`
mess from today.
