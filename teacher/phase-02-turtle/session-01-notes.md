## Session 1 — Teacher Notes

*Phase 2, Python with Turtle · Session 1 of 8 · Title: Welcome to
Python — typing instead of dragging*

### Purpose of this session

This is the second-most-important transition session in the
curriculum (the first being Phase 1 Session 1). Five jobs, in
priority order:

1. **Land the typing-not-dragging shift gracefully.** This is the
   single most likely place for kids to get demoralized. Some kids
   who flew through Scratch will struggle today because their
   typing isn't fast or because syntax errors feel like personal
   failures. Your job is to make typing-and-fixing feel normal,
   even fun.
2. **Get every student to "I typed code and it ran" within the
   first 30 minutes.** That moment carries them through the rest
   of the session. If a kid hasn't run their first program by the
   30-minute mark, that's the kid you focus all your attention on.
3. **Reset the peanut butter rule.** Phase 3 Session 1 is the
   *planned* PB&J callback (per CURRICULUM-DECISIONS.md), but
   today is when syntax precision starts mattering for the first
   time. Reference the rule constantly.
4. **Make error messages friendly, not scary.** Today is
   guaranteed to produce errors. The "make a typo on purpose"
   exercise is structured to make the *first* error a planned,
   funny moment instead of a frustrating accident. Lean into it.
5. **Establish the Thonny workflow.** Editor → save → run →
   shell. Same workflow they'll use for the rest of the
   curriculum. They need it to be muscle memory.

### Before class

**Bring:** nothing physical (unless you want a second machine to
demo errors on without messing up your "good" demo file).

**Set up:**

- Demo machine with Thonny open. Have a fresh empty editor window
  ready.
- Verify Thonny works on every student machine. *Do this before
  class starts.* Open Thonny on each one, run a one-line program
  (`print("hello")`), close. If a machine has issues, swap it out
  before students arrive.
- Verify the `turtle` module imports cleanly on at least two
  student machines. (It's stdlib, should always work, but test
  anyway — Linux Mint sometimes ships Python without `tkinter`,
  which `turtle` depends on. If `import turtle` fails, install
  `python3-tk` via apt.)
- Have the W202NA machines on early — Thonny launch is slow on
  them, and you don't want kids watching a spinner during class.

**Prep time:** ~30 minutes. Test every machine. This pays off.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — Phase 1 is done, congrats,
  here's the new tool, no more blocks.
- **Part A: Thonny tour + first program** (~45 min) — tour ~5
  min, type the first program ~10 min, run it ~5 min, the typo
  exercise ~10 min, build the square ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: colors and shapes** (~30 min) — colors and pensize
  ~10 min, penup/pendown ~10 min, free build (triangle / initials
  / house) ~10 min.
- **Wrap-up** (~5 min).

If running short, **the free build at the end of Part B is the
cuttable piece.** The Part A checkpoint (square drawn) is the
session.

### Teaching Part A

The frame matters. Open with something concrete:

> "For the next eight weeks, no more dragging blocks. We're going
> to type real code. It's going to feel weird at first, and you
> are going to make typos, and the computer is going to complain
> about it. That's normal. That's how every programmer's day
> goes. We're going to get good at fixing typos together."

Then walk into Thonny.

#### The Thonny tour

Demo at the projector if possible:

- Open Thonny. Point at the editor (top), shell (bottom), Run
  button.
- "Code goes up here. Click Run, the computer reads your code,
  and what happens shows up down here."
- Type `print("hello")` in the editor. Run. "hello" appears in
  the shell. Mark this moment: "you wrote your first Python
  program. It said hello."

Now have the kids do the same — open Thonny, type `print("hello")`,
run, see "hello." This is the muscle memory you want before
moving to anything else.

#### Type the first turtle program

Walk through it slowly at the projector:

- `import turtle` — "asking for the turtle toolbox"
- `t = turtle.Turtle()` — "making a new turtle, naming it `t`"
- `t.forward(100)` — "telling the turtle to walk 100 pixels"

Then **stop talking** and let students type it themselves. **Walk
the room.** Look for:

