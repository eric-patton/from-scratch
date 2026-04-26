## Session 14 — Teacher Notes

*Phase 6, Pygame · Session 14 of 14 · Title: Milestone
project work day 2 + demo day*

### Purpose of this session

Phase 6 finale + curriculum midpoint. Five jobs, in
priority order:

1. **Get every kid to "demo-able."** A working version
   + at least one demo-able interaction.
2. **Run the demos well.** Same format as Phases 4-5
   (with Git log), plus Phase 6 additions: GitHub URL +
   live audience play.
3. **Push every kid's repo to GitHub.** Today is the
   "your code on the internet, with your name on it"
   moment. Don't let kids skip it.
4. **Celebrate the curriculum midpoint.** Six milestones
   shipped. Most adults have shipped *zero*. Drive this
   home.
5. **Bridge to Phase 7 (web).** Big shift incoming.
   Frame it carefully — three new languages, different
   runtime, new design dimension.

### Before class

**Bring:** nothing physical (maybe a small acknowledgment
for the 6-milestone milestone — stickers, a
group photo, etc.).

**Set up:**

- Demo machine with Pygame.
- Projector ready for both game demos and GitHub URLs.
- A backup of the Phase 7 framing speech / blurb.
- Optional: a brief "what each kid built across all
  six phases" recap if you have it.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Today: finish + demo
  + close the phase.
- **Part A — Final polish** (~35 min). Polish, bug-fix,
  buddy-test, README, GitHub push.
- **Part B — Demo day** (~40 min). 3-5 min per kid.
  Adjust per class size.
- **Phase 6 close + Phase 7 framing** (~10 min).

For a class of 6-8, demos fit in 35 min. For larger,
trim to 3 min per kid or split across two sessions.

### Teaching Part A — polish

#### "Working > impressive"

Same Phase 4-5 push:

> "A working basic version beats a half-finished
> ambitious one. Polish what works."

#### Push every kid to GitHub

This is the new requirement vs Phase 5. Walk past every
kid:

> "Have you pushed today's progress?"

If no: walk through it. If they don't have a repo yet
(missed Session 7 or never set it up): help them set
up. Today's session expects every kid to have a public
repo by demo time.

For kids stuck on PAT/auth: prioritize getting them
unstuck. The push is non-negotiable for the demo.

#### README is part of "finished"

Every milestone repo should have at minimum:

- One paragraph: what the game is.
- Controls.
- How to run.

No README = the demo includes "and here's where the
README would go." Fine but suboptimal.

#### Buddy test for game-feel

Game-feel matters for Pygame more than for any other
phase. The "hand the keyboard to a buddy with no
instructions" test reveals real UX bugs:

- Buddy uses arrows; game expects WASD.
- Buddy doesn't know how to start.
- Buddy doesn't know they died.
- Buddy doesn't realize they won.

Fix the worst of these in the polish window.

#### When the demo is in 30 minutes

Triage time. If the game is broken: roll back via Git.

```
$ git log --oneline
$ git restore .
# OR
$ git reset --hard <last-working-commit>
```

A working older state is better than a broken newer
state for demos.

### Teaching Part B — demos

#### Set the celebratory tone

This is bigger than usual. Frame:

> "Today is special. You've finished half the curriculum.
> Six projects shipped. We're going to go around the
> room — each of you shows your game, walks us through
> how you built it, and someone in the audience plays
> it. After everyone, we celebrate."

#### Demo format additions

Phase 6 demo includes:

1. Title screen first impression.
2. Live gameplay.
3. Audience plays (hand keyboard around).
4. GitHub URL — open in browser, show repo, show `git log`.
5. One hard thing.
6. One question.

The GitHub URL part is new. Prep your projector / shared
display to easily switch between the kid's game and
their browser tab.

#### Audience plays

Best moment in any Pygame demo. Hand the keyboard to a
classmate. Watch their face. Watch the original
designer's face when their game is being played by
someone else for the first time.

If a game has a multiplayer mode (Pong, tank battle,
sumo), have *two* kids play. Audience watches.

#### What to ask each kid

Genuine, specific questions:

- "What was the trickiest bug?"
- "What feature did you cut?"
- "If you had another week, what would you add?"
- "What surprised you about Pygame?"
- "How did your buddy testing go?"

