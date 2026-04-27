# From Scratch Programming Class — Curriculum Decisions

This document captures the design decisions made for the From Scratch
programming curriculum. It exists to:

1. Onboard future collaborators (including future-Eric) without re-deriving everything.
2. Prime AI assistants (Claude Code, etc.) with project context.
3. Serve as a tiebreaker when curriculum questions come up later.

When a decision is revisited, update this doc. When a new decision is made,
add it here.

---

## About the class

- **Teacher:** Eric Patton ("Mr. Eric" to students). Principal software engineer,
  15+ years experience.
- **Setting:** Originally designed for a weekly evening class at a local church, alongside Bible study. Other deployment patterns (more or less frequent meetings, secular settings) are possible — the design assumes weekly 90-120 min sessions but the curriculum content doesn't.
- **Students:** Kids and teens of the congregation. Recommended minimum age 9
  (needs reading/typing fluency for the post-Scratch transition).
- **Cost:** Free. Students keep their machines forever; the class itself is
  free for life — students can return any time, even years later.
- **Class size:** Probably 8-10 students, mixed ages.
- **Session length:** 90-120 minutes weekly, structured as two ~45-minute halves
  with a hard checkpoint between them so a half-session day still produces a
  complete unit.
- **Future possibility:** A separate adult class may eventually be added.

## Hardware

All students run **Linux Mint XFCE** on x86. Two tiers:

- **Standard tier:** Refurbished mini desktops (e.g., ThinkCentre M710q),
  6th/7th-gen Intel i5, 8GB RAM, 256GB SSD.
- **Free tier:** Three donated ASUS VivoBook W202NA laptops (Celeron N3350,
  4GB RAM, eMMC). Underpowered — curriculum must accommodate them.

Eric images all machines before day one with all tools pre-installed.
Students never deal with installation friction during the curriculum.

## Hardware-driven constraints

- **IDE:** Thonny for Python (not VS Code) — consistent across all machines,
  works fine on the W202NAs.
- **Web dev:** Vanilla JS and CDN-loaded libraries only. No Webpack, Vite, or
  other heavy build tools — the W202NAs cannot handle them comfortably.
- **No 3D:** No 3D game development, deferred indefinitely. Hardware can't
  handle it; complexity isn't worth it.
- **GUI library:** customtkinter (not plain Tkinter, not PyQt). Modern
  appearance, MIT licensed, runs fine on W202NAs, identical mental model to
  Tkinter so all Tk resources still apply.

---

## Goals (in priority order)

These are the north star. When making curriculum decisions, ask: which option
better serves these, in this order?

1. **Logical thinking and decomposition.** Transferable to anything. Programming
   gives immediate, honest feedback about decomposition quality. This is the
   primary goal even for students who never write code professionally.
2. **Programming as a practical life tool.** The "I have a repetitive task,
   I can automate it" instinct. Pays dividends for the 80% of students who
   won't become professional programmers but will end up in jobs where a
   small script saves real time.
3. **Foundation for a programming career.** Confidence and transferable
   fundamentals — not language-specific mastery. Students should leave
   knowing how to *learn* a new language when they need to.

### Sub-goal: comfort with not knowing

A first-class skill. Students should leave able to face an unfamiliar problem
and think "I don't know how yet, let me figure out where to start" rather
than "I can't do this."

---

## Curriculum arc

Roughly 80-100 sessions of 90-120 minutes each — about 150 hours of
class time total. How long that takes depends on meeting frequency:
~1.5-2 years at one session per week, closer to a year at twice a
week. The curriculum is designed around the once-a-week cadence but
adapts cleanly.

| Phase | Topic | Sessions |
|-------|-------|----------|
| 1 | Scratch | 8-10 |
| 2 | Python transition (Turtle) | 6-8 |
| 3 | Python basics | 14-16 |
| 4 | Intermediate Python + CLI + Git | 8-10 |
| 5 | customtkinter (desktop GUIs) | 6-8 |
| 6 | Pygame (2D games) | 12-15 |
| 7 | HTML / CSS / vanilla JS | 15-18 |
| 8 | Flask (web apps) | 12-15 |

