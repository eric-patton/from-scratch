## Session 8: Milestone project work day 2 + demo day

*Phase 5 — customtkinter · Session 8 of 8*

### What we're learning today

Today is the **last session of Phase 5.** First half:
finish your app — fix bugs, add the last features, make
sure it runs cleanly. Second half: **demo to the class.**
By the end, you'll have shipped your fifth milestone
project — and your first real desktop app.

### You'll need to remember from last time

- **Your project plan** from last week.
- **Whatever you got working** last week.
- **Your buddy** for testing.
- **Git** — commit your final changes today.
- **All your widget tools** — labels, buttons, entries,
  layouts, callbacks, state, persistence.

---

### Part A: Final polish

You have about 35 minutes to finish.

#### What "finished" means

Same three rules as always:

1. **It runs without crashing** under normal use.
2. **It does what your plan said it would do** — at least
   the simplest version.
3. **You can explain how it works.**

If your app doesn't meet all three, focus on getting
there before adding anything new.

#### Polish ideas (Phase 5 specific)

- **Try it like a user.** Click around. Type weird things.
  See what breaks. Fix the obvious bugs.
- **Window size.** Does it look right when you open it?
  Adjust `app.geometry("WxH")` to fit your widgets.
- **Window title.** Make sure `app.title("...")` says
  something meaningful.
- **Empty-state handling.** If your app shows a list, what
  happens when the list is empty? An empty area is fine
  but a placeholder label is friendlier.
- **Labels make sense.** Buttons say what they do.
  Placeholder text in entries is helpful.
- **Theme** — try `ctk.set_appearance_mode("dark")` and
  `ctk.set_default_color_theme("blue")` (or "green",
  "dark-blue") near the top of your file. Looks polished.
- **Save your work** — if your app stores data, make sure
  the save/load actually works. Close and reopen to test.
- **Add a README** — `README.md` in your project folder
  with one paragraph about what your app does and how to
  run it. Real projects have one.
- **Clean up commits.** Look at `git log`. Are messages
  clear? They don't have to be perfect, but should
  describe what changed.
- **All committed.** `git status` should say "working
  tree clean" before the demo.

#### Buddy test

About 15 min in, **swap with your buddy.** They use your
app for a few minutes; you use theirs. Notice things they
get wrong (clicking the wrong button, not seeing what to
type). Those are real UX bugs.

**Checkpoint:** *Your app runs the basic version of what
you planned, and your `git log` shows the journey.* **This
is the natural stop point if class is cut short — but
today, demo time is next.**

---

### Part B: Demo day

Each person gets **3-5 minutes**. Same format as before,
plus the Phase 4 twist: **show your Git log.**

#### How a demo works

When it's your turn:

1. **Show your app.** Run it. Use it. Walk us through
   what it does.
2. **Tell us about it.** What is it? Who is it for?
3. **Show your Git log.** Run `git log --oneline`. Walk
   us through how the app came together — first commit,
   last commit, a turning point.
4. **Tell us one thing that was hard.** Bug stories,
   design decisions, things that took longer than
   expected. Maybe also one thing that was easier than
   you thought.
5. **Take one question.**

For Phase 5 demos especially, **let the audience use the
app** if there's time. A GUI is meant to be touched.
Hand the keyboard or mouse to a buddy.

#### After everyone demos

Mr. Eric will say a few specific things about each
project. Then we're done — Phase 5 is complete.

### What you accomplished

- You **shipped your fifth milestone project.**
- You used **the customtkinter widget toolbox** to build
  a real desktop app.
- You used **Git** to track every step of the journey.
- (If you used persistence) Your app has **memory** —
  state survives between runs.
- (If you used a class) You wrote **production-style
  GUI code.**
- You built **something with a real interface** — buttons,
  text inputs, layouts. Not a script, not a turtle drawing
  — a *desktop app.*
- You **finished Phase 5.** GUI programming is yours.

### What's next: Phase 6 — Pygame (games)

Phase 6 is **games.** Real, animated, interactive games
with graphics, sounds, scoring, and game loops.

What's different:

- **Animation.** Your customtkinter apps sat there waiting
  for the user. Pygame programs run a *frame loop* — 60
  times a second, draw the screen and update.
- **Real graphics.** Sprites, images, colors, shapes.
- **Sound.** Play sound effects and background music.
- **Real game design** — collision detection, scoring,
  game over screens, levels.
- **Bigger projects.** Phase 6 is longer than Phase 5
  because games are bigger than apps.

You'll build classic arcade games (Pong, Snake, Asteroids)
and then **your own game** for the milestone.

Bring your machine and your enthusiasm. See you in
Phase 6.

### If you missed this session

Two cases:

**Missed only the demo half:** Show your app to Mr. Eric
at the start of next week's class. Same kind of feedback
you'd have gotten in the demo.

**Missed the whole session:** No big deal. Finish your app
at home using your Session 7 plan, and bring it next week.
Or just join us in Phase 6 — you've already shipped enough
this phase to be proud.

### Stretch and extension ideas

If you have time after demos, or want to keep building at
home:

- **Polish more.** Add features, more widgets, better
  styling.
- **Package it.** Tools like PyInstaller can turn your
  Python file into a standalone `.exe` or `.app` that
  runs without Python installed. Advanced — ask Mr. Eric.
- **Share it.** Send the folder to a friend (with Python
  installed) and have them try it. Real users, real
  feedback.
- **Write a longer README** — installation instructions,
  examples, screenshots, future ideas.
- **Save a copy of every milestone project.** They're
  yours. Five so far.

### What's next

Phase 6 — games with Pygame. See you there.
