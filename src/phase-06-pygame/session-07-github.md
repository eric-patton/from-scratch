## Session 7: GitHub — push to the world

*Phase 6 — Pygame · Session 7 of 14*

### What we're learning today

Up to now, your code has lived **only on your machine.**
If your hard drive died tomorrow, all your projects would
be gone. Today we put your code on **GitHub** — a free
service that stores Git repositories in the cloud and
shares them with anyone you want. By the end of class,
your Pong from last week will be on the internet, with
your name on it, at a real URL anyone can visit.

This is a foundational moment. Every working programmer
in the world uses GitHub (or something like it). Today
you join them.

### You'll need to remember from last time

- **Your Pong project** from Session 6 — the folder.
- **Git** from Phase 4 Sessions 5-6 — `init`, `add`,
  `commit`, `log`, `status`.
- **The terminal** from Phase 4 Session 1 — `cd`, `ls`.

### What you'll need today

- A **GitHub account.** If you don't have one yet, we'll
  create one in class. (You'll need an email address.)
- Your Pong project folder, with a Git history (you've
  been committing as you go since Session 6, right?).

---

### Part A: Your first push to GitHub

#### What is GitHub?

A **Git repository** lives on your machine. So far, all
your repos do. But Git is built to be *distributed* —
copies of the same repo can live on multiple machines,
and you can sync them.

**GitHub** is a website where Git repos live in the
cloud. Other people (or future-you on a different
machine) can grab a copy. You can push your changes up;
others can pull them down. It's a shared whiteboard for
code.

A few things GitHub adds on top of plain Git:

- **A web view** of your code — anyone can browse it in
  a browser.
- **Issues** — a bug tracker.
- **Pull requests** — a way to suggest changes to
  someone else's code.
- **Profiles** — your `github.com/<username>` page is a
  real portfolio.

For now, we just want **storage and sharing.** The other
features will come up over time.

#### Step 1 — Make a GitHub account

If you already have one, skip this.

1. Go to **github.com**.
2. Click **Sign up.**
3. Pick a username — this becomes part of your URLs and
   profile, so pick something you'd be okay with for
   years. (Real name is fine. Nickname is fine. Avoid
   anything you'd regret.)
4. Use an email address you actually check. GitHub will
   send a verification email.
5. Pick a strong password. Save it somewhere safe.
6. Verify your email (click the link in the email
   GitHub sent).

Tell Mr. Eric your username when you're done.

#### Step 2 — Create an empty repo on GitHub

1. After logging in, click the **+** in the top-right,
   then **New repository.**
2. **Repository name:** `pong`. (Or whatever you called
   your project.)
3. **Description (optional):** "My first Pygame project."
4. **Public.** (Private hides it from everyone. Public
   means anyone can see it. For a personal project,
   public is fine.)
5. **Do NOT check** "Add a README file" or any other
   options. We want a *completely empty* repo.
6. Click **Create repository.**

GitHub shows you a page with setup instructions. **Don't
follow those yet** — they're for fresh projects, but
ours already has commits. We'll use slightly different
commands.

#### Step 3 — Connect your local repo to GitHub

Open a terminal. `cd` into your Pong project folder:

```
$ cd ~/projects/pong          # adjust to wherever yours is
$ git status                  # confirm you're in the right place
```

Now connect this local repo to the empty GitHub repo:

```
$ git remote add origin https://github.com/YOUR-USERNAME/pong.git
```

(Replace `YOUR-USERNAME` with your actual GitHub
username. You can also copy this exact URL from the
GitHub setup page.)

What this does:

- **`git remote add`** — register a remote (a Git repo
  somewhere else).
- **`origin`** — the conventional name for "the main
  remote." You'll see this everywhere in Git.
- **The URL** — where the remote lives.

Confirm it worked:

```
$ git remote -v
```

Should show two lines (one for fetch, one for push) both
pointing at your GitHub URL.

#### Step 4 — Push

```
$ git push -u origin main
```

What this does:

- **`git push`** — send commits to a remote.
- **`-u origin main`** — "send my `main` branch to the
  `origin` remote, and remember that connection." (The
  `-u` is short for `--set-upstream`. Future pushes can
  just be `git push` — no arguments needed.)

You'll be asked for your GitHub **username** and a
**password.**

For the password, **don't use your account password** —
GitHub stopped accepting that for command-line use in
2021. Instead, use a **Personal Access Token (PAT).**
Mr. Eric will help you create one if you haven't already.

(See the **Personal Access Token setup** section below
for the full steps.)

After you enter username and PAT, Git pushes your
commits. You'll see something like:

```
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
...
To https://github.com/YOUR-USERNAME/pong.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

That last line is the win.

#### Step 5 — Look at it on GitHub

Refresh the GitHub page in your browser. **Your code is
there.** Click around. Click on `pong.py` to see the
code. Click on `README.md` if you have one (or skip it
if you don't).

The URL is something like
`https://github.com/YOUR-USERNAME/pong`. You can share
that with anyone in the world. They can read your code
in their browser.

**Checkpoint:** *Your Pong is on GitHub. You can see it
in your browser at your `github.com/YOUR-USERNAME/pong`
URL.* **This is the natural stop point if class is cut
short.**

---

### Part B: Make it look nice (and update it)

Time to add polish. A bare folder of code is fine — but
a **good README** turns it into a real project.

#### Add a README

If you don't already have one, create a `README.md` in
your project folder:

```markdown
# Pong

My first Pygame project — a recreation of the 1972
classic, two-player Pong.

## How to play

- Left paddle: **W** (up) and **S** (down)
- Right paddle: **↑** (up) and **↓** (down)
- First to 10 wins.

## How to run

You need Python 3 and Pygame.

```
pip install pygame
python pong.py
```

## Built with

- Python
- Pygame
- A lot of patience
```

Save. The triple-backticks (` ``` `) make code blocks in
Markdown. The `#` and `##` make headings.

#### Commit and push the README

```
$ git status              # see the new README
$ git add README.md
$ git commit -m "Add README with controls and run instructions"
$ git push
```

Notice the second push — no `-u origin main` needed
anymore. Git remembers from before.

Refresh GitHub. Your README **shows up on the repo
page** — automatically rendered with proper formatting.
Nice.

#### Stretch — add a screenshot

A picture sells your project. Take a screenshot of Pong
running. Save it as `screenshot.png` in the project
folder. Add to your README:

```markdown
## Screenshot

![Pong in action](screenshot.png)
```

The `![alt text](file)` syntax embeds an image in
Markdown.

```
$ git add screenshot.png README.md
$ git commit -m "Add screenshot to README"
$ git push
```

Refresh GitHub. The image appears.

#### Stretch — push more projects

Pick another project — your fruit catcher, your collector,
any of your milestones. Same process:

1. Make a new repo on GitHub (empty).
2. In the project folder, `git remote add origin <URL>`.
3. `git push -u origin main`.

Each project becomes its own repo on your profile. After
a few of these, **your `github.com/YOUR-USERNAME` page is
a portfolio.**

#### Stretch — explore other people's repos

Browse to `github.com/python` to see Python's source.
Or `github.com/pygame/pygame` to see Pygame's. **Real
production code, written by professionals, all visible.**
This is one of the best things about software — most of
it is open and you can read it.

(Don't *copy* without permission — open code has licenses
that say what you can and can't do. But *reading* is
always allowed.)

#### Extension — clone a repo

`git clone <URL>` makes a local copy of any GitHub repo.
Try cloning a small Pygame example from
`github.com/pygame/pygame` (look in the `examples/`
folder).

```
$ git clone https://github.com/pygame/pygame.git
```

Now you have all of Pygame's source code in a folder.
You can read it, run examples, even modify your local
copy.

---

### Personal Access Token setup

GitHub uses Personal Access Tokens (PATs) instead of
passwords for command-line access. To create one:

1. On GitHub, click your profile picture → **Settings.**
2. In the left sidebar, scroll down to
   **Developer settings.**
3. **Personal access tokens** → **Tokens (classic)**
   → **Generate new token (classic).**
4. **Note:** "Class machine" or similar.
5. **Expiration:** No expiration is easiest for a class
   machine, but 90 days is more secure.
6. **Scopes:** Check **repo** (the top-level box —
   selects all repo permissions).
7. Click **Generate token.**
8. **COPY THE TOKEN** somewhere safe. You won't see it
   again after leaving this page.

When `git push` asks for a password, **paste the token.**

If your machine is configured to remember credentials,
you'll only need to do this once. If not, every push
will ask.

(Modern alternative: SSH keys. More setup, no passwords
ever after that. We can cover this if there's interest.)

---

### Wrap-up

Before we leave, share with the room:

- For everyone — what's your GitHub URL? Show your repo.
- Is your README up?
- Did you push more than one project?
- Anyone explore another GitHub repo? See anything cool?

Today you went from **"my code is on my machine"** to
**"my code is on the internet, with my name on it."**
That's a real shift. You can now:

- Share a working project as a single URL.
- Show your portfolio to anyone (parents, friends,
  teachers, future employers).
- Recover your code from any machine — `git clone` your
  own repo.
- Collaborate with others (we'll touch this in later
  phases).

This is real software-engineering infrastructure. Used
correctly, it lasts your whole career.

You learned today:

- **GitHub** is a free Git hosting service.
- **`git remote add origin <URL>`** — connect a local
  repo to a remote.
- **`git push -u origin main`** — send commits to the
  remote (the first time).
- **`git push`** — same thing, after the first time.
- **Personal Access Tokens** for password-replacement.
- **Markdown READMEs** make repos look real.
- **Public repos** = portfolio.

### If you missed this session

You'll need a GitHub account and a project to push.

1. Create a GitHub account at github.com if you don't
   have one.

2. Make a Personal Access Token (steps in this handout,
   under "Personal Access Token setup").

3. In your project folder:
   ```
   git remote add origin https://github.com/USERNAME/REPO.git
   git push -u origin main
   ```

4. Add a README with what your project does and how to
   run it.

5. Push the README.

About 30-45 minutes the first time. Once your Git +
GitHub setup works, future pushes are instant.

### Stretch and extension ideas

- **Push every project you've built so far** — Phase 1
  through Phase 6. Each becomes a repo. Your profile
  fills up.
- **Customize your profile.** Settings → Profile. Add a
  photo, bio, website.
- **Star repos you like.** Click the star button on any
  repo to bookmark it.
- **Follow people whose work you like.** Pygame
  developers, classmates, anyone.
- **Try GitHub Pages** — a feature that turns any HTML
  in your repo into a public website. We'll use this
  more in Phase 7.
- **SSH key setup** — replace passwords with key-based
  auth. Faster, more secure. Ask Mr. Eric if you're
  interested.
- **`.gitignore`** — a file that tells Git which files
  to *not* track (like `__pycache__/`, `.DS_Store`,
  `*.pyc`). Add one to your projects:
  ```
  __pycache__/
  *.pyc
  .DS_Store
  ```

### What's next

Next week: **sound and music.** Pygame can play sound
effects and background music. We'll add bounce and score
sounds to Pong, then experiment with music. Your games
go from silent to *alive.*
