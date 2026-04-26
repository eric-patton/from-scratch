## Session 7: Testing — making sure your code works

*Phase 4 — Intermediate Python · Session 7 of 9*

### What we're learning today

How do you *know* your code works? You can run it once and
see — but what about next week, after you've changed
something? What about the edge cases you didn't think to
test? Today we learn **automated tests** — code that checks
other code. By the end of class, you'll have a small
program with its own test file that catches bugs
automatically.

### You'll need to remember from last time

- **Multi-file programs** — `tools.py` and `main.py`
  imported from each other.
- **Functions with return values** (Phase 3 Session 6).
- **Git** — we'll commit our tests alongside our code.
- **`assert`** — we touched it briefly in Session 6 of
  Phase 2 and Session 12 of Phase 3 stretches; today it
  becomes central.

---

### Part A: `assert` — the simplest test

Open Thonny and create a new folder for today. Save it as
`testing_practice`. Inside, create `math_tools.py`:

```python
# math_tools.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def double(x):
    return x * 2
```

Save.

Now create `test_math_tools.py` in the same folder:

```python
# test_math_tools.py
from math_tools import add, subtract, double

assert add(2, 3) == 5
assert add(0, 0) == 0
assert add(-1, 1) == 0

assert subtract(10, 3) == 7
assert subtract(5, 5) == 0

assert double(4) == 8
assert double(0) == 0
assert double(-3) == -6

print("All tests passed!")
```

Save. From a terminal, in this folder:

```
$ python test_math_tools.py
All tests passed!
```

You just ran your first tests.

#### What `assert` does

`assert condition` checks if a condition is true. If it's
true, nothing happens (the line just runs). If it's false,
the program **crashes immediately** with an
`AssertionError`.

So `assert add(2, 3) == 5` says: "I claim that `add(2, 3)`
returns `5`. If not, something is wrong — crash."

When all assertions pass, you reach the `print("All tests
passed!")` line. When one fails, the program crashes
*before* that line, telling you which assertion failed.

#### Watch a test fail

Open `math_tools.py` and **break it on purpose**:

```python
def add(a, b):
    return a - b   # typo! should be a + b
```

Save. Run the tests:

```
$ python test_math_tools.py
Traceback (most recent call last):
  File "test_math_tools.py", line 4, in <module>
    assert add(2, 3) == 5
AssertionError
```

The very first assertion failed. Python told you exactly
which line — `assert add(2, 3) == 5` — meaning `add(2, 3)`
did *not* return `5`.

Fix the typo (back to `a + b`). Run again. All pass.

This is the magic: **the test caught the bug.** You didn't
have to manually check each function — running the test
file did it for you. And next time you change the code, you
can run the tests again to make sure you didn't break
anything.

#### Test functions for organization

When you have lots of tests, group them into functions:

```python
# test_math_tools.py
from math_tools import add, subtract, double

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    print("add tests passed")

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0
    print("subtract tests passed")

def test_double():
    assert double(4) == 8
    assert double(0) == 0
    assert double(-3) == -6
    print("double tests passed")

# run all tests
test_add()
test_subtract()
test_double()
print("\nAll tests passed!")
```

Each test function checks one thing. The bottom of the file
calls them all in turn.

When something breaks, the print statements tell you which
group is the last one that worked — the broken function is
the next one. Useful narrowing-down.

**Checkpoint:** *You have a code file (`math_tools.py`) and
a test file (`test_math_tools.py`) that runs assertions
against the code, and you've seen at least one assertion
fail when you broke the code.* **This is the natural stop
point if class is cut short.**

---

### Part B: Test a real project

Now we'll write tests for something more substantial —
either the Pet class from Session 4, or a project of your
choice.

#### Recreate the Pet class (or use yours)

In your folder, create `pet.py`:

```python
# pet.py
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
    
    def feed(self, amount):
        self.hunger = self.hunger - amount
        if self.hunger < 0:
            self.hunger = 0
    
    def is_hungry(self):
        return self.hunger > 3
```

Save.

Now create `test_pet.py`:

```python
# test_pet.py
from pet import Pet

def test_new_pet():
    pet = Pet("Rex")
    assert pet.name == "Rex"
    assert pet.hunger == 5
    print("test_new_pet passed")

def test_feed_reduces_hunger():
    pet = Pet("Rex")
    pet.feed(2)
    assert pet.hunger == 3
    print("test_feed_reduces_hunger passed")

def test_feed_never_below_zero():
    pet = Pet("Rex")
    pet.feed(100)
    assert pet.hunger == 0
    print("test_feed_never_below_zero passed")

def test_hungry_check():
    pet = Pet("Rex")
    assert pet.is_hungry() == True   # starts with hunger=5, > 3
    pet.feed(2)
    assert pet.is_hungry() == False  # hunger is now 3, not > 3
    print("test_hungry_check passed")

test_new_pet()
test_feed_reduces_hunger()
test_feed_never_below_zero()
test_hungry_check()
print("\nAll tests passed!")
```

Run:

```
$ python test_pet.py
test_new_pet passed
test_feed_reduces_hunger passed
test_feed_never_below_zero passed
test_hungry_check passed

All tests passed!
```

Walk through what's new:

- **Each test function tests *one specific thing*.** Pet
  starts with the right state. Feed reduces hunger. Feed
  doesn't go below zero. The hungry check works correctly.
