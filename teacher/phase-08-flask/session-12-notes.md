## Session 12 — Teacher Notes

*Phase 8, Flask · Session 12 of 13 · Title:
Milestone project work day 1*

### Purpose of this session

Last milestone planning. Five jobs, in priority
order:

1. **Get every kid to a plan + a deployed URL
   skeleton.** Both are non-negotiable for next
   week's demo.
2. **Triage scope ruthlessly.** Full-stack apps
   over-scope easily.
3. **Reinforce the deploy loop.** Code locally,
   push to GitHub, pull on PythonAnywhere,
   reload. Practice it today.
4. **Per-user data discipline.** Every query
   filters by user. Same lesson as Session 10.
5. **Set up Session 13 (final demo +
   curriculum close).**

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine.
- Seed list ready.
- Triage list of "doesn't fit in two
  sessions."
- Verify each kid has GitHub + PythonAnywhere
  setup before class. Kids who don't get help
  now.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session
  11 (deployment).
- **Part A — Plan** (~15 min). 9 questions.
  Mr. Eric reviews.
- **Part A — Setup + initial deploy** (~15 min).
- **Part A — Build the simplest version** (~50 min).
- **Wrap-up** (~5 min). Each kid shares
  idea + URL.

The 50-minute build is the heart. Roam.

### Teaching the planning step

#### 9 questions vs 8

Phase 8 adds:

- **Question 5: Database tables.** Forces them
  to think about data structure up front.
- **Question 6: Routes.** Lists all URLs they'll
  need.

Both are non-negotiable for a Flask app.

#### Triage: things that won't fit

When a kid shows you the plan, listen for:

- **Real-time chat / live updates.** Needs
  WebSockets — out of scope.
- **Image / file uploads** beyond the basics.
  Possible but fiddly.
- **Email notifications.** Needs SMTP setup.
- **OAuth login** (sign in with Google). Real
  apps do this; setup is involved.
- **Payments.** Stripe integration is real
  work.
- **Mobile native apps.** Web only.
- **Real-time collaboration.** Operational
  Transform / CRDTs — way too much.
- **Sophisticated search.** Full-text search
  with Postgres or Elasticsearch — out of
  scope. SQLite `LIKE` is fine.

Things that *do* fit:

- Multi-table apps with auth.
- CRUD on user-owned items.
- Search/filter with `LIKE`.
- Public/private content modes.
- Simple admin or moderation.
- Class-friendly multi-user apps.

#### Common over-scope: "I'll have AI features"

> "AI APIs need API keys, cost money, and the
> code is mostly the API call (which we know
> from Phase 7's fetch). For class: skip. Build
> something else; explore AI APIs after the
> curriculum if you want."

#### Common over-scope: "I'll deploy a real
   product"

> "Real products need lots more — moderation,
> abuse handling, terms of service, privacy
> policy, GDPR for EU users, scaling. *Way*
> beyond what fits in two sessions.
>
> *For class*: build something fun, demo to
> classmates, that's enough. If you want to
> launch a real product later, the foundation
> here gets you started."

#### Encourage borrowing

A kid building a notes-app variant with their
own theme? **Encouraged.** A different domain
(recipes, books, journal entries) but the same
shape? **Perfect.** Variations on Session 10
are great milestones.

### Teaching the build step

#### "Deploy on day 1"

Push every kid:

> "Push your skeleton to GitHub *today*. Deploy
> to PythonAnywhere *today*. Even if it's just
> 'Hello world' or signup-only.
>
> Why? *Deployment issues are the worst at the
> last minute.* If your URL works today, all
> your future commits are 'just push.' If you
> wait, the night before demo you're scrambling
> with WSGI configs."

This is real CI/CD discipline. Worth instilling.

#### Roaming priorities

1. **Plan triage** — first 15 minutes.
2. **Deploy verification** — next 15.
3. **Code support** — bulk of session.

Get every kid past the deploy hurdle before
moving to code questions.

#### When a kid's app crashes on PythonAnywhere

Walk through:

1. **Error log** — Web tab, "Server log"
   link.
2. **Trace the error** — usually missing
   import or missing module.
3. **Fix locally**, push, pull, reload.

The error-log → fix → reload loop is real
production debugging.

### Common stumbles

- **Plan too ambitious.** Triage at review.
- **No GitHub setup.** Catch up. Phase 6
  Session 7 + Session 11.
- **No PythonAnywhere account.** Sign up now.
- **Database file committed accidentally.**
  Add to `.gitignore`, `git rm --cached`.
- **`secret_key` hardcoded "dev-secret."**
  Fine for class; mention env vars.
- **Forgot per-user filter.** Walk through
  Session 10 lesson.
- **Deploy works, app crashes on first
  request.** Probably DB path issue. Use
  `__file__`-relative path.
- **Forms broken on deployed app.**
  `methods=["GET", "POST"]` missing.
- **Static files 404 on deployed app.**
  PythonAnywhere static-files mapping in
  Web tab.
- **Migration mid-session** — if they change
  the schema, the deployed DB needs `ALTER
  TABLE` or recreation.

### Differentiation

- **Younger kids (9-10):** Pick a simpler
  idea — habit tracker, reading log, bookmark
  manager. Goal: signup + add-and-list
  working at a URL.
- **Older kids (12+):** Push for full CRUD
  + at least one bonus.
- **Advanced (any age):** Push for multi-table
  + search + public mode + polished CSS.
- **Struggling:** A kid who can't write the
  plan is the kid you focus on. Walk through
  the 9 questions together.

### What to watch for

- **Plans too ambitious.** Spot at review.
- **Kids who plan and never deploy.** Cut
  planning short. Get to deploy.
- **Buddies signing up for each other's
  in-progress apps.** Real testing. Encourage.
- **Excitement about real users.** "My friends
  can use this?" Yes.
- **Frustration with deployment errors.**
  Patience. Walk through error logs.
- **Kids deploying before pushing.** Verify
  the deploy reflects their latest code.
- **Last-session energy.** Some kids might
  feel "we're almost done!" — channel into
  finishing strong.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 13 (final demo + curriculum
  close).** Today's project becomes their
  final demo at a real URL.
- **Phase 7 callback:** they have a personal
  homepage. Cross-link to this Flask app
  for a unified portfolio.
- **Career-long callback:** the deploy-via-
  push workflow is real software engineering.
- **Peanut butter callback opportunity:** the
  forgot-to-pull-on-PythonAnywhere bug — code
  on GitHub is updated, but the URL still
  shows old version. Precision: deploy is a
  separate step.

### Materials checklist

- [ ] Demo machine
- [ ] Seed list
- [ ] Triage list
- [ ] Pre-class verification of GitHub +
      PythonAnywhere accounts
- [ ] Projector
- [ ] Class roster
