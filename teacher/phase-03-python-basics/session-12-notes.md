## Session 12 — Teacher Notes

*Phase 3, Python basics · Session 12 of 16 · Title: Hangman —
a complete game*

### Purpose of this session

The biggest project in Phase 3 so far. Same role as Phase 1
Session 7 (Apples and Rocks) and the number-guessing game
(Session 7) — synthesis of accumulated skills. Five jobs, in
priority order:

1. **Demonstrate that students can build a non-trivial game
   from the toolkit they have.** Hangman pulls together
   sequences, loops, conditionals, functions, lists, strings,
   and (optionally) file I/O. This is the most ambitious
   single-session project in Phase 3.
2. **Practice the build-incrementally pattern.** Five clear
   steps, each runnable. Models how real programs are built —
   never type the whole thing then debug; build a piece, test,
   add the next piece.
3. **Reinforce functions for organization.** The
   `make_display(secret, guessed_letters)` function isolates a
   pure transformation. Functions used as "do one thing well"
   building blocks — the pattern they'll use forever.
4. **Demonstrate code-vs-data separation.** The hardcoded word
   list is fine; the file-based word list is *better* because
   it separates the *what* (words) from the *how* (game
   logic). One of the most-important real-world patterns.
5. **Set up Session 13 (error handling).** Hangman is robust
   to most user behavior, but what if the user enters a number
   instead of a letter? Or empty input? Today's game handles
   this poorly; next week's `try/except` fixes it.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Pre-built complete hangman (with file loading) ready to demo.
- Optional: pre-create a `words.txt` file with 20-30 good words
  for kids to use.
- This is the longest project of Phase 3 so far. Plan to
  reserve some Part B time for individual help.

**Prep time:** ~20 minutes. Build the full game once. Decide
your word list.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was file I/O.
  Anyone build the persistent notes program at home?
- **Part A: build the display** (~35 min) — the plan ~3 min,
  pick a word ~5 min, show with blanks ~10 min, make it a
  function ~10 min, test ~5 min, checkpoint ~2 min.
- **Break** (~5 min).
- **Part B: full game** (~40 min) — game loop ~25 min, words
  from file ~10 min, stretch/extensions ~5 min.
- **Wrap-up** (~5 min).

Hangman is genuinely longer than other Phase 3 projects. **Don't
skip Part A's checkpoint** — make sure every kid has a working
`make_display` function before adding the game loop. Trying to
debug the loop without trusting the display function is awful.

If running short, **Step 5 (words from file) and the
extensions can be cut.** The base game with hardcoded words is
the goal.

### Teaching Part A

#### The plan

Walk through the six-step plan at the projector or whiteboard
*before any code.* This is decomposition modeled in real time.

> "Don't type yet. Let's name what we're building. The computer
> picks a word. The user sees underscores for unguessed letters.
> User guesses one letter at a time. If it's in the word, fill
> in the blank. If not, count it. Win when full; lose after too
> many wrong."

This is goal #1 of the curriculum. Plant the habit.

#### Step 1: pick a word

`random.choice(words)` is the new piece (we used `random.randint`
in Session 7). Walk through:

> "`random.choice` takes a list and picks one item at random.
> Same `random` module as last session, different function."

The `print(f"DEBUG: secret is {secret}")` is the same testing
pattern from Session 7. Mention again:

> "Print the secret while we're testing. Remove later."

#### Step 2: show with blanks

This is the hardest single piece of the session. Walk through
the logic carefully:

```python
display = ""
for letter in secret:
    if letter in guessed_letters:
        display = display + letter
    else:
        display = display + "_"
```

Mental model: build up the display one character at a time. For
each letter in the secret, decide what to show.

If kids are stuck, walk through what `display` is at each step
of the loop:
- Start: `display = ""`
- After letter 'p' (not guessed): `display = "_"`
- After letter 'y' (not guessed): `display = "__"`
- ...
- After letter 'n': `display = "______"`

Use the debugger if needed!

#### Step 3: make it a function

The function refactor is the canonical Phase 3 move. Walk
through what changes:

- Wrap in `def make_display(secret, guessed_letters):`
- Replace the hardcoded use of those variables with parameters
- Add `return display` at the end

Then **test the function with different inputs:**

```python
print(make_display("python", []))                # ______
print(make_display("python", ["p", "n"]))        # p____n
print(make_display("python", ["p", "y", "t", "h", "o", "n"]))   # python
```

This is **unit testing in spirit** — verify the function works
on multiple cases before depending on it. Mention:

> "Real programmers test functions like this all the time. We
> built this function; now let's prove it works on a few
> cases before relying on it."

### Teaching Part B

#### The game loop

This is a lot of code. Walk through the structure once at the
projector, then have students type it.

The flow:
1. Show display + status.
2. Check win.
3. Check lose.
4. Get input.
5. Validate (already-guessed check with `continue`).
6. Add to guessed list.
7. Update wrong count if applicable.
8. Loop.

The `continue` statement is new. Walk through:

