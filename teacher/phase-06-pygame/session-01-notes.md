## Session 1 — Teacher Notes

*Phase 6, Pygame · Session 1 of 14 · Title: Welcome to
Pygame — the frame loop*

### Purpose of this session

Phase 6 opener. Five jobs, in priority order:

1. **Land the frame loop mental model.** This is the
   single biggest concept in Phase 6. Read input, update
   state, draw screen — repeat 60 times a second. If they
   leave understanding *only* this, the session worked.
2. **Land the contrast with Phase 5's event-driven model.**
   They just spent 8 weeks on "wait for the user to
   click." Pygame is the opposite — the loop runs all the
   time whether the user does anything or not. Different
   shape.
3. **Land the Pygame coordinate system.** `(0, 0)` is
   top-left, y goes *down*. This catches kids whose
   intuition is from math class.
4. **Land animation = changing values across frames.**
   The bouncing rectangle is the simplest demonstration.
   Variables that change each frame become motion.
5. **Set up Session 2 (drawing).** Today is loop +
   rectangle. Next is the full drawing toolbox.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame installed and tested.
- Pre-built bouncing rectangle (the Part A end-state) for
  comparison if needed.
- Pre-built 2D bouncing version (the Part B stretch) as
  a "wow" to show.

**Prep time:** ~15 minutes. Run the demo programs once
before class to make sure Pygame is working — Pygame on
Linux Mint can occasionally need an extra package
(`libsdl2-dev`) if it didn't install cleanly.

### Timing and flow

Total: ~90 min.

- **Welcome and Phase 6 framing** (~10 min). Phase 5 was
  apps. Phase 6 is games. Demo a finished game (a polished
  Pygame example or a YouTube clip of one) for inspiration.
- **Part A: minimum Pygame program** (~25 min). Type the
  full minimum program together, line by line. Run it.
  Pause to discuss each line.
- **Part A: rectangle, movement, bouncing** (~20 min).
  Add the rect, add x increment, add bouncing.
- **Break** (~5 min).
- **Part B: tweaks** (~25 min). 2D bouncing, color
  changes, multiple rects, keyboard.
- **Wrap-up** (~5 min).

If running short, **the keyboard tweak in Part B can be
cut** — it's covered in detail in Session 4. The 2D
bouncing version is the priority Part B goal.

### Teaching Part A

#### The big mental shift — frame loop vs event loop

Spend real time on this contrast:

> "In Phase 5, your app sat there waiting. The user clicked,
> something happened. The user typed, something happened.
> No clicks, no typing — nothing happened. The app *waited.*
>
> Pygame is the opposite. The loop runs all the time. Even
> if you do nothing, the program is busy — 60 times a
> second, asking 'any input? any updates? draw the screen.'
> 
> Why? Because games animate. Things move *whether or not*
> the user does anything. The bullet keeps flying, the
> enemy keeps walking, the timer keeps counting down. That
> only happens because the loop is always running."

Use a metronome metaphor if it helps. Or a heartbeat.

#### Type the program together

Don't paste — type it line by line on the projector with
the kids following. Each line, briefly say what it does.

Three lines deserve dwelling on:

- **`pygame.init()`** — "always at the top, starts
  Pygame."
- **`screen.fill((30, 30, 40))`** — "this *erases* the
  previous frame. Every frame starts with a clean slate."
- **`pygame.display.flip()`** — "this *shows* what we
  drew. Without it, the window stays blank."

The `screen.fill` → `flip` ordering is non-negotiable.
Drill it.

#### The "but my window is frozen" trap

If a kid forgets to handle `pygame.QUIT`, clicking the X
does nothing. They'll have to force-quit. Walk through
Activity Monitor / Task Manager / `kill` if it happens.
Better: catch this before it happens by building the
event handling first.

#### Coordinates

Worth a paper sketch on the board:

```
(0,0) ────────► x
  │
  │
  ▼
  y
```

Most kids' first reaction: "Wait, y goes *down*?" Yes.
This is graphics convention, not math convention. Pygame
inherited it from C-era graphics libraries.

#### The bouncing animation

Frame the moment the rectangle starts moving:

> "What just happened? Each frame, `x` got bigger by 2.
> 60 frames per second × 2 pixels = 120 pixels per second.
> The rectangle is *moving* because the variable is
> changing and we're drawing in the new spot every frame.
> *That's all animation is.*"

Then frame bouncing:

> "When `x` gets too big, we *flip the velocity.* Now the
> rectangle moves left. When `x` gets too small (off the
> left edge), flip again. Bouncing is just velocity
> negation."

This is real game programming. Get it landed.

### Teaching Part B

#### 2D bouncing is the goal

Most kids should achieve 2D bouncing in Part B. It's a
small extension of Part A and feels great when it works.

#### Color randomization is the "wow"

Watching a multi-color rectangle bounce around screen is
delightful. Encourage it.

#### Multiple rects is the conceptual extension

For kids who want more, multiple bouncing rects forces
them to think about *lists of objects.* That's the
foundation for sprite groups (Session 9). Don't push it
on everyone, but it's a great stretch.

#### Keyboard is the appetizer

The space-to-reverse-direction trick is a teaser for
Session 4. Don't go deep — show the pattern, let kids try
it, move on.

### Common stumbles

- **Forgot `pygame.init()`.** Cryptic error. Add it.
- **Forgot `pygame.display.flip()`.** Window opens but
  stays blank or has garbage. Add it.
- **Forgot `clock.tick(60)`.** Rectangle moves at thousands
  of pixels per second; window may be unresponsive on
  slower machines.
- **Drew before filling.** Trail effect (each frame's
  rectangle stays). Sometimes kids *like* this. Either
  way, point out the order: fill THEN draw.
- **Filled after drawing.** Nothing visible at all
  (everything got erased). Order matters.
- **Forgot to handle QUIT.** Window can't be closed.
  Force-quit and add the handling.
- **Window opens and immediately closes.** Usually means
  `running` got set to `False` at the wrong place, or
  there's an unhandled exception. Look at the terminal.
- **Mixing up x and y.** Drawing at `(150, 250)` when they
  meant `(250, 150)`. Walk through coordinates.
- **`pygame` not installed.** `ModuleNotFoundError`.
  `pip install pygame` from terminal.
- **Bouncing condition wrong.** They write `x > 600` but
  the rectangle is 100 wide so it goes 100 pixels off-screen.
  Walk through: `x` is the *left edge* of the rectangle.

### Differentiation

- **Younger kids (9-10):** Goal is the bouncing rectangle
  (Part A). 2D bouncing in Part B is a stretch. Don't
  push past that.
- **Older kids (12+):** All Part B stretches are fair
  game. Push for multiple rects + color changes combined.
- **Advanced (any age):** Suggest:
  - Acceleration / gravity (`dy` increases each frame)
  - Mouse-controlled rectangle (poll mouse position each
    frame)
  - Rectangles that "eat" smaller ones on collision
- **Struggling:** A kid stuck on the minimum program is
  the kid you focus on. Most common cause: typo, missing
  `init()`, or missing `flip()`.

### What to watch for

- **The "the rectangle is moving!" reaction.** First
  successful animation gets visible delight. Pause for it.
- **Frustration with coordinates.** Some kids will draw
  at the "wrong" spot for a while because their intuition
  is upside-down. Patience.
- **The "this is way more code than customtkinter" feeling.**
  Yes, it is. Frame: "customtkinter did a lot of work for
  you. Pygame gives you direct control. More power, more
  responsibility."
- **Buddies pair-debugging the frame loop.** Encourage.
- **Kids who try to add features before the basics work.**
  Redirect: "Bouncing first, fancy stuff later."

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 2 (drawing).** Today's `pygame.draw.rect` is
  one of many. Next: circles, lines, polygons.
- **Session 3 (sprites).** Drawing rectangles and circles
  is fine for prototypes. Real games use *images*.
  `Rect` returns as the foundation for sprite collision.
- **Session 4 (input).** Today's "press space to flip"
  scales up to full keyboard control.
- **Session 6 (Pong).** Today's bouncing rectangle is
  conceptually a Pong ball — bounces off walls. Add
  paddles and a score and you're 80% there.
- **Phase 5 callback:** Yes, customtkinter and Pygame both
  have a "main loop." But Pygame's runs constantly, drives
  animation. customtkinter's waits for events. Different
  shape, same word.
- **Peanut butter callback opportunity:** the order of
  `fill` and `draw` is a precision moment. The computer
  does *exactly* what they say. Wrong order = wrong
  result.

### Materials checklist

- [ ] Demo machine with Pygame installed
- [ ] Pre-built bouncing rectangle (Part A end-state)
- [ ] Pre-built 2D bouncing version (Part B)
- [ ] Optional: a video clip or live demo of a polished
      Pygame game for inspiration
- [ ] Projector
- [ ] Class roster