After Phase 8, students who continue can branch into electives: APIs,
databases, Raspberry Pi/microcontrollers, a second language, etc.

### Sequencing principles

- **CLI, Git, debugging, and documentation reading are woven through the
  Python phases**, not taught as isolated blocks. Kids learn them as means
  to ends they care about.
- **Phase 2 uses Python Turtle** as the bridge from Scratch to "real" Python.
  Stdlib, visual, runs on the W202NAs, real Python syntax.
- **Eric will build a custom grid-world coding toy** in Phase 6 as a Pygame
  project. Originally Eric considered using a code-to-move grid-world as
  the post-Scratch bridge, but Python Turtle won out for being simpler,
  stdlib-only, and quicker to typing-real-Python. The grid-world idea
  survives as a Phase 6 Pygame creation that motivated students can
  build, extend, or write puzzles for — making them the *creators* of the
  kind of toy they might have *used* on other coding-education sites.
- **Functions/abstractions deferred to Python.** Scratch's custom blocks are
  clunky enough that the friction outweighs the benefit.
- **Git introduced mid-Phase 4, local-only at first.** GitHub appears in
  Phase 6 when students have things they actively want to share.

---

## Handouts and textbook

### Format: handouts ARE the textbook

Single source of truth. Each session's student handout is written as a
self-contained chapter. mdBook compiles them into a browsable, searchable
static site.

This means handouts are written in **prose-with-exercises voice**, not
terse bullet lists — a student must be able to read the chapter cold and
follow it without having attended class. Length: ~1000-3000 words per
session, depending on phase complexity.

### Two-file format per session

- `src/phase-XX-name/session-XX-title.md` — student-facing, becomes textbook chapter
- `teacher/phase-XX-name/session-XX-notes.md` — Eric's working document

These are parallel files, never combined. The teacher notes can reference
the student handout; the student handout never references teacher notes.

### Student handout structure

1. Title block (session number, phase, position in phase)
2. **What we're learning today** — student-voice intro, 2-3 sentences
3. **You'll need to remember from last time** — bullet list, ~3-5 items
4. **Part A** — concept + guided exercise. Ends at a checkpoint. Stands alone.
5. **Part B** — extended practice or mini-project. Tiered (base / stretch / extension).
6. **Wrap-up**
7. **If you missed this session** — self-paced catch-up, ~20-30 min independent
8. **Stretch and extension ideas**
9. **What's next** — one sentence

### Teacher notes structure

