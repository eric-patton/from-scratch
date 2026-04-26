## Session 1 — Teacher Notes

*Phase 4, Intermediate Python · Session 1 of 9 · Title: The
command line — your first `cd`, `ls`, `python`*

### Purpose of this session

The fourth major transition session in the curriculum. The
shift from "click green button" to "type commands in a
terminal" changes how kids work. Five jobs, in priority order:

1. **Land the terminal as a real tool.** Many kids have never
   intentionally opened a terminal. Today is when it stops
   being scary.
2. **Land `cd / ls / pwd` as muscle memory.** These three
   commands cover ~90% of file system navigation. Drill them.
3. **Land `python script.py` as the new run workflow.**
   Replaces the green button. Foundation for every later
   Phase 4 session.
4. **Reframe "the editor + green button" as one of many
   workflows.** Real developers use editors AND terminals
   together. Today is the introduction to the second half.
5. **Set up Git for Sessions 5-6.** Git is a CLI tool;
   without command-line fluency, Git is much harder. Today's
   work directly enables Git later.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with a terminal open and a Python file ready
  to run.
- Verify the terminal works on every student machine.
  Especially: where is the terminal app on Linux Mint XFCE?
  (Applications → System → Terminal Emulator, OR right-click
  on the desktop.) Make sure students can find it.
- Verify `python --version` (or `python3 --version`) works.
  Linux Mint usually has both `python` and `python3`; pick
  the one that works on the class machines and use it
  consistently.
- Pre-test running an earlier Python script from the
  terminal.

**Prep time:** ~25 minutes. Test the workflow on each machine
type (M710q and W202NA). Especially worth testing if `python`
or `python3` is the working command.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — Phase 3 is done; today
  starts a different kind of phase.
- **Part A: terminal basics** (~40 min) — open terminal ~5
  min, pwd ~5 min, ls ~10 min, cd ~15 min, practice
  navigation ~5 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: running Python** (~35 min) — find an old program
  ~5 min, navigate to its folder ~10 min, run it ~5 min,
  practice with multiple files ~10 min, stretch commands
  (mkdir/cat/rm) ~5 min.
- **Wrap-up** (~5 min).

If running short, **the stretch commands and `python -i` can
be cut.** The basic `cd / ls / python script.py` workflow is
the session.

### Teaching Part A

#### The framing

Open with the cultural shift framing:

> "For three phases, you've used Thonny's green button to
> run Python. Today we learn another way: the terminal.
> You'll type a command, the computer does what you said.
> No buttons, no menus, just text in and text out.
>
> "The terminal feels weird at first. It's also what
> *every* professional programmer uses every day. We learn
> it now."

This sets expectations honestly.

#### Open a terminal

Walk to the projector. Show how to open the terminal on
the class machine. Make sure every student has it open
before moving on.

The "where is the terminal?" question is the most common
beginner stumble. Show explicitly:

- The icon in the Applications menu (System → Terminal
  Emulator typically).
- The right-click-desktop option (often the easiest).
- Optional: `Ctrl-Alt-T` keyboard shortcut on many Linuxes.

Different distributions have different defaults. Show what
works on YOUR machines.

#### `pwd` — where am I?

Mechanical. Show, have them try.

> "The terminal always thinks of you as being *somewhere* —
> in some folder. `pwd` tells you where. The path it shows
> is the full address of the folder, starting from the root
> of the file system."

The output (`/home/yourname`) is the home directory. Worth
pointing out.

#### `ls` — what's here?

Walk through plain `ls` first, then `ls -la`.

The flag concept (`-la`) is important and new:

> "Most commands accept *flags* — extra options that change
> how they work. They start with a dash. `-l` is one flag
> ('long format'); `-a` is another ('include hidden').
> Together: `-la` (or `-al` — order doesn't matter for
> single-letter flags)."

Don't get into the long-form flags (`--all` etc.) yet.
Single-letter is enough.

The hidden files (`.bashrc`, `.config`, etc.) are worth
noting briefly:

> "Files starting with a dot are hidden by default. They're
> usually configuration files for various programs. You can
> see them with `ls -a`. Don't delete or edit ones you
> don't recognize."

#### `cd` — change directory

The big one. Walk through:

- `cd Desktop` (or any subfolder) — go into it
- `pwd` to confirm you moved
- `ls` to see what's there
- `cd ..` — back up one level
- `cd` (no argument) — back to home

The `..` (parent folder) is the most surprising. Demo
explicitly:

> "Two dots is the parent — one level up from where you
> are. So `cd ..` always takes you up. `cd ../..` goes up
> two levels. `cd ../Music` goes up one and into Music."

The "navigate around" practice time is essential. Walk the
room. Help kids who get confused.

Common navigation confusion:
- Tried to `cd` into a file (not a folder) — gets an error.
- Tried to `cd` to something that doesn't exist — error.
- Used wrong case (`cd documents` vs `cd Documents`) — Linux
  is case-sensitive.

### Teaching Part B

#### Run an existing script

The "run an old program" exercise is the payoff. Walk
through at the projector:

- Navigate to where the script is (`cd Documents/python` or
  wherever).
- Confirm you can see it (`ls`).
- Run it (`python hangman.py`).
- Use the program normally.
- When it ends, you're back at the prompt.

