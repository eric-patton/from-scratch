## Session 1 — Teacher Notes

*Phase 3, Python basics · Session 1 of 16 · Title: Welcome to
Python (without the turtle)*

### Purpose of this session

The third major transition session in the curriculum (after Phase
1 Session 1 and Phase 2 Session 1). The leap is from "visual
turtle output" to "text in a shell." Five jobs, in priority
order:

1. **Run the planned PB&J callback.** This is locked in
   CURRICULUM-DECISIONS.md and CLAUDE.md as Phase 3 Session 1's
   opener. Bring the bread. The frame is "you've grown — now
   precision matters even more because we're losing visual
   feedback."
2. **Land `print` and `input`.** Both are mechanically simple
   but conceptually new in this context. `input()` is a
   genuinely new mechanic (program *waits* for user; user
   responds; program *resumes*).
3. **Acclimate students to text-only output.** Several kids
   will miss the turtle. Frame the change positively: "this is
   how most real software works." Don't let nostalgia for the
   turtle become a problem.
4. **Reset the typing-precision discipline.** Phase 2 trained
   them on Python typing, but with the turtle they got visual
   feedback when something was off. Without the turtle, mistakes
   are quieter. Land that mid-session: "the peanut butter rule
   matters more today, not less."
5. **Start using the shell.** The shell is where output goes,
   where errors appear, and where they can experiment quickly.
   Today is when it stops being "that thing at the bottom" and
   becomes "the place programs talk to me."

### Before class

**Bring:**

- Loaf of bread (sliced)
- Jar of peanut butter
- Jar of jelly
- Butter knife
- A plate
- Napkins / paper towels
- A comb (or whatever absurd "spreading tool" you used in Phase 1
  Session 1) — the same prop, returning for the callback
- A trash bag for cleanup

**Set up:**

- Demo machine with Thonny open. Have an empty editor and the
  shell visible.
- Verify Thonny still works on every student machine. Should be
  fine; sanity check anyway.
- Pre-test that `input()` works as expected on at least one
  W202NA. The shell should show the prompt and wait for input.

**Prep time:** ~25 minutes including the grocery run.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and frame** (~5 min) — quick "Phase 2 is done, today
  we shift" intro.
- **Part A: PB&J callback + print** (~40 min) — the PB&J
  callback ~15 min, framing why we're doing it again ~5 min,
  hello world + print exercises ~15 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: input** (~35 min) — the first input demo ~10 min,
  multi-question program ~10 min, free build (base/stretch/
  extension) ~15 min.
- **Wrap-up** (~5 min).

The PB&J callback is shorter than Phase 1 Session 1's original
demo (which ran ~25-30 min). Today is more like 10-15 min — they
already get the lesson; the point is the *callback*, not a
re-teach.

If running short, **the free build at the end of Part B is the
cuttable piece.** The PB&J callback and the basic
print + input exercises are the session.

### Teaching Part A

#### The PB&J callback

This is the planned moment. Set it up properly:

> "Today is the start of Phase 3 — Python without the turtle.
> Before we start, I need a sandwich. Help me out."

Bring out the bread, etc. Run the same exercise as Phase 1
Session 1: students give instructions, you execute literally.

**But notice the difference.** They will be *much better* than
they were 18 weeks ago. The instructions will be tighter. They
might pre-emptively name assumptions. The room will laugh
faster, more knowingly.

When the demo wraps (5-10 minutes is plenty — don't milk it),
mark the moment:

> "Look how much better you are at this. Eighteen weeks ago you
> couldn't even open the peanut butter. Today you're pre-empting
> assumptions before I have to fail at them. Programming has
> taught you how to give instructions. That's not nothing."

Then the pivot:

> "Here's why we're doing this today. For all of Phase 2, the
> turtle was your safety net. If your code was wrong, the
> turtle drew the wrong thing — visual feedback. Today the
> turtle is gone. From now on, the *only* feedback you have is
> what your program prints, plus error messages. The peanut
> butter rule matters MORE in Phase 3, not less. Let's begin."

That transition is the lesson of the callback. Land it cleanly.

#### Hello world

After the callback, the technical content is fast. Demo at the
projector:

- Open a new file in Thonny.
- Type `print("Hello, world!")`.
- Save as `hello.py`.
- Run.
- Point at the shell: "see, your message showed up here."

> "This is the part of Thonny you've been ignoring for two
> phases. Now it matters. The shell is where your program talks
> to you when there's no turtle."

Have students do the same. Then explore variations:

- `print` with multiple arguments separated by commas
- `print` with math: `print("Five plus three:", 5 + 3)`
- Multiple `print` calls on different lines

The "comma between things in print" mechanic is worth pointing
out — they can mix strings and numbers freely. The space between
items in the output is automatic.

### Teaching Part B

#### The first input

Demo at the projector:

```python
name = input("What's your name? ")
print("Hello, " + name + "!")
```

Run it. Type your name when prompted. Show the result.

Walk through:

- The prompt appears in the shell.
- The program *pauses* — that's new. Until now, programs ran
  top to bottom without stopping.
- After Enter, the program continues with the input value.
- The result is saved in `name` — a variable, just like always.

The `+` for string concatenation is the new syntax. Demo:

```python
print("Hello" + "World")    # "HelloWorld"
print("Hello, " + "World")  # "Hello, World"
```

You have to include the spaces yourself. `+` doesn't add spaces.

Also note: you can't `+` a number and a string (`"Hello" + 5`
would error). Strings combine with strings; numbers combine with
numbers; mixing them needs conversion (which is next week's
topic). For today, keep everything as strings.

