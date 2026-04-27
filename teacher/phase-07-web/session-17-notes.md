## Session 17 — Teacher Notes

*Phase 7, Web · Session 17 of 17 · Title: Milestone
project work day 2 + demo day*

### Purpose of this session

Phase 7 finale + bridge to Phase 8. Five jobs, in
priority order:

1. **Get every kid to "demo-able at a live URL."**
   The URL part is non-negotiable. Public site or
   no real Phase 7 demo.
2. **Run the demos well.** Format is similar to
   Phase 6 with a key addition: **audience visits
   the URL during the demo.**
3. **Push every kid to verify their URL works.**
   Pre-demo URL check is critical.
4. **Celebrate the public-internet moment.** Their
   work is *truly* shareable now. Pause for it.
5. **Bridge to Phase 8 (Flask).** Final phase
   incoming. Front-end → back-end. The full stack.

### Before class

**Bring:** nothing physical (maybe a small
celebration item — stickers, certificates, etc.).

**Set up:**

- Demo machine with browser + Thonny.
- Projector with browser ready.
- A list of every kid's expected GitHub Pages URL
  to verify ahead of time.
- Phase 8 framing notes.

**Prep time:** ~15 minutes (plus testing each kid's
URL ahead of class).

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Today: finish +
  demo + close phase.
- **Part A — Final polish** (~35 min). URL
  verification, polish, README, push.
- **Part B — Demo day** (~40 min). 3-5 min per kid
  with URL audience visits.
- **Phase 7 close + Phase 8 framing** (~10 min).

For 6-8 kids, demos fit in 35-40 min. For more,
trim to 3 min per kid.

### Teaching Part A — polish

#### Verify URLs first

Walk past every kid in the first 10 minutes:

> "Open your URL on your machine. Does it load?
> Does it work? Anything broken?"

Common issues at this stage:

- URL 404s (Pages config wrong, or no
  `index.html`).
- Site loads but JS broken (file path issue, or
  external resource blocked).
- Layout wrecked on certain widths.
- Feature works locally but fails on Pages.

Fix these *first*. Polish is secondary.

#### "Working > impressive"

Same as every milestone:

> "A simple working app at a live URL beats a
> half-finished ambitious one. Polish what works."

#### README is part of finished

Push every kid:

> "Add a README to your repo with: what your app
> does, the live URL, and one sentence about how
> to use it. *Today.*"

This makes their GitHub repos look real. Good for
parents to see, future-them to see.

#### Buddy URL test

The Phase 7 specific: **buddies visit each other's
URLs on their machine.** Different from Phase 6
where the game ran on Mr. Eric's machine.

> "Send your URL to your buddy. They open it. They
> use it. Anything broken? Now's the time."

Real "shareable" moment.

#### Mobile check

If a kid has a phone (or you do): visit their URL
on the phone. Does it work? If broken, the
problem is usually:

- Hardcoded widths in CSS.
- Tiny text.
- Buttons too small to tap.

Add a `@media (max-width: 600px)` rule with bigger
fonts / different layout.

### Teaching Part B — demos

#### Set the celebratory tone

> "Today is special. You finished Phase 7 — the
> web. Your code is on the internet. Anyone can
> visit. We're going around the room — each of
> you shows your URL, walks us through the app,
> someone else opens it on their machine. After
> everyone, we celebrate."

#### Demo format additions

Phase 7 demo:

1. URL on the projector.
2. Live use.
3. **A classmate visits the URL on their machine.**
4. Walk through code or repo briefly.
5. One hard thing.
6. One question.

The audience-visits-URL part is the Phase 7
unlock. Hand laptops around.

#### What to ask each kid

Specific:

- "What was the trickiest CSS issue?"
- "How did you find the API you used?"
- "What feature did you cut?"
- "If you had another week, what would you add?"
- "Did you test on a phone?"

#### After all demos

Brief acknowledgment per kid (specific). Then:

