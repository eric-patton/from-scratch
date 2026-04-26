## Session 7 — Teacher Notes

*Phase 4, Intermediate Python · Session 7 of 9 · Title:
Testing — making sure your code works*

### Purpose of this session

Testing is the discipline that separates "code that works
right now" from "code I can change next month without
breaking." Five jobs, in priority order:

1. **Land `assert` as the foundation of testing.** Built-in,
   simple, sufficient for today.
2. **Land "tests catch bugs you'd miss otherwise."** The
   "break on purpose, watch the test catch it" demo is the
   lesson.
3. **Land the test-file convention.** `test_*.py` files
   alongside the code they test. Real Python convention.
4. **Land "test happy AND edge cases."** Bugs hide where you
   weren't looking.
5. **Set up the milestone (Sessions 8-9).** Milestone
   projects should include at least a few tests.

Note: pytest is mentioned as a stretch extension. We're not
formally teaching pytest because it requires `pip install`
and adds conceptual weight. Plain `assert` is sufficient for
the testing *mindset*.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with terminal.
- Optional: pre-built math_tools / test_math_tools / pet /
  test_pet for destination preview.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was Git
  practice. Anyone use branches at home?
- **Part A: assert basics** (~40 min) — math_tools setup ~5
  min, first assertions ~10 min, watch a test fail ~10 min,
  test functions for organization ~10 min, checkpoint ~5
  min.
- **Break** (~5 min).
- **Part B: test a real project** (~35 min) — Pet class ~5
  min, test_pet ~15 min, find a bug ~5 min, run_tests
  helper stretch ~10 min.
- **Wrap-up** (~5 min).

If running short, **the run_tests helper and pytest
extension can be cut.** The base test_pet that catches a
deliberate bug is the goal.

### Teaching Part A

#### The framing

Open with the question:

> "How do you *know* your code works? You ran it once, it
> seemed fine. But did you check every input? What about
> negative numbers? What about zero? When you change
> something next month, will you remember to re-check
> everything? That's what tests are for."

The "I won't remember to re-check" angle resonates. It's
true.

#### `assert`

Walk through `assert add(2, 3) == 5`. Then deliberately
break `add` to make it fail. The "AssertionError" is the
visceral payoff:

> "The test crashed because the assertion failed. Python
> told you which line — `assert add(2, 3) == 5` — meaning
> `add(2, 3)` didn't return `5`. The test caught your bug
> immediately."

Without the test, the bug might have slipped past you to
discover only when something downstream broke.

#### Test functions for organization

Mechanical refactor. Wrap each set of related assertions in
a function:

```python
def test_add():
    assert add(2, 3) == 5
    ...
    print("add tests passed")
```

Then call them at the bottom.

> "When you have lots of tests, group them into functions.
> Each function tests one thing. The print at the end of
> each gives you progress feedback."

The "progress feedback" naming matters — kids should see the
prints as a feature, not noise.

### Teaching Part B

#### Recreate Pet (or use theirs)

Most kids should have the Pet class from Session 4. If
they've lost it, the simplified version in the handout is
fine.

Note this version uses `hunger` as a number (0-10) rather
than the boolean from Session 4. More interesting tests.

#### Build test_pet.py

The four tests cover:
1. New pet has right initial state
2. Feed reduces hunger
3. Feed doesn't go below zero (edge case!)
4. is_hungry returns the right value (state-dependent)

Walk through the structure once at the projector. Then
have students build their own.

The "each test creates its own pet" principle is worth
naming:

> "Notice — every test creates a fresh `Pet`. We don't
> share pets between tests. Why? Because if test 1 changes
> the pet's state, test 2 wouldn't be testing what it
> thinks. Fresh state for each test = independent tests."

This is the principle of **test isolation.** Real testing
frameworks have features for this; today we just create
fresh instances.

#### The deliberate bug

Open `pet.py`. Change `>` to `>=` in `is_hungry`. Run the
tests:

```
test_new_pet passed
test_feed_reduces_hunger passed
test_feed_never_below_zero passed
AssertionError
```

