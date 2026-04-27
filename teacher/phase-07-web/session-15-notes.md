## Session 15 — Teacher Notes

*Phase 7, Web · Session 15 of 17 · Title: GitHub
Pages — host your work*

### Purpose of this session

The "your work goes public" session. Five jobs, in
priority order:

1. **Get every kid's homepage on a public URL.** The
   single most important outcome.
2. **Land the deploy-via-push workflow.** Edit, commit,
   push → live in a minute. Real CI/CD on the cheap.
3. **Land the URL pattern.** `<username>.github.io/
   <repo>/` for normal repos; `<username>.github.io/`
   for the special repo.
4. **Set up Sessions 16-17 (milestone).** The
   milestone *must* be deployed by demo. Today's
   skill is the prerequisite.
5. **Celebrate the public URL moment.** This is real.
   Their work is on the internet. Match the energy.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Your own GitHub Pages demo URL ready to show.
- A pre-built `homepage` repo from a prior class (or
  Mr. Eric's own homepage) that's already deployed
  — so you can demo the URL working.
- Any kids who don't have GitHub accounts (missed
  Session 7 of Phase 6) — pre-identify them so you
  can help with account creation in class.

**Prep time:** ~20 minutes.

### Timing and flow

Total: ~90 min — possibly tight.

- **Welcome and recap** (~5 min). "Your work goes
  public today."
- **Part A: push homepage repo** (~25 min).
- **Part A: enable Pages, get URL** (~15 min).
- **Part A: edit, push, watch deploy** (~10 min).
- **Break** (~5 min).
- **Part B: deploy more projects** (~25 min).
- **Wrap-up** (~5 min). URL share-around.

If running short, **drop "deploy more projects."**
The base goal — homepage on a public URL — is the
priority.

### Teaching the framing

#### "From your machine to the world"

Open with the framing:

> "Your work has lived on your laptop. The kids
> next to you can see it on your screen. *That's
> it.*
>
> Today: your work lives on the internet. *Anyone*
> with the URL can see it. Your parents on their
> phone. Your friend in another state. Anyone, any
> device, any time.
>
> That's the *real* power of the web. Today you
> claim it."

This framing matters. The "my code is on the
internet" feeling is a real shift.

### Teaching Part A

#### GitHub setup checks

Before pushing the homepage, verify each kid:

1. Has a GitHub account.
2. Has a working PAT (or SSH key).
3. Has `git` working in their terminal.

If any are missing: catch up first. Phase 6 Session
7 is the reference.

#### Push the homepage

Walk through `git init` → first commit → connect
remote → push. Same as Phase 6 Session 7.

The most common stumble: kids who didn't have their
homepage in a `git`-ed folder yet. Walk through.

#### Enable Pages — slow, dramatic

The Settings → Pages → Save flow is mechanical but
slightly satisfying. Walk through on the projector
slowly:

1. Open the repo on GitHub.
2. Settings tab.
3. Pages (left sidebar — easy to miss).
4. Source: "Deploy from a branch."
5. Branch: main, folder: / (root).
6. Save.

The "Your site is live at..." message at the top
— that's the moment.

#### Wait for deploy

The first deploy takes 1-2 minutes. Use the time:

