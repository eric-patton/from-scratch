## Session 16: Milestone project work day 1

*Phase 7 — Web · Session 16 of 17*

### What we're learning today

Today is *your* day. You'll plan a web project — your
design, your code, hosted on GitHub Pages by demo
day — and start building it. Next week you'll finish
it and demo your **live URL** to the class.

This is your **seventh milestone project.** You have
every tool you need.

### You'll need to remember from last time

- **HTML structure** — semantic tags.
- **CSS** — the box model, Flexbox.
- **JavaScript** — DOM, events, fetch, localStorage.
- **Canvas** if your project includes graphics.
- **GitHub Pages** — for hosting.
- **Git** — commit as you go; push to deploy.

---

### Part A: Plan your project

#### The plan

Take a piece of paper or open a blank text file.
Answer these eight questions:

1. **What's the project?** *(One sentence. "A
   recipe collector." "A canvas paint app." "A
   weather widget.")*

2. **What does the user do with it?** *(How do
   they interact?)*

3. **What HTML elements does it need?** *(Forms?
   Lists? Canvas? Image grid?)*

4. **What does it look like?** *(Sketch the layout
   on paper. Where's the navbar, content,
   footer?)*

5. **What's the JavaScript doing?** *(Click
   handlers? DOM updates? Fetch from an API?)*

6. **Does it need persistence?** *(localStorage?
   What state?)*

7. **What's the simplest version?** *(Build this
   FIRST. Just the core. No fancy features.)*

8. **What's one stretch feature?** *(After core
   works.)*

#### Phase 7 requirements

Your milestone must:

- **Have HTML, CSS, and JavaScript** (use all
  three).
- **Be hosted on GitHub Pages** by the demo —
  with a public URL you can share.
- **Run without crashing** under normal use.
- **Look styled** (not raw HTML — at minimum,
  custom font + color).

Bonus:

- Uses fetch (calls a public API).
- Uses localStorage (persists state).
- Uses canvas (graphics or game).
- Looks decent on mobile (resize browser to
  test).

#### If you don't have an idea

Pick one and modify:

**Content / portfolio sites:**
- A **recipe site** — your favorite recipes, with
  photos.
- A **book/movie review site** — list, ratings,
  notes.
- A **multi-page personal site** — about, blog,
  projects, contact.
- A **fan site for a game/anime/band** — info,
  pictures, links.

**Interactive apps:**
- A **flashcard study app** — questions on
  cards, flip to see answer.
- A **trivia game** — multiple choice, score
  tracking.
- A **simple calculator** — buttons, display.
- A **unit converter** — pick from/to units.
- A **countdown timer / pomodoro** — start,
  pause, reset.
- A **tip calculator** — bill amount + tip
  percent.
- A **password generator** — length, character
  types.

**Data-driven (uses fetch):**
- A **random Pokemon explorer** — search by name,
  show stats and image.
- A **weather widget** — fetch current weather
  for a city.
- A **trivia quiz** — fetch questions from
  trivia API.
- A **NASA picture of the day** — fetch and
  display.
- A **dad joke generator** — fetch a new one
  each click.

**Canvas / drawing:**
- A **paint app** — pick color, draw, save.
- A **pixel art editor** — grid of cells, click
  to color.
- A **simple drawing pad** with brush options.

**Canvas games:**
- A **catcher game** like Session 13 — your
  theme.
- **Snake** — grid, snake grows, eats food.
- **Breakout / brick breaker** — paddle, ball,
  bricks.
- A **flappy bird clone** — gravity, tap to flap,
  pipes.
- A **dodger game** — avoid falling things,
  survive as long as possible.
- A **memory match** — flip cards, match pairs.

**Collaborative / shareable:**
- A **shared list** with copyable URL (data in
  URL fragment).
- A **tip sheet** for some topic you're an expert
  on.
- A **class profile collection** — each student
  has a card.

Pick one. Spend two minutes. Don't overthink.

#### Show Mr. Eric

When your plan is ready, show it to Mr. Eric.
He'll either say "go build it" or ask one question.

#### Set up the project

```
$ cd ~                          # or wherever
$ mkdir my_project
$ cd my_project
$ touch index.html              # create empty file
$ git init
$ git add index.html
$ git commit -m "Initial project setup"
```

Push to GitHub now (so deployment works later):

1. Create a new public repo on GitHub.
2. Connect:
   ```
   $ git remote add origin https://github.com/USERNAME/my_project.git
   $ git push -u origin main
   ```
3. Enable GitHub Pages in Settings → Pages.

Now any push deploys immediately. Build with the
URL ready to go.

#### Build the simplest version first

Look at your answer to question 7. Build *that*
first. Get something on screen. Get one feature
working. Iterate.

For each significant change:

1. Make the change.
2. Open `index.html` in browser. Test.
3. `git add` + `git commit -m "..."`.
4. (Optional, but encouraged) `git push` — deploy
   the in-progress version.
5. Move to the next thing.

#### Use what you've learned

- **Semantic HTML** — `<header>`, `<main>`,
  `<footer>`.
- **CSS variables** for a centralized palette.
- **Flexbox** for layout.
- **DOM manipulation** with `querySelector`,
  `addEventListener`.
- **Forms** with `preventDefault`.
- **localStorage** for any state worth keeping.
- **Canvas** if your project is graphics-heavy.
- **Fetch** if your project pulls data from APIs.

The complete list of patterns is in Sessions 1-15.
Skim them when stuck.

### Wrap-up

Last 5 minutes: each of you, in one sentence, tell
the room **one thing you got working today.**

Bring your project (and the deployed URL!) next
week. We'll finish, then demo.

If you got far, **push to GitHub and verify the
URL works** before next week. The demo requires
the URL to be live.

### If you missed this session

Open Thonny.

1. Spend 10-15 minutes answering the eight planning
   questions.

2. Set up the project folder + `index.html` +
   `git init` + commit.

3. Push to a new GitHub repo. Enable Pages.

4. Build the simplest version. Commit and push as
   you go.

About 60-90 minutes total. By next week you should
have:

- An `index.html` with at least the page
  structure.
- One core feature working.
- A live GitHub Pages URL.
- Several Git commits.

If you don't have an idea, pick from the seed list.

### Stretch and extension ideas

- **Add fetch** if you didn't plan on it.
- **Add localStorage** for any state.
- **Add canvas** for a visual element.
- **Make it responsive** with `@media` queries.
- **Multi-page site** — about, projects, etc.
- **README on the repo** with description and live
  URL.
- **Custom favicon** in the browser tab.

### What's next

Next week is the **last session of Phase 7.** You'll
have time to finish, polish, and **demo your live
URL** to the class. Each person gets 3-5 minutes.
Bring a working app at a public URL.