- **Each test creates its own pet.** Fresh start; no
  interference between tests.
- **Tests both happy and edge cases.** `feed(2)` is normal;
  `feed(100)` is "what if someone overfeeds?"

The fourth test is interesting — it tests `is_hungry()`
*after* a state change, ensuring the method updates correctly.

#### Find a bug

Now break `pet.py` deliberately:

```python
def is_hungry(self):
    return self.hunger >= 3   # changed from > to >=
```

Run the tests:

```
$ python test_pet.py
test_new_pet passed
test_feed_reduces_hunger passed
test_feed_never_below_zero passed
Traceback (most recent call last):
  File "test_pet.py", line 28, in <module>
    test_hungry_check()
  ...
AssertionError
```

The change broke `test_hungry_check`. The tests caught it
immediately. Without tests, you might have spent hours
wondering why your game felt slightly off ("the pet seems
hungry too easily").

Fix it (back to `>`) and tests pass again.

That's the **base goal.**

#### Stretch — a `run_tests` helper

Wrap the test-running into a helper that catches errors and
reports cleanly:

```python
def run_tests(test_functions):
    passed = 0
    failed = 0
    for test in test_functions:
        try:
            test()
            passed = passed + 1
        except AssertionError:
            print(f"FAIL: {test.__name__}")
            failed = failed + 1
    
    print(f"\n{passed} passed, {failed} failed")

run_tests([
    test_new_pet,
    test_feed_reduces_hunger,
    test_feed_never_below_zero,
    test_hungry_check,
])
```

Now even if a test fails, the others keep running, and you
get a summary at the end:

```
4 passed, 0 failed
```

Or if there's a problem:

```
FAIL: test_hungry_check
3 passed, 1 failed
```

`test.__name__` is a Python feature — every function has a
`.__name__` attribute that gives you its name as a string.
Useful for error messages.

#### Extension — assertion messages

Add a message to `assert` so failures are more
self-explanatory:

```python
assert pet.hunger == 0, f"After overfeeding, hunger should be 0 but was {pet.hunger}"
```

The string after the comma is shown when the assertion
fails:

```
AssertionError: After overfeeding, hunger should be 0 but was -95
```

Way more useful than just `AssertionError`. Real testing
frameworks (like pytest) build on this idea.

#### Extension — pytest

Real Python testing uses a tool called **pytest**.
Install it:

```
$ pip install pytest
```

Then test files written in pytest's style:

```python
# test_pet_pytest.py
from pet import Pet

def test_new_pet():
    pet = Pet("Rex")
    assert pet.name == "Rex"
    assert pet.hunger == 5

def test_feed_reduces_hunger():
    pet = Pet("Rex")
    pet.feed(2)
    assert pet.hunger == 3

# ... more tests ...
```

No `print` statements; no `run_tests` call at the bottom.
Just functions starting with `test_`. Then run with
`pytest`:

```
$ pytest
====== test session starts ======
collected 4 items

test_pet_pytest.py ....                                [100%]

====== 4 passed in 0.01s ======
```

`pytest` finds all functions starting with `test_` and runs
them. Reports clearly. Has tons of features for bigger
projects.

We're using basic `assert` today because it's built-in.
`pytest` is what real projects use; mention to anyone
curious.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who tested the Pet class — did you find any
  bugs?
- For the kids who broke their code on purpose — did the
  tests catch it?
- For the kids who tried pytest — was it easier or harder?

You learned today the **discipline** that separates
casual code from professional code. **Code with tests is
trustworthy.** When you change something, you can re-run the
tests and know in seconds whether you broke anything else.
Without tests, you have to manually check everything every
time — which means you don't, and bugs sneak through.

Real projects have *thousands* of tests. They run
automatically every time someone commits code. If a test
fails, the change is rejected. This is how huge projects
stay reliable.

The next two sessions are your **milestone project** —
this time, with multi-file structure, Git from day one, and
*tests* for the important parts. Real software-engineering
practice.

### If you missed this session

Open Thonny and create a folder. Inside it:

1. Make `math_tools.py` with a few simple functions
   (`add`, `subtract`, `double`).

2. Make `test_math_tools.py` with `assert` statements
   testing each function.

3. Run from the terminal: `python test_math_tools.py`. See
   the "All tests passed" message.

4. Break one of your functions on purpose. Run the tests.
   See the failure. Fix it. Run again.

5. Group tests into functions and call them from the
   bottom of the file.

About 35 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- **`pytest`** — the real Python testing tool. `pip
  install pytest` then run with `pytest`. Used by every
  major Python project.
- **Test edge cases** — empty inputs, very large inputs,
  negative numbers, zero. Real bugs hide in edge cases.
- **Test that exceptions are raised** — sometimes you want
  to verify that bad input *does* error. With pytest:
  ```python
  import pytest
  def test_divide_by_zero():
      with pytest.raises(ZeroDivisionError):
          divide(10, 0)
  ```
- **Test-driven development** — write tests *first*, before
  the code. Code passes when all tests pass. Real practice.

### What's next

Next week is the start of your **milestone project** for
Phase 4. This time, you'll use **multi-file structure**
from day one, **Git from day one**, and at least **a few
tests** for the important pieces. You're not just writing
code anymore — you're doing *software engineering.*