- **Capitalization mistakes.** Python is case-sensitive. `Turtle`
  vs `turtle`. The function name `Turtle()` has a capital T (it's
  a class). The module name `turtle` is lowercase. Both matter.
- **Missing parentheses.** Empty `()` after `Turtle` is required.
- **Missing periods.** `t.forward(100)`, not `t forward(100)`.
- **Single quotes vs double quotes.** Either works for strings.
  Smart-quotes (curly quotes) don't. If a kid's text editor or
  OS replaced their quotes with curly ones, it'll break. (Thonny
  doesn't do this by default but watch for it.)
- **Smart caps.** Some kids' machines might autocapitalize the
  first letter of a line. Disable in Thonny preferences if needed.

The first time you see a kid hit a syntax error, this is the
moment to make it ordinary. **Don't fix it for them.** Sit down,
read the error message together out loud, ask "what does it think
is wrong?" Walk through finding the line number and the broken
character. They fix it themselves.

#### The save-and-run workflow

Saving is its own thing. Demo at the projector:

- File → Save As (or Ctrl-S)
- Pick a folder
- Name the file with a `.py` extension
- Then click Run

If a kid tries to run an unsaved file, Thonny will sometimes
prompt them to save first. Walk them through that.

The `.py` extension matters. Without it, the file is just text.
Some kids will try to call their file `first_turtle` (no
extension) and get confused. Walk them through.

#### The "make a typo on purpose" exercise

This is the most important pedagogical move of the session. Set
it up explicitly:

> "We're now going to break it on purpose. Type `t.forwerd(100)`
> with a typo. Save. Run. Watch what happens."

When the error appears, gather everyone's attention:

> "Look at the bottom panel. That red text — that's an error
> message. Errors aren't bad. They're the computer telling you
> what went wrong. Let's read it together."

Read the error out loud as a group. Translate it. "It said the
turtle has no `forwerd`. We meant `forward`. That's our peanut
butter problem — we said `forwerd`, the computer did exactly what
we said, which was nothing because there's no such thing as
`forwerd`."

This is the line that matters: **errors mean the computer was
trying to do what you said and couldn't.** Frame errors as
*helpful*, not as failures.

The kids will fix the typo themselves now. They've already done it
once.

#### Building the square

After the typo exercise, building the square is mechanical. They
type 8 lines (4× forward, 4× right), run, see the square.