> "`continue` skips the rest of this iteration and jumps back
> to the top of the loop. So if the kid guessed an
> already-tried letter, we say 'already guessed' and continue
> — back to showing the display, getting another guess. We
> don't append to the list, don't count it, just try again."

#### Words from a file

Callback to last week. The pattern is exactly what we taught:

```python
words = []
with open("words.txt", "r") as f:
    for line in f:
        word = line.strip()
        if word:
            words.append(word)
```

The `if word:` check filters out blank lines (empty strings
are falsy in Python). Mention briefly:

> "If a line is blank, the strip gives an empty string, which
> Python treats as 'false' in an `if`. So this skips blank
> lines."

Have kids actually create `words.txt` (in Thonny — File → New,
type words, save as `words.txt`). The "data and code separated"
is a real, visible thing they can manipulate.

#### Stretch — wrong letters list

Mechanical. Adds another tracking variable.

#### Extension — visual hangman

The ASCII art is mechanical (just strings with newlines).
Worth mentioning:

> "The `\\` is how you write a single backslash in a string.
> The `\` character is special in Python strings, so we
> escape it."

Don't get into general escape sequences. Just `\\` for one
backslash.

#### Extension++ — play again

Same outer-loop pattern as Session 7's number-guessing game.

### Common stumbles

- **`make_display` returns nothing.** Forgot `return` (Phase
  2 habit dies hard). Symptom: the printed display is `None`.
- **Win check before display update.** If win check uses an
  old `display` variable, it lags. Make sure `display` is
  recomputed each loop iteration.
- **Case sensitivity.** Kid types `"P"` but the word is
  `"python"`. The check `"P" in "python"` is False. Use
  `.lower()` on the input AND ensure the word list is
  lowercase.
- **`continue` vs `break` confusion.** `continue` skips to
  the next iteration; `break` exits the loop entirely. If a
  kid uses `break` for already-guessed, the game ends.
- **Forgot to remove the DEBUG print.** Game cheats. Same fix
  as Session 7.
- **`random.choice([])`** errors if the list is empty. Could
  happen if `words.txt` doesn't exist or is empty. Mention.
- **File path issues.** `open("words.txt")` looks in the
  current working directory. If words.txt is in a different
  folder, it fails. Easiest fix: put both files in the same
  folder.
- **List of all-guessed letters keeps growing.** That's
  intentional — we use it to detect already-guessed. Don't
  let kids "fix" this if they think it's a bug.

### Differentiation

- **Younger kids (9-10):** May find the full game challenging.
  Focus on Part A (the display function). If they get the
  display function working, that's a real win for today; the
  game loop can be next week's homework.
- **Older kids (12+):** Will probably finish the base game.
  Push them through file loading and at least one extension.
  If they finish: ask them to add a hint system (after N
  wrong guesses, reveal one letter for free).
- **Advanced (any age):** Will fly through. Push them to:
  - The visual hangman ASCII art
  - A proper play-again loop
  - Difficulty levels (different word lists, different
    max_wrong)
  - Categories with menu selection
- **Struggling:** A kid who can't get the display function
  working in Part A is the kid you focus on. Sit with them
  and use the debugger. Walk through what `display` is at
  each iteration. Once they have the function, the rest is
  mechanical.

### What to watch for

- **The "I built a real game" reaction.** Hangman is a
  recognized game; building one feels like a real
  accomplishment. Affirm.
- **Buddies playing each other's games.** Encourage. Real
  testing — they'll find edge cases the developer missed.
- **Kids adding their own words.** Personalization. Some
  kids will add silly words, biblical names, names of
  classmates. All good.
- **The "code separated from data" insight.** When kids
  realize they can edit `words.txt` without touching
  `hangman.py`, several get the "ohhh" moment.
- **Frustration with the display function logic.** This is
  the conceptually hardest part. Patience. Use the debugger.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 13 (next week, error handling).** The hangman game
  doesn't handle weird user input gracefully (typing a number,
  hitting Enter without a letter, etc.). Try/except will fix
  this.
- **Session 14 (text adventure or CSV reader).** A text
  adventure has the same shape as hangman — game state in
  variables, loop until done, commands change state. Same
  pattern, different specifics.
- **Sessions 15-16 (milestone + demo).** Today's hangman is a
  reasonable starting point for kids whose milestone idea
  isn't well-formed. They could clone the structure and adapt
  to a different game.
- **Phase 4 (intermediate Python).** Hangman could be
  refactored with classes (Game, Player, Word). Today's
  function-driven version is the foundation.
- **Phase 6 (Pygame).** A graphical hangman — same logic, but
  with sprites and mouse input. Today's mental model
  transfers directly.
- **Peanut butter callback opportunity:** the case-sensitivity
  bug ("P" vs "p") is a precision moment. The computer
  compared exactly what was typed; capital-P is not the same
  as lowercase-p; therefore not in the word.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Pre-built complete hangman (with file loading) for
      destination preview
- [ ] Optional: pre-prepared `words.txt` file
- [ ] Projector (essential — long session, lots to walk through)
- [ ] Class roster
