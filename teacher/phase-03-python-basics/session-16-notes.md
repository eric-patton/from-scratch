## Session 16 — Teacher Notes

*Phase 3, Python basics · Session 16 of 16 · Title: Milestone
project work day 2 + demo day*

### Purpose of this session

Last day of Phase 3. Same shape as Phase 1 Session 9. Six
jobs, in priority order:

1. **Make absolutely sure every kid demos something.** Same
   rule as Phase 1 — no kid leaves without showing the room
   what they built.
2. **Land the polish vs. features distinction.** Most kids
   should be polishing today, not adding features. Help them
   choose.
3. **Run a clean demo half.** Same format as Phase 1 — 3-5
   min per kid, specific praise, one question per demo.
4. **Mark the Phase 3 close warmly.** Phase 3 is the longest
   foundational phase. Acknowledge the journey.
5. **Set up Phase 4 transition.** Phase 4 introduces the
   command line and Git — both genuinely new tools that
   change how kids work. Frame as "professional tooling."
6. **Note transition signals.** Watch for kids who'll need
   extra support with the CLI/Git transition.

### Before class

**Bring:**

- Snacks if you can (demo days deserve food).
- Class roster with two columns: project name + one specific
  praise note per kid.
- Optional: small "Phase 3 complete" recognition.

**Set up:**

- Demo machine free for kids who'll demo on it.
- Each kid's project file accessible on their demo machine.
- Chairs/spots arranged for viewing during Part B.

**Prep time:** ~20 minutes. Review your Session 15 notes about
each kid's project status. Walk in knowing where each kid is.

### Timing and flow

Total: ~90 min. Same constraints as Phase 1 Session 9 and
Phase 2 Session 8.

- **Welcome and frame** (~5 min).
- **Part A: polish + buddy test** (~35 min) — polish ~25 min,
  buddy swap ~10 min.
- **Break** (~5 min).
- **Part B: demos** (~35 min) — at 3-4 min per kid, 8 kids =
  ~30 min plus transitions.
- **Wrap-up + Phase 4 preview** (~10 min).

If you have ~6 kids, demos are 4-5 min each. If 8+, push
hard on 3 min each.

If running over: **demos take priority over polish.** Cut
polish time to keep demo time.

### Teaching Part A

#### Open with the polish framing

> "Today's tight. You have 30 minutes to finish, then we
> demo. Here's the rule: if your project works, spend this
> time on POLISH — error messages, formatting, comments,
> small touches. If it doesn't work, FIX IT. Don't add new
> features today; you don't have time."

This sets expectations. Some kids will want to add cool new
features; redirect.

#### Walk the room aggressively

Triage:
- **Working, polishing:** Let them. Suggest specific polish
  ideas if they're stuck on what to add.
- **Mostly working, has a bug:** Help debug.
- **Doesn't run:** Help cut features until something runs.
  Better to demo a tiny working thing than a broken
  ambitious thing.
- **Hasn't built much:** Spend the most time. Help them get
  the simplest possible version running for the demo.

#### The polish menu

The handout lists specific polish moves. Worth pointing out
which ones to suggest based on what kids built:

- **Trivia game:** error handling for non-numeric answers,
  better feedback ("right" vs. "wrong, the answer was X")
- **Journal/notes app:** save to file with timestamps,
  better display of past entries
- **Calculator:** input validation, formatted decimal output
- **Text adventure:** look command, more descriptive
  responses to invalid commands
- **Quiz/study app:** track which questions were missed,
  show a final score

Be specific in suggestions. Generic "add polish" doesn't
help; "add error handling for when the user types non-numeric
input" does.

#### Buddy test

After ~25 min, pause:

> "Five minutes — swap with your buddy and play each other's
> programs."

Walk during. Buddies often find bugs the developer missed.
Encourage discussion.

### Teaching Part B (demos)

Same format as Phase 1 Session 9 and Phase 2 Session 8:

- Show
- Tell us about it
- Tell us what was hard
- Take one question
- Mr. Eric gives specific praise

The first demo sets the tone. Pick a kid you trust to model
the format.

#### Specific praise (again)

This is the most important thing you do today. Praise that's
*specific to what the kid built* models the kind of attention
you want them giving each other.

