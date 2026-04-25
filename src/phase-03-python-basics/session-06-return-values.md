## Session 6: Functions that return values

*Phase 3 — Python basics · Session 6 of 16*

### What we're learning today

You've been writing functions since Phase 2. Until now, those
functions just *did* things — drew shapes, printed messages.
Today you'll learn how to write functions that **give you back
a value** — like `len("hello")` returns `5`, or `int("42")`
returns `42`. Functions that return values are how real Python
programs are organized. By the end of class, you'll have
written a grade calculator that uses two of your own
return-value functions.

### You'll need to remember from last time

- **`while` loops** — `while condition:` runs as long as the
  condition is true.
- **The Thonny debugger** — bug icon button, Step Over (F6).
- **Functions** — `def name(parameters):` followed by an
  indented body.
- **`int(input(...))`** — the canonical pattern for numeric
  user input.

---

### Part A: `return`

Open Thonny and start a new file. Save it as `returns.py`.

#### Two kinds of functions

You've seen functions that *do* something:

```python
def greet(name):
    print(f"Hello, {name}!")
```

This function prints a message. After it runs, it's done.
Nothing comes back to the calling code.

But you've also *used* functions that give you something back:

```python
length = len("hello")     # length is now 5
upper_name = "sam".upper()  # upper_name is now "SAM"
age = int("42")           # age is now 42
```

`len`, `upper`, and `int` all **return values.** That's the
new word: a function "returns" a value when it gives something
back to the code that called it.

Today you'll write your own return-value functions.

#### Your first return

Type this:

```python
def double(x):
    return x * 2

result = double(5)
print(result)
```

Save. Run. The shell shows `10`.

Walk through what's new:

- `def double(x):` — function takes one parameter.
- `return x * 2` — the function calculates `x * 2` and **returns
  it** to the caller.
- `result = double(5)` — call the function with 5; whatever the
  function returns gets put into `result`.
- `print(result)` — print the returned value.

The `return` statement is what's new. When `return` runs, the
function stops *immediately* and gives the value back to
whoever called it.

#### Where the value goes

A function call (`double(5)`) is now an **expression** with a
value (in this case, `10`). That means you can use it
*anywhere* a value would work:

```python
print(double(5))         # prints 10 directly
print(double(5) + 3)     # prints 13 (10 + 3)
big = double(double(5))  # double of double — big is 20
```

That last one is a little wild: `double(5)` returns 10, then
`double(10)` returns 20. Functions calling functions, all in
one line.

#### Multiple parameters, one return

```python
def add(a, b):
    return a + b

print(add(3, 4))    # 7
print(add(10, 20))  # 30
```

Same pattern: take input parameters, do math, return the
answer.

#### `return` ends the function

Once `return` runs, the function stops. Anything after `return`
is dead code:

```python
def double(x):
    return x * 2
    print("This will never run!")  # never executes
```

Useful when you want to exit early based on a condition:

```python
def safe_divide(a, b):
    if b == 0:
        return 0     # exit early to avoid divide-by-zero
    return a / b
```

If `b` is 0, the function returns 0 and stops. Otherwise, it
runs the second `return`. Same way `break` works in loops, but
for functions.

**Checkpoint:** *You've written at least one function that
returns a value, called it, and used the returned value (saved
it in a variable, printed it, or used it in an expression).*
**This is the natural stop point if class is cut short.**

---

### Part B: A grade calculator

Time to build something with multiple return-value functions
working together.

#### What you're building

A program that asks for three test scores, calculates the
average, and tells the user their letter grade. Two functions:

- `average(a, b, c)` — returns the average of three numbers
- `letter_grade(score)` — returns "A", "B", "C", "D", or "F"
  based on the score

Then the main program calls both.

#### Build the average function

```python
def average(a, b, c):
    return (a + b + c) / 3

# test it
print(average(80, 90, 100))   # should print 90.0
print(average(70, 75, 80))    # should print 75.0
```

Run. Both should match. The function takes three numbers,
returns their average.

The parentheses around `(a + b + c)` matter — they ensure the
addition happens before the division. Same order-of-operations
rule as math class.

#### Build the letter_grade function

```python
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# test it
print(letter_grade(95))   # A
print(letter_grade(82))   # B
print(letter_grade(50))   # F
```

