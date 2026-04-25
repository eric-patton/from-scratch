# Instructions for Claude

This file orients AI assistants (Claude Code, etc.) working on this
repository. Read it before doing anything else.

## What this project is

A two-year programming curriculum for kids and teens (ages 9+) at Old
Zion Hill church, taught by Eric Patton ("Mr. Eric" to students). The
deliverable is a textbook compiled from per-session student handouts,
plus matching teacher notes and lesson code.

## Read these first

Before making any changes or generating any content, read:

1. **`CURRICULUM-DECISIONS.md`** — locked design decisions, goal hierarchy,
   phase arc, conventions. This is the single source of truth for "why
   are we doing it this way." Honor it.
2. **`README.md`** — high-level project overview and repository layout.
3. **Any existing session files** in `src/` and `teacher/` that touch the
   area you're working on. Match their voice, structure, and depth.

If a request seems to conflict with `CURRICULUM-DECISIONS.md`, surface
the conflict to Eric rather than silently overriding. The decisions
doc is updated when decisions change — don't change behavior without
updating the doc.

## Voice and audience

### Student handouts (`src/`)

- **Audience:** kids and teens, ages 9-15, mixed reading levels.
- **Voice:** warm, direct, second-person. "You'll learn..." not
  "Students will learn..." Talk *to* the student, not about them.
- **Tone:** playful where it fits, never condescending. Kids notice
  condescension instantly. Trust them with real ideas; explain
  unfamiliar terms when introduced.
- **Length:** ~1000-3000 words per session, depending on phase complexity.
  Phase 1 (Scratch) shorter; Phase 7 (web) longer.
- **Voice principle:** the handout must read coherently to a student
  who missed class. They are a textbook chapter, not lecture notes.

Refer to the teacher as **"Mr. Eric,"** never "Mr. Patton" or "the
teacher." Students already call him Mr. Eric from other church
activities.

### Teacher notes (`teacher/`)

- **Audience:** Eric, future-Eric, possible future co-teachers.
- **Voice:** practical, candid, peer-to-peer. Eric is a principal
  software engineer with 15+ years of experience — write to that level.
  Don't over-explain pedagogy basics; do flag genuinely tricky teaching
  moments.
- **Include:** specific moves to make, things to watch for, common
  stumbles, how to handle the bored advanced kid and the lost younger
  kid, what to say at key moments.
- **Always include an "After class" section** for Eric to fill in
  post-session. This is the highest-compound-interest part of teacher
  notes — five minutes of reflection makes year two substantially
  better than year one.

## File conventions

### Per-session, three artifacts

For session N of phase X (e.g., Phase 1 Scratch Session 3):

- `src/phase-01-scratch/session-03-loops.md` — student handout
- `teacher/phase-01-scratch/session-03-notes.md` — teacher notes
- `code/phase-01-scratch/session-03-loops/` — lesson code (when applicable;
  Scratch sessions may not have code files)

Filenames use kebab-case. Phase numbers and session numbers use leading
zeros (`01`, not `1`) for correct sorting.

### Student handout structure

Every student handout has these sections, in this order:

1. **Title block** — `## Session N: Title` followed by phase/position line
2. **What we're learning today** — 2-3 sentences, student voice
3. **You'll need to remember from last time** — bullet list, 3-5 items
   (use "Nothing! This is your first session." for Session 1 of a phase
   if appropriate)
4. **Part A** — concept + guided exercise. Must end at a checkpoint that
   stands alone if class is cut short. Mark this clearly.
5. **Part B** — extended practice or mini-project. Tiered when relevant
   (base / stretch / extension).
6. **Wrap-up**
7. **If you missed this session** — self-paced ~20-30 min catch-up version
8. **Stretch and extension ideas**
9. **What's next** — one sentence

### Teacher notes structure

Every teacher notes file has these sections, in this order:

1. **Purpose of this session** — what jobs it's doing, in priority order
2. **Before class** — materials, setup, prep time estimate
3. **Timing and flow** — rough minute-by-minute, where to cut if short
4. **Teaching Part A** — specific moves, lines to land, things to model
5. **Teaching Part B** — same
6. **Common stumbles** — student misconceptions and how to address
7. **Differentiation** — younger / older / advanced / struggling
8. **What to watch for** — behavioral signals, kids needing attention
9. **After class** — explicitly blank, for Eric to fill in post-session
10. **Connections forward** — callbacks, future references
11. **Materials checklist** — at the very end, for quick scanning

