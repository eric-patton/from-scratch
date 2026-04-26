## Session 15: Milestone project work day 1

*Phase 3 — Python basics · Session 15 of 16*

### What we're learning today

Today is *your* day. You'll plan a Python program of your own
choosing, then start building it. There's no new programming
concept this week — instead, you'll use everything you've
learned in Phase 3 to make something that's yours, not Mr.
Eric's. Next week you'll finish it and demo it to the class.

### You'll need to remember from last time

- **Everything from Sessions 1-14.** Print, input, types,
  strings, conditionals, loops, functions, return values,
  lists, dicts, file I/O, error handling.
- **Your text adventure** from last week — proof that you can
  build a substantial Python program.
- The **idea** you brought with you today. (If you didn't,
  Part A has a list to start from.)

---

### Part A: Plan your project

The most important step in any project isn't typing — it's
**deciding what to build.** A clear plan saves hours of
flailing later.

#### The plan

Take a piece of paper or open a blank text file. Answer these
five questions about your project. Keep it short:

1. **What's the program?** *(One sentence. Examples: "A trivia
   game with Bible questions." "A daily journal that saves to a
   file." "A story generator that mixes random elements." "A
   calculator that handles tip and tax.")*

2. **What does the user do?** *(How do they interact? Type
   answers? Pick from a menu? Both?)*

3. **What functions or data structures will you need?**
   *(Brainstorm 3-5. Examples: a `dict` of trivia questions,
   a function `ask_question(q)`, a function `save_journal(text)`,
   a list of items, etc.)*

4. **What's the simplest version that's still cool?** *(If
   you only had today and next week to build this, what would
   you do FIRST? What would you add LATER if there's time?)*

5. **What might go wrong, and how will you handle it?**
   *(Bad input? Missing file? Wrong type? Use try/except or
   `if` validation. Worth thinking about up front.)*

#### If you don't have an idea

Pick one and modify it slightly:

- **A trivia game** — questions stored in a list of dicts (or
  a file). User answers; track score. Multiple categories?
- **A budget tracker** — log income and expenses to a file;
  show totals and remaining; persist between runs.
- **A daily journal** — append today's entry to a file with a
  date stamp; let the user read past entries.
- **A study flashcard app** — load cards from a file; quiz
  the user; track which ones they got wrong.
- **A name generator** — combine random first names and last
  names from lists; build a fantasy/normal/silly name for a
  character.
- **A "mad libs" story builder** — load a story template with
  blanks; ask the user for words; print the filled-in story.
- **An extended text adventure** — take last week's adventure
  and add items, locked doors, NPCs, multiple endings.
- **A simple bank account** — deposit, withdraw, check balance;
  persist between runs.
- **A favorite Bible verses collection** — add, search,
  random-of-the-day; saved to a file.

Pick one. Spend two minutes deciding. Don't agonize.

#### Show Mr. Eric

When your plan is ready, show it to Mr. Eric. He'll either
say "go build it" or ask one question that helps you tighten
it up.

#### Start building — the simplest version first

Look at your answer to question 4. Build that **first.** Get
the simplest version running before adding anything fancy.

If your plan is "trivia game with score and difficulty
levels," the simplest version might be:

1. One hardcoded question.
2. Ask it.
3. Print "right" or "wrong."

Then *iterate*: add a list of questions. Then a score. Then
loading from a file. Then difficulty levels. Each step
working before the next starts.

This is **iterative development.** Real programmers do this.
The kid who writes 200 lines and then tries to debug all of
it at once will have a much harder time than the kid who
writes 20 lines, tests, adds 20 more, tests again.

#### When you get stuck

The five-step checklist from
[Getting unstuck](../appendices/getting-unstuck.md) — read
the code, read the error, narrow down, rubber duck, ask buddy
— plus today's specific tools:

- **Use the Thonny debugger** (Session 5). Step through your
  code. Watch the variables.
- **Use `print()` to inspect.** Add `print(variable)` lines to
  see what's happening. Remove them later.
- **Open your textbook chapters.** Sessions 1-14 are your
  reference. If you forgot how lists work, Session 8 is right
  there.
- **Ask your buddy.** Explain what you're trying to do.
- **Ask Mr. Eric.** Last resort, after the first four.

### Wrap-up

Last 5 minutes: each of you, in one sentence, tell the room
**one thing you got working today** in your project. Could be
a function. Could be a menu. Could be reading a file
correctly. Whatever's working — that's a win.

Bring your project file (or just your machine) next week.
We'll finish, then demo to the class.

### If you missed this session

Open Thonny and start a new file. Then:

1. Spend 10-15 minutes answering the five planning questions
   above on paper or in a text file.

2. Start building the *simplest* version of your project (look
   at your answer to question 4).

3. When you come next week, you'll be ready to keep building
   and finish for the demo.

If you don't have an idea, the seed list above is a starting
point. Pick one and modify.

### Stretch and extension ideas

If your base project is working and you want to add more:

- **Save state to a file** so the program remembers between
  runs (Session 11).
- **Wrap risky input in `try/except`** so the program doesn't
  crash on bad data (Session 13).
- **Refactor into functions** so the main code is short and
  readable (Session 6).
- **Add a menu** so the user can pick what to do
  (Session 9 / 10).
- **Use a list or dict of dicts** to organize complex data
  (Sessions 8-10).
- **Add ASCII art** to make output visually interesting (the
  visual hangman pattern from Session 12).

Whatever you add, add it **one piece at a time** and **test
after each piece.** Big changes that touch many things are
how programs break.

### What's next

Next week you'll have time to finish, polish, and **demo your
project to the rest of the class.** Each person will get 3-5
minutes. Don't worry — it's a friendly demo, not a test.
Bring a working program, bring your enthusiasm, and the rest
takes care of itself.
