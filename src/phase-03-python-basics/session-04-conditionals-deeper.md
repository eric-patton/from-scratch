## Session 4: Conditionals — combining decisions

*Phase 3 — Python basics · Session 4 of 16*

### What we're learning today

You already know `if`, `elif`, and `else` from Phase 2. Today
we add three small but powerful words — **`and`**, **`or`**,
and **`not`** — that let you combine multiple conditions into
one decision. By the end of class, you'll have built a
"rollercoaster eligibility checker" that asks the user several
things and tells them if they can ride.

### You'll need to remember from last time

- **f-strings** — `f"Hello, {name}!"`.
- **Comparison operators** — `>`, `<`, `==`, `!=`, `>=`, `<=`.
- **`if/elif/else`** from Phase 2 Session 6 — "if condition,
  do this; elif condition, do that; else, do the other."
- **`int(input(...))`** for numeric input.

---

### Part A: `and`, `or`, `not`

Open Thonny and start a new file. Save it as `decisions.py`.

In real life, decisions usually involve multiple things at once.
"Can I ride the rollercoaster?" depends on **age AND height.**
"Can I get my driver's license?" depends on **age OR a special
permit.** "Should I take an umbrella?" depends on whether it's
**NOT sunny.**

Python has three words for combining conditions:

| Word | What it means | Example |
|---|---|---|
| `and` | both must be true | `age >= 13 and height >= 50` |
| `or` | at least one must be true | `name == "Sam" or name == "Alex"` |
| `not` | the opposite | `not age >= 18` |

#### `and` — both conditions

```python
age = 15
height = 60

if age >= 13 and height >= 50:
    print("You can ride!")
else:
    print("Sorry, not yet.")
```

The `if` runs only if **both** parts are true. Age must be at
least 13, *and* height must be at least 50. If either fails, the
combined condition is false.

Try changing `age = 12`. The condition fails (because 12 isn't
>= 13). Try changing `height = 40`. Same — fails because
height isn't >= 50.

#### `or` — at least one

```python
name = input("What's your name? ")

if name == "Sam" or name == "Alex" or name == "Jordan":
    print("Welcome, friend!")
else:
    print(f"Hi, {name}.")
```

The `if` runs if the name matches **any** of the three. The `or`
operator means "at least one of these has to be true."

#### `not` — the opposite

```python
is_raining = True

if not is_raining:
    print("Leave the umbrella at home.")
else:
    print("Bring your umbrella!")
```

`not` flips a true to false (or vice versa). `not True` is
`False`. `not False` is `True`.

`not` is most useful when the variable already has a yes/no
meaning. `not is_raining` reads naturally: "if it's not
raining."

#### Combining all three

You can mix them. Here's a full example:

```python
age = 14
has_permission = True

if (age >= 13 or has_permission) and not age < 8:
    print("You can play this game.")
else:
    print("Not allowed.")
```

