## Session 9 — Teacher Notes

*Phase 4, Intermediate Python · Session 9 of 9 · Title:
Milestone project work day 2 + demo day*

### Purpose of this session

Last day of Phase 4. Same shape as previous demo days. Six
jobs, in priority order:

1. **Make absolutely sure every kid demos something.** Same
   rule as always.
2. **Land "polish, don't add new features."** Same rule.
3. **Run a clean demo half** with the new Phase 4 wrinkle:
   showing Git log as part of the demo.
4. **Mark the Phase 4 close.** Phase 4 is the "professional
   toolkit" phase. Acknowledge.
5. **Set up Phase 5 (customtkinter) transition.** Visual
   programming returns. Frame as exciting after the all-
   text Phase 4.
6. **Note transition signals.** Phase 5 is class-heavy —
   note kids who'll need extra support with classes.

### Before class

**Bring:**

- Snacks if you can.
- Class roster with project name + praise note column.
- Optional: small "Phase 4 complete" recognition.

**Set up:**

- Demo machine free for demos.
- Each kid's project files accessible.
- Chairs/spots arranged for viewing.

**Prep time:** ~20 minutes. Review your Session 8 notes
about each kid's project status.

### Timing and flow

Total: ~90 min.

- **Welcome and frame** (~5 min).
- **Part A: polish + buddy test** (~30 min) — polish ~20
  min, buddy swap ~10 min.
- **Break** (~5 min).
- **Part B: demos** (~35 min) — at 3-4 min per kid; build
  in ~5 min slack for the Git log walkthroughs.
- **Wrap-up + Phase 5 preview** (~10 min).

If running over: **demos take priority over polish.** Cut
polish time.

### Teaching Part A

#### Polish framing

> "Today's tight. Polish, don't add new features. If your
> project works, focus on commit messages, tests, README.
> If it doesn't, FIX it. We demo soon."

#### Specific Phase 4 polish moves

The handout mentions running tests, cleaning up commit
messages, and writing a README. These are real-project
moves worth encouraging:

- **Tests should pass.** If they don't, fix the code or
  fix the test (depending on which is wrong).
- **Commit messages** can be reviewed with `git log`. Some
  will be embarrassing ("asdf", "stuff", "more stuff").
  Future maintainers (including future-them) appreciate
  clarity. Don't *amend history* — bad form for a real
  project — just commit better going forward.
- **README** is the most important file in a real project.
  Even a one-paragraph README beats no README.

#### Buddy test

Same as always. Buddies often find bugs the developer
missed.

### Teaching Part B (demos)

#### The Git log addition

This is new for Phase 4 demos. Walk the first kid through
showing their `git log --oneline`:

> "Run `git log --oneline` in your project. Read off a few
> commits — the first one, a turning point, the last one.
> Tell us the *story* of building it."

Most kids' commit histories will be short and informal.
That's fine. The point is to make the *process* visible —
real software has a history; today's projects do too.

A great demo includes:
- The first commit ("Initial setup")
- A point where they took a wrong turn and recovered
- The last commit before the demo

#### Specific praise

Same as always. Specific to the project. Today, you can
also praise *process*:

- "I love that your first commit was just setup, then you
  built up from there."
- "The 'fix bug in score calculation' commit message tells
  me exactly what changed there."
- "Three branches with experiments? Real engineering
  discipline."

#### Handling broken projects

Same as always — describe what it should do, give specific
praise for the design.

### The Phase 4 close + Phase 5 preview

After demos:

> "Phase 4 is done. Nine sessions. The professional toolkit
> is yours. You can run programs from the terminal,
> organize code across multiple files, save versions with
> Git, write tests that catch bugs. That's the same set of
> tools every developer at Google or Microsoft uses every
> day. You have it.
>
> "Next phase — Phase 5 — we go visual again. We'll build
> *desktop apps* — programs with real windows, buttons,
> forms. Heavy use of classes (every widget is a class), so
> the practice from Session 4 becomes daily. By the end,
> you'll have built an app that looks like real software.
>
> "See you next week."

### Common stumbles

Same as previous demo sessions. Plus Phase 4 specific:

- **Tests don't pass.** If broken, fix or remove. A failing
  test is a red flag for the demo.
- **Git status shows uncommitted changes.** Commit before
  demoing — clean working tree is the right starting state.
- **Project file is in the wrong place.** Multi-file
  projects mean kids might run from the wrong directory.
  Walk through.

### Differentiation

Same as previous demo sessions.

### What to watch for

- **Kids whose Git history is impressive.** Lots of small,
  clear commits — that's professional practice landing.
  Affirm.
- **Kids whose tests caught a real bug.** "I broke
  something during build, my test caught it" is a great
  story. Highlight.
- **Reactions to others' demos.** Note who lights up at
  what.
- **End-of-phase mood.** Phase 4 is heavy on workflow; some
  kids may be tired. Phase 5's return to visual should be
  energizing.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- **Best demo (was anyone surprising?):**
- **End-of-phase mood:**
- **Phase 5 readiness check** — anyone who needs extra
  support with classes?
- Adjustments for next year.

### Connections forward

- **Phase 5 (customtkinter).** Class-heavy. Today's
  multi-file + class habits become the daily workflow.
- **Phase 6 (Pygame + GitHub).** Local Git becomes
  collaborative Git. Today's commit habits scale up.
- **Buddy reassignments before Phase 5** — end of phase
  rotation per the buddy system policy.
- **Personal projects from Phase 4.** Some kids will keep
  iterating. Encourage. The multi-file/Git/test discipline
  carries forward.

### Materials checklist

- [ ] Snacks (if possible)
- [ ] Class roster with project name + praise note column
- [ ] Optional: "Phase 4 complete" recognition
- [ ] Demo machine + viewing arrangement
- [ ] Each kid's project accessible on their demo machine