Bad: "Great job, that was awesome!"
Good: "I really liked how your trivia game tells you the
correct answer when you get it wrong — that turns the game
into a learning tool, not just a quiz."

If you can't think of something specific, ask the kid: "what
was your favorite part of building this?"

#### Handling a project that doesn't quite work

Same as Phase 1 — if a project crashes mid-demo:

- "Oh, that's a bug. Can you tell us what *should* have
  happened?"
- They explain the intended behavior.
- You give specific praise for the design.

The bug becomes part of the story; embarrassment is not.

### The Phase 3 close + Phase 4 preview

After demos, before kids leave:

> "Phase 3 is done. Sixteen sessions. The longest phase in
> the curriculum so far. You learned everything you need to
> write small Python programs that actually do things — talk
> to people, save data, handle errors, organize information
> with lists and dicts. That's a real toolkit. You have it
> now.
>
> "Next phase — Phase 4 — we move into *professional* tools.
> We'll learn the command line: how programmers actually run
> programs (no green button). We'll learn Git: how
> programmers track and save their code. And we'll start
> writing programs that span *multiple files* — programs
> that are too big for one Python file.
>
> "These are the tools real software developers use every
> single day. Phase 4 is where you start *looking like* a
> programmer. See you next week."

This is a meaningful moment. Land it.

### Common stumbles

- **Kid wants to add features instead of polishing.**
  Redirect.
- **Kid's project file got lost.** If they were saving
  locally and the file's gone, that's tough. Recovery
  options: Time Machine / file history; ask if they emailed
  it; reconstruct from memory. (This is partly why Git is
  Phase 4 — version control prevents this.)
- **Kid refuses to demo.** Same as Phase 1 — let them demo
  privately to you instead.
- **Demos run long.** Cut praise to 15 sec, make questions
  optional. Don't cut anyone's actual demo.
- **Kid's program crashes immediately on demo.** See "handling
  a project that doesn't quite work" above.

### Differentiation

- **Younger kids (9-10):** Their projects will likely be
  smaller. Praise the *thinking* — what they decided to
  build, why. Don't compare to older kids' work.
- **Older kids (12+):** May have more polished projects.
  Praise *risk-taking* — what they tried that they hadn't
  done before.
- **Advanced (any age):** May have built something genuinely
  impressive. Celebrate without putting other kids' work in
  the shade.
- **Struggling:** A kid whose project is barely functional
  needs the most careful demo handling. Their experience of
  Phase 3's last day must be "I built something and people
  saw it."

### What to watch for

- **Kids' reactions to others' projects.** Some will be
  impressed. Some will get jealous. Some inspired. All
  useful info.
- **The "I want to do that next time" comments.** Note who
  said what. Phase 4 projects can pull from this.
- **The end-of-phase mood.** If kids leave proud and curious
  about Phase 4, you nailed it. If they leave deflated, the
  timing was too tight or you forgot the warm close.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- **Best demo (was anyone surprising?):**
- **Hardest moment of the day:**
- **End-of-phase mood:**
- **Phase 4 readiness check** — anyone who needs extra
  support for the CLI/Git transition?
- Adjustments for next year

### Connections forward

- **Phase 4 (next week, intermediate Python).** The CLI is a
  shift; warn kids that "running Python from the terminal
  feels weird at first but is what real developers do."
- **Git introduction** (mid-Phase 4 per CURRICULUM-DECISIONS.md).
  Today's kids who lost project files will be especially
  receptive to "Git would have prevented this."
- **Buddy reassignments before Phase 4.** End of phase =
  buddy rotation per the buddy system policy. Use today's
  signals (who solo-built confidently, who needed scaffolding).
- **Personal projects from today.** Some kids will keep
  iterating. Encourage. The goal-2 hook (programming as a
  tool for *their* things) is taking root.
- **Public showcase eligibility.** Today's projects are
  showable. They could feature in the next public showcase
  alongside Phase 1-2 projects.

### Materials checklist

- [ ] Snacks (if possible)
- [ ] Class roster with project name + praise note column
- [ ] Optional: "Phase 3 complete" recognition cards
- [ ] Demo machine setup; chairs arranged for viewing
- [ ] Each kid's project file accessible on demo machine
