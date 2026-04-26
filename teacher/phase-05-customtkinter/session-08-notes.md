## Session 8 — Teacher Notes

*Phase 5, customtkinter · Session 8 of 8 · Title: Milestone
project work day 2 + demo day*

### Purpose of this session

Phase 5 finale. Five jobs, in priority order:

1. **Get every kid to "demo-able."** A working basic
   version + at least one demo-able interaction.
2. **Run the demos well.** Each kid presents, gets
   acknowledged, takes a question. Same format as Phases
   1-4 milestones; the rhythm matters.
3. **Show the Git log.** Reinforce that the *journey* is
   part of the project. Commit messages tell a story.
4. **Bridge to Phase 6 (Pygame).** Frame the shift from
   event-driven apps to frame-loop games.
5. **Close Phase 5 with energy.** Five milestones shipped
   is genuinely huge — call it out.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine for kids who need to plug in to
  project (assume they bring their own laptop running
  the app).
- Projector ready.
- Phase 6 framing prepared — quick "this is what's next"
  blurb.
- Optional: small treat / acknowledgment for shipping
  five milestones.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Today: finish + demo.
- **Part A — Final polish** (~35 min). Polish, bug-fix,
  buddy-test, README.
- **Part B — Demo day** (~45 min). 3-5 min per kid.
  Adjust per class size.
- **Wrap-up + Phase 6 framing** (~5 min).

For a class of ~6-8 kids, demos fit in 35 minutes (4-5
min per kid including transitions). For larger classes,
trim demos to 3 min per kid or split across two sessions.

### Teaching Part A — polish

#### "Working > impressive"

Push every kid to **runs cleanly first, features second.**
A kid with a basic working app is in better shape than a
kid with a half-finished ambitious app.

> "Demo a working basic version, not a broken impressive
> version. Polish what works."

#### Theme suggestion

The `set_appearance_mode("dark")` and color theme tweaks
are zero-cost wins. Suggest them universally:

> "Add this two lines to the top of your app:
> `ctk.set_appearance_mode('dark')` and
> `ctk.set_default_color_theme('green')`. Free polish."

#### README

Even a one-paragraph README in their project folder is
a real-software practice. Encourage everyone to write
one. Sample: "What it does. How to run it
(`python main.py`). One thing it does well."

#### Buddy test is critical

Real users find real bugs. Push pairs to swap apps
around minute 15. The buddy clicks, types, finds the bug
the original author can't see (because the author knows
exactly what to type).

#### When the demo is in 30 minutes

If a kid's app is broken with 30 minutes left, focus on
**rollback** (`git log` to find the last working commit,
`git restore` or revert to it) rather than forward
progress. A broken-but-recent state is worse than a
slightly-older working state.

### Teaching Part B — demos

#### Set the tone

Each demo is a celebration, not a critique. Mr. Eric
goes first to model the format if helpful (or recap
Session 6's todo app as the reference).

#### What to ask

Same "one question" rule. Suggested questions:

- "What was the trickiest bug?"
- "What would you add if you had more time?"
- "What's something you learned that surprised you?"
- "Walk us through what happens when I click [this
  button]."

Ask the question that genuinely interests you about
*their* project, not a generic one.

#### Audience etiquette

Quick reminder before demos start:

- Watch the demo (not your own screen).
- Clap at the end of each.
- One question, kindly worded.

#### Hand the keyboard over

GUIs are meant to be touched. After a kid demos, let a
classmate try clicking around. Live testing is part of
the experience.

#### After all demos

Brief acknowledgment per kid (specific — what *they* did
well). Then frame Phase 6:

> "You've built five milestones. Five projects you can
> point to and say 'I built that.' That's more shipped
> projects than most working programmers had at your
> age. Phase 6 is games — Pygame, real animation, real
> sound. See you there."

### Common stumbles

- **App doesn't run on demo day.** Triage: is it Python
  not installed? Path issue? Missing customtkinter? If
  so, demo on Mr. Eric's machine. If it's their bug,
  walk them through it briefly *or* roll back via Git.
- **Forgot the README.** No big deal. Mention it as
  "next time."
- **Nervous to demo.** Pair them up — buddy demos
  alongside if they want.
- **Demo runs long.** Soft cap: 5 min. Mr. Eric
  interrupts politely if it's running over.
- **Demo runs short.** That's fine. "Quick and clean"
  is also a valid style.
- **Comparison anxiety.** A kid sees someone else's
  ambitious app and feels theirs is small. Counter:
  "Both shipped. Both work. Both are real."

### Differentiation

- **Younger kids (9-10):** A working basic app is
  enough. Emphasize the *journey* in the demo (what
  they built first vs. what they ended up with).
- **Older kids (12+):** Push for state + persistence in
  their demo. The "wow" of "watch it remember things
  across runs" is real.
- **Advanced (any age):** Their class-structured app
  with multiple features is the model. Push them to
  explain *why* they used a class.
- **Struggling:** A kid whose app barely runs needs
  the **show what works** treatment. Even one button
  doing one thing is a real demo. Validate it.

### What to watch for

- **Pre-demo nerves.** Some kids freeze. Pair them with
  a buddy if needed.
- **Real audience engagement** when GUIs get demoed.
  More so than text projects — visible apps are
  satisfying.
- **The "I made a real app" reaction** during their own
  demo. Visible processing.
- **Phase fatigue.** Some kids may be tired of
  customtkinter. Phase 6 (games) is the reset — frame
  it as the next big thing.
- **The kid who quietly finished something amazing.**
  Some kids ship far more than expected. Acknowledge
  publicly without comparing.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Phase 6 (Pygame).** Frame loops, sprites, sound,
  collision detection. Different mental model from
  event-driven GUIs.
- **Phase 7 (web).** HTML/CSS forms have the same
  shapes as customtkinter forms. Today's mental model
  transfers.
- **Phase 8 (Flask).** Real web apps with state and
  persistence. The "data + redraw" pattern from Session
  6 reappears.
- **Long-term:** kids who built useful apps may keep
  using and extending them at home. Encourage. The
  best learning happens in self-directed projects.

### Materials checklist

- [ ] Projector
- [ ] Optional: backup demo machine (in case a kid's
  app won't run on theirs)
- [ ] Phase 6 framing notes
- [ ] Optional: acknowledgment for five-milestone
  shipping
- [ ] Class roster
