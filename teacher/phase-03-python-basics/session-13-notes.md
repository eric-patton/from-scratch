## Session 13 — Teacher Notes

*Phase 3, Python basics · Session 13 of 16 · Title: Error
handling — `try` and `except`*

### Purpose of this session

Error handling separates programs that *technically work* from
programs that are *actually usable.* Five jobs, in priority
order:

1. **Land `try / except` syntax.** Mechanical but new structure.
2. **Land "catch specific exceptions, not bare except."** A
   habit worth establishing early. Bare `except:` is one of the
   most common bad-Python smells.
3. **Land the try-again loop pattern.** `while True: try: ...
   return ... except: print error` — extremely common idiom.
4. **Apply to existing programs.** Today's value is in
   *retrofitting* programs from earlier sessions to be more
   robust. The hangman input function is a perfect target.
5. **Set up the integration project (Session 14).** Robust
   programs need error handling everywhere. Today's tools are
   the foundation.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: have the hangman from last week ready to retrofit
  with the input function.
- Verify a deliberately-bad input (`int("hello")`) produces
  a `ValueError` you can show.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was hangman.
  Anyone play their game with friends?
- **Part A: try/except** (~40 min) — the crash demo ~5 min,
  basic try/except ~10 min, exception types ~5 min, why
  specific ~5 min, try-again loop ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: robust input** (~35 min) — ask_for_number base ~10
  min, bounded version stretch ~10 min, hangman / notes
  retrofit extensions ~15 min.
- **Wrap-up** (~5 min).

If running short, **the bounded-numbers stretch can be cut.**
The basic ask_for_number function is the goal.

### Teaching Part A

#### The crash demo

Open with the visceral problem:

```python
age = int(input("How old are you? "))
```

Run. Type "hello." Crash. Show the traceback.

> "Look at this. The user just typed something the program
> wasn't expecting and the whole thing crashed. That's a
> *terrible* user experience. Real programs don't do this.
> Real programs handle the error and ask again."

This sets up the "we need a tool" feeling.

#### Basic try/except

Walk through at the projector:

```python
try:
    age = int(input("How old are you? "))
    print(f"In ten years you'll be {age + 10}.")
except ValueError:
    print("That's not a number!")
```

Step through:
- `try:` block runs first.
- If everything works, `except` is skipped.
- If `ValueError` happens, jump to the `except` block.

> "We *try* the risky code. If it works, great. If it raises
> a `ValueError`, we catch it in the `except` block and do
> something cleaner than crashing."

Run with good input — works. Run with bad input — handled
gracefully. The before-and-after is the lesson.

#### The exception types table

Walk through quickly. Don't memorize. The point: many things
can fail; each has a name; you can catch each one specifically.

The most common ones in this class:
- `ValueError` (input conversion)
- `FileNotFoundError` (open)
- `KeyError` (dict lookup)
- `ZeroDivisionError` (math)

Others come up in specific contexts; kids will learn them as
they hit them.

#### Why specific

Demo the bare `except:`:

```python
try:
    age = int(input("Age? "))
except:
    print("Something went wrong.")
```

Run with bad input — works. But:

> "What if there's a bug in my code somewhere? Like I typo'd
> a variable name? With bare `except:`, my program doesn't
> crash — but I don't know there's a bug. The bare except
> *hides bugs.* Catch only the specific error you expected."

This is professional advice that kids would otherwise have to
learn the hard way.

#### The try-again loop

The canonical pattern. Build at the projector:

```python
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("That's not a number. Try again.")
```

Walk through:
- Loop forever.
- Try the conversion.
- If it works, `break` (we have valid input).
- If it doesn't, `except` runs (print message), then loop
  continues.

The placement of `break` matters — *inside* the try, after
the operation that might fail. If the int() succeeds, we
reach break. If it fails, we don't reach break.

This pattern is the most-common application of try/except in
real Python. Drill it.

### Teaching Part B

#### The `ask_for_number` function

This combines functions (Session 6), return values (Session
6), the try-again loop (today), and `try/except` (today).

```python
def ask_for_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a number. Try again.")
```

The `return` *inside* the `try` is the slick part. If the
conversion works, we return immediately — function ends, loop
exits, value flows back to caller. If it fails, we never
reach return; the except runs; loop continues.

> "This is a tiny function. But you can now use it everywhere
> you need a number from the user, and bad input is handled
> automatically. That's the power of functions plus
> try/except."