The fourth test catches it.

> "Look. Three tests still pass. The fourth catches the
> change. Without tests, you might never have noticed —
> until weeks later when your game feels 'slightly off.'
> Tests catch this immediately."

This is the lesson. Make it land.

#### Stretch — run_tests helper

The helper that catches AssertionError and reports cleanly
is the bridge to pytest. Worth showing for kids who finish
early.

The `test.__name__` attribute is new:

> "Every function in Python has a `.__name__` attribute
> giving you its name as a string. Useful when you're
> writing tools that report on functions."

Don't dwell. Just show.

#### Extension — assertion messages

`assert condition, "message"` adds a message to the failure.
Real improvement in debugging:

```
AssertionError: After overfeeding, hunger should be 0 but was -95
```

> "Always include a message in important asserts. Future-
> you (or your teammate) will thank you when a test fails
> at 11pm and they need to figure out what broke."

#### Extension — pytest

Pytest is what real projects use. Mention briefly:

```
$ pip install pytest
$ pytest
```

It auto-discovers `test_*.py` files and `test_*` functions.
Better output. More features. Don't formally teach today —
this is a "for the curious" pointer.

### Common stumbles

- **`assert` doesn't crash with no message.** Sometimes
  kids think a passing assert is a "success" — show that no
  output is the success signal.
- **Tests pass even when code is broken.** Usually means
  the test is testing the wrong thing. Walk through what
  the assertion actually checks.
- **Test for the function that doesn't exist.** Forgot to
  define or `import` the function. NameError.
- **Imported the wrong function name.** `from math_tools
  import addd` (typo) — ImportError.
- **Test changes shared state.** A test modifies a global
  and the next test sees the modification. This is exactly
  why we make fresh instances.
- **`assert` confused with `=` or `==`.** The keyword is
  `assert`, then a condition. The condition uses `==` for
  equality.
- **Used `print(condition)` instead of `assert condition`.**
  Print just shows; assert *checks*.

### Differentiation

- **Younger kids (9-10):** Focus on Part A. The Pet tests
  in Part B may be too much; building one or two Pet tests
  is plenty.
- **Older kids (12+):** Will pick up assert quickly. Push
  through the Pet tests, the run_tests helper, and pytest
  if they're motivated.
- **Advanced (any age):** Suggest:
  - `pytest` (full installation and use)
  - Test fixtures (in pytest)
  - Mocking (advanced)
  - Test-driven development workflow
  - Testing with parameters (`@pytest.mark.parametrize`)
- **Struggling:** A kid who can't get a basic assert
  passing is the kid you focus on. Most common cause:
  syntax error in the assertion or wrong import.

### What to watch for

- **The "the test caught my bug!" reaction.** Several kids
  will visibly process this. Affirm.
- **Buddies trading bug ideas.** "Try changing your `add`
  to `a - b`. Do your tests catch it?" Encourage. Real
  testing practice.
- **The "I want to test EVERYTHING I've built" reaction.**
  Some kids will. Encourage but caution about scope —
  testing every line of every old project is overkill;
  testing the *important* pieces of new projects is the
  goal.
- **Frustration with tests that fail when they shouldn't.**
  Usually a typo in the assertion. Walk through.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 8 (next week, milestone day 1).** Milestone
  projects should include tests for the important pieces.
- **Session 9 (milestone demo).** Tests can be part of the
  demo: "I changed this thing and the tests still all
  passed."
- **Phase 5+ (every later phase).** Real projects have
  tests. The habit established today carries forward.
- **Phase 8 (Flask).** Web apps especially benefit from
  tests; pytest is standard. Today's foundation.
- **The peanut butter callback opportunity:** the "tests
  pass even when code is broken" bug is a precision
  moment. The test checked exactly what was written; the
  assertion was wrong; the bug slipped through. Be specific
  about what you're checking.

### Materials checklist

- [ ] Demo machine with Thonny + terminal
- [ ] Optional: pre-built math_tools and test files
- [ ] Projector (helpful for the "watch a test fail" demo)
- [ ] Class roster