This checks: "if (you're 13 or older OR you have permission),
AND (you're NOT under 8), then you can play."

The parentheses group the conditions like math. `and` is
checked after `or` by default — using parentheses makes the
order explicit and makes the code easier to read.

> **Tip:** when conditions get complicated, **put each part on
> its own line.** Python lets you split a long condition with
> backslashes or by surrounding it with parentheses. Most
> programmers use parentheses. We'll see that in the
> rollercoaster project.

**Checkpoint:** *You've used `and`, `or`, and `not` in at least
one program, and you've seen how Python evaluates a combined
condition.* **This is the natural stop point if class is cut
short.**

---

### Part B: The rollercoaster eligibility checker

Time to build something that uses all this.

#### What you're building

A program that asks the user their age and height, then tells
them whether they can ride the rollercoaster. The rules:

- You must be at least **13 years old.**
- You must be at least **48 inches tall.**

Both conditions must be true to ride.

#### Base goal

```python
print("Welcome to the Rollercoaster Eligibility Checker!")

age = int(input("How old are you? "))
height = int(input("How tall are you, in inches? "))

if age >= 13 and height >= 48:
    print("You can ride! Have fun!")
else:
    print("Sorry, you can't ride this one.")
```

Save. Run. Try a few combinations:
- `age = 15, height = 60` — should pass.
- `age = 10, height = 70` — should fail (too young).
- `age = 14, height = 40` — should fail (too short).

That's the base goal. Working program, simple combined
condition.

#### Stretch — tell them WHY

A vague "sorry, you can't ride" isn't very helpful. Use
multiple branches to tell the user *exactly* what's wrong:

```python
if age >= 13 and height >= 48:
    print("You can ride! Have fun!")
elif age >= 13 and height < 48:
    print("You're old enough, but you're a little too short.")
elif age < 13 and height >= 48:
    print("You're tall enough, but you're a little too young.")
else:
    print("You're both too young and too short. Come back in a few years!")
```

Now the program gives specific feedback for each failure case.
Four possible outcomes; one branch per outcome.

#### Extension — refactor with intermediate variables

The repeated `age >= 13` and `height >= 48` checks are awkward.
Save the results in *named variables* for cleaner code:

```python
print("Welcome to the Rollercoaster Eligibility Checker!")

age = int(input("How old are you? "))
height = int(input("How tall are you, in inches? "))

old_enough = age >= 13
tall_enough = height >= 48

if old_enough and tall_enough:
    print("You can ride! Have fun!")
elif old_enough:
    print("You're old enough, but you're a little too short.")
elif tall_enough:
    print("You're tall enough, but you're a little too young.")
else:
    print("You're both too young and too short. Come back in a few years!")
```

Notice what's different:

- `old_enough = age >= 13` saves the result of the comparison
  (a True or False value) in a variable. This is called a
  **boolean** — a value that's either `True` or `False`.
- The `if` statements now read more like English.
- The repetition is gone.

This is a common trick in real code: when conditions are
repeated or complex, give them names.

You could push this even further:

```python
if old_enough and tall_enough:
    print("You can ride! Have fun!")
else:
    if not old_enough:
        print("- You're too young.")
    if not tall_enough:
        print("- You're too short.")
    print("Try again later!")
```

Now you list *all* the failures, not just the first one. That
uses `not` to invert each check.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the base — did your eligibility check
  work for the test cases?
- For the stretch — was anyone surprised by the "old enough but
  too short" message?
- For the extension — did the named variables version feel
  cleaner?

You learned today the three small words that make Python's
conditionals genuinely powerful. **`and`, `or`, `not`** turn
simple yes/no checks into real decisions about complicated
situations. Every program that handles "what should we do here?"
ends up using these.

You also met **booleans** — values that are `True` or `False`.
Booleans are the third major type after numbers and strings,
and you'll see them constantly from here on.

### If you missed this session

Open Thonny and start a new file. Save as `decisions.py`. Then:

1. Try basic `and`, `or`, `not` examples:
   ```python
   age = 15
   if age >= 13 and age < 20:
       print("Teenager.")
   ```

2. Build the rollercoaster eligibility checker (Part B base):
   - Ask for age and height
   - Check `age >= 13 and height >= 48`
   - Print "you can ride" or "sorry"

3. Try the stretch — separate branches for each failure case.

About 30 minutes. If you get stuck, ask your buddy at the start
of next class.

### Stretch and extension ideas

- The order of `or` and `and` matters when they're mixed.
  `True or True and False` is `True` because `and` is
  evaluated first. Use parentheses when in doubt: `(True or
  True) and False` is `False`.
- `True` and `False` (with capital T and F) are Python's
  built-in booleans. You can assign them directly: `is_raining
  = True`.
- The `bool()` function converts other values to True/False.
  `bool(1)` is True; `bool(0)` is False; `bool("")` is False;
  `bool("hello")` is True. Try them.
- Compound conditions with three or more parts:
  `if x > 0 and y > 0 and z > 0:` — works for any number of
  parts.

### What's next

Next week we deepen **loops** and meet **the Thonny debugger**
— a tool that lets you watch your program run line by line. The
debugger is the single most useful thing for figuring out why
your program isn't doing what you thought it would. By the end
of next week, you'll have a new debugging superpower.
