## Session 7: Number-guessing game

*Phase 3 — Python basics · Session 7 of 16*

### What we're learning today

Today we put together everything from Sessions 1-6 into your
**first real Python game**. The computer thinks of a secret
number; you have to guess it; the computer tells you "too high"
or "too low" until you get it right. By the end of class, you'll
have a game you can play (and have your friends play) — built
entirely from the building blocks you've already learned.

### You'll need to remember from last time

- **`print` and `input`** for output and asking the user.
- **`int(input(...))`** to get a number from the user.
- **`if/elif/else`** for branching.
- **`while` loops** for "until something is true."
- **`break`** to exit a loop early.
- **f-strings** for output with variables.

That's pretty much everything. Today is integration.

---

### Part A: Build the basic game

Open Thonny and start a new file. Save it as `guessing_game.py`.

#### The plan

Before writing any code, talk through what the game does:

1. The computer picks a secret number between 1 and 100.
2. The user guesses a number.
3. If the guess is too low, say so. If too high, say so. If
   correct, celebrate and stop.
4. Repeat from step 2 until the user gets it right.

That's three new things to learn (random numbers, comparing
guesses, looping until correct) plus stuff you already know
(input, print, conditionals).

#### Step 1: Random numbers

To pick a random number, we use Python's `random` module:

```python
import random

secret = random.randint(1, 100)
print(secret)   # for testing — we'll remove this later
```

`import random` brings in the random module (just like `import
turtle` did in Phase 2). `random.randint(1, 100)` returns a
random whole number from 1 to 100, including both ends.

Save and run a few times. Each run gives a different number.

The `print(secret)` is just so we can see it during development.
We'll remove it for the actual game.

#### Step 2: Get a guess

```python
import random

secret = random.randint(1, 100)
print(secret)   # for testing

guess = int(input("Guess a number from 1 to 100: "))
print(f"You guessed {guess}.")
```

Run. Type a number when prompted. The program echoes it back.

Familiar from Session 2's `int(input(...))` pattern.

#### Step 3: Compare and respond

```python
import random

secret = random.randint(1, 100)
print(secret)

guess = int(input("Guess a number from 1 to 100: "))

if guess < secret:
    print("Too low!")
elif guess > secret:
    print("Too high!")
else:
    print("You got it!")
```

Run. Now the program tells you if your guess was too high, too
low, or correct.

But there's a problem: the program runs the input only *once*.
You guess wrong, the program ends. Time to add a loop.

#### Step 4: Loop until correct

We want to keep asking until the user guesses right. That's a
classic `while` loop pattern from Session 5.

```python
import random

secret = random.randint(1, 100)
print(secret)   # for testing

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it!")
        break
```

The `while True:` loop runs forever until `break`. Inside, we
ask, compare, and either keep going or break out.

Save and run. Try to guess. Keep going until you get it right.
The program ends when you do.

#### Step 5: Remove the cheating print

Now that the game works, remove (or comment out) the
`print(secret)` line at the top. The user shouldn't see the
secret!

```python
import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it!")
        break
```

That's the **base game.** A complete, playable
number-guessing game in 11 lines of Python.

**Checkpoint:** *You have a working number-guessing game that
generates a random number, asks for guesses, and tells the user
when they're right (or whether they're too high/too low).*
**This is the natural stop point if class is cut short.**

---

### Part B: Make it a real game

The base game works but is bare. Let's add features.

#### Stretch — count attempts

Players want to know how well they did. Count attempts:

```python
import random

secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"You got it in {attempts} tries!")
        break
```

The variable `attempts` starts at 0, increases with each guess,
and the final message uses it.

Try it. How few attempts can you do? (With perfect binary
search — guess 50, then 25 or 75, etc. — you can always win in
7 or fewer tries for a number from 1 to 100.)

#### Extension — limited tries

Add a lose condition: the user gets only N attempts. If they
run out, the computer wins.

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_tries = 10
won = False

print(f"I'm thinking of a number between 1 and 100. You have {max_tries} tries.")

while attempts < max_tries:
    attempts = attempts + 1
    guess = int(input(f"Try {attempts}/{max_tries}: "))
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"You got it in {attempts} tries!")
        won = True
        break

if not won:
    print(f"You ran out of tries! The number was {secret}.")
```

What's new:

- `max_tries = 10` — the limit, in a variable so it's easy to
  change.
- `won = False` — a boolean to track whether the user won.
- `while attempts < max_tries:` — loop condition includes the
  attempt counter.
- After the loop, an `if not won:` to handle the lose case.

Now the game is genuinely competitive — there's a chance to
lose.

#### Extension — play again

Wrap the whole game in another loop so the user can play
again:

```python
import random

while True:
    # ... (the entire game from above) ...
    
    again = input("\nPlay again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing!")
        break
```

Now after the game ends (win or lose), the user is asked if
they want another round. If they type "y" (or "Y"), another
game starts. Anything else and the program quits.

That's a *play loop* — common pattern in real games.

#### Extension++ — a clean version with functions

If you've finished everything else, refactor the game into
functions:

```python
import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_tries = 10
    
    print(f"I'm thinking of a number between 1 and 100. You have {max_tries} tries.")
    
    while attempts < max_tries:
        attempts = attempts + 1
        guess = int(input(f"Try {attempts}/{max_tries}: "))
        
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {attempts} tries!")
            return True
    
    print(f"You ran out of tries! The number was {secret}.")
    return False

# main loop
while True:
    play_game()
    again = input("\nPlay again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing!")
        break
```

The whole game is in one function (`play_game`). The function
returns `True` if the user won and `False` if they lost (we
don't actually use the return value here, but it's good
practice). The main code is just two lines: play, ask if they
want to play again.

This is how real games are organized — small functions for each
piece, a simple top-level loop calling them.

---

### Wrap-up

Before we leave, share with the room:

- What's the *fewest* tries anyone got the number in?
- For the kids who built the limited-tries version — did anyone
  lose? Did the lose message work right?
- For the kids who refactored into functions — did the code feel
  cleaner?

You built a complete game today. **A complete game.** With
random elements, user input, win and lose conditions, optional
replay. That's the same shape as a thousand commercial puzzle
games — yours is just simpler.

Most importantly, you built it from **stuff you already knew.**
No new programming concepts, just a new combination. This is
what programming starts to feel like once you have the
fundamentals: you take the parts you know and arrange them into
something new.

### If you missed this session

Open Thonny and start a new file. Save as `guessing_game.py`.
Then build the game step by step:

1. `import random` and `secret = random.randint(1, 100)`. Print
   secret while testing.
2. Ask for a guess with `int(input(...))`.
3. Compare with `if/elif/else`. Print "too high" / "too low" /
   "correct."
4. Wrap in a `while True:` loop with a `break` on the correct
   guess.
5. Remove the print(secret) once it works.

About 30-40 minutes for the base game. Then try adding attempt
counting (Part B stretch). If you have time, try the limited
tries or play-again extensions.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- **Hint system** — if the guess is within 5 of the secret,
  print "Very close!" instead of just "too high/too low."
- **Difficulty levels** — at the start, ask "easy / medium /
  hard?" Each one uses a different range (1-50, 1-100, 1-500)
  or different max tries (15 / 10 / 5).
- **Track best score** — across multiple games, remember the
  fewest tries it took to win.
- **Reverse the game** — the *user* picks a number, and the
  computer guesses (using binary search). Trickier — give it a
  shot if you're feeling ambitious.

### What's next

Next week we learn about **lists** — Python's way of holding
*multiple values* in a single variable. Lists are arguably the
most important data structure in all of Python; they unlock a
huge range of programs you couldn't write before.