- Walk around, help kids who need it.
- Mention the URL pattern.
- Hint at the bigger picture (frame Phase 7's whole
  arc — "you've gone from blank file to deployed
  site in 17 sessions").

#### The URL moment

When kids click their URL and see their page:

> "*That* is the URL. Send it to your parents.
> Right now. They can open it on their phone."

Pause. Let it land. Some kids will visibly process
it.

#### Edit, push, deploy

Show the loop. Edit a heading. Save. Commit. Push.
Wait 30 seconds. Reload the URL. Change appears.

> "*This* is how real deployments work. Push to
> main, the world sees it. Big sites, small sites
> — same pattern."

(Real production has staging, CI, tests, etc. We're
keeping it simple.)

### Teaching Part B

#### "Each project = one repo = one URL"

Frame:

> "Every Phase 7 project can have its own URL. Todo
> list at one URL. Game at another. Fetch demo at
> another. Your homepage links to them all."

Push curious kids toward deploying multiple. The
process is repetitive but not hard.

#### Cross-linking — the portfolio realization

When kids realize they can link their deployed
projects from their homepage:

> "*That's a portfolio.* Your homepage is the front
> door; each project is a room. Anyone can tour."

Several kids will get visibly excited about this.
Real web identity.

#### Pygame note

Real talk:

> "Phase 6 Pygame games can't run on GitHub Pages
> directly — they need Python on the user's
> machine. Today's deployment is for HTML/CSS/JS
> only. To put a Pygame game online, you'd need
> tools like Pyodide (running Python in the
> browser) — outside our scope.
>
> So: deploy Phase 7 projects today. Phase 6
> projects can have *pages about them* (with
> screenshots, descriptions, GitHub links) but
> not playable in browser."

Manage expectations.

### Common stumbles

- **No GitHub account / lost PAT.** Catch up. Phase
  6 Session 7.
- **Push errors.** Wrong remote URL, wrong PAT,
  wrong branch name. Same Phase 6 Session 7
  troubleshooting.
- **Settings → Pages doesn't show source options.**
  Repo is private — Pages requires public for free
  accounts. Make repo public.
- **404 on the URL.** Deploy still in progress.
  Wait 1-2 more minutes.
- **404 after deploy.** Repo doesn't have an
  `index.html`. Make sure file is at root, named
  exactly `index.html`.
- **Page loads but stylesheet missing.** Path issue
  in `<link href="styles.css">`. Make sure path
  is correct relative to `index.html`.
- **External resources don't load.** Mixed content
  — the page is HTTPS but loading HTTP resources.
  Use HTTPS URLs.
- **Old version showing after push.** Browser
  cache. Hard reload (Ctrl+Shift+R).
- **GitHub Pages takes 5+ minutes.** Sometimes
  slow. Wait.
- **Repo named `username.github.io` doesn't work.**
  Username case-sensitivity. Lowercase only.

### Differentiation

- **Younger kids (9-10):** Goal is *one* deployed
  URL. Stop there. The deployment loop is enough.
- **Older kids (12+):** Push for multiple deployed
  projects + cross-linking from homepage.
- **Advanced (any age):** Suggest:
  - The `username.github.io` root repo
  - Custom domain (if they have one)
  - Add proper README to each repo with screenshots
  - Verify mobile rendering
  - Try a static site generator like Jekyll (built
    into Pages — out of curriculum scope)
- **Struggling:** A kid who can't get the push
  working is the kid you focus on. Most common
  cause: PAT expired, wrong username in URL.

### What to watch for

- **The "MY URL!" reaction.** Real moment, real
  pride. Pause for it.
- **Buddies trading URLs.** Encourage. They'll
  visit each other's sites.
- **Excitement about parents seeing it.** "Can I
  send this to my mom?" Yes. Real.
- **Concerns about privacy.** Public repos = anyone
  can see the code. Some kids/parents may worry.
  Mention private repos exist (free for personal
  use, can also use Pages with paid tier).
- **Kids hitting 404s.** Common. Walk through —
  usually just needs more wait time, or
  `index.html` placement.
- **Excitement about portfolio.** Some kids will
  immediately deploy 5 projects. Encourage.
- **Pygame frustration** — "why can't I deploy my
  Pygame games?" Validate, frame the technical
  reason, redirect to the canvas game from
  Session 13.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sessions 16-17 (milestone).** Their milestone
  goes live. URL is part of the demo.
- **Phase 8 (Flask).** Backend deploys are a
  different beast (need running servers — Render,
  Railway, etc.). Mention briefly.
- **Career-long callback:** every developer needs a
  way to share their work. GitHub Pages is the
  free/easy entry. Real production teams use
  similar (but more complex) deployment systems.
- **Peanut butter callback opportunity:** the
  forgot-`index.html` or wrong-folder bug is a
  precision moment. Server serves what's there;
  if it's not, 404.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Mr. Eric's example deployed page ready
- [ ] Pre-identified kids needing GitHub help
- [ ] Projector
- [ ] Class roster