#### Multi-question

The multi-question program is mechanical. Have students build
their own version with their own questions. Encourage
personalization — favorite Bible verse, favorite hymn, what they
ate for breakfast, anything that makes their program theirs.

#### Stretch — conditional

The conditional stretch reuses Phase 2 Session 6's `if/else`
syntax. Worth pointing out:

> "Notice — we're using `if` and `else` from Phase 2. You
> already know this. The new thing today is just `input` and
> `print`. The other tools are still in your toolbox."

This is the moment when kids start to see the curriculum as
*cumulative* — each phase builds on the last.

#### Extension — function

Same callback to Phase 2 Session 4. The function takes the input
as a parameter, prints a greeting. Combines:
- input (today)
- variables (always)
- functions (Phase 2 Session 4)
- string concatenation (today)

Three concepts, one tiny program. This is the integration model
for the whole phase.

### Common stumbles

- **Forgot the closing parenthesis of `print(...)`.** SyntaxError.
  Common because the lines are short.
- **Forgot the closing quote.** SyntaxError, but with a confusing
  message about "EOL while scanning string literal." Worth
  showing.
- **Mixing `+` with non-strings.** `"Hello, " + 5` gives
  `TypeError`. Today everything from `input()` is a string, so
  the only way kids hit this is by trying `print("Five plus
  three:" + 5 + 3)`. Don't formally teach why; show the
  comma-separated alternative.
- **Smart-quotes from copy-paste.** Same as Phase 2 — curly
  quotes break things.
- **`input` without a prompt.** `input()` works but the user
  has no idea what to type. Always pass a prompt string.
- **The cursor in the shell after a prompt.** Some kids will
  type their answer in the *editor* instead of in the shell. The
  shell is where you type when input is waiting. Walk them
  through this if needed.
- **`name` getting overwritten.** If a kid does
  `name = input(...)` twice, the first value is lost. They
  may want to use different variable names.

### Differentiation

- **Younger kids (9-10):** May find the shift from visual to
  text disappointing. Lean into the multi-question Part B build
  — let them write silly questions and silly answers. The fun
  comes from personalization.
- **Older kids (12+):** Will pick up `print`/`input` instantly.
  Push them to the function extension. If they finish: ask them
  to build a tiny conversation tree — multiple `if/elif/else`
  branches based on the user's answer.
- **Advanced (any age):** May know `print`/`input` already.
  Have them try `int(input(...))` for numeric input (foreshadows
  Session 2 on types). Or have them write a function that takes
  user input and returns something — return values land in
  Session 6.
- **Struggling:** A kid who can't get the basic `print("Hello")`
  working in Part A is the kid you focus on. Most common cause:
  using smart quotes, missing parens, or not pressing Run.
  Walk them through.

### What to watch for

- **The "I miss the turtle" sentiment.** A few kids will say
  this out loud. Validate but reframe: "the turtle was great
  for learning; text is how most real software works. We'll see
  graphics again in Phase 6 (Pygame), and they'll be way more
  capable than the turtle was."
- **Frustration when programs "do nothing."** Without visual
  feedback, kids may run a program and not realize it's waiting
  for input. Watch for "my program crashed!" that's actually
  "my program is waiting for me to type."
- **The "this is just like talking to the computer" reaction.**
  When someone first builds a multi-question program and reads
  it back to themselves, several kids realize they've built a
  primitive chatbot. Affirm.
- **Buddy collaboration on the silly questions.** Buddies will
  trade ideas for absurd questions. Encourage. The personality
  goes into the questions, not the code.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- **PB&J callback landed?** — was the moment effective?
- Adjustments for next year:

### Connections forward

- **Session 2 (next week, variables and types).** The "input
  always returns a string" tease at the end of today's handout
  is the setup. Next week formalizes types and shows how to
  convert between them.
- **Session 3 (strings).** Today's `+` concatenation is the
  baseline; f-strings in Session 3 are the upgrade.
- **Session 7 (number-guessing game).** Combines today's
  print/input with conditionals and loops into the first
  real Phase 3 game.
- **The Reading Error Messages appendix** is currently a stub.
  Phase 3 will start producing more error messages than Phase 2
  did (more contexts, less visual feedback). Worth filling in
  the appendix by Session 5 or so.
- **Peanut butter callbacks** are now constant. The bread
  doesn't come out again, but the rule applies whenever a
  precision mistake happens. "Remember the peanut butter? Same
  thing here."

### Materials checklist

- [ ] Bread, PB, jelly, knife, plate, napkins, comb (the same
      props from Phase 1 Session 1 if you still have them)
- [ ] Trash bag, paper towels
- [ ] Demo machine with Thonny open
- [ ] Projector (helpful for the print/input demos)
- [ ] Class roster
