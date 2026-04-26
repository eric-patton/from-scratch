## Session 8 — Teacher Notes

*Phase 4, Intermediate Python · Session 8 of 9 · Title:
Milestone project work day 1*

### Purpose of this session

Same shape as previous milestone day 1 sessions (Phase 1
Session 8, Phase 3 Session 15). The key difference: Phase 4
projects use **multi-file + Git + tests** — real software
engineering practice. Five jobs, in priority order:

1. **Force every student to plan before coding.** Same as
   always.
2. **Force Git from day one.** Project is in a Git repo
   before significant code is written. Commits along the way.
3. **Help every student scope realistically.** Phase 4
   tools enable bigger projects but also enable
   over-ambition. Push for "simplest version first."
4. **Set up Session 9's success.** Every kid leaves with
   at least *something* running and at least one commit.
5. **Make sure every kid has at least one idea.** Same as
   always.

### Before class

**Bring:**

- Printed copies of the six planning questions for any kid
  without paper.
- A pen for sign-offs.
- Optional: printed seed-ideas list.

**Set up:**

- Demo machine ready.
- Class roster with each student's name and any project
  ideas they mentioned in earlier Phase 4 sessions.

**Prep time:** ~15 minutes including printing. Plus: review
your Phase 4 notes about which kids mentioned which ideas.

### Timing and flow

Total: ~90 min.

- **Welcome and intro** (~5 min) — what today is, the new
  Phase 4 expectations (multi-file, Git, optional tests).
- **Part A: planning** (~25 min) — silent planning ~10
  min, sign-offs (overlap) ~10 min, set up project + first
  commit ~5 min.
- **Build time** (~50 min) — pure build with Git commits
  along the way; you circulate.
- **Wrap-up** (~10 min) — "one thing I got working" plus
  "show me your git log."

If running short, **the wrap-up `git log` showcase can be
cut.**

### Teaching the planning step

The frame matters. Same as before but with new emphasis:

> "Today you build a project using everything we've learned
> in Phase 4. Multi-file. Git from day one. Tests if you
> can. This is what real software engineering looks like —
> not just writing code, but organizing it across files,
> tracking it with Git, verifying it with tests."

Then have them work through the six questions. Walk the
room.

Specific moves:

- **Stuck on Q1:** Use the seed list.
- **Overscoped (very common in Phase 4 — the new tools
  enable bigger ambition):** Push hard on Q5. "What's the
  ONE thing you build first?"
- **Missing files plan (Q3):** Help them think about what
  goes where. "What's the user interface? Main code.
  What's the data? Maybe a separate file. Any reusable
  helpers? Another file."
- **Skipped tests (Q6):** Encourage at least one
  `assert`-based test on their core function. Even one is
  better than none.

#### Sign-off

Look for:
- All 6 questions answered
- Q5 (simplest version) is buildable in ~50 min
- Q3 (files) is plausible (at least 2 files)

If yes, sign off. If no, ask one question.

#### Set up with Git from day one

This is the key new requirement. Walk through at the
projector:

```
$ mkdir my_project
$ cd my_project
$ git init
# create main.py with a hello-world placeholder
$ git add main.py
$ git commit -m "Initial setup"
```

Every kid should have done `git init` and made at least
one commit before writing real code.

> "Git from day one. The first commit is just 'I made a
> project.' Then every meaningful change is its own commit.
> Don't wait until the end to start using Git."

### Teaching build time

Same as previous milestones — walk the room, help individuals,
**don't take their keyboard.**

New things to watch for in Phase 4:

- **Are they committing?** Walk by, peek at their `git log
  --oneline`. If they have one commit from setup and
  nothing since, encourage commits.
- **Are they using multi-file structure?** If their entire
  project is in `main.py`, prompt: "what could be its own
  file? Could the data go somewhere else?"
- **Are they using tests?** Optional but encouraged. Even
  one `assert`-based test for a critical function shows
  the discipline.

### Common stumbles

- **No idea for a project.** Same as always — seed list.
- **Way too ambitious idea.** Phase 4 tools enable bigger
  ambition, which means more risk. Push to Q5.
- **All in one file.** Phase 4 should use multi-file.
  Encourage early splitting.
- **Forgot to git init.** Commit history starts empty.
  Easy fix: `git init` before more work.
- **Forgot to commit.** Kid's been working an hour, no
  commits. "When did you last commit?" Then commit now.
- **Changed too much before committing.** Hard to write
  one good commit message. Future-them won't know what
  changed when. Commit smaller chunks.
- **Frozen at the keyboard.** Same as always — sit, help
  with first line, hand back keyboard.

### Differentiation

- **Younger kids (9-10):** Push toward simpler seed ideas.
  Help them scope down. Multi-file is OK with two files;
  don't force more.
- **Older kids (12+):** Will overscope. Push hard on Q5.
  Demand commits along the way.
- **Advanced (any age):** Trust them with bigger scope.
  Push them on:
  - Real test coverage
  - Branch-based experiments
  - Documentation in the code (docstrings)
  - Type hints (optional, advanced Python)
- **Struggling:** A kid who's been struggling needs to
  build the simplest possible version that works. A
  two-file program with one Git commit is a totally valid
  milestone.

### What to watch for

- **Kids skipping Git.** Address immediately. "Have you
  committed yet today?" Push.
- **Kids who scope down their ambitious plans during Part
  A.** Lesson landing.
- **Kids inspired by other kids' ideas.** Encourage; ideas
  spread.
- **Buddies helping each other with Git.** Encourage.
  Buddy-paired Git is great practice.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **Project status per kid (rough notes):**
- **Git usage check** — anyone who didn't commit at all
  today?

### Connections forward

- **Session 9 (next week, demo).** Today's project gets
  finished and shown.
- **Phase 5 (customtkinter).** Multi-file structure, Git,
  classes — all today's habits transfer.
- **Phase 6 (Pygame + GitHub).** Local Git becomes shared
  Git. Today's habits become collaborative habits.
- **Public showcase.** Today's projects are showable.

### Materials checklist

- [ ] Printed planning questions
- [ ] Pens
- [ ] Optional: seed-ideas list
- [ ] Class roster with notes from earlier Phase 4 sessions
- [ ] Demo machine ready (for git demos as needed)
