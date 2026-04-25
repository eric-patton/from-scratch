# Teacher notes

This directory holds prep notes, policies, and working documents for
running the class. **Nothing in here is published to the textbook.**
mdBook only builds files in `src/`, so this whole tree stays internal.

If you're a future co-teacher (or future Eric), start here, then read
[`CURRICULUM-DECISIONS.md`](../CURRICULUM-DECISIONS.md) and
[`CLAUDE.md`](../CLAUDE.md) at the repo root. Those two carry the
*why* behind every structural choice in the class. This directory is
the *how*: what to do in the room, week by week.

## Layout

```
teacher/
├── README.md                       this file
├── policies/
│   ├── attendance.md               how absences are handled
│   ├── buddy-system.md             how pairings work
│   └── showcase-rhythm.md          milestone and showcase cadence
└── phase-XX-name/
    └── session-XX-notes.md         per-session prep notes
```

Per-session teacher notes live in parallel with the student handouts:

- `src/phase-01-scratch/session-01-welcome.md` — what students read
- `teacher/phase-01-scratch/session-01-notes.md` — what you read
  before walking in

The split is deliberate. Student handouts are clean, public, and
become textbook chapters. Teacher notes are private working
documents — full of "skip the second example, it confused everyone
last year" and similar reality. Mixing them was a mistake we caught
early. Keep them separate.

## Per-session structure

Every teacher notes file has these sections, in this order:

1. **Purpose of this session** — what jobs it's doing, in priority
   order
2. **Before class** — materials, setup, prep time estimate
3. **Timing and flow** — rough minute-by-minute, where to cut if
   running short
4. **Teaching Part A** — specific moves, lines to land, things to
   model
5. **Teaching Part B** — same
6. **Common stumbles** — student misconceptions and how to address
7. **Differentiation** — younger / older / advanced / struggling
8. **What to watch for** — behavioral signals, kids needing
   attention
9. **After class** — *blank by design.* Fill in after teaching, for
   next year's run.
10. **Connections forward** — callbacks, future references
11. **Materials checklist** — at the very end, for quick scanning

The **After class** section is the highest-compound-interest piece.
Five minutes of post-session reflection makes year two of the class
substantially better than year one. By year three, your teacher
notes are worth more than the handouts.

The scaffolder script `tools/new-session.sh` produces both the
student handout and this notes file pre-filled with the right
section structure. Use it.