> "You've finished Phase 7. Your work has a URL.
> Anyone in the world can use it.
>
> Seven projects shipped:
> - [Phase 1]
> - [Phase 2]
> - [Phase 3]
> - [Phase 4]
> - [Phase 5]
> - [Phase 6]
> - [Phase 7]
>
> Three of those are *on the internet right now*
> — your homepage, your todos, today's project.
>
> Phase 8 is the last phase. The back-end. Python
> on a server. Real multi-user apps. See you
> next week."

### Teaching the Phase 8 bridge

Frame Phase 8 carefully:

> "Phase 8 is the back-end. Server-side code. Until
> now everything has run *on the user's machine*
> — Pygame on their computer, your web pages in
> their browser.
>
> Phase 8: code that runs on a *server somewhere*.
> Multiple users hit it. Their data is stored
> centrally. Real apps.
>
> Tools: Python (you know it), HTML (you know it),
> Flask (a web framework that ties them together),
> SQLite (a database). All beginner-friendly.
>
> By Phase 8 demo, you'll have built a full-stack
> app — front-end and back-end — like a real
> software engineer. Last big climb."

### Common stumbles

- **URL 404s on demo day.** Pages config issue.
  Triage: is the repo public? Is `index.html` at
  root? Settings → Pages set?
- **Site shows but feature broken.** External
  file path issue (CSS, JS, image). Fix paths,
  push.
- **Forgot to push final version.** Demo shows
  old version. Push fresh.
- **API call works locally but not on deployed
  site.** Mixed content (HTTP API + HTTPS Pages),
  or CORS issue. Switch to HTTPS API.
- **Mobile broken.** Suggest media query.
- **Demo runs long.** Polite cap at 5 min.
- **Pre-demo nerves.** Pair with buddy.
- **Comparison anxiety.** Their site is "small"
  next to someone's elaborate one. "Both shipped.
  Both work. Both at real URLs."

### Differentiation

- **Younger kids (9-10):** A working basic site at
  a URL is enough. Demo what works.
- **Older kids (12+):** Push for full polish —
  README, mobile, all features working.
- **Advanced (any age):** Push for cross-linked
  multi-project portfolio. Suggest custom domain.
- **Struggling:** A kid whose site barely runs
  needs the **show what works** treatment. Even
  one feature is a real demo.

### What to watch for

- **The "MY URL!" moment** during their demo. Real.
- **Buddies visiting URLs in real time during
  someone's demo.** Encourage. Gives instant
  feedback.
- **Excitement about parents seeing it.** Many kids
  send the URL to family during/after class.
- **"What if I want this on a custom domain?"**
  Real interest. Out of curriculum scope but
  affirm.
- **Phase 8 anticipation** — "We're learning the
  back-end?" Yes. Build excitement.
- **The "I'm tired of HTML" moment** — some kids
  might be ready to be done. Phase 8 reframe is
  the reset (Python again, just on a server).
- **End-of-curriculum thinking.** Phase 8 is the
  last. Some kids may start asking "what after
  this?" Time to think about that.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Phase 8 (Flask).** The full-stack capstone.
  Server-rendered pages, databases, user accounts.
  Today's HTML/CSS skills + Phases 3-4 Python =
  ready.
- **Career-long callback:** every web developer
  needs front-end + back-end. Today closes the
  front-end story. Phase 8 opens the back-end.
- **Long-term:** kids may keep building. Their
  GitHub Pages stays free forever. Their apps can
  grow.
- **Peanut butter callback opportunity:** the
  forgot-to-push-before-demo bug is a precision
  moment. The deployed version isn't the same as
  the local version unless you push.

### Materials checklist

- [ ] Demo machine with browser
- [ ] Projector
- [ ] List of expected URLs to verify ahead of
      class
- [ ] Phase 8 framing notes
- [ ] Optional: small celebration items
- [ ] Class roster
