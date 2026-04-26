## Session 7 — Teacher Notes

*Phase 6, Pygame · Session 7 of 14 · Title: GitHub —
push to the world*

### Purpose of this session

Real software-infrastructure session. Five jobs, in
priority order:

1. **Get every kid's first repo on GitHub.** By end of
   class, every kid has a public URL pointing at their
   Pong code.
2. **Land the local-repo / remote-repo distinction.**
   Git is local; GitHub is one of many possible remotes.
   The relationship is `add origin → push -u → push`.
3. **Land Personal Access Token authentication.** The
   2021 password change still bites kids who try to use
   their account password. Get PAT setup right the first
   time.
4. **Land the README as the project's front door.**
   Markdown matters. A bare folder of code is fine; a
   README turns it into a real project.
5. **Set up future phases.** GitHub becomes the default
   place to put work. Phase 7 (web) will use Pages.
   Future contributions to other projects start here.

### Before class

**Bring:** nothing physical, but **homework for the
parents/students** the week before:

> "Next week we're putting your code on GitHub. Bring
> an email address to class. If you can, create a
> GitHub account at github.com beforehand using that
> email — it speeds up class."

**Set up:**

- Demo machine with Git + a sample project ready to push.
- A GitHub account ready to demo with (Mr. Eric's, or a
  dedicated `from-scratch-demo` account).
- The link `https://github.com/settings/tokens` ready to
  open on the projector for PAT walkthrough.
- Optional handout: PAT setup steps printed (since the
  exact UI changes occasionally).

**Prep time:** ~30 minutes. **Plus** any prep with
parents about email addresses / account creation. This
session has more setup than usual.

### Timing and flow

Total: ~90 min — possibly tight. Account creation is the
wildcard.

- **Welcome and framing** (~5 min). What is GitHub.
  Why does this matter.
- **Account creation** (~10-20 min). Some kids will
  already have one. Others will need to create. Email
  verification can be slow.
- **PAT setup** (~10 min). On projector first, then
  every kid does it.
- **Create empty GitHub repo** (~5 min).
- **`git remote add` + `git push`** (~15 min). The
  command sequence on every kid's machine.
- **Break** (~5 min).
- **README + push the README** (~20 min).
- **Stretches** (~10 min). Push more projects, screenshot,
  explore others' repos.
- **Wrap-up** (~5 min). Each kid shares their URL.

If running short, **stretches can be cut.** The base goal
— "kid has at least one repo on GitHub" — is the
priority.

### Teaching the GitHub flow

#### Account creation can be a bottleneck

Several things can go wrong:

- **No email.** Have a backup plan — a parent's email,
  a generic class email, etc. Some families don't give
  kids email addresses.
- **Email verification slow.** Gmail sometimes delivers
  fast; school-managed email can take minutes.
- **Username taken.** Have a fallback pattern ready
  (initials + last name, or a hobby word + number).
- **Already has an account but forgot login.** Reset
  via email.
- **Age verification.** GitHub requires users to be 13+.
  Younger kids technically can't have accounts. **Talk
  to parents about this in advance.** A parent's account
  used by the family is a workaround if needed.

If a kid can't get an account in class, they can still
follow along — running `git remote add` etc. against a
URL that won't work. The push will fail; that's OK.
Catch up next week.

#### Demo the whole flow first

Before kids start on their own, run the whole flow on
the projector once:

1. Show creating an empty GitHub repo.
2. Show running `git remote add origin <URL>`.
3. Show `git push -u origin main` (with PAT).
4. Show refreshing GitHub and seeing the code.

Then kids do it on their own. They have the visual
memory.

#### PATs — the unavoidable annoyance

GitHub stopped accepting account passwords for command-
line use in **August 2021.** Kids will absolutely try
their password and absolutely get an obscure error like:

```
remote: Support for password authentication was removed on August 13, 2021.
```

When this happens, walk through PAT creation:

1. github.com → Profile → Settings.
2. Developer settings (bottom of left sidebar — easy to
   miss).
3. Personal access tokens → Tokens (classic).
4. Generate new token (classic).
5. Note: name it "class machine".
6. Expiration: pick "no expiration" for simplicity, or
   90 days for security. (Strongly suggest "no expiration"
   for class machines — kids will forget to renew.)
7. Scopes: check `repo` (the top-level box, selects
   everything under it).
8. Generate.
9. **COPY THE TOKEN** — tell kids to paste it somewhere
   safe (a text file in their home folder is fine for
   class). Once they leave the page, they can't see it
   again.

When `git push` asks for password, paste the token.

#### Credential caching

On Linux Mint with Git's default config, credentials
are *not* cached — every push prompts again. Solutions:

**Option 1: Cache for 1 hour:**
```
git config --global credential.helper "cache --timeout=3600"
```

**Option 2: Store permanently (less secure):**
```
git config --global credential.helper store
```

For class machines, Option 2 is fine. The PAT lives in
plaintext at `~/.git-credentials` — acceptable risk for
a class machine.

#### When `git push` shows "branch 'main' set up to
track 'origin/main'"

