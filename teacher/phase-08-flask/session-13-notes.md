## Session 13 — Teacher Notes

*Phase 8, Flask · Session 13 of 13 — final
session of the entire curriculum · Title:
Milestone day 2 + demo + curriculum close*

### Purpose of this session

Last session ever. Five jobs, in priority order:

1. **Get every kid's milestone live and
   demoable.** Public URL, working signup, basic
   features.
2. **Run the demos with gravity.** Not just
   another demo — the *capstone*. Audience signs
   up live.
3. **Close out the curriculum properly.** Eight
   phases, eight milestones. Real arc. Match the
   moment.
4. **Frame "what's next."** Not the end of
   programming — the beginning of *their*
   programming life. Direction without
   prescription.
5. **Make it memorable.** This is the moment
   they'll remember.

### Before class

**Bring:**

- Optional: certificates, small celebration items,
  a group photo plan.
- Optional: a printed "every kid's 8 milestones"
  recap sheet.

**Set up:**

- Demo machine.
- Projector ready for URLs and DB Browser.
- Each kid's expected URL pre-tested in the days
  before.
- Phase 9 talking points (career directions,
  framework recommendations).
- A short "from Mr. Eric" note ready (1-2
  minutes, sincere, specific).

**Prep time:** ~45 minutes — including pre-
testing all URLs and identifying any kid whose
demo is at risk.

### Timing and flow

Total: ~120 min — *let it run long.* Build in
buffer for celebration.

- **Welcome and recap** (~5 min). "This is the
  last session."
- **Part A — Final polish** (~30 min). URL
  verification, polish, push.
- **Part B — Demo day** (~50 min). 5-7 min per
  kid (longer than usual).
- **Curriculum close** (~25 min). Recap of all
  phases, frame "what's next," personal note,
  celebration.
- **Optional group activity** (~10 min). Photo,
  food, reflection.

### Teaching the framing

#### "Last session"

Open clearly:

> "This is the *last session* of the From Scratch
> Programming Class. Eight phases. Today we
> finish your eighth project. You demo. Then we
> close out the journey we started together.
>
> *No pressure*."

