## Session 1: Welcome to Python (without the turtle)

*Phase 3 — Python basics · Session 1 of 16*

### What we're learning today

Phase 2 used the turtle to give your code something visual to
do. Phase 3 leaves the turtle behind. Today we'll learn the two
most-used commands in all of Python: **`print`** (Python tells
you something) and **`input`** (Python asks you something). By
the end of class, you'll have written a program that talks to
the person running it.

### You'll need to remember from last time

- **Thonny.** Open the editor, type code, save with `.py`, click
  the green Run button.
- **Variables.** `name = "Sam"` puts the value `"Sam"` in a
  variable called `name`.
- **The peanut butter rule.** Still in effect. Maybe even more
  in effect today.
- **You finished Phase 2.** You wrote real Python code with
  functions, loops, conditionals, all of it. Today builds on
  that.

---

### Part A: A familiar friend (and `print`)

You may notice **Mr. Eric brought the bread back today.** Loaf,
peanut butter, jelly, knife, plate. The whole setup from Session
1 of Phase 1.

Same exercise: tell Mr. Eric how to make a peanut butter and
jelly sandwich, step by step. He'll do exactly what you say.

But notice: **you're way better at this now.** Eighteen weeks
ago, the room couldn't even get past "open the peanut butter."
Today, the instructions are tighter, more careful. Some of you
are already saying things like "grab the handle of the knife
between your thumb and forefinger" without being prompted.

That's not nothing. **Programming has changed how you give
instructions.** You think about steps differently. You notice
when something is ambiguous. That's a skill you'll have for the
rest of your life.

#### Why we're doing it again now

For all of Phase 2, the turtle was your safety net. If your code
was wrong, the visual feedback told you immediately — "the
square's lopsided" or "the turtle went off-screen." Today the
turtle goes away. We're using just text.

That means the **peanut butter rule matters even more.** With
text, mistakes are quieter. A missing letter, a missing colon, a
typo in a variable name — and your program either crashes or
quietly does the wrong thing. There's no visual to clue you in.

Today you start writing programs that talk to people. People
expect their programs to work. That puts more pressure on you to
be precise. Welcome to real programming.

#### Hello, world

Open Thonny. Start a new file. Save it as `hello.py`.

Type just one line:

```python
print("Hello, world!")
```

Save. Run.

Look at the **shell** at the bottom of Thonny. You should see:

```
Hello, world!
```

That's it. That's your first non-turtle Python program.

What's different from Phase 2:

- No `import turtle`. We're not using the turtle today.
- No `t = turtle.Turtle()`. No turtle.
- Output goes to the **shell** at the bottom, not to a separate
  drawing window.

Try a few more `print` calls:

```python
print("Hello, world!")
print("My name is", "your name here")
print("Five plus three is", 5 + 3)
print("Three tens is", 10 * 3)
```

Save. Run.

Each `print` call shows up on its own line in the shell.

Notice that `print` can take **multiple things separated by
commas**. Each thing gets printed with a space between. Numbers
don't need quotes (they're values); text needs quotes (it's a
string).

> "Writing 'Hello, world!' as your first program is a tradition.
> Every programming language ever has a 'hello world' program.
> You just joined that tradition."

**Checkpoint:** *You have a Python file that prints at least
three different lines to the shell when you run it.* **This is
the natural stop point if class is cut short.**

---

### Part B: Asking the user something

Now the other half — `input`. This is how a program asks the
user a question and gets their answer.

#### Your first interactive program

Replace your code with this:

```python
name = input("What's your name? ")
print("Hello, " + name + "!")
```

Save. Run.

Watch the shell. You'll see:

```
What's your name?
```

…and then nothing happens. The program is **waiting for you.**

Type your name and press Enter. Now:

```
What's your name? Sam
Hello, Sam!
```

Walk through what happened:

- `input("What's your name? ")` — printed the prompt, waited for
  the user to type and press Enter, then *returned* what the
  user typed.
- `name = input(...)` — saved what the user typed in a variable
  called `name`.
- `print("Hello, " + name + "!")` — used the variable in the
  output.

The `+` between strings is **string concatenation** — a fancy
word for "stick them together." `"Hello, " + "Sam" + "!"` becomes
`"Hello, Sam!"`. Like joining links in a chain.

#### Multi-question version

Try this — a longer version that asks multiple things:

```python
name = input("What's your name? ")
color = input("What's your favorite color? ")
food = input("What's your favorite food? ")

print("Nice to meet you, " + name + "!")
print("Did you know that " + color + " " + food + " is delicious?")
```

Run it. Type three answers. The program echoes back a sentence
about you.

Yes, the sentences are absurd. That's the fun part.

#### Try this on your own

Pick one:

- **Base goal:** Build a multi-question program that asks at
  least four things and uses all the answers in some output.
  Make the questions whatever you want — favorite Bible verse,
  favorite hymn, where you'd like to travel, what you ate for
  breakfast.

- **Stretch:** Use a conditional (callback to Phase 2 Session
  6!) to react to one of the answers:

  ```python
  color = input("What's your favorite color? ")
  if color == "blue":
      print("Great choice!")
  else:
      print("That's a fine color too, but blue is the best.")
  ```

  Try this for one or two of your questions.

- **Extension:** Wrap a greeting in a function (callback to
  Phase 2 Session 4!):

  ```python
  def greet(name):
      print("Hello, " + name + "!")
      print("Welcome to Python.")

  your_name = input("What's your name? ")
  greet(your_name)
  ```

  Now you've combined input + functions + variables in one tiny
  program.

---

### Wrap-up

Before we leave, share with the room:

- What questions did your program ask?
- Did anyone get a particularly weird sentence in their output?
- For the kids who did the conditional stretch — did the
  computer agree with your favorite color?

You learned today how to make programs **talk to people.** Every
website that asks for a username, every game that asks "would
you like to start a new game?", every spreadsheet that prompts
"are you sure you want to delete?" — they're all doing what
your program did today. Just at bigger scale, with prettier
graphics. The core mechanic is the same: print a question, wait
for input, do something with the answer.

The turtle was a fun way to learn. Text is how most software
actually works under the hood.

### If you missed this session

Open Thonny and start a new file. Save it as `hello.py`. Then:

1. Type `print("Hello, world!")`. Save. Run. Look at the shell at
   the bottom — your message appears.

2. Add a few more `print` lines with different text or
   simple math.

3. Now try `input`:
   ```python
   name = input("What's your name? ")
   print("Hi, " + name + "!")
   ```
   Save. Run. Type your name when prompted.

4. Build a multi-question version (the Part B base goal above).

About 30 minutes. If anything's confusing, ask your buddy at the
start of next class.

### Stretch and extension ideas

- The user can also enter numbers, but `input()` always returns
  a **string** even if they type a number. To do math with the
  number, you need to convert it: `age = int(input("How old are
  you? "))`. We'll talk about why next week — try it for now.
- `input()` will also work with no prompt: `answer = input()`
  — but it's confusing for the user (they don't know what to
  type). Always pass a prompt.
- `print` with no arguments — `print()` — outputs a blank line.
  Useful for spacing your output.

### What's next

Next week we formalize **variables and types** — what's the
difference between `42`, `42.0`, and `"42"`, and why does it
matter? (Spoiler: this is the answer to "why does `input()` give
me a string when I typed a number.")
