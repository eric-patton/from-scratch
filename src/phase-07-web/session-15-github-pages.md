## Session 15: GitHub Pages — host your work

*Phase 7 — Web · Session 15 of 17*

### What we're learning today

You've built websites. They run on **your computer.**
Today they run on **the internet** — anyone with the
URL can visit, no install required. **GitHub Pages**
hosts static websites directly from your GitHub repos,
free, with custom URLs at `<username>.github.io`. By
the end of class, your personal homepage will be at a
real URL you can share with anyone.

This is the moment your code becomes **shareable to
the world.**

### You'll need to remember from last time

- **Phase 6 Session 7** — Git remote, push to GitHub.
  PATs.
- **Your homepage** from Session 6 (or any other
  HTML/JS project worth deploying).
- **The terminal** — `cd`, `git`.

---

### Part A: Deploy your homepage

#### What's GitHub Pages?

GitHub Pages is a **free static hosting service**
built into GitHub. You push HTML/CSS/JS to a repo,
flip a setting, and GitHub serves your site at a
public URL.

Limits:

- **Static only.** No backend code (no Python/Node
  on the server). Just HTML, CSS, JS, images.
- **Public for free** (private with a paid plan).
- **~1 GB total** per site (huge for our scale).
- **Soft bandwidth limit** of ~100 GB/month (also
  huge for personal sites).

For everything we've built in Phase 7 — homepages,
todos, canvas games, fetch demos — GitHub Pages is
perfect.

#### Step 1 — Push your homepage repo

If you don't already have your homepage in a GitHub
repo:

1. Make a folder for it on your machine.
2. Inside, you should have at least `index.html` and
   `styles.css`.
3. From the terminal:
   ```
   $ cd ~/projects/homepage    # or wherever yours is
   $ git init
   $ git add .
   $ git commit -m "Initial homepage"
   ```
4. On GitHub, create a new repo (let's say named
   `homepage`).
5. Connect and push:
   ```
   $ git remote add origin https://github.com/YOUR-USERNAME/homepage.git
   $ git push -u origin main
   ```

(All of this is Phase 6 Session 7. Refresher if
needed.)

#### Step 2 — Enable Pages

1. Go to your repo on GitHub.
2. Click **Settings** (top of the repo).
3. In the left sidebar, click **Pages**.
4. Under **Source**, pick **Deploy from a branch.**
5. Under **Branch**, pick **main** and **/ (root).**
6. Click **Save.**

GitHub now starts deploying your site. Takes 1-2
minutes the first time.

#### Step 3 — Visit your URL

Wait a moment, then refresh the Pages settings page.
At the top you'll see:

> **Your site is live at https://YOUR-USERNAME.github.io/homepage/**

Click it. **Your homepage loads at a real public
URL.**

That URL is **shareable.** Send it to anyone —
parents, friends, classmates. They can visit on
their phone, their laptop, anywhere with internet.
**Your code is on the internet.**

#### Step 4 — Make a change, push, watch deploy

The whole point: your site updates automatically
when you push.

1. Edit your `index.html`. Change a heading or add a
   line.
2. Save. Reload your *local* file to verify.
3. From terminal:
   ```
   $ git add .
   $ git commit -m "Update homepage"
   $ git push
   ```
4. Wait 30-60 seconds.
5. Reload the public URL. **Your change is live.**

This is **the deployment loop.** Edit → commit →
push → live within a minute.

#### A note on the URL pattern

GitHub Pages URLs follow a pattern:

- **`https://USERNAME.github.io/REPO-NAME/`** — for
  any normal repo.
- **`https://USERNAME.github.io/`** — for a special
  repo named `USERNAME.github.io`. This is your
  *root* GitHub Pages site.

If you want your homepage at `<username>.github.io`
(no `/repo-name/`), name your repo **exactly**
`USERNAME.github.io` (replace USERNAME with yours).

For now, keep it simple — `homepage` repo, URL ends
in `/homepage/`.

**Checkpoint:** *Your homepage is live at a public
URL. You can share the link.* **This is the natural
stop point if class is cut short.**

---

### Part B: Deploy more projects

Each of your Phase 7 projects can become its own
public URL.

#### Pick a project

Each kid: pick another HTML/CSS/JS project from
Phase 7 that you'd like to share:

- **Todo list** (Sessions 10-11)
- **Canvas game** (Session 13)
- **Fetch demo** (Session 14) — cat facts, dog
  photos, joke combo, Pokemon search
- **Anything else** you've built

#### Same process