(Light. They've earned levity.)

### Teaching Part A — final polish

#### URL verification first

Walk past every kid in the first 10 minutes:

> "Open your URL on your machine. Does it work?
> Does signup work? Did you remember to push
> *and* pull *and* reload?"

Common failures:

- Pushed but didn't pull on PythonAnywhere.
- Pulled but didn't reload.
- App crashes on signup (database file
  permissions, missing column, etc.).
- 500 errors — check error log.

Triage *now.* Not at demo time.

#### Production polish quick wins

For the polish-minded:

- **`secret_key` from env var.**
- **`.gitignore`** for `*.db`.
- **README** with description + URL.
- **`requirements.txt`**.
- **Window title.**

If running short, skip these. Working app is
the priority.

#### Buddy URL test — the multi-user moment

Buddies sign up on each other's apps. **Real
multi-user testing.** Each kid sees their app
populate with other users' data.

> "*Their data joins yours in your database.*
> You're now hosting real users."

Pause for that.

### Teaching Part B — demo day

#### Set the celebratory tone

> "Today is bigger than usual. You've shipped
> *eight projects.* Today's demo is the
> capstone.
>
> Show your URL. Sign up live as me. Use the
> app. Have classmates sign up. Show your
> repo. Tell us what was hard.
>
> *Take your time.* This is the last demo."

Allow 5-7 minutes per kid (vs. usual 3-5).

#### Demo format

Phase 8 demo:

1. URL on projector.
2. **Sign up live as Mr. Eric** (or someone
   fresh).
3. Use the app — show all features.
4. **A classmate signs up on their machine**
   during the demo.
5. Show GitHub repo + git log.
6. Show database structure if interesting.
7. Hard thing + question.

Encourage the audience to engage:

> "Be active demo audiences. Try their apps on
> your machine. Ask questions. *This is what
> launching software looks like* — your peers
> using your work."

#### What to ask each kid

Specific to their project. After demos so many
phases, you know each kid. Ask:

- "What was the hardest bug?"
- "Which Phase 8 concept clicked best?"
- "What feature would you add with another
  week?"
- "How does this compare to your Phase 5
  customtkinter app — better, worse, same?"
- "Are you going to keep using this?"

#### After all demos

Each kid: brief, specific acknowledgment.
Mention what they did *across the curriculum*
if you can — "you started in Phase 1 with the
peanut butter problem; today you're shipping
multi-user apps."

That continuity matters.

### Teaching the curriculum close

#### Recap of all phases

Walk through the 8-phase arc:

> "Let's count what you did:
>
> - **Phase 1** — Scratch. Sequences, loops,
>   events. Visual programming.
> - **Phase 2** — Python Turtle. Same ideas,
>   real syntax.
> - **Phase 3** — Python basics. Strings, lists,
>   dicts, files. Real Python.
> - **Phase 4** — CLI + Git. Multi-file programs,
>   classes, version control.
> - **Phase 5** — customtkinter. Desktop GUIs.
> - **Phase 6** — Pygame. Real games.
> - **Phase 7** — Web. HTML, CSS, JavaScript.
> - **Phase 8** — Flask. Back-end. Today.
>
> *Eight phases. Eight projects shipped.* Most
> adults have shipped zero. You have eight."

The arc framing matters. Make it concrete.

#### "Three on the internet"

> "Three of your projects are on the internet
> right now. Your Phase 7 homepage. Your Phase
> 7 milestone. And — today — your Phase 8 app
> with real users."

That's *real* shipping. Beyond what most
working programmers had at their age.

#### Frame "what's next"

Not prescriptive. Suggestive:

- **Keep building.** The single best growth
  path.
- **Open source.** Read others' code; try
  contributing.
- **Frameworks** — React, Django, etc. when
  they want.
- **Specialties** — web, mobile, games, data,
  systems. Pick by curiosity.
- **Outside-programming skills** — make you a
  better engineer.

The handout's "What's next" section covers
this. Read aloud parts that resonate.

#### A personal note from Mr. Eric

Speak from the heart:

- What you saw them grow through.
- One specific moment per kid (if you can).
- "You earned this."
- "Keep building."
- "Come back if you want help with something
  new."

This is the moment. Don't rush.

#### Celebration

- Group photo (with permission).
- Snacks if appropriate.
- Stickers, certificates, whatever feels
  right for the group.
- Each kid says one thing they're proud of, or
  one favorite project across all 8.

### Common stumbles (still happen on the last
day)

- **URL down on demo day.** Triage to working
  state.
- **Forgot to pull on PythonAnywhere.** Pull,
  reload.
- **App crash on signup.** Quick fix or roll
  back.
- **Empty repo.** Push everything.
- **Demo nerves.** Pair with a buddy if
  needed.
- **Long-winded demos.** Politely pace.
- **Kids comparing themselves to each other.**
  Reframe: "Both shipped. Both work. Both are
  yours."

### What to watch for

- **The "I'm a programmer" moment.** Some kids
  realize it during their demo. Some during the
  recap. Real shift in self-image.
- **Buddies signing up enthusiastically.**
  Encourage.
- **Quiet pride.** Some kids won't say much
  but will be visibly satisfied.
- **The "what now?" question.** Real.
  Reassure: programming has no end.
- **Tears.** Possible. Last-day-of-something
  emotions are real for some kids.
- **Parent attendance.** If parents come for
  the final demo, weave them in. Their kid
  shipped real software.
- **Your own emotions.** This is a year+ of
  your life. It's OK to feel it.

### After class

*(Last "After class" of the curriculum. Use it.)*

- What was the most important moment of the
  curriculum?
- Which kid's growth was most significant?
- What would you do differently for the next
  cohort?
- What follow-up is needed for any kid?
- Stay in touch with these kids. They were
  yours for a year.

### Connections forward

- **No formal Phase 9.**
- **For Mr. Eric:** future cohorts. Same arc,
  refined.
- **For students:** their own programming
  journeys.
- **For the curriculum:** updates as
  technologies shift, as you learn what works.
- **Career-long callback:** you taught them to
  build. The rest unfolds.

### Materials checklist

- [ ] Demo machine + projector
- [ ] Each kid's URL pre-tested
- [ ] List of every kid's 8 milestones for
      the recap
- [ ] Phase 9 talking points (what's next)
- [ ] A short personal note ready
- [ ] Optional: photo plan, snacks,
      certificates, stickers
- [ ] Class roster (last time on this list)