That's the win. Refresh GitHub, see the code, celebrate.

#### Some kids' main branch may be `master`

If a kid's local branch is called `master` (older Git
default), they'll need:

```
git push -u origin master
```

Or, rename to main first:
```
git branch -m main
git push -u origin main
```

GitHub now defaults the main branch to `main`. Match it.

### Teaching the README

#### Markdown is a real skill

Frame:

> "Markdown is plain text with a few special characters
> for formatting. `#` makes a heading. Triple backticks
> make code blocks. `[text](url)` makes a link. That's
> 90% of what you need. Anywhere you write notes (Slack,
> Discord, Reddit, GitHub), Markdown works."

Show the GitHub-rendered version side by side with the
raw text. The "click the code button to see source" trick
helps.

#### Encourage personality

A README doesn't have to be sterile. Encourage:

> "Tell me what your game is, how to play, what was hard,
> what you're proud of. This is *your* project. Show me
> it's yours."

A README that says "This is my Pong game I built in
class!! It took 90 minutes and the trickiest part was
the score" beats a corporate "Pong is a classic
two-player game implemented in Python."

### Common stumbles

- **Account creation fails.** Email issues, username
  issues, age issues. See above.
- **`fatal: remote origin already exists`.** They ran
  `remote add origin` twice. Use `git remote set-url
  origin <URL>` to fix.
- **Wrong URL.** Most often: typo in username, typo in
  repo name, missing `.git`. Walk through.
- **Wrong protocol.** Used `git@github.com:USER/REPO.git`
  (SSH) without setting up SSH keys. Switch to
  `https://github.com/USER/REPO.git`.
- **`Permission denied`.** PAT wrong, or username wrong,
  or PAT lacks `repo` scope. Walk through.
- **`Updates were rejected because the remote contains
  work that you do not have locally`.** They created
  the GitHub repo with "Add a README" checked, so the
  remote has a commit they don't. Fix:
  ```
  git pull origin main --allow-unrelated-histories
  ```
  (Then resolve any conflicts.) Or: delete the GitHub
  repo and re-create empty.
- **`! [rejected] main -> main (fetch first)`.** Same
  as above.
- **PAT not accepted.** Token expired, scope wrong, or
  pasted with extra whitespace.
- **README doesn't render.** Filename wrong (`readme.md`
  works on most systems but `README.md` is canonical).
- **Image in README doesn't show.** File path wrong, or
  image not committed.

### Differentiation

- **Younger kids (9-10):** May need parent help for
  account creation. Goal is one repo pushed.
- **Older kids (12+):** Push for multiple repos + a
  good README.
- **Advanced (any age):** Suggest:
  - SSH key setup
  - GitHub Pages on a static site
  - Forking and cloning others' repos
  - Issue tracking on their own repo
  - GitHub Actions (way too advanced for now, but
    mention exists)
- **Struggling:** A kid who can't get the push working
  is the kid you focus on. Most common cause: PAT
  setup, or wrong URL.

### What to watch for

- **The "MY CODE IS ON THE INTERNET" reaction.** Some
  kids are visibly thrilled. Acknowledge.
- **Kids comparing URLs.** "What's your username?" is
  good — they're navigating each other's profiles.
- **Buddies pair-debugging the push.** Encourage. Git
  errors are mysterious; fresh eyes help.
- **Kids who add too much to a README before the basic
  push works.** Redirect: "Push first, polish later."
- **Privacy concerns.** Some parents may be wary of
  public repos with kids' names. Mention private repos
  exist (also free) and let kids/families choose.
  Public is encouraged for portfolio reasons but not
  required.
- **Adversarial behavior.** Two kids might play tricks
  on each other's repos (issues, comments). Address
  if it happens — same rules as any social space.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 8 (sound).** They'll add sounds to Pong.
  Push the new version with sound — first taste of
  "iterate and re-push."
- **Session 9-12.** All future code can be pushed.
  Habit-forming.
- **Sessions 13-14 (milestone).** Their milestone game
  goes on GitHub for the demo. Showing the URL is part
  of the demo.
- **Phase 7 (web).** GitHub Pages turns repo HTML into
  a public site. Their first hosted site lives on
  github.io.
- **Phase 8 (Flask).** Real deployment platforms
  (Heroku, Render, Vercel) all start by connecting a
  GitHub repo.
- **Career-long callback:** GitHub stays relevant for
  the rest of programming life. This is foundational.
- **Peanut butter callback opportunity:** the PAT
  password-vs-token confusion is a precision moment. The
  computer needs *this specific kind* of credential, not
  a similar-looking thing.

### Materials checklist

- [ ] Demo machine with Git + sample project
- [ ] Mr. Eric's GitHub account (or dedicated demo
      account) ready
- [ ] PAT setup link ready: github.com/settings/tokens
- [ ] Optional: PAT setup printed handout (UI changes
      occasionally)
- [ ] Pre-class email to parents about GitHub accounts
      and the 13+ age requirement
- [ ] Projector
- [ ] Class roster
- [ ] List of any kids who need help with account
      creation