The "the program ran" moment lands the lesson. Several kids
will visibly process this — it really IS the same as the
green button, just done differently.

#### Why this matters

Spend a moment on the "why":

> "Three reasons. One: you don't need an editor. Two: every
> other tool — Git, web servers, package managers — is
> command-line first. Learning the terminal unlocks all of
> them. Three: it's faster once you're used to it."

This sets up the rest of Phase 4.

#### `python` vs `python3`

Some Linux distributions have both. Tell kids which to use
on YOUR machines, and stick with it consistently.

> "On our machines, the command is `python` (or `python3`
> — whichever works). Stick with one for consistency."

If a kid hits "python: command not found", they need
`python3`. If a kid hits a really old Python version (2.x),
they need `python3`. Walk through.

#### Stretch — useful commands

The table is reference material. Walk through `mkdir`, `cat`,
maybe `rm` (with the loud warning).

> "`rm` deletes files. *Permanently.* No trash can, no
> undo. Always look at what you're about to delete. Real
> programmers occasionally delete things they shouldn't
> have. Don't be one of them today."

The `rm` warning is important. Some kids will try it and
delete something important. Better they hear the warning
twice than zero times.

#### Stretch — `python -i`

Useful but not essential. Mention briefly. Some kids will
love it — running their script and then poking at the
variables interactively.

#### Extension — `chmod +x` and `#!`

The shebang + chmod pattern makes scripts feel like real
commands. Real engineering practice. Worth showing for
kids who finished other stretches.

> "This is how Python tools that work like commands —
> `pip`, `pytest`, lots of others — are made. They're just
> Python scripts with a shebang at the top, marked
> executable, that you can run from anywhere."

### Common stumbles

- **Can't find the terminal.** Walk through Applications
  menu and right-click desktop options.
- **`python: command not found`.** Try `python3`.
- **Case sensitivity.** `cd documents` fails when folder is
  `Documents`. Linux cares about case.
- **Spaces in folder names.** `cd My Documents` fails — it
  thinks "My" is a folder and "Documents" is something else.
  Quote it: `cd "My Documents"`. Or rename folders without
  spaces.
- **Got lost.** `cd` (no args) takes you home, always. Then
  start over.
- **`ls` shows nothing.** The folder is empty. Or it's
  showing hidden files only and you didn't use `-a`. Try
  `ls -a`.
- **`python myscript.py` runs old code.** They edited and
  saved in Thonny, but the terminal is showing cached
  output? Unlikely; usually means they ran a different file.
  Check `pwd` and `ls`.
- **Tab completion confusion.** Pressing Tab after a few
  letters auto-completes if there's only one match. If not,
  beeps or shows options. Some kids panic at the beep.
- **Pasting into terminal.** Right-click → Paste, or
  Ctrl-Shift-V (NOT plain Ctrl-V). Different terminals work
  differently.

### Differentiation

- **Younger kids (9-10):** Slow typists may find the
  terminal frustrating. Be patient. The tab-completion trick
  helps a lot.
- **Older kids (12+):** Will pick this up fast. Push them
  to the stretch commands and the `chmod +x` pattern.
- **Advanced (any age):** Suggest:
  - Pipes (`ls | wc -l` to count files)
  - Output redirection (`python script.py > output.txt`)
  - Aliases (in `~/.bashrc`)
  - The `find` command for searching
  - Bash scripts (a file of commands)
- **Struggling:** A kid who can't get a basic Python script
  running from the terminal in Part B is the kid you focus
  on. Most common cause: wrong directory, wrong python
  command, or typo in filename.

### What to watch for

- **The "I'm not sure where I am" moment.** Common. Help kids
  use `pwd` to orient.
- **Frustration with case sensitivity.** Lower-case errors
  are constant the first day.
- **The "I ran my old program from a black window!"
  satisfaction.** The cultural shift moment. Affirm.
- **Kids who try to use the mouse in the terminal.** Gently
  redirect — keyboard only.
- **Kids who read everything the terminal prints.** Good
  habit. Encourage. The terminal is talking to you.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **CLI fluency check** — note any kid struggling with
  basic navigation; they'll need extra support before Git
  in Sessions 5-6.

### Connections forward

- **Session 2 (next week, multi-file).** Multi-file programs
  need to be run from the terminal in their containing
  folder; the CLI is the workflow.
- **Sessions 5-6 (Git).** Git is *all* CLI. Today's fluency
  is a prerequisite.
- **Session 7 (testing).** Tests are typically run from the
  terminal too.
- **Phase 6 (Pygame).** Running Pygame programs is the same
  pattern: `python game.py`. Phase 4's CLI workflow scales
  up.
- **Phase 8 (Flask).** Web servers are run from the terminal
  (`python app.py` or `flask run`). Today's foundation.
- **Peanut butter callback opportunity:** the "case
  sensitivity" gotcha is a precision moment. The terminal
  did exactly what was typed; `Documents` and `documents`
  are different things to Linux.

### Materials checklist

- [ ] Demo machine with terminal open
- [ ] Pre-tested workflow on each machine type (M710q + W202NA)
- [ ] Confirmed `python` (or `python3`) command
- [ ] Old Python script to run as the demo
- [ ] Projector (essential — the terminal is hard to demo
      from one machine)
- [ ] Class roster