## Recurring devices to honor

These are established class culture; reference them when relevant:

- **The peanut butter problem** (Session 1 Phase 1). Computers do exactly
  what you say, not what you mean. Callback whenever a student gets
  frustrated their code "doesn't work" because of a precision/literalness
  issue. Explicit callback moments planned for end of Phase 1 and start
  of Phase 3.
- **The "explain how it works" rule.** A student isn't done with an
  exercise until they can explain their own code. This is the enforcement
  mechanism for the AI policy and the bulwark against cargo-cult coding.
- **Buddy first, Mr. Eric second.** Students ask their buddy before
  asking the teacher.
- **"Done for today" vs. "done with the topic."** Perfectionists need
  permission to stop. Surface this in handouts when relevant.

## What to do when uncertain

- If a curriculum question isn't covered in `CURRICULUM-DECISIONS.md`,
  ask Eric rather than guessing.
- If two locked decisions seem to conflict, surface that explicitly —
  it's a doc bug, not a license to improvise.
- If you're tempted to add a topic that "would be cool to cover," check
  it against the goal hierarchy in `CURRICULUM-DECISIONS.md`. The
  curriculum is intentionally lean.

## What to avoid

- **Don't pad.** Sessions should run as long as they need to, not as
  long as a template suggests.
- **Don't introduce build tools** (Webpack, Vite, npm-heavy workflows).
  The W202NA hardware can't handle them. CDN + vanilla JS in the web phase.
- **Don't introduce 3D graphics or 3D game development.** Hardware
  constraint, deferred indefinitely.
- **Don't switch IDEs or frameworks** without updating
  `CURRICULUM-DECISIONS.md` first. Thonny for Python, customtkinter for
  GUI, Pygame for games, Flask for web — these are committed.
- **Don't write to `teacher/`-style files in `src/`** or vice versa.
  The split is deliberate.
- **Don't reproduce song lyrics, copyrighted poems, or large chunks of
  copyrighted material** in handouts. Original examples only.
- **Don't generate names of real children or families** in examples.
  Use generic names ("Alex," "Sam") or biblical names that aren't
  identifying. Eric will populate any real-student-specific content.

## Working style preferences

Eric is a principal engineer. He prefers:

- **Direct over diplomatic.** If a proposed approach has problems,
  say so plainly. Don't bury concerns under hedges.
- **Reasoned recommendations over option dumps.** When asked "what
  should we do," give a clear recommendation with reasoning, not a
  menu of equally-weighted choices. Offer alternatives only when the
  tradeoffs genuinely warrant a real decision from him.
- **Small batches with checkpoints.** When designing many sessions,
  do 2-3 at a time, then pause for review and calibration before
  continuing. Don't dump 10 sessions at once.
- **Acknowledge errors quickly.** If you made a mistake, own it, fix
  it, move on. No excessive apology, no hedging, no defensiveness.

## Git and commits

This is a personal-account repo. Commit attribution and SSH routing
diverge from the system defaults — get this right or commits land
under the wrong identity.

- **Remote URL:** `git@github-personal:eric-patton/from-scratch.git`.
  Uses the `github-personal` SSH host alias from `~/.ssh/config`,
  which routes through `id_ed25519_personal` and authenticates as
  `eric-patton`. The default `github.com` host routes through the
  *work* key and authenticates as `eric-patton-bam` — wrong account
  for this repo.
- **Commit email:** `ursine.blue@proton.me`, set per-repo via
  `git config user.email` inside this repo. Global git config still
  carries the work email — don't change it globally.
- **Author name:** `Eric Patton` (global config, no override needed).
- **Ignored from git:** `CONVERSATION-CONTEXT-INTERNAL.md` is in
  `.gitignore` — working notes, not for the public repo.

## Current status

See the **Status** section at the bottom of `CURRICULUM-DECISIONS.md`
for what's locked and what's still open. As of this writing:

- Infrastructure is locked.
- Phase 1 Session 1 is drafted (both files).
- Sessions 2-9 of Phase 1 are next, in two-file format, in batches of 2-3.
- Phase 2 design hasn't started.