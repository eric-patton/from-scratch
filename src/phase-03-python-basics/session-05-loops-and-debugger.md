## Session 5: Loops (deeper) and the Thonny debugger

*Phase 3 — Python basics · Session 5 of 16*

### What we're learning today

Two new things today, both useful: the `while` loop (a different
kind of loop from the `for` loop you already know), and the
**Thonny debugger** — a tool that lets you watch your program
run line by line and see exactly what's happening inside. The
debugger is the single most useful tool for figuring out why
your code isn't doing what you thought it would. By the end of
class, you'll have a new debugging superpower.

### You'll need to remember from last time

- **`for` loops** — `for i in range(N):` runs N times.
- **Combined conditionals** — `and`, `or`, `not`.
- **Booleans** — `True` and `False`.
- **Indentation** — code inside a loop or `if` is indented.

---

### Part A: The `while` loop

Open Thonny and start a new file. Save it as `while_loop.py`.

#### What `while` does

A `for` loop runs a known number of times — `for i in range(10):`
runs ten times. Period.

A `while` loop runs **as long as a condition is true.** The
program checks the condition before each iteration; if it's
true, run the body and check again; if it's false, stop.

```python
count = 1
while count <= 5:
    print(f"Count is {count}")
    count = count + 1

print("Done!")
```

Save. Run.

```
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
Done!
```

Walk through what happened:

- `count = 1` — start the variable at 1.
- `while count <= 5:` — check: is 1 <= 5? Yes. Run the body.
- Inside: print, then `count = count + 1` (now count is 2).
- Back to the `while` check: is 2 <= 5? Yes. Run again.
- ...continue until count is 6. Now `6 <= 5` is False. Stop.
- After the loop, "Done!" prints.

The structure: `while CONDITION:` then indented body. Same
indentation rule as `if` and `for`.

#### Why `while` instead of `for`?

`for` loops are great when you know how many times to repeat —
"draw 10 squares" or "for each letter in this word."

`while` loops are great when you don't know how many times —
"keep asking the user until they give a valid answer" or "keep
playing until the player wins."

Try this — a guess-the-number style program:

```python
secret = 7
guess = 0   # start with anything that's not the secret

while guess != secret:
    guess = int(input("Guess a number: "))
    if guess != secret:
        print("Nope, try again.")

print(f"You got it! The number was {secret}.")
```

Save. Run. Try to guess 7. The loop runs until you guess right.

This wouldn't be easy with a `for` loop — you don't know how
many guesses it'll take.

#### Watch out for infinite loops

The dangerous thing about `while` loops: if the condition never
becomes false, the loop runs forever. This is called an
**infinite loop.**

```python
count = 1
while count <= 5:
    print(count)
    # OOPS: forgot to update count!
```

Run this. The shell prints `1` over and over forever. Press
the **red Stop button** in Thonny (or Ctrl-C in the shell) to
kill it.

Every `while` loop must do something inside that *eventually
makes the condition false.* Most often that's updating a
variable (like `count = count + 1` in the example).

#### `break`

Sometimes you want to exit a loop early. The `break` statement
does that:

```python
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break
    print(f"You said: {answer}")

print("Goodbye!")
```

`while True:` is a deliberate "infinite" loop — but `break`
exits it when the user types "quit." Common pattern.

**Checkpoint:** *You've written a `while` loop that runs at
least three times before stopping (either by a count
variable or by user input).* **This is the natural stop point
if class is cut short.**

---

### Part B: The Thonny debugger

Now for the debugging superpower.

#### What the debugger is

Most of the time when your code is wrong, you read the code,
spot the bug, fix it. But sometimes — especially with loops and
multi-step programs — you can't tell what's wrong by reading.
Variables change in ways you didn't expect. The control flow
goes somewhere you didn't intend.

The **debugger** lets you watch your program run *line by line*
and see the value of every variable at every step. It's like
having superpowered slow-motion vision.

#### A buggy program

Type this exactly. There's a deliberate bug:

```python
word = "hello"
vowel_count = 0

for letter in word:
    if letter in "aeiou":
        vowel_count = 1

print(f"Vowels in '{word}': {vowel_count}")
```

Save as `vowel_bug.py`. Run.

```
Vowels in 'hello': 1
```

But "hello" has *two* vowels (e, o). Why does the program say
1? Reading the code carefully, you might spot it. But let's use
the debugger to *see* the bug happen.

#### Running with the debugger

In Thonny, look at the toolbar. Next to the green Run button,
there are some other buttons. The one that looks like a **bug**
icon is "Debug current script."

Click the **bug icon** (or press Ctrl-F5).

