## Session 17: Milestone project work day 2 + demo day

*Phase 7 — Web · Session 17 of 17*

### What we're learning today

Today is the **last session of Phase 7.** First half:
finish your project — fix bugs, add the last
features, push the polished version. Second half:
**demo your live URL** to the class. Anyone with
internet can visit; **your audience is the world.**

### You'll need to remember from last time

- **Your project plan** from last week.
- **Whatever you got working** last week.
- **Your buddy** for testing.
- **Git** + GitHub Pages — push to deploy.

---

### Part A: Final polish

You have about 35 minutes to finish.

#### What "finished" means

Same three rules as always:

1. **It runs without crashing** under normal use.
2. **It does what your plan said** — at least the
   simplest version.
3. **You can explain how it works.**

If your project doesn't meet all three, focus on
getting there before adding anything new.

#### Phase 7 specific polish

- **Verify the live URL works.** Push your latest,
  wait 30 seconds, visit the URL, click around.
  Don't assume — verify.
- **Test on a phone if you can.** Open the URL on
  a phone or resize your browser window. Looks
  ok? If text is unreadable or buttons too small,
  add a `@media (max-width: 600px)` rule.
- **Add a meaningful page title** — `<title>...
  </title>` shows in the browser tab.
- **Add a favicon** — a small icon in the tab.
  Drop a `favicon.png` next to `index.html` and
  link from `<head>`.
- **Console clean** — open DevTools console. Any
  errors? Fix or suppress.
- **README on the repo** — what the project does,
  the live URL, controls or instructions.
- **All committed and pushed** — `git status`
  should say "working tree clean" before demo.

#### Buddy test

About 15 min in, **swap with your buddy.** They
visit your URL on their machine. They click around.
You do the same.

For Phase 7 specifically: **send the URL via chat
or paper.** Nothing makes a site feel real like
visiting it on a different machine.

Notice things they get wrong (control confusion,
unclear next step). Real UX testing.

#### Push your final version

```
$ git status                # see what's pending
$ git add .
$ git commit -m "Final polish"
$ git push
```

Wait 30-60 seconds. Visit the URL. Verify
everything looks right.

**Checkpoint:** *Your project runs at a live URL,
the basics work, and you can demo it.* **This is
the natural stop point if class is cut short — but
today, demo time is next.**

---

### Part B: Demo day

Each person gets **3-5 minutes**.

#### How a demo works

When it's your turn:

1. **Show your URL.** Open it on the projector.
   Walk us through the page.
2. **Use it live.** Click buttons. Type things.
   Let us see it actually working.
3. **Have a classmate visit your URL on their
   machine.** Real test of "shareable to anyone."
4. **Tell us about it.** What is it? Who is it
   for?
5. **Show your GitHub repo.** Open the URL in a
   browser. Show your `git log`.
6. **Tell us one thing that was hard.** Bug
   stories, design decisions, things that took
   longer than expected.
7. **Take one question.**

#### Make sure your URL is shareable

Type your URL in the chat / on a piece of paper.
Other students should visit *during* your demo.
**Real audience reaction.**

#### After everyone demos

Mr. Eric will say a few specific things about each
project. Then we celebrate Phase 7 completion.

### What you accomplished

- **Seventh milestone project.** Shipped.
- **A real live URL** anyone can visit.
- **HTML + CSS + JavaScript** all combined into one
  app.
- **Hosted on the internet** — your code reaches
  beyond your machine.
- **Public GitHub repo** with the source code
  visible to anyone.
- **You finished Phase 7.** The web is yours.

### What's next: Phase 8 — Flask (web apps)

Phase 8 is the **back-end** — Python on a server
that responds to web requests, generates HTML,
talks to a database, and powers real multi-user
apps.

What's different:

- **Server-side code.** Python runs on a server,
  not in the browser. Your code processes
  requests, generates responses.
- **Persistent data across users.** A real
  database (we'll use SQLite — simple, file-based).
  Multiple users can share data.
- **User accounts and login** — finally possible
  with a backend.
- **Routes** — URLs that map to Python functions.
  `/login`, `/profile`, `/dashboard`.
- **Templates** — HTML files with placeholders
  Python fills in.

You'll build:

- A simple Flask app (Hello world).
- A multi-page server-rendered site.
- A note-taking app with user accounts and
  database storage.
- A milestone full-stack app.

What's the same:

- Python (Phase 3-4 + Phase 6).
- HTML and CSS (Phase 7).
- Git + GitHub for source control.

Phase 8 is the **last phase** of the curriculum.
After it, you'll have built apps end-to-end —
front-end (browser) AND back-end (server) — like a
real software engineer.

Bring your machine and your enthusiasm. See you in
Phase 8.

### If you missed this session

Two cases:

**Missed only the demo half:** Show your live URL
to Mr. Eric at the start of next week's class.
Same kind of feedback you'd have gotten in the
demo.

**Missed the whole session:** No big deal. Finish
your project at home using your Session 16 plan,
push it to GitHub Pages, and bring the URL next
week. Or just join us in Phase 8 — you've already
shipped enough this phase to be proud.

### Stretch and extension ideas

If you have time after demos, or want to keep
building at home:

- **Polish more.** Add features, more sound, better
  art, smoother interactions.
- **Share your URL widely.** Family, friends,
  anyone. Get real feedback.
- **Add analytics** — see how many people visit.
  Plausible Analytics or Simple Analytics are
  privacy-respecting and free for small sites.
- **Multiple deployed projects** — your portfolio
  grows.
- **Try a static site generator** like Jekyll
  (built into GitHub Pages — out of curriculum
  scope but accessible).
- **Save a copy of every milestone project.** They
  are yours. Seven so far.

### What's next

Phase 8 — Flask. The back-end. See you there.
