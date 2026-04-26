## Session 13 — Teacher Notes

*Phase 6, Pygame · Session 13 of 14 · Title: Milestone
project work day 1*

### Purpose of this session

Their game, their design. Five jobs, in priority order:

1. **Get every kid to a plan.** Seven-question plan
   gates the build. No code without a plan.
2. **Get every kid to a working window.** By end of
   class, every kid should have at least a player
   on screen and one mechanic working.
3. **Triage scope ruthlessly.** Pygame games are
   easier to over-scope than apps were. Catch this at
   plan-review time.
4. **Reinforce sprite-class default.** Phase 6 milestones
   should default to sprite classes, not raw lists.
5. **Set up Day 2.** What state every kid needs to be
   in to demo successfully next week.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame.
- Have the seed list in mind (the handout has the full
  list).
- Optional: 2-3 finished example games to show as
  inspiration. Not as templates — as "this is the kind
  of thing that fits in two sessions."
- A scope-reality-check list: things that don't fit in
  two sessions (see below).

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 12.
  Today: their game.
- **Part A — Plan** (~15 min). Seven questions. Mr.
  Eric reviews each plan.
- **Part A — Setup + first build** (~60 min). Folder,
  `git init`, first file, first commit. Then build the
  simplest version. Commit as they go.
- **Wrap-up** (~10 min). Each kid shares one win.

The 60-minute build is the heart. Roam constantly.
Catch problems early.

### Teaching the planning step

#### Seven questions, not six

Phase 6 adds two requirements to past milestones:
**states** and **sprites**. The questions reflect this:

- Q4 is about sprites (and forces them to *think* in
  sprites).
- Q5 is about states (forces them to think about screens
  beyond just gameplay).

Make sure both are answered. A plan with no states or
no sprites isn't a Pygame plan; it's a script idea.

#### Triage: things that won't fit in two sessions

When a kid shows you the plan, listen for:

- **Online multiplayer.** No.
- **3D anything.** No (curriculum-banned).
- **Procedurally generated worlds** (anything with
  serious world-gen). Too much.
- **AI/ML "smart" enemies** beyond "move toward
  player." Too much.
- **Big asset libraries** they don't have. Big art /
  sound projects.
- **Story-driven games** with lots of dialog. The
  text + UI burden is huge.
- **Saving/loading complex game state.** Highscore is
  fine; full save-game state is too much.
- **Networking, file uploads, web integration.** Out
  of phase scope.

Things that *do* fit:

- Single-screen arcade games (Snake, Brick Breaker,
  Asteroids, Frogger, Space Invaders simple, dodgers).
- Simple puzzles (Sokoban, sliding tiles, color match).
- Two-player local games (tank battles, sumo, racing).
- Reaction games (whack-a-mole, fast clicks).
- Simple platformers (single screen, jump-and-survive).
- Grid-world variants.

#### Common over-scope: "I'll add levels"

Kids will say "and there'll be ten levels" and "boss
fights" and "an upgrade store." Push back:

> "Get the *one screen* working perfectly first. Levels
> are a stretch. If you have a great game with one
> level, that's better than a buggy game with ten."

#### Encourage borrowing

Several kids will (and should) build a Pong variant or a
fruit-catcher variant or a grid-world variant. Encourage:

> "Variations on what we've built are great. Take Pong
> and add power-ups. Take fruit catcher and make the
> 'fruit' something themed. Take grid-world and make it
> about your character."

### Teaching the build step

#### "Window before mechanics"

Push every kid to **get a window on screen first.**
Even empty. Even just a player sprite that doesn't move.
*Then* add mechanics. Don't write game logic with no
window to test it in.

#### Sprite class default

> "Use sprite classes. Even for the simplest game. Even
> if it feels like overkill. The pattern is your friend
> for any game with multiple objects. Player class.
> Enemy class. Item class. Group for each."