Two things change:

- The program pauses at the first line, with that line
  highlighted.
- A panel appears (often on the right) showing **variables and
  their values.** Right now, no variables exist yet.

#### Stepping through

Find the **"Step over" button** (looks like an arrow stepping
over a line — usually called Step Over, F6 on most systems).
Click it once.

The first line ran. Look at the variables panel — `word` is now
`"hello"`. You can *see* the variable that just got created.

Click "Step Over" again. Now `vowel_count` is `0`.

Click again. The `for` loop starts. Watch what `letter` is — it's
`"h"`. The loop is on its first iteration, looking at the first
character of "hello".

Click again. The `if` checks: is `"h"` in `"aeiou"`? No. Skip
the body.

Click again. Loop continues. Now `letter` is `"e"`.

Click again. `if` checks: is `"e"` in `"aeiou"`? Yes! Run the
body.

Click again. `vowel_count = 1`. The variables panel updates —
`vowel_count` is now `1`.

Click again. Loop continues. Now `letter` is `"l"`. `if` is
False, skip.

Click. `letter` is `"l"` again. Skip.

Click. `letter` is `"o"`. `if` is True! Run the body.

Click. `vowel_count = 1`. **Wait — it's still 1, not 2.**

That's the bug. Every time the program finds a vowel, it sets
`vowel_count` to `1` (overwriting the previous value), instead
of *adding 1* to the existing count.

#### Fix the bug

Change `vowel_count = 1` to `vowel_count = vowel_count + 1`.

Save. Run normally (green button). Output:

```
Vowels in 'hello': 2
```

You found and fixed a bug by *watching the program run.* That's
the debugger.

#### Why this matters

You'll often be in this situation: your program runs but does
the wrong thing, and you don't know why. Reading the code more
carefully helps sometimes. The debugger helps *every* time —
it shows you exactly what's happening.

The same workflow works for any Python program:

1. Click the bug icon to start debugging.
2. Watch the variables panel.
3. Click "Step Over" to advance one line at a time.
4. Notice when a variable becomes wrong. That's where the bug is.

You can also click **"Resume"** (or F8) to run normally until
the next error or until the program ends.

#### Try it

Open one of your earlier programs (the rollercoaster checker,
the name analyzer, or the age calculator). Run it with the
debugger. Step through. Watch the variables change.

You don't need to find a bug — just practice using the
debugger. The fluency you build by using it on working code
makes it much easier to use when you actually need it.

---

### Wrap-up

Before we leave, share with the room:

- What's a situation where a `while` loop made more sense than
  a `for` loop?
- For the debugger demo — was it surprising to *see* the
  vowel_count being set to 1 every time?
- For the kids who debugged an earlier program — did anything
  surprise you about how it ran?

You learned today the most important debugging skill in any
programming language: **watching your program execute, step by
step.** The Thonny debugger is small and friendly; debuggers
in bigger languages (like JavaScript or Java) work the same way
but with more features. The mental model carries over.

You also learned `while` — the loop for "until something is
true." Combined with `for` (for known counts), these are the
two loop tools you'll use for the rest of your programming
life.

### If you missed this session

Open Thonny and start a new file. Save as `while_loop.py`. Then:

1. Build a `while` loop that counts up:
   ```python
   count = 1
   while count <= 5:
       print(f"Count is {count}")
       count = count + 1
   ```
   Save, run.

2. Build the guess-the-number version (Part A above).

3. Open `vowel_bug.py` (Part B). Type it in with the bug. Run
   it normally — see the wrong answer (1 vowel for "hello").
   Now click the **bug icon** in Thonny instead of the green
   Run button. Step through with F6. Watch the variables
   panel. Find where `vowel_count = 1` is wrong (should be
   `vowel_count + 1`). Fix it.

About 40 minutes. The debugger takes a few minutes to get
comfortable with — keep stepping through.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- **Step Into** (F7) — for stepping *inside* a function call,
  not just over it. Useful when you have a function with a bug.
- **Set a breakpoint** — click in the leftmost margin next to
  a line number. The program will pause when it reaches that
  line. Useful for skipping past parts you've already verified.
- **`continue`** (in loops) — like `break`, but skips the rest
  of the *current iteration* and moves to the next one. Less
  useful than `break`; mention if asked.
- **`while` with multiple exit conditions** — `while not done
  and not error:`. Combine booleans with `while`.

### What's next

Next week we deepen **functions** — specifically, functions
that *return* a value (like `len("hello")` returns `5`). Until
now, functions just *did* things. Next week they'll start
giving you results back, which is what makes them genuinely
powerful.
