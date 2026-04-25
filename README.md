# From Scratch Programming Class

A free programming curriculum for kids and teens (ages 9+), originally
built for a weekly class at a local church. This repository contains
the full curriculum: student handouts (which compile into a textbook),
teacher notes, lesson code, and supporting tooling.

## What this is

About 150 hours of curriculum content, designed for ages 9 and up,
that takes students from no programming experience through Scratch,
Python, desktop apps, 2D games, web development, and small web
applications. How long that takes depends on how often the class
meets — roughly 1.5-2 years at one session per week, closer to a
year at twice a week. The class is free for life — students keep
their machines, and they can come back any time, even years later.

The full curriculum design rationale lives in
[`CURRICULUM-DECISIONS.md`](./CURRICULUM-DECISIONS.md).

## The textbook

Every session's handout is written as a self-contained chapter.
Compiled with [mdBook](https://rust-lang.github.io/mdBook/), the
handouts become a browsable, searchable textbook. Students can use it
to catch up on missed sessions, read ahead, or reference material long
after the class is over.

The textbook is hosted at *(GitHub Pages URL — TBD)* and a local copy
lives on every student's machine for offline reading.

### Building the textbook locally

Prerequisites: [`mdbook`](https://rust-lang.github.io/mdBook/guide/installation.html)

```sh
mdbook build      # builds the static site to ./book/
mdbook serve      # serves locally at http://localhost:3000 with live reload
````

## Repository layout

```
src/                  textbook source (student-facing) — published
code/                 starter code, exercises, and reference solutions
teacher/              teacher prep notes (not published)
assets/               images, diagrams, screenshots
tools/                internal scripts (session scaffolding, build helpers)
appendices/           cross-cutting reference material (in src/)
```

Each session has three matching artifacts:

- `src/phase-XX-name/session-XX-title.md` — student handout (textbook chapter)
- `teacher/phase-XX-name/session-XX-notes.md` — teacher prep notes
- `code/phase-XX-name/session-XX-name/` — starter code, exercises, solutions

Solutions are intentionally public, in clearly-labeled `solutions/` subdirectories. The honor-system framing: "If you peek before trying, you're cheating yourself, not me."

## For students

Open the textbook at _(URL)_ or read the local copy on your machine. Each chapter corresponds to one class session. If you missed a session, look for the **If you missed this session** section near the end of the chapter — it's a self-paced version that gets you ready for next time.

## For parents

The textbook's [for-parents page](./src/for-parents.md) _(coming soon)_ explains what students will learn, when, and how. The class is free and open to kids ages 9 and up. Local logistics (where, when, who teaches) vary by instance.

## For other teachers / churches

This curriculum is licensed permissively because the goal is for it to be useful beyond the original church class. Fork it, adapt it, run your own class. The only ask is attribution.

- **Textbook content:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Code (lesson code, scripts, tooling):** MIT

If you adopt this curriculum at another church or organization, Eric would love to hear about it. Open an issue or send a pull request.

## Contributing

For now, this is primarily Eric's project, but corrections, typo fixes, and suggested improvements via pull request are welcome. For larger changes (new phases, restructuring), open an issue first to discuss.

## Status

Currently in active design. Phase 1 (Scratch) Session 1 is drafted; Sessions 2-9 are next. Curriculum is being written ahead of teaching, with adjustments planned after the first year of running it.

See [`CURRICULUM-DECISIONS.md`](./CURRICULUM-DECISIONS.md) for the locked-in design decisions and open questions.