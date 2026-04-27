## Session 16 — Teacher Notes

*Phase 7, Web · Session 16 of 17 · Title: Milestone
project work day 1*

### Purpose of this session

Their web project, their design. Five jobs, in
priority order:

1. **Get every kid to a plan.** 8-question plan
   gates the build.
2. **Get every kid to a deployed URL.** Push the
   skeleton today, even if there's just a heading.
   Live URL = real demo.
3. **Triage scope ruthlessly.** Web projects can
   easily over-scope. Catch at plan-review.
4. **Reinforce push-to-deploy workflow.** Every
   commit *can* be a deploy. Build the muscle.
5. **Set up Day 2.** Demo prep starts today.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Have the seed list ready.
- Optional: 2-3 finished example projects from
  prior classes for inspiration.
- A scope-reality-check list of "doesn't fit in
  two sessions."

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 15.
  Today: their project.
- **Part A — Plan** (~15 min). 8 questions. Mr.
  Eric reviews.
- **Part A — Setup, push, enable Pages** (~15 min).
- **Part A — Build the simplest version** (~50 min).
- **Wrap-up** (~5 min). Each kid shares one win.

The 50-minute build is the heart. Roam constantly.

### Teaching the planning step

#### 8 questions, plus deployment

Phase 7 milestone has *two* requirements past
previous phases:

1. **Hosted on GitHub Pages.** Live URL.
2. **Looks styled** (not raw HTML).

Make sure both are covered in the plan.

#### Triage: things that won't fit

When a kid shows you the plan, listen for:

- **Multi-user / accounts / auth.** No backend = no
  accounts.
- **Real-time collaboration.** Needs a backend.
- **Anything that needs a server-side database.**
- **Real video processing / AI / ML.** Way too much.
- **Native mobile app.** Web only.
- **Complex animations / WebGL / Three.js.** Not in
  curriculum scope.

Things that *do* fit:

- Single-page apps with localStorage.
- Static content sites.
- Canvas games (with the Session 13 patterns).
- Fetch-based data displays.
- Calculators, converters, generators.
- Multi-page sites (linked HTML files).
- Image galleries.

#### Common over-scope: "I'll add accounts"

> "Accounts need a backend. We don't have one in
> this phase. Phase 8 (Flask) covers that.
>
> Without accounts, you can do *single-user* state
> with localStorage — perfect for personal apps.
> Add 'accounts' to your future-features list."

#### Common over-scope: "I'll fetch from a private API"

Most fun APIs are public. Push toward those.

If they need data unique to them (their
schedule, their photos), localStorage handles it
single-user.

#### Encourage borrowing

A kid building a "Pokemon explorer" extending
Session 14's search? **Encouraged.** A todo with
their own theme? Fine. Bigger versions of any
in-class example are great milestone material.

### Teaching the build step

#### "Deploy on day 1"

Push every kid to **deploy something today.** Even
just a `<h1>Coming soon</h1>` deployed to a real
URL. Why?

> "If you wait until next session to deploy, you
> have no buffer. Something will go wrong. Today:
> get the URL working, *then* build. Every commit
> is a deploy. By demo, you'll have a polished
> live site."

This is real CI/CD discipline. Worth instilling.

#### "Push every commit"

Encourage habit:

> "Every time you commit, push. Watch your changes
> go live in 30 seconds. Develop the
> commit-and-deploy reflex now."

#### Roaming priorities

Walk constantly. Help with:

- **Plan review.** First priority.
- **Pages setup.** Second.
- **Code questions.** Third.

Catch kids who are stuck early. The 50-minute build
is where most of the value happens.

#### When a kid's repo isn't deploying

Most common:

1. Repo is private (Pages requires public for free
   accounts).
2. No `index.html` at root.
3. Pages source not set in Settings.
4. Just need to wait — first deploy can take 5+
   minutes.

Walk through. Don't move on until their URL works.

### Common stumbles

- **Plan too ambitious.** Triage at plan review.
- **Forgot to enable Pages.** Walk through.
- **Pages enabled but 404.** No `index.html` at
  root. Or wrong branch selected.
- **No GitHub account.** Catch up. Phase 6 Session
  7.
- **Git push errors.** PAT issues, wrong remote.
- **Layout broken when pushed.** CSS file path
  wrong. Likely an absolute path that worked
  locally but not on Pages. Use relative paths.
- **JS not running on deployed site.** External JS
  file path wrong, or browser caching old version.
- **API doesn't work on Pages.** Probably mixed
  content (HTTP API, HTTPS Pages). Use HTTPS APIs.
- **Image not showing on deployed site.** File not
  pushed (forgot `git add image.png`), or wrong
  case (Linux servers are case-sensitive).

### Differentiation

- **Younger kids (9-10):** Pick a simpler idea —
  recipe site, calculator, simple flashcard. Goal:
  HTML+CSS+a little JS, deployed.
- **Older kids (12+):** Push for full HTML+CSS+JS
  with at least one of: fetch, localStorage,
  canvas.
- **Advanced (any age):** Push for multi-feature
  apps with all bonus categories. Full README.
  Mobile-tested.
- **Struggling:** A kid who can't write the plan
  is the kid you focus on. Walk through the 8
  questions together. Suggest a seed-list idea.

### What to watch for

- **Plans too ambitious.** Triage at review.
- **Kids who plan and never start coding.** Cut
  planning short.
- **Kids who skip planning and hit a wall.** Pull
  aside, re-plan.
- **Buddies trading project ideas.** Encourage.
- **Excitement about the URL.** "I can send the
  link to my mom right now?" Yes. Real.
- **Kids deploying broken pages.** Yes — that's OK.
  Iterate.
- **Sound/music projects.** HTML5 Audio works fine.
  Phase 6 Session 8 sound knowledge applies.
- **Phase 6 callback projects** (kid wants to do
  Pong on canvas) — encourage.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 17 (demo).** Their URL is the demo.
- **Phase 8 (Flask).** Backend for the things that
  needed accounts/databases. Some milestone
  projects could be expanded in Phase 8.
- **Career-long callback:** "Plan, build smallest,
  iterate, deploy" is the modern web workflow.
  Real practice.
- **Peanut butter callback opportunity:** scope
  creep + deploy timing — a plan that designed
  more than two sessions can fit, and then
  scrambled at the end. Precision: budget time.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Seed list (in handout, but ready to suggest)
- [ ] Optional: example finished projects
- [ ] Triage list of "won't fit"
- [ ] Projector
- [ ] Class roster