1. Purpose of this session (what jobs it's doing)
2. Before class (materials, setup, prep time)
3. Timing and flow (rough minute-by-minute, where to cut if running short)
4. Teaching notes per Part A / Part B
5. Common stumbles
6. Differentiation (younger, older, advanced, struggling)
7. What to watch for
8. **After class** — blank section to fill in *after* teaching, for next year
9. Connections forward (callbacks, future references)
10. Materials checklist

The "After class" section is the highest-value compound-interest piece —
five minutes of post-session notes makes year two of the class
substantially better than year one.

---

## Repo layout

```
from-scratch/
├── README.md
├── CURRICULUM-DECISIONS.md     ← this file
├── CLAUDE.md                   ← orientation for AI assistants
├── book.toml                   ← mdBook config
├── LICENSE                     ← CC BY-SA 4.0 (textbook content)
├── LICENSE-CODE                ← MIT (lesson code, scripts)
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml          ← build + deploy textbook to Pages
│
├── src/                        ← textbook source (mdBook convention)
│   ├── SUMMARY.md              ← table of contents, the curriculum spine
│   ├── introduction.md
│   ├── for-parents.md
│   ├── for-students.md
│   ├── phase-01-scratch/
│   ├── phase-02-turtle/
│   ├── phase-03-python-basics/
│   ├── phase-04-intermediate-python/
│   ├── phase-05-customtkinter/
│   ├── phase-06-pygame/
│   ├── phase-07-web/
│   ├── phase-08-flask/
│   └── appendices/
│       ├── getting-unstuck.md
│       ├── reading-error-messages.md
│       ├── glossary.md
│       ├── keyboard-shortcuts.md
│       ├── thonny-reference.md
│       └── installing-on-your-own-computer.md
│
├── code/                       ← lesson code (starter / exercises / solutions)
│   └── phase-XX-name/
│       └── session-XX-name/
│           ├── starter/
│           ├── exercises/
│           └── solutions/      ← public, labeled clearly as spoilers
│
├── teacher/                    ← teacher prep notes, NOT published
│   ├── README.md
│   ├── phase-XX-name/
│   │   └── session-XX-notes.md
│   └── policies/
│       ├── attendance.md
│       ├── buddy-system.md
│       └── showcase-rhythm.md
│
├── assets/                     ← images, diagrams, screenshots
│   └── phase-XX-name/
│       └── session-XX/
│
└── tools/                      ← internal scripts
    ├── new-session.sh          ← scaffolds new session files from templates
    └── build-book.sh           ← wraps `mdbook build`
```

### Layout decisions

- **One repo, not many.** Single clone, single source of truth.
- **Solutions are public**, in clearly-labeled `solutions/` subdirectories.
  Students who peek when stuck still learn; parents and buddies need access;
  policing it is a losing battle. Cultural framing: "If you peek before
  trying, you're cheating yourself."
- **`teacher/` lives in the same repo** but is excluded from the mdBook build.
  Version-controlled alongside everything else; Eric will thank himself in
  year two.
- **Phase numbering with leading zeros** (`phase-01-scratch`) for correct
  sorting.
- **Per-phase session numbering** (`session-01` resets each phase) so
  reordering phases doesn't renumber sessions. `SUMMARY.md` provides the
  global ordering.
- **Assets mirror source structure.** Predictable, easy cleanup.
- **`tools/new-session.sh`** is a high-priority early script. Scaffolds the
  three matching files (student handout, teacher notes, code dir) from
  templates. Saves ~10 min per session and prevents template drift.

### Hosting

- **GitHub Pages** for the public textbook (default).
- **Local copy on every student machine** as part of the image, for offline
  reading. Updated by `git pull` once Phase 4 introduces Git.

### Tooling choices

- **mdBook** (Rust-based) — simpler than MkDocs Material, faster, cleaner
  default output. The simplicity wins for this project.
- **Markdown only.** No fancy extensions that lock us into a renderer.

### License

- **Content (handouts, textbook):** CC BY-SA 4.0
- **Code (examples, exercises, tooling):** MIT

Both chosen so other churches/teachers can build on this work freely
with attribution.

---

## Milestones and showcases

### Distinction

- **Milestone project** = capstone of a phase, every student does it,
  proves they internalized the phase. Part of curriculum.
- **Showcase** = public-facing event where students demo to family/church.
  Less frequent than milestones.

### Rhythm

| Event | Frequency | Audience | Length |
|-------|-----------|----------|--------|
| Internal demo day | End of each phase (~6-8/yr) | Class only | ~30-45 min within session |
| Public showcase | Twice yearly (fall, spring) | Families, church | ~90 min standalone event |

### Showcase format

- **Stations, not stage.** Each student at a table with their machine,
  family circulates. Less terrifying than presenting; richer conversations.
- **Project cards.** Each student has a card with project name, what it does,
  what they learned, what was hardest. Pre-written.
- **Big-screen rotation.** Projector cycles through 30-second highlights for
  ambient atmosphere and grandparents who can't walk around.
- **Food.** Non-negotiable.
- **Public recognition.** Eric says a few words about each student at wrap-up.
- **~90 min total:** 15 setup, 60 open demo, 15 wrap-up.

### Internal demo day format

- Each student demos their milestone project ~3-5 min.
- Other students ask one question per demo (builds engagement habit).
- Eric models specific, concrete praise.
- Fits into Part B of a regular session.

### Implications for curriculum design

- Every phase ends with a milestone project that's demoable in 3-5 minutes
  and visually/audibly interesting.
- Milestones produce artifacts students can keep — runnable game, app icon,
  hosted page.
- Public showcases pull from milestone projects + personal projects;
  students choose what to demo.
- Phase length is partly constrained by milestone difficulty. Don't pad.

---

## Policies

### Attendance

- **No formal attendance requirement.** Free church class; kids show up
  because they want to.
- **Track casually** so Eric notices patterns. Three weeks missed = check in
  with student/parents.
- **No special re-teaching for absentees.** They read the chapter, do the
  catch-up exercise, ask their buddy. Preserves Eric's prep time and respects
  the student.
- **Two-strikes courtesy:** kid returning after 3+ consecutive absences gets
  ~5 min catch-up at start of class — enough to participate today, not a
  full re-teach.
- **Exception: missed milestone sessions.** Make sure the student gets a
  chance to do the milestone (later session's Part B, or at home). Don't
  let them skip the "I built something" moment.

### Buddy system

- **Every student has a buddy, assigned by Eric.** Self-selection breeds
  cliques and orphans the quiet kid.
- **Mixed-experience pairings by default.** Newer student gets help; older
  student gets the depth that comes from teaching.
- **Reassign every ~8-10 sessions** (roughly per phase). Prevents stagnation,
  exposes everyone to multiple working styles.
- **Buddies sit together.** Physical proximity does most of the work.
- **The rule: ask your buddy first, then Mr. Eric.** Cuts interrupt rate,
  forces students to articulate their stuck point.
- **Public mentor recognition** for older students buddying well. Rocket
  fuel for kids who'd otherwise be bored.
- **Be thoughtful about pairings**, especially across genders as students
  hit middle-school age. Standard youth-ministry instincts apply.

### What "done" means

An exercise is **done** when:

1. **It does what the prompt asks** (working, not pretty).
2. **The student typed the code themselves** (not copied from buddy or solution).
3. **The student can explain how it works** (line by line if asked).

Tiered targets: base (everyone) / stretch (try it) / extension (extra).
"Done" applies to base. Stretch and extension are bonus, never required.

A student can be "done for today" without being "done with the topic." Tell
perfectionists explicitly that they can stop.

**Milestone projects** have a higher bar: must be demoable for 3 minutes.

The "explain how it works" rule is the most important and the most often
skipped — it's the thing that separates real learning from cargo-cult coding.

### AI policy

- **AI is allowed for asking questions, not for getting answers.**
  - "Explain what a list comprehension does" — fine.
  - "What does this error message mean?" — fine.
  - "Write the function for me" — not fine.
- The "explain how it works" rule is the enforcement mechanism. If a student
  can't explain their own code, it doesn't matter where it came from.
- Framing: AI is a tool, like a calculator. A calculator doesn't excuse you
  from understanding multiplication; AI doesn't excuse you from
  understanding code.
- Becomes more relevant Phase 3 onward.

---

## Class culture

### The peanut butter problem

Day 1, Session 1: Eric pretends to be a computer; students give instructions
to make a PB&J sandwich; Eric executes them with willful, deadpan literalness
(jar on bag, comb-as-spreader, etc.). Establishes "computers do what you say,
not what you mean" as the foundational frame for the entire curriculum.

Bring back as callbacks at:

- End of Phase 1 (Scratch demo day) — "look how far you've come"
- Start of Phase 3 (Python Session 1) — when syntax precision is about to bite

Anytime a student gets frustrated their code "doesn't work" → peanut butter
callback.

### Mixed ages and skill levels

- Pair programming by default, rotating pairs every few weeks.
- Tier every project: base / stretch / extension.
- Older / advanced students mentoring younger ones is the highest-leverage
  move. Structured, not ad-hoc.
- If parent volunteers are available as floor-walkers, take them.

### New students joining mid-curriculum

Realistic volume: 2-4 newcomers per year after the initial cohort.

Strategies:

- **Scratch as always-available on-ramp.** Once main cohort moves past Scratch,
  Scratch handouts become a self-paced track. New 9-year-old works through
  Scratch with a mentor while Eric teaches the main lesson.
- **Explicit entry points:** start of Python (after Scratch), start of
  customtkinter (Python basics only), start of web dev (new language).
  Newcomers with prior experience can join at these points with a prep packet.
- **Peer mentorship as infrastructure**, not charity. Recognized publicly.
- **Optional summer intensive** if a cluster of newcomers arrives — 4-6 week
  catch-up bootcamp.

Honest tradeoff: a kid who joins month 18 won't have the same depth as one
who started day one. Goal is "good experience, meaningful finishing point,
doesn't feel lost" — not "identical experience."

### Cross-cutting skills introduction timing

- **Debugging:** day 1 of Python informally ("read the error message"),
  formalized with Thonny's debugger mid-Phase 3.
- **Documentation reading:** modeled live from early Python. "I don't
  remember, let's look it up together" — repeatedly.
- **Getting unstuck:** lives in `appendices/getting-unstuck.md`. Referenced
  constantly.
- **Git:** mid-Phase 4, local-only first. Remote (GitHub) added in Phase 6.

---

## Status

### Locked decisions

- Goal hierarchy (1: logical thinking, 2: practical tool, 3: career foundation)
- Phase arc and rough session counts
- customtkinter for GUI phase
- Handouts-are-the-textbook approach
- Two-file split (student / teacher) per session
- mdBook + GitHub Pages + local copies
- CC BY-SA content / MIT code license
- Twice-yearly public showcases + per-phase internal demo days
- Buddy system mechanics
- "Done" definition (3-part rule)
- AI policy
- Repo layout
- **Phase 1 (Scratch) — all 9 sessions drafted** (Welcome/PB&J,
  Sequences, Loops/Pen, Events, Conditionals, Variables, Putting
  It Together, Milestone Day 1, Milestone Day 2 + Demo Day)
- **Phase 2 (Python with Turtle) — all 8 sessions drafted**
  (Welcome to Python, Turtle commands, Loops, Functions,
  Variables, Conditionals, Garden Scene, Milestone + Demo)
- **Phase 3 (Python basics) — all 16 sessions drafted**
  (Welcome/PB&J callback, Variables and types, Strings + f-strings,
  Conditionals deeper, Loops + debugger, Return values,
  Number-guessing game, Lists, More lists, Dictionaries,
  File I/O, Hangman, Error handling, Text adventure,
  Milestone Day 1, Milestone Day 2 + Demo)
- **Phase 4 (Intermediate Python + CLI + Git) — all 9 sessions
  drafted** (Command line, Multi-file programs, Stdlib modules,
  Light classes intro, Git intro, Git in practice, Testing,
  Milestone Day 1, Milestone Day 2 + Demo)
- **Phase 5 (customtkinter desktop apps) — all 8 sessions
  drafted** (Welcome/first window, Buttons + events, Inputs,
  Choices, Layouts + frames, Putting it together (todo app),
  Milestone Day 1, Milestone Day 2 + Demo)
- **Phase 6 (Pygame 2D games) — all 14 sessions drafted**
  (Welcome/frame loop, Drawing, Sprites, Movement, Collision,
  Build Pong together, GitHub intro, Sound + music,
  Sprite classes + groups, Grid-world intro, Grid-world
  extending, Game state, Milestone Day 1, Milestone Day 2 +
  Demo). **Note:** `grid_world.py` itself (the actual game
  used in Sessions 10-11) is spec'd in the Session 10 teacher
  notes but not yet built — needs ~1-2 hours before those
  sessions can run.
- **Phase 7 (HTML/CSS/JS web) — all 17 sessions drafted**
  (Welcome to the web, HTML tags + structure, CSS basics,
  Box model, Flexbox, Personal homepage, Forms,
  JavaScript intro, DOM, Interactive todo list, localStorage,
  Canvas, Canvas mini-game, Fetch + JSON, GitHub Pages,
  Milestone Day 1, Milestone Day 2 + Demo). **No CSS Grid**
  — Flexbox only per design call.
- `tools/new-session.sh` scaffolder + `tools/build-book.sh`
- GitHub Actions deploy to Pages

### Open questions / future decisions

- Specific milestone project list per phase
- Capstone for the full curriculum (after Phase 8)
- When/whether to add an adult class

### Known unknowns to revisit

- Real session pacing once Phase 1 has run (likely shorter for older students,
  longer for younger; will need to calibrate)
- Whether 9 sessions is actually right for Phase 1 (may be 8 or 10 in practice)
- Whether `customtkinter` ships well via the machine image (verify before Phase 5)
- Whether mdBook build pipeline plays nicely with the textbook's eventual size