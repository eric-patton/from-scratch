## Session 7 — Teacher Notes

*Phase 5, customtkinter · Session 7 of 8 · Title: Milestone
project work day 1*

### Purpose of this session

Their app, their design. Five jobs, in priority order:

1. **Get every kid to a plan.** Before they touch code,
   they need to know what they're building. The six-question
   plan is the gate.
2. **Get every kid to a working window.** Even if it's
   just title + a button that does nothing, the *structure*
   of "I am building a real app" needs to be in place by
   end of class.
3. **Reinforce commit-as-you-go.** Phase 4 introduced this;
   this session bakes it in for GUI work.
4. **Triage early bad ideas.** A kid choosing something
   that won't fit in 90 minutes (or won't fit in
   customtkinter) needs gentle redirect *now*, not next
   week.
5. **Set up Day 2.** What state every kid needs to be in
   to demo successfully next week.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with customtkinter.
- Have the seed-list ideas ready in front of you (the
  student handout has the full list — same one to suggest
  if a kid's stuck).
- Optional: a few example finished apps to show as
  inspiration. Not as a template — as a "this is the kind
  of thing that fits in two sessions."

**Prep time:** ~10 minutes. Re-read the seed list and
pre-think which ideas fit easily in two sessions vs. which
are too ambitious.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 6: they
  built a real app. Today they design their own.
- **Part A — Plan** (~15 min). Six questions. Then
  Mr. Eric checks every plan.
- **Part A — Setup + first build** (~60 min). Folder,
  `git init`, first file, first commit. Then build the
  simplest version. Commit as they go.
- **Wrap-up** (~10 min). Each kid shares one win.

The 60-minute build block is the heart. Roam constantly.
Catch problems early.

### Teaching the planning step

#### The six questions are non-negotiable

Don't let kids skip planning. Five minutes of writing
saves an hour of "what should I do next?" Walk around,
make sure every kid has answered all six.

The most common shortcut: writing #1 ("a calculator") and
skipping straight to coding. Catch this. The widgets
question (#3) is often the most useful — it forces them
to *visualize* the window before building.

#### Triage the plans

When a kid shows you the plan, say one of:

- **"Go build it."** — Plan is reasonable, scoped to fit.
- **"What's the simplest version?"** — They've designed a
  sprawling app. Push them to the core.
- **"What if you cut [feature]?"** — Specific feature is
  out of scope (3D, audio playback, internet API, etc.).
- **"Want to try [seed-list item] instead?"** — Plan
  doesn't fit. Redirect.

Things that **won't** fit in two sessions:
- Multiplayer games over the internet.
- Real audio/video playback (use placeholder buttons).
- 3D anything (curriculum-banned anyway).
- Apps that need a real database. (JSON file is fine.)
- Anything requiring a backend server.
- Apps requiring large image/sound asset libraries.

Things that **will** fit:
- Single-window forms with state.
- Simple games (memory match, tic-tac-toe, dice rolls).
- Calculators / converters.
- Note/list/flashcard apps.
- Drawing pads with `CTkCanvas`.
- Anything todo-shaped (with their own twist).

#### Encourage borrowing

Several kids will (and should) build something that
resembles Session 6's todo app with their own theme. That's
**fine and encouraged**. Their habit-tracker, their
shopping list, their reading log — same shape, their
domain.

### Teaching the build step

#### "Window before logic"

Push every kid to **get a window on screen first.** Even
empty. Even just a label. Then add widgets. Then add
behavior. Don't write logic before there's a window to
attach it to.

#### "Commit before you forget what you did"

After 10-15 minutes of work, ask:

> "When was your last commit?"

If they look blank, walk them through `git status`,
`git add`, `git commit`. Build the muscle memory.

#### Pair-debugging

Encourage the buddy system. If a kid is stuck for more
than 5 minutes, they should buddy up with someone whose
window is on screen.

#### When to redirect to a class

If a kid's `main.py` is ballooning and there are lots of
top-level globals, suggest the class refactor:

> "Your code is getting big. Want to wrap it in a class
> like the Session 6 stretch? It'll be easier to add more
> features."

Don't force it. If the global version works, the global
version works.

### Common stumbles

- **Plan too ambitious.** Most common issue. Triage at
  plan-review time.
- **Forgot to `git init`.** Discover at first commit.
  No big deal — `git init` then commit.
- **Plan but no widgets sketched.** Push them to think
  about layout *before* coding. Drawing on paper is
  encouraged.
- **Stuck on "what should the app look like?"**
  Suggest: copy Session 6's layout (header, input row,
  list area) and modify.
- **Got widgets on screen but no callbacks wired.**
  Common at the end of class. Redirect: get one button
  doing one thing before the next widget.
- **Forgot to attach `command=`** to buttons. Same bug
  as Session 2. Walk through.
- **Layout mess.** Mixed pack and grid in same container.
  Same Session 5 bug. Pick one.
- **Trying to play sound or video.** Redirect: print to
  console as a placeholder.

### Differentiation

- **Younger kids (9-10):** Pick a simpler idea. Calculator
  with 2 numbers, dice roller, simple quiz. Goal: a
  working window with one or two callbacks.
- **Older kids (12+):** Push for state + redraw. Goal: a
  working app with a list or grid that updates.
- **Advanced (any age):** Push for class structure +
  persistence. Goal: production-style code.
- **Struggling:** A kid who can't write the plan is
  the kid you focus on. Walk through the six questions
  with them. Suggest a seed-list idea.

### What to watch for

- **Kids who plan and plan and never start coding.**
  Cut planning short — get them to the keyboard.
- **Kids who skip planning and hit a wall by minute 30.**
  Pull them aside, do the planning together.
- **Buddies trading ideas.** Encourage. Real design
  collaboration.
- **Kids feature-creeping early.** Redirect: "Get the
  base working, *then* add features."
- **Kids hitting customtkinter limits** (no built-in
  audio, etc.). Redirect to placeholder approach.
- **Excitement.** Some kids will love this — building
  *their* idea is genuinely thrilling. Channel it.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 8 (demo).** Today's project becomes next
  week's demo. Push every kid to a state where *some*
  version works, even if minimal.
- **Phase 6 (Pygame).** Their first attempt at a real
  game. Many of the design instincts here (plan, state,
  iterate) transfer directly.
- **Peanut butter callback opportunity:** kids who
  designed something the computer can't actually do
  (live audio, real internet) hit a precision moment —
  the computer takes their plan literally.

### Materials checklist

- [ ] Demo machine with customtkinter
- [ ] Seed-list ideas (in handout, but have them in mind)
- [ ] Optional: example finished apps
- [ ] Projector
- [ ] Class roster
