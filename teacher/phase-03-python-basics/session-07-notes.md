## Session 7 — Teacher Notes

*Phase 3, Python basics · Session 7 of 16 · Title: Number-
guessing game*

### Purpose of this session

The first real text-based game in Phase 3. Same role as Phase 1
Session 7 (Apples and Rocks) and Phase 2 Session 7 (garden
scene): synthesis. Five jobs, in priority order:

1. **Demonstrate that students can build a complete game from
   the toolkit they have.** No new programming concepts. Today
   shows the cumulative power of Sessions 1-6.
2. **Introduce `import random`.** Genuinely new (we used
   `import turtle` in Phase 2 but that was the only import).
   Today's `random.randint(1, 100)` is the first time `import`
   serves a real practical purpose in Phase 3.
3. **Practice the build-incrementally pattern.** Walk through
   the game in five small steps, each one runnable and testable.
   Models how real programs get built — small additions, each
   verified before the next.
4. **Demonstrate the `print(secret) for testing` pattern.**
   Real-world debugging trick: print intermediate values while
   developing, remove (or comment out) before shipping. Models
   professional practice.
5. **Set up Session 8 (lists).** The number-guessing game has
   *one* secret number. Next week's lists let you have many
   things at once — perfect setup for "now what if you wanted to
   track all the previous guesses?"

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Pre-built complete game (with attempt counter and limited
  tries) ready to demo as the destination preview.
- Verify `import random` works on at least one student machine.
  (It's stdlib; should always work.)

**Prep time:** ~15 minutes. Build the game once, play it twice.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was return values.
  Anyone use the debugger again at home?
- **Part A: build the game** (~50 min) — the plan ~3 min,
  random numbers ~5 min, get a guess ~5 min, compare ~10 min,
  loop until correct ~15 min, remove the cheating print ~2
  min, checkpoint ~10 min.
- **Break** (~5 min).
- **Part B: features** (~25 min) — attempt counter (stretch)
  ~10 min, limited tries or play-again (extension) ~15 min.
- **Wrap-up** (~5 min).

If running short, **the function-refactor extension++ can be
cut.** The base game + attempt counter is the goal.

### Teaching Part A

#### Open with the destination

Show the finished game (with limited tries and play-again) on
the projector. Play it. Lose intentionally so kids see the
"out of tries" message. Play again to win.

> "By the end of class, you'll have built this. Plus, the
> entire thing is built from stuff you already know. Let's go."

#### The plan-it-first move

Walk through the four-step plan at the projector or whiteboard
**before any code:**

1. Computer picks a secret number.
2. User guesses.
3. Compare and respond.
4. Repeat until correct.

This is the decomposition habit. Goal #1 of the curriculum.
Make it explicit:

> "Before we type a single line, we know what we're building.
> Each of these four steps becomes a few lines of code. We'll
> build them in order."

#### Step 1: random

The `import random` is the new piece. Frame it:

> "We've used `import` once before — `import turtle` in Phase 2.
> Today we use a different module — `random`. It's another
> Python toolbox; this one helps with random numbers."

Walk through `random.randint(1, 100)`. Note the inclusive-
both-ends behavior — both 1 and 100 are possible.

The `print(secret)` for testing is a *deliberate* teaching
moment:

> "We're going to print the secret to the screen — even though
> the user shouldn't see it — because we're testing right now.
> Real programmers do this all the time during development:
> add temporary print statements to see what's happening, then
> remove them before sharing the code. We'll remove it at the
> end."

This models pro debugging practice early. Worth naming.

#### Steps 2-3: input and compare

Mechanical. Familiar from previous sessions. The interesting
part is the order:

```python
if guess < secret:
    print("Too low!")
elif guess > secret:
    print("Too high!")
else:
    print("You got it!")
```

The `else` catches the equal case implicitly — if it's not <
and not >, it must be ==. Worth pointing out:

> "We don't have to write `elif guess == secret:` because the
> only remaining possibility is equal. The else covers it."

#### Step 4: the loop

The `while True:` + `break` pattern is the canonical "loop
until something happens" idiom. Walk through:

> "We want to keep asking until they guess right. We don't
> know how many guesses that'll take, so a `for` loop with a
> fixed count is wrong. A `while True:` loops forever — and we
> use `break` to exit when we're done."

Some kids will try `while guess != secret:` instead. That also
works! Walk through:

```python
guess = -1   # something that's definitely not the secret
while guess != secret:
    guess = int(input(...))
    ...
```

The `while True / break` version is generally preferred (fewer
"sentinel" variables to worry about), but both are valid.
Don't be religious; whichever a kid lands on naturally is
fine.

#### Step 5: remove the cheating print

> "Now we play the game ourselves. But — the print at the top
> still shows the secret. That's only useful while testing.
> We remove it now."

Comment it out (`# print(secret)`) or delete it. Run again,
play normally. The game works.

This is the moment they shift from "testing builders" to
"actual users." Make it concrete.

### Teaching Part B

#### Attempt counter

The first feature add. Mechanical:

- New variable `attempts = 0` outside the loop.
- `attempts = attempts + 1` inside the loop body.
- Final message uses `{attempts}` in the f-string.

Have students try it. Then play. The "best guess in 5 tries!"
moment is satisfying.

#### Limited tries (extension)

This adds a lose condition, which makes the game *real*. Two
new variables (`max_tries`, `won`), changed `while` condition,
and an after-loop check.

Walk through the new control flow at the projector:

> "The loop runs while attempts is less than max. Inside, we
> increment, ask, compare. If they win, set `won = True` and
> break. After the loop ends — either because they won and
> broke, or because they used all attempts — we check: did
> they win? If not, reveal the answer."

The `won = False` then `won = True` then check pattern is the
classic "did the loop succeed?" idiom. Worth naming.

#### Play again (extension)

The outer `while True:` wrap with a "play again?" prompt at
the end is mechanical. Just be careful about indentation —
the entire previous game (including the inner while loop)
needs to be inside the outer one.

Some kids will struggle with the indentation. Let them.

#### Function refactor (extension++)

For the kids who finish everything else. Wrap the entire
game in `def play_game():`. Returns `True` or `False`. Main
loop just calls it.

This is real Python style. Worth showing if anyone gets there
— for everyone else, save it as a Phase 4+ topic.

### Common stumbles

- **Forgot `import random`.** NameError on `random.randint`.
  Easy fix.
- **`random.randint(1, 100)` returns 100 sometimes** — yes,
  both ends are inclusive. If a kid is surprised, mention this.
- **Forgot `int(input(...))`.** Comparing a string to an int
  is always false (or worse — different types compare in
  unintuitive ways). Symptom: every guess is "too low" or
  errors out.
- **Forgot `break`.** Loop runs forever even after the right
  guess. Symptom: keeps asking even though they got it.
- **`break` at wrong indent level.** Has to be inside the
  `else:` branch (where the correct guess is detected). If
  it's outside the `if/elif/else`, it breaks the loop on every
  guess.
- **Removed `print(secret)` but the program still cheats** —
  if a kid printed `secret` somewhere else by mistake. Search
  for any other reference.
- **Played-again prompt loops infinitely** — usually a missing
  `break` or wrong indentation. Walk through.
- **Counter variable defined inside the loop.** `attempts = 0`
  inside the loop resets it every iteration. Move outside.

### Differentiation

- **Younger kids (9-10):** May find the cumulative integration
  challenging. Don't worry about Part B's extensions for them
  — getting the base game working is plenty.
- **Older kids (12+):** Will move quickly through base + stretch.
  Push them to limited-tries and play-again.
- **Advanced (any age):** Will finish all extensions. Push them
  to the function refactor (extension++). Or suggest:
  - Difficulty levels (variable for `max_tries` and range)
  - Hint system ("very close!" if within N of secret)
  - Reverse the game (computer guesses, user says higher/lower)
- **Struggling:** A kid who can't get the basic game working
  is the kid you focus on. Most common cause: indentation in
  the `while/if/else` nesting. Walk through it carefully. Use
  the debugger if needed.

### What to watch for

- **The "wait, I built this entirely from things I knew?"
  realization.** Several kids will visibly process this. Affirm
  loudly. This is the cumulative power of the curriculum
  showing up.
- **Buddies playing each other's games.** Encourage. Friendly
  competition over fewest-tries is great.
- **Kids who add their own touches** (silly variable names,
  funny messages, extra features). Encourage. Personalization
  is goal-2 in action.
- **The "I want to keep working on this" moment.** Several kids
  will want to take this game home and add stuff. Encourage.
  Tell them to bring their improved version next week.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 8 (next week, lists).** Today's game has *one*
  secret number. Next week introduces lists; you can have many
  things at once — including, e.g., remembering all previous
  guesses.
- **Session 12 (hangman).** Same general structure as today —
  game state in variables, while loop until done, win/lose
  conditions. Hangman just has more state (the word, the
  guessed letters).
- **Phase 4 (CLI tools).** This game *is* a CLI tool —
  text-based, runs from a terminal. Today is the prototype for
  the more elaborate tools in Phase 4.
- **Phase 6 (Pygame).** Translate today's game into Pygame:
  same logic, graphical input/output. Same `import` pattern,
  same game loop structure, just with sprites instead of text.
- **The peanut butter callback opportunity:** the "forgot to
  break, loop never ends" bug is a precision moment. The
  computer did exactly what you said; you didn't tell it to
  stop, so it didn't.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Pre-built finished game (limited tries + play-again) for
      destination preview
- [ ] Projector (helpful for the step-by-step build)
- [ ] Class roster