Avoid generic. Each kid built something unique;
acknowledge it.

#### After all demos

Quick acknowledgment per kid (specific). Then the
phase-close:

> "You've finished Phase 6. *And* you're halfway through
> the entire curriculum. Six projects:
> - [Phase 1 milestone]
> - [Phase 2 milestone]
> - [Phase 3 milestone]
> - [Phase 4 milestone]
> - [Phase 5 milestone]
> - [Today]
>
> All shipped. All real. All on your machine — and
> several on the internet."

If you can name what each kid built across the six
phases, even better. The "I remember when you built X"
recall is meaningful.

#### Phase 7 framing

Then the bridge:

> "Phase 7 starts the back half. We're moving to *the
> web.* HTML, CSS, JavaScript — three new languages.
>
> What changes: your work is *shareable as a URL.* No
> install. No 'first install Python.' Send a link, the
> recipient sees it. That's a different kind of power
> from desktop apps.
>
> What's the same: variables, functions, loops, classes,
> state machines, debugging. All the *thinking*
> transfers. Just the syntax shifts.
>
> Phase 7 is the longest phase yet (about 17 sessions).
> But you have the foundation. See you next week."

### Common stumbles

- **Game crashes on demo.** Triage — roll back if
  needed. Demo what works.
- **Forgot to push.** Walk through quickly.
- **PAT expired or lost.** Walk through regenerating.
- **Demo runs long.** Soft cap 5 min. Polite
  interruption.
- **Demo runs short.** Fine. "Quick and clean" is a
  valid style.
- **Comparison anxiety.** A kid's game feels small
  next to someone's elaborate one. Counter: "Both
  shipped. Both work. Both are *yours*."
- **Pre-demo nerves.** Pair with a buddy if needed.
  Buddy demos alongside.
- **Audience hands the keyboard back without playing.**
  Encourage them to actually try at least once.
- **Phase fatigue.** Some kids may be tired of Pygame.
  The Phase 7 reframe is the reset — frame it as a
  fresh start with a new dimension (visual design via
  CSS).

### Differentiation

- **Younger kids (9-10):** A working basic game is
  enough. Emphasize the *journey* in the demo.
- **Older kids (12+):** Push for full polish — title,
  game-over, sound, README.
- **Advanced (any age):** Push for class-based scenes,
  persistence, and a clean GitHub presentation. Full
  README with screenshot, clear commit history.
- **Struggling:** A kid whose game barely runs needs
  the **show what works** treatment. Even one mechanic
  is a real demo.

### What to watch for

- **Pre-demo nerves.** Pair them up if needed.
- **The "I made a real game" reaction** during their
  own demo. Visible processing.
- **Audience engagement during Pygame demos** — usually
  the most engaged demos of any phase. Kids will lean
  in, ask to try, react to gameplay.
- **The GitHub URL pride.** Kids opening their repo on
  the projector — they own a thing on the internet
  now. Some will be visibly proud.
- **The "can I keep adding to it?" question.** Yes.
  Encourage. Open-source projects last; their game can
  too.
- **The pseudo-conclusion energy.** Phase 6 close-out
  is genuinely a big moment. Match the energy. Don't
  rush past it.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Phase 7 (web).** HTML/CSS/JS. Different language,
  same thinking. Canvas-based games will use Phase 6
  patterns directly.
- **Phase 8 (Flask).** Python on a server, generating
  HTML. Builds on Phases 3-4 (Python) + Phase 7 (web).
- **Long-term:** Pygame games can be expanded forever.
  Some kids will keep building at home. Encourage —
  the best programming learning happens in self-directed
  projects.
- **Curriculum midpoint:** Phase 6 close is the actual
  midpoint of the 8-phase curriculum. Acknowledge.
  Some kids may not realize it.
- **Career-long callback:** every game they build from
  here on uses today's vocabulary. Pong, fruit catcher,
  grid-world, milestones — these are Phase 6's
  contributions to their permanent toolbox.

### Materials checklist

- [ ] Projector with easy switching between game and
      browser
- [ ] Optional backup demo machine
- [ ] Phase 7 framing notes
- [ ] Optional acknowledgment for 6-milestone shipping
- [ ] List of each kid's milestones across all 6 phases
      (for the celebration moment)
- [ ] Class roster
