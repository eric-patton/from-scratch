## Session 6 — Teacher Notes

*Phase 6, Pygame · Session 6 of 14 · Title: Build Pong
together*

### Purpose of this session

The first big build of Phase 6. Five jobs, in priority
order:

1. **Land integration.** Sessions 1-5 each taught one
   piece. Today they all combine. The "click" moment is
   when kids realize they already had everything they
   needed.
2. **Land step-by-step building.** Six steps, each one
   playable. This is *how real games get built* — start
   with a window, add one thing, run it, add the next.
   Not "type the whole thing and pray."
3. **Land `pygame.Rect(x, y, w, h)` directly.** Up to
   now, rects came from `image.get_rect()`. Now we
   create them from scratch — useful for paddles, walls,
   collision zones.
4. **Land "the basics make a real game."** Pong is ~60
   lines of code. It's a real game. The conceptual
   ceiling is closer than they think.
5. **Set up Sessions 7-8.** Pong is the artifact for
   Session 7 (push to GitHub) and the platform for
   Session 8 (add sound).

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame.
- Pre-built Pong (the Step 6 end-state) for comparison.
- Pre-built Pong with all stretches (angle bounce, AI,
  center line, win screen) as the "where this could
  go" demo.

**Prep time:** ~20-30 minutes. Build all six steps once
before class so you're fluent typing them on the
projector.

### Timing and flow

Total: ~90 min — possibly tight. Be prepared to extend
or simplify.

- **Welcome and recap** (~5 min). The "we're building
  Pong today" framing. Show the finished game.
- **Part A: Steps 1-3** (~25 min). Window, paddles,
  movement.
- **Part A: Steps 4-5** (~20 min). Ball + paddle bounce.
- **Break** (~5 min).
- **Part A: Step 6 (score)** (~15 min).
- **Part B: stretches** (~15 min). Angle-bounce is the
  best polish.
- **Wrap-up + buddy matches** (~5 min).

If running short: **the win-screen and AI stretches can
be cut.** Getting to the end of Part A — a working
two-player Pong — is the goal.

### Teaching Part A — the six-step build

#### Don't skip the runs

The session's biggest pacing risk is going too fast and
having a kid silently lose track at Step 3. **Run after
every step.** Make every kid demo their working
intermediate state to their buddy.

> "Step 1: window. *Run.* Step 2: paddles. *Run.* Step
> 3: paddles move. *Run and try them.* If something
> doesn't work, fix it before we add the ball."

#### Step 2 — `pygame.Rect` direct creation

The `pygame.Rect(x, y, w, h)` constructor is new (we've
only used `image.get_rect()` before). Frame:

> "We're not loading an image. We just want a *rectangle*
> — for the paddle's shape AND for collision detection
> later. `pygame.Rect(x, y, w, h)` makes one directly."

The paddle math (`HEIGHT // 2 - PADDLE_HEIGHT // 2`)
deserves a moment:

> "We want the paddle vertically centered. The screen's
> middle is at HEIGHT // 2. The paddle's middle is at
> PADDLE_HEIGHT // 2 from its top. So the *top* of the
> paddle goes at HEIGHT // 2 - PADDLE_HEIGHT // 2."

Some kids will use `(HEIGHT - PADDLE_HEIGHT) // 2` —
also correct, slightly more elegant. Either is fine.

#### Step 3 — boundary check while moving

Notice the boundary check is *baked into* the movement,
not separate:

```python
if keys[pygame.K_w] and left_paddle.top > 0:
    left_paddle.y -= PADDLE_SPEED
```

Two conditions: key pressed AND paddle not at top.
Cleaner than `clamp_ip` here because we have direction
to consider.

You could also use `clamp_ip(screen.get_rect())` after
all the movement — same result. Mention as alternative.

#### Step 4 — ball as variables (then refactor in Step 5)

I deliberately introduce the ball with `ball_x`,
`ball_y`, and a `pygame.draw.circle` first, then
*refactor* to a `Rect` in Step 5. This shows the value
of the Rect explicitly:

> "We *could* keep the ball as floats. But to do
> collision in Step 5, we'd have to write our own check
> ('is the ball in the rect?'). Easier: make the ball a
> Rect too. Then `colliderect` does it for us."

Some kids might balk at the refactor. Frame:

> "Real code gets refactored. You write something that
> works, then you find a better shape. We did that —
> now we'll change it."

#### Step 5 — the bounce gotcha

The "ball stuck in paddle" bug is real. With high speeds
and unfortunate positions, the ball can overlap the
paddle, the bounce flips, the ball moves further into
the paddle, the bounce flips again. Stuck.

Real Pong fixes this with:

```python
if ball_rect.colliderect(left_paddle):
    ball_dx = abs(ball_dx)    # always positive after bounce
```

(Always go *right* after hitting the left paddle.)

The angle-bounce stretch in Part B uses this pattern. If
you have time and the kids are following well, mention
the bug and the fix during Step 5. Otherwise, save for
the stretch.

