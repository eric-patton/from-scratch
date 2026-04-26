## Session 12: Hangman — a complete game

*Phase 3 — Python basics · Session 12 of 16*

### What we're learning today

Today we build the **biggest Phase 3 project so far** — a
complete game of **hangman**. The computer picks a secret word;
you guess letters one at a time; if you guess too many wrong,
you lose. By the end of class, you'll have a working game that
uses *every* idea you've learned in Phase 3 — input/output,
strings, lists, conditionals, loops, functions, file I/O.

### You'll need to remember from last time

- **Lists** — `[]`, `.append()`, indexing, `in`.
- **Strings** — indexing, `for letter in word:`, `.lower()`.
- **`while True:` and `break`** for game loops.
- **Functions with return values** — Session 6.
- **`import random` and `random.choice(...)`** — picks a
  random item from a list.
- **`with open(filename) as f:`** — reading from a file.

---

### Part A: Build the display

Open Thonny and start a new file. Save it as `hangman.py`.

#### The plan

Hangman:

1. The computer picks a secret word.
2. The user sees the word with `_` for letters they haven't
   guessed.
3. The user guesses one letter at a time.
4. If the letter is in the word, fill in the blanks.
5. If not, count it as a wrong guess.
6. Win when all letters are filled in. Lose after too many
   wrong guesses.

We'll build it in steps.

#### Step 1: Pick a word

```python
import random

words = ["python", "scratch", "turtle", "function", "variable", "computer"]
secret = random.choice(words)
print(f"DEBUG: secret is {secret}")
```

`random.choice(words)` picks one item from the list at random.
We're printing the secret while developing — we'll remove it
later, like in Session 7.

Run a few times. Each time, a different secret word.

#### Step 2: Show the word with blanks

The display should show one `_` for each letter that hasn't
been guessed. Right now, no letters have been guessed. So:

```python
import random

words = ["python", "scratch", "turtle", "function", "variable", "computer"]
secret = random.choice(words)
guessed_letters = []

# build the display
display = ""
for letter in secret:
    if letter in guessed_letters:
        display = display + letter
    else:
        display = display + "_"

print(f"Word: {display}")
```

Walk through:

- `guessed_letters = []` — empty list of letters guessed so far
  (none yet).
- For each letter in the secret word, if it's been guessed,
  show it. Otherwise show `_`.
- Build up the `display` string letter by letter.

Run. The display should be all underscores — like `______` for
"python."

#### Step 3: Make it a function

The "build the display" code will run multiple times (every
time the user guesses). Pull it into a function:

```python
def make_display(secret, guessed_letters):
    display = ""
    for letter in secret:
        if letter in guessed_letters:
            display = display + letter
        else:
            display = display + "_"
    return display

# test it
print(make_display("python", []))                # ______
print(make_display("python", ["p", "n"]))        # p____n
print(make_display("python", ["p", "y", "t", "h", "o", "n"]))   # python
```

Now `make_display` is a reusable function that takes the secret
and the list of guessed letters, and returns the display
string. Test it with different inputs to be sure.

**Checkpoint:** *You've built a `make_display` function and
tested it with different combinations of secret words and
guessed letters.* **This is the natural stop point if class is
cut short.**

---

### Part B: The full game loop

Now we add input, the game loop, win and lose conditions.

#### Step 4: The game loop

```python
import random

def make_display(secret, guessed_letters):
    display = ""
    for letter in secret:
        if letter in guessed_letters:
            display = display + letter
        else:
            display = display + "_"
    return display

# setup
words = ["python", "scratch", "turtle", "function", "variable", "computer"]
secret = random.choice(words)
guessed_letters = []
wrong_count = 0
max_wrong = 6

# game loop
while True:
    display = make_display(secret, guessed_letters)
    print(f"\nWord: {display}")
    print(f"Guessed: {guessed_letters}")
    print(f"Wrong: {wrong_count}/{max_wrong}")
    
    # win check
    if display == secret:
        print(f"You won! The word was {secret}.")
        break
    
    # lose check
    if wrong_count >= max_wrong:
        print(f"You lose! The word was {secret}.")
        break
    
    # get a guess
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in secret:
        print("Good guess!")
    else:
        wrong_count = wrong_count + 1
        print("Wrong!")
```

Save. Run. Play.

Walk through what's new:

- `wrong_count = 0` and `max_wrong = 6` — track how many wrong
  guesses, with a limit.
- The `while True:` loop with `break` for both win and lose.
- `display = make_display(...)` recomputes each loop.
- **Win check**: `if display == secret:` — once the display
  has no more underscores, all letters are guessed.