Demo using the function in a small program. Show how the
calling code is now *simple* — no try/except needed at the
call site.

#### Stretch — bounded numbers

The bounded version uses `continue` to "ask again" without
going through `except`:

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
            print("That's not a number.")
```

Two ways to "ask again": `except` (for type errors) and
`continue` (for range errors). Both lead back to the top of
the loop.

#### Extension — apply to hangman

The hangman input doesn't really need `try/except` (no
conversion to fail). It needs **input validation** — `if`
checks for empty / multiple / non-letter.

This is a good distinction:

> "`try/except` is for things that might *crash*. Validation
> with `if` is for things that are *valid syntactically but
> wrong logically.* Both are about handling bad input
> gracefully; they're just different tools for different
> situations."

The `guess.isalpha()` method is new. Mention briefly:

> "Strings have lots of these is-something methods.
> `.isalpha()` is True if every character is a letter.
> `.isdigit()` for all digits. `.isspace()` for whitespace.
> Useful for validation."

#### Extension — file-not-found

Refactor the Session 11 notes program to use proper
`try/except FileNotFoundError`. Same pattern, different
exception. Worth pointing out:

> "Same try/except shape works for ANY exception type. ValueError
> for bad number input. FileNotFoundError for missing file.
> KeyError for missing dict key. The pattern is reusable."

### Common stumbles

- **Bare `except:` instead of specific.** Habit dies hard.
  Reinforce: "name the exception you're catching."
- **`break` outside the `try`.** Wrong place; the loop never
  exits even on success. Move inside.
- **`return` outside the `try`.** Same problem.
- **`except` block does nothing useful.** `except ValueError:
  pass` silently ignores the error. Sometimes wanted (e.g.,
  the file-not-found case from Session 11), often a
  code smell.
- **Catching the wrong exception type.** `except KeyError:`
  on a `try` that does `int()` won't catch `ValueError`.
  Match the type to the operation.
- **Using try/except for control flow that should be `if`.**
  Don't use `try` to check whether something *might* be true;
  use `if`. Use `try` for things that genuinely *might error*.

### Differentiation

- **Younger kids (9-10):** May find error handling abstract.
  Lean on the visceral payoff — type bad input, see the program
  ask again instead of crash. The `ask_for_number` function
  is great for them; ignore the bounded stretch.
- **Older kids (12+):** Will pick this up fast. Push them
  through the hangman retrofit. If they finish: ask them to
  add validation to a different earlier program (number-
  guessing game, score tracker, etc.).
- **Advanced (any age):** Suggest:
  - `try/except/else` — `else` runs only if no exception
  - `try/except/finally` — `finally` always runs
  - `raise ValueError("message")` — raising your own errors
  - Custom exception classes (`class MyError(Exception):`) —
    Phase 4+ topic
- **Struggling:** A kid who can't get the basic `try/except`
  working is probably hitting a syntax error (forgot colon,
  wrong indent). Walk through.

### What to watch for

- **The "the program asked again instead of crashing" reaction.**
  Several kids will visibly process this. Affirm.
- **Buddies finding edge cases in each other's programs.** The
  validation extension naturally invites this. Encourage.
- **The "this should be in EVERYTHING I write" insight.**
  Today's pattern is genuinely useful constantly. Reinforce.
- **Frustration at the `bare except` rule.** Some kids will
  push back: "but it's easier!" Explain: yes, but it hides
  bugs and you'll regret it. Establish the habit.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 14 (next week, integration project).** Robust
  programs need error handling everywhere. Today's tools used
  throughout next week's project.
- **Phase 4 (intermediate Python).** Custom exceptions, more
  complex error hierarchies, exception chaining.
- **Phase 7 (web).** Error pages, form validation, HTTP error
  codes — all built on this foundation.
- **Phase 8 (Flask).** Route handlers wrapped in try/except for
  graceful errors; database operations need exception
  handling; file uploads need validation. All today's
  patterns, scaled up.
- **The peanut butter callback opportunity:** the bare-except
  hiding bugs is a precision moment. The computer caught
  *every* error including ones you didn't expect; you wanted
  to know about them; you didn't because of bare except.
  Be specific.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: hangman from last week ready to retrofit
- [ ] Projector (helpful for the crash demo and the
      try-again loop walkthrough)
- [ ] Class roster