Notice: each branch has its own `return`. As soon as one
returns, the function stops — no need for an explicit `else`
in some cases. (We use `elif/else` here for clarity, but you
could also write five separate `if`s ending with `return`.
Both work.)

#### Combine them

```python
def average(a, b, c):
    return (a + b + c) / 3

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# main program
print("Enter your three scores:")
math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))

avg = average(math, science, english)
grade = letter_grade(avg)

print(f"Your average is {avg:.1f}")
print(f"Your letter grade is {grade}")
```

Save. Run. Type some scores. The program reports your average
and letter grade.

Notice what happened:

- `avg = average(math, science, english)` — the average
  function's return value goes into `avg`.
- `grade = letter_grade(avg)` — the letter_grade function's
  return value goes into `grade`. It uses `avg`, which came
  from the previous function.

**One function's output is the next function's input.** This
is one of the most common patterns in real programs.

The `:.1f` in the f-string is *formatting* — it means "show
this float with 1 decimal place." `90.0` is shown as `90.0`,
not `90.00000000001` or whatever the underlying value is. Try
`:.2f` for two decimal places, `:.0f` for no decimal point.

That's the **base goal.**

#### Stretch — variables stay inside

Try this experiment. Add a variable inside a function:

```python
def double(x):
    secret = x * 2
    return secret

print(double(5))    # 10
print(secret)       # ERROR
```

Run. The first print is `10`. The second gives:

```
NameError: name 'secret' is not defined
```

Why? `secret` is a variable created **inside** the function.
After the function ends, the variable goes away. It's
**local** to the function — only the code inside can see it.

This is called **scope.** Variables inside a function live only
inside the function. To get a value out, **return it.**

This is why `return` matters so much: it's the only good way to
get a value out of a function.

#### Extension — refactor the rollercoaster

Open last week's rollercoaster eligibility checker (or rebuild
it). Refactor it to use return-value functions:

```python
def is_old_enough(age):
    return age >= 13

def is_tall_enough(height):
    return height >= 48

def can_ride(age, height):
    return is_old_enough(age) and is_tall_enough(height)

# main program
age = int(input("How old are you? "))
height = int(input("How tall are you? "))

if can_ride(age, height):
    print("You can ride!")
else:
    print("Sorry, not yet.")
```

Now the program is built out of small, focused, named
functions. Each one returns a True/False (a boolean — remember
those?). The main `if` reads almost like English: `if
can_ride(age, height):`.

This is how real Python code is structured: small functions
that return values, composed together.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the grade calculator — what scores
  produce a B?
- For the stretch — were you surprised that `secret` wasn't
  available outside the function?
- For the extension — does the rollercoaster code read more
  like English with named functions?

You learned today the most important concept in writing
*reusable* code: functions that return values. **Most real
Python programs are organized as collections of small functions
that take inputs and return outputs.** You can think about each
function as a little machine: pour something in the top, get
something out the bottom.

You also learned about **scope** — variables inside a function
are *local*. They don't leak out. The only way to get a value
out is to `return` it. This is a feature, not a limitation —
it's what lets functions stay independent and reusable.

### If you missed this session

Open Thonny and start a new file. Save as `returns.py`. Then:

1. Build a `double` function:
   ```python
   def double(x):
       return x * 2

   print(double(5))    # 10
   ```

2. Build an `add` function with two parameters that returns
   their sum.

3. Build the grade calculator from Part B (average and
   letter_grade functions).

4. Try the stretch — see what happens when you try to print a
   variable that was defined inside a function.

About 35-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- A function can return *anything* — a number, a string, a
  boolean, even another value built from those. Try writing a
  function `describe(age)` that returns a string like `"adult"`
  or `"kid"`.
- A function can return *multiple values* using a tuple:
  `return name, age, height`. The caller unpacks with
  `n, a, h = my_function()`. Try it. (We won't use this much in
  Phase 3, but it's a Python feature.)
- **Recursive functions** — functions that call themselves.
  Mind-bending; useful for some problems. Don't worry about it
  yet but know it exists.
- A function with no `return` returns `None` automatically. Try
  `def nothing(): pass` then `print(nothing())`. You'll see
  `None`.

### What's next

Next week is your **first real Python project** — a
**number-guessing game.** The computer thinks of a number; you
have to guess it; the computer tells you "too high" or "too
low" until you get it right. It uses everything you've learned:
input, output, conditionals, loops, functions, return values.
Game on.