- **Lose check**: `if wrong_count >= max_wrong:` — used too
  many guesses.
- **Get a guess**: `.lower()` to make the comparison
  case-insensitive.
- **Already guessed**: check before adding; `continue` skips
  the rest of this iteration and goes back to the top of the
  loop.
- **Track wrong guesses**: only increment if the letter isn't
  in the word.

That's the **base game** — a complete, playable hangman.

#### Step 5: Words from a file

Right now the word list is hardcoded. Let's load it from a
file (callback to Session 11!).

First, create a file `words.txt` (in the same folder as
`hangman.py`) with a few words, one per line:

```
python
scratch
turtle
function
variable
computer
keyboard
monitor
```

(Actually create this file in Thonny, save as `words.txt`. Or
write a quick one-time program to create it.)

Then in `hangman.py`, replace the hardcoded list:

```python
# load words from file
words = []
with open("words.txt", "r") as f:
    for line in f:
        word = line.strip()
        if word:    # skip blank lines
            words.append(word)

secret = random.choice(words)
```

Now the word list lives in `words.txt`. To add or change words,
edit the file — no need to touch the Python code.

This is the base + file enhancement. **Most real games and
apps work this way** — the data lives in files, the code lives
in code, they're separate.

#### Stretch — show the wrong letters

Currently, `guessed_letters` shows ALL letters guessed (right
and wrong mixed together). Show *just* the wrong ones for
clarity:

```python
wrong_letters = []

# inside the loop, replace the wrong-guess block:
if guess in secret:
    print("Good guess!")
else:
    wrong_count = wrong_count + 1
    wrong_letters.append(guess)
    print("Wrong!")

# update the display each round:
print(f"Wrong letters: {wrong_letters}")
```

Two lists now — one for all guessed (to avoid duplicates), one
for just the wrong ones (for display).

#### Extension — visual hangman

Add ASCII art that shows the "hangman" stick figure progressing
as wrong guesses pile up. Build a function that returns the
right picture for the wrong count:

```python
def make_hangman(wrong_count):
    if wrong_count == 0:
        return ""
    elif wrong_count == 1:
        return "  O"
    elif wrong_count == 2:
        return "  O\n  |"
    elif wrong_count == 3:
        return "  O\n /|"
    elif wrong_count == 4:
        return "  O\n /|\\"
    elif wrong_count == 5:
        return "  O\n /|\\\n /"
    else:
        return "  O\n /|\\\n / \\"

# call it inside the loop:
print(make_hangman(wrong_count))
```

The `\n` makes the picture span multiple lines. The `\\` is an
escaped backslash. (To print one `\`, you write `\\` in the
string.)

#### Extension++ — play again loop

Wrap the whole game in another loop so the user can play
multiple times (callback to Session 7's number-guessing game).

```python
while True:
    # ... entire game ...
    
    again = input("\nPlay again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing!")
        break
```

---

### Wrap-up

Before we leave, share with the room:

- For the kids who finished the base game — what's the
  hardest word you've had?
- For the kids who added words to the file — how many do you
  have?
- For the visual-hangman extension — does the figure look
  right?

You built a **complete game** today. Hangman uses *every
concept from Phase 3 so far* — print, input, types, strings,
conditionals, loops, functions, lists, and (with the file
extension) file I/O. That's not nothing.

You also encountered a key real-world pattern: **data and code
separated.** The words list lives in a text file; the game
logic lives in Python. To change the words, you don't touch
the code. This separation is how almost all real software is
organized.

### If you missed this session

Open Thonny and start a new file. Save as `hangman.py`. Then:

1. Build the `make_display(secret, guessed_letters)` function
   from Part A. Test it with a few inputs.

2. Add the game loop from Part B (Step 4) — `while True:`,
   win check, lose check, get guess, track wrong count.

3. Play it. Get the hardcoded version working before trying
   to load words from a file.

4. Optionally: create a `words.txt` file with a list of words
   and load it (Step 5).

About 50-60 minutes — this is a long session. If you get stuck,
ask your buddy at the start of next class.

### Stretch and extension ideas

- **Difficulty levels** — different word lists for easy/medium/
  hard, or different `max_wrong` values.
- **Categories** — words organized by category (animals,
  colors, programming terms). User picks a category.
- **Two-player mode** — one player enters a word, the other
  guesses. (Tricky: hide the word as it's typed.)
- **Save high scores to a file** — fewest wrong guesses, best
  word completion, etc.

### What's next

Next week we learn **error handling** — `try/except` for
making programs that don't crash when the user types something
unexpected. You've already seen one `try/except` in Session
11; next week we'll cover it properly and use it to make your
programs robust.