#### Step 6 — score is satisfying

The moment a score appears and the ball resets is the
moment Pong feels *real*. Pause for it. Let kids react.

The font setup is a callback to Session 2 stretch. Some
kids may need a quick reminder.

### Teaching Part B — the polish

Pick one or two stretches based on the room's energy.
**Angle-bounce by hit-position** is the highest-payoff
polish — turns Pong from "ball bounces in straight lines"
to "real Pong with strategy."

Walk through the math briefly:

> "Where on the paddle did the ball hit? `relative` is
> -1 if it hit the very top, 0 if dead center, +1 if the
> very bottom. Multiply by 8 and that's the new vertical
> speed. Top of paddle = ball goes up; bottom = ball
> goes down."

The AI stretch is fun for kids who finish early. Frame:

> "AI here is dumb — 'move toward the ball.' That's all
> it takes to make a passable Pong opponent. Real game
> AI is more sophisticated; for Pong this is plenty."

### Common stumbles

- **Skipped a step.** Most failures here. Diagnose:
  "Which step did you last save and run successfully?"
  Go back to there.
- **Paddle moves off screen.** Boundary check missing
  or wrong. Walk through `top > 0` and `bottom < HEIGHT`.
- **Ball doesn't bounce off paddles.** Forgot
  `colliderect` check, or bouncing wrong direction.
- **Ball stuck in paddle.** Mentioned above. The
  `abs(ball_dx)` fix from the angle stretch resolves it.
- **Ball stuck on top/bottom edge.** The `if ball.top
  < 0 or ball.bottom > HEIGHT: ball_dy = -ball_dy` flips
  but doesn't *unstick.* If the ball is fully off-screen
  briefly, it can flip every frame. Solve by also
  clamping: `ball_rect.top = max(0, ball_rect.top)`.
  Mention if a kid hits this; otherwise skip.
- **Score updates but ball doesn't reset.** Forgot to
  call `reset_ball()`. Or `reset_ball` is missing the
  `global ball_dx` if a kid put the speed reset there.
- **Score appears stacked or overlapping.** Position math
  for the right score is fiddly. Walk through.
- **`pygame.Rect()` argument confusion.** `(x, y, w, h)`
  not `(x1, y1, x2, y2)`. Easy mistake.
- **Both paddles share movement.** Used `keys[K_w]` to
  move both. Read code carefully.

### Differentiation

- **Younger kids (9-10):** Goal is finishing Step 6 — a
  working Pong. No stretches. Pair them with a buddy
  who's faster.
- **Older kids (12+):** Push for the angle-bounce stretch.
  It's the highest-payoff polish.
- **Advanced (any age):** Push for AI opponent + win
  screen. Or suggest:
  - Powerups (paddle grows / shrinks for 5 seconds)
  - Variable ball speed (slower at start of round, faster
    after each rally)
  - Multiple balls
  - Background graphics
  - Different paddle styles per player
- **Struggling:** A kid stuck on Step 1 or 2 is the kid
  you focus on. Most common cause: typo, wrong constant
  values.

### What to watch for

- **The "we made Pong!" reaction.** Step 6 working = the
  big moment. Pause for it.
- **Kids playing each other.** Encourage between steps.
  After Step 3 (paddles move), they can already pretend.
  After Step 6, it's real.
- **Buddies pair-debugging.** Encourage. Pong has lots
  of moving parts; two sets of eyes help.
- **Frustration with paddle math.** Walk through with
  paper and pencil if needed.
- **Kids tempted to make the paddles fancy** (gradients,
  images) before the basics work. Redirect: "Polish
  later, mechanics first."
- **The "Pong is so simple, can I make a real game?"
  reaction.** Yes. That's the rest of the phase.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 7 (GitHub).** Pong is the artifact they push.
  "Your first thing on GitHub" is their first complete
  game.
- **Session 8 (sound).** Add bounce + score sound effects
  to Pong. Two lines of code, huge feel improvement.
- **Session 9 (sprite classes).** Pong's two paddles +
  one ball is a perfect place to introduce the Sprite
  class. Ball as one Sprite, paddles as another.
- **Sessions 13-14 (milestone).** Many kids will build
  variants of Pong (Brick Breaker, Paddle vs Bricks,
  multi-ball Pong). That's good — variations on a
  template are real game design.
- **Phase 7 (web).** Browser canvas Pong is a classic
  HTML/JS exercise. Same shape, different language.
- **Peanut butter callback opportunity:** the "ball stuck
  in paddle" bug is a precision moment. Code did exactly
  what was written, even though it produced the "wrong"
  result.

### Materials checklist

- [ ] Demo machine with Pygame
- [ ] Pre-built Pong (Step 6 end-state)
- [ ] Pre-built Pong with stretches (angle, AI, win
      screen) for "where this could go" demo
- [ ] Optional: a video clip of original 1972 Pong for
      historical context
- [ ] Projector
- [ ] Class roster