1. Make sure the project is in its own folder with
   at least `index.html`.
2. `git init`, commit, push to a new GitHub repo.
3. Enable Pages on that repo.
4. Visit the URL.

15 minutes per project once you have the rhythm.

#### Add links between your sites

Your homepage can **link to your other deployed
projects** — making your portfolio cohesive.

In your homepage's HTML:

```html
<section>
    <h2>My projects</h2>
    <ul>
        <li><a href="https://USERNAME.github.io/todo/">Todo app</a></li>
        <li><a href="https://USERNAME.github.io/catcher/">Catcher game</a></li>
        <li><a href="https://USERNAME.github.io/dog-jokes/">Dogs &amp; jokes</a></li>
    </ul>
</section>
```

Push the homepage. Now your homepage URL is the
**hub** for everything you've built.

#### Stretch — README on each repo

Each repo benefits from a `README.md` with:

- What the project does.
- Live URL.
- Screenshot.
- How to run locally.

When you visit `github.com/USERNAME/REPO`, the README
shows. Real-developer professionalism.

#### Stretch — custom domain (mention only)

You can use a custom domain (like `myname.com`)
instead of `username.github.io/...`. Requires
buying a domain (~$10/year) and configuring DNS.

If you have a domain, GitHub's Pages settings has a
"Custom domain" field. Out of scope for class but
worth knowing about.

#### Stretch — GitHub Pages from a subfolder

If you want to deploy *only* part of a repo (e.g.,
your `dist/` folder), the GitHub Pages settings let
you pick the source folder. Useful for build-step
sites — but not relevant for our vanilla-JS
projects.

#### Extension — share your URLs in the class

Make a class shared list. Everyone adds their URLs.
Visit each other's projects. **Real audience for
your work.**

#### Extension — push existing repos to Pages

Every repo from Phase 6 (your Pong, fruit catcher
variants, etc.) — those are *Pygame* games,
unfortunately *not* deployable to Pages (they need
Python on the user's machine).

But if you also rebuilt any of those games in
canvas (Session 13), you can deploy those.

For Pygame games, you can:

- Deploy a *page about the game* with screenshots
  and a download link.
- Convert to canvas (significant work).
- Use a tool like Pyodide or Brython to run Python
  in the browser (advanced).

For now, focus on the HTML/CSS/JS projects.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — **show your live URL.** Type it
  into a browser. Watch it load.
- Have someone else try yours on their machine /
  phone. **It works.**
- Anyone deploy more than one project? Show your
  homepage as the hub.
- Did seeing your URL on the internet feel like
  *a moment*?

Today you learned:

- **GitHub Pages** — free static hosting from your
  GitHub repos.
- **Enable in Settings → Pages.**
- **URL pattern:** `<username>.github.io/<repo>/`
- **Update via git push** — deployments are
  automatic.
- **Special repo name** for the root URL.

This is **a real production deployment workflow.**
Every push to `main` deploys to the public URL.
Tens of millions of sites use this exact pattern
(it's also what powers many open-source
documentation sites — like the one you're reading
right now, hosted on GitHub Pages).

You can now **share your work as URLs.** That's
the web's superpower. Your code, on the internet,
free, available globally, without server
maintenance.

Next two weeks: **your milestone web project.**
Your design, your code, hosted on GitHub Pages by
demo day.

### If you missed this session

You need a GitHub account (Phase 6 Session 7) and
a project with at least an `index.html`.

1. Push your project to a new GitHub repo.

2. In repo Settings → Pages, set source to "main"
   branch, "/ (root)" folder.

3. Wait 1-2 minutes.

4. Visit `https://USERNAME.github.io/REPONAME/`.

5. (Stretch) Deploy more projects.

About 30-45 minutes. By the end you should have at
least one URL you can share.

### Stretch and extension ideas

- **Deploy multiple projects.**
- **Cross-link** your projects from your homepage.
- **Add READMEs** to each repo.
- **Try `<username>.github.io`** as the URL — needs
  a special repo name.
- **Custom domain** if you have one.
- **Set up an `about.html` and `projects.html`** as
  separate pages in your homepage repo.
- **Verify mobile** — visit your URL on a phone.
  Does it look right?
- **Track visitors** with a simple analytics service
  (advanced — Plausible, Simple Analytics).

### What's next

Next week: **milestone planning + work day 1.** You
plan and start *your* web project. Your design,
your code. The week after, you finish and **demo
your live URL** to the class.

Bring an idea or two. Or come empty-handed — we
have a seed list ready.