A few kids will resist (they remember the "list of
rects" pattern from Session 5). Let them choose, but
gently push toward sprites for anything more than 3
objects.

#### Three-state minimum

Every milestone should have title + playing + game-over.
Walk past every kid:

> "What happens when the game starts? Title screen?
> Or just into gameplay? Add a title."

Title screen is *easy* to add (Session 12 pattern). It
takes a game from "toy" to "game."

#### Commit early, commit often

After 10-15 minutes of work, ask:

> "When was your last commit?"

Same as Phase 4-5. Build the muscle memory.

#### Push to GitHub if time

For kids who finished Session 7's GitHub setup, encourage
pushing today's progress before leaving. The next session
will require a push for the demo, so getting it sorted
early helps.

#### When to suggest scaling back

If a kid's plan is "Snake with multiplayer over the
internet, with leaderboards, and 5 different game modes":

1. Show empathy first ("That sounds awesome").
2. Ask: "What's the simplest version of *just* Snake?"
3. Help them carve out the core.
4. Add: "If you finish that and have time, the other
   stuff can come."

This isn't about killing dreams. It's about scoping the
*minimum playable thing* first.

### Common stumbles

- **Plan too ambitious.** Most common issue. Triage at
  plan-review.
- **Forgot to `git init`.** Discover at first commit.
  Easy fix: init then commit.
- **No sprite classes.** Doing everything with raw
  rects in lists. Encourage refactor early before too
  much code accumulates.
- **No state machine.** Game starts with gameplay
  immediately. Add a title.
- **Got widgets on screen but no movement.** Common at
  end of class. Redirect: get one input working before
  adding more sprites.
- **Forgot to add sprite to a group.** Sprite exists in
  memory but doesn't get drawn or updated.
- **Layout mess.** Mixed pack and grid... wait, that's
  customtkinter. In Pygame: drawing without filling
  first, leaving trails. Walk through.
- **Sound files missing.** Forgot to copy assets to
  the project folder.
- **Working out of the wrong directory.** Pygame can't
  find image files. Walk through file paths.

### Differentiation

- **Younger kids (9-10):** Pick a simple idea — Brick
  Breaker, Snake, basic dodger. Goal: a working window
  with player movement and one mechanic.
- **Older kids (12+):** Push for sprite classes + 3
  states. Goal: a playable game by end of session.
- **Advanced (any age):** Push for sound + persistence
  + GitHub push. Goal: a polished game-in-progress.
- **Struggling:** A kid who can't write the plan is
  the kid you focus on. Walk through the seven
  questions with them. Suggest a seed-list idea.

### What to watch for

- **Plans that are way too ambitious.** Spot in plan
  review.
- **Kids who plan and never start coding.** Cut planning
  short.
- **Kids who skip planning and hit a wall.** Pull aside,
  do the planning together.
- **Buddies trading ideas.** Encourage. Real
  collaboration.
- **Feature-creep early.** Redirect: "Base first."
- **The "I have an idea I'm excited about" energy.**
  Channel it into commits and runs.
- **Kids using sprite classes naturally vs avoiding
  them.** Note who needs the nudge for next time.
- **Quiet kids designing something quietly clever.**
  Ask. Sometimes the quietest plan is the best.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 14 (demo).** Today's project becomes next
  week's demo. Push every kid to a state where some
  version works.
- **Phase 7 (web).** Many of these milestones could be
  redone in browser JS. The design instincts transfer.
- **Career-long callback:** "Plan, build the smallest
  version, iterate" is *the* fundamental software
  workflow. Every session of every phase reinforces it,
  but milestones are the explicit teach.
- **Peanut butter callback opportunity:** scope creep —
  a plan that designed something the available time
  literally can't fit — is a precision moment. The
  computer doesn't know what's feasible; you do.

### Materials checklist

- [ ] Demo machine with Pygame
- [ ] Seed list of game ideas (in handout)
- [ ] Optional: example finished games
- [ ] Triage list of "doesn't fit in two sessions"
- [ ] Projector
- [ ] Class roster