Some kids will hit copy-paste shortcuts (Ctrl-C / Ctrl-V) and try
to copy line 1 to lines 5, 7, 9. **Let them.** Programmers do
this. The Phase 1 callback ("remember repeat 4? next week we'll
do that in Python too") is the right framing.

### Teaching Part B

Less structured. Kids try colors, pensize, and penup/pendown,
then build a triangle/initials/house of their choice.

- The triangle is a sneaky callback to the polygon stretch from
  Phase 1 Session 3 (turn = 360 / sides). Some kids will remember
  this; some won't. Don't tell them upfront — let them realize
  the connection.
- For initials: kids will need to figure out where to lift the
  pen and where to drop it. This is genuine spatial reasoning.
  Don't give them the moves; let them work it out.
- For the house: similar. Tell them they need a square plus a
  triangle on top. Where does the triangle start? Up to them.

Walk the room. Help kids find Python features when they ask:

- "How do I move without drawing?" — `penup()` / `pendown()`
- "How do I make the turtle face a specific direction?" —
  `setheading(0)` (right), `setheading(90)` (up), etc. Don't
  formally teach yet; mention as a stretch if asked.
- "How do I jump to a spot?" — `goto(x, y)` — same, only mention
  if asked.

### Common stumbles

- **Capitalization errors.** Python is case-sensitive. `Turtle` vs
  `turtle`. Constant. Be patient.
- **Missing parentheses.** Empty `()` after `Turtle` is required;
  forgetting it gives a confusing error.
- **Smart quotes.** If text gets pasted from elsewhere, quotes
  may be curly, which Python rejects. Type the quote inside Thonny
  to be safe.
- **Forgetting to save before running.** Thonny usually prompts
  but not always. If "Run" does nothing or runs old code, save
  first.
- **The turtle window getting hidden behind Thonny.** Easy fix:
  Alt-Tab or click the window in the taskbar. Surprisingly common
  cause of "my code doesn't do anything."
- **Trying to write Scratch-style code.** Some kids will type
  things like `move 100` thinking it's a command. Gently redirect
  to the `t.forward(100)` syntax.
- **`import turtle` only on first run.** Once `import turtle`
  has run in the same shell, subsequent runs of just `t.forward(100)`
  may seem to work. But every fresh run needs the import. Make
  sure students keep `import turtle` and `t = turtle.Turtle()`
  at the top of every program for now.
- **Two windows: editor and turtle.** Some kids will type into the
  turtle window thinking it's where code goes. Redirect to the
  Thonny editor.

### Differentiation

- **Younger kids (9-10):** Typing is genuinely hard for kids who
  haven't learned to touch-type. Be patient. Pair them with a
  buddy who types faster, but make sure they do their own typing.
  Watch for kids whose typing is so slow they can't finish; if
  that's a real issue, consider home practice on typing tutor
  websites.
- **Older kids (12+):** Will probably blow through Part A. Push
  them on the Part B challenges (initials, house). If they finish:
  ask them to draw a five-pointed star. (Hint: 5 sides, 144°
  turns. Sneaky math.)
- **Advanced (any age) with prior Python experience:** Will
  finish everything quickly and want more. Suggest:
  `t.circle(50)` (draws a circle of radius 50), or have them
  buddy a struggling kid through Part A.
- **Struggling:** A kid who can't get the first program to run
  in Part A is the kid you focus on. Common causes: typing too
  slowly to keep up (pair with a buddy who types), not saving
  before running (walk through the workflow), or fundamental
  Thonny confusion (sit with them, do it together once).

### What to watch for

- **The "I typed real code and it ran!" face.** Many kids will
  get visibly excited at this moment. Some will look surprised.
  All good. Note them.
- **Kids who go quiet.** Quiet today usually means struggling. The
  loud kids are typing and erroring and laughing; the silent ones
  often haven't gotten anything to work. Check in with quiet kids
  every 10 minutes or so.
- **Frustration spikes.** Errors will frustrate some kids,
  especially perfectionists. Three signals: long sighs, head
  drops, "I hate this." Address immediately. "Errors are normal.
  This is what programmers do all day. Let's read the message
  together."
- **Kids comparing typing speed.** Some kids will feel bad they
  type slowly. Reframe: "typing speed doesn't matter. The kids
  who become great programmers are the ones who *think clearly*,
  not the ones who type fast."

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with (especially anyone who didn't
  get their first program running in Part A):
- Adjustments for next year:
- **Typing-speed concerns** — any kid you should suggest typing
  practice to?

### Connections forward

- **Session 2 (next week, sequences in Python).** Builds on
  today's typing. More turtle commands, more drawings, real
  Python sequences. The square they typed manually today comes
  back as foreshadowing for loops next session.
- **Session 3 (loops in Python).** The "you had to type the
  square 8 lines manually" tedium today is the motivation for
  `for i in range(4):` next session. Mirror Phase 1 Session 3's
  setup (drag 10 move blocks → ugh → here's `repeat`).
- **Phase 3 Session 1 (planned PB&J callback per CURRICULUM-
  DECISIONS.md).** Today is the *first* taste of typing
  precision. Phase 3 Session 1 is when you bring back the bread
  and the comb for the formal callback.
- **Reading error messages appendix** — currently a stub. Today
  was the first encounter with errors; the appendix is worth
  filling in by Session 3 or 4.
- **Peanut butter callback opportunity:** every typo today is a
  precision moment. "What did you write? What did you mean? The
  computer can't tell."

### Materials checklist

- [ ] All machines tested with Thonny pre-class
- [ ] `import turtle` verified on at least two machines
- [ ] Demo machine with Thonny open
- [ ] Projector (helpful for the tour and the typo demo)
- [ ] Class roster
- [ ] Spare typing-skill check: keep a list of kids whose typing
      slows them down significantly today
