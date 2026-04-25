## Session 3 — Teacher Notes

*Phase 2, Python with Turtle · Session 3 of 8 · Title: Loops in
Python — `for` and `range`*

### Purpose of this session

Loops were a major Phase 1 milestone (Session 3 of Scratch). Now
they return in Python with new syntax. Four jobs, in priority
order:

1. **Land Python's `for / range / colon / indented body` syntax.**
   The shape is mechanical and they'll use it constantly. Get it
   into muscle memory today.
2. **Introduce indentation as part of Python's grammar.** This is
   the single most surprising syntactic feature of Python for
   anyone coming from another language. Some kids will love it
   (visually clean) and some will fight it. Either way, address
   it head-on.
3. **Reward last week's tedium.** Last week's "your code is
   getting long" pain has a payoff today. Make the contrast
   visible: 8 lines becomes 3.
4. **Foreshadow variables.** The `i` in `for i in range(N)` is a
   variable. Today they use it as a placeholder; in Session 5
   they'll learn what variables really are. The spiral exercise
   actually uses `i * 2` — first taste of computing with a
   variable.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open and the Session 1 manually-typed
  square ready to show as the contrast point.
- Verify Thonny's auto-indent is on (it's on by default — when
  you press Enter after a colon, the cursor indents 4 spaces).
- Optional: have the spiral and flower-of-squares programs
  pre-built so you can show "here's what we're building toward"
  if energy flags.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was the scene.
  Anyone hit the "this is getting long" feeling?
- **Part A: the for loop** (~40 min) — the long-square recap ~5
  min, the for-loop reveal ~10 min, indentation discussion ~10
  min, polygon variations (triangle, pentagon, hexagon) ~10 min,
  checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: patterns** (~35 min) — spiral ~15 min, base goal
  (colorful shape or row of squares) ~10 min, nested loop
  flower stretch ~10 min, wrap-up ~5 min.
- **Wrap-up** (~5 min).

If running short, **the nested loops stretch can be cut.** The
spiral is the second wow moment; don't cut it.

### Teaching Part A

#### The reveal

Open with the long-square recap. Show last week's manually-typed
square (or have a kid type it). Then say:

> "Look at this. Eight lines. Same two lines repeated four times.
> Watch what we can do."

Then type the loop version at the projector. Run it. Same square,
3 lines.

> "Three lines instead of eight. And if I want a 100-sided shape,
> I just change the 4 to 100, instead of typing 200 lines. *This
> is what loops do.*"

The reveal lands when you do it dramatically. Don't undersell it.

#### Walking through the syntax

Each part of `for i in range(4):` matters. Walk through:

- `for` — the keyword that starts a loop
- `i` — the loop variable (placeholder; we don't have to use it
  yet)
- `in range(4)` — the sequence to loop through
- `:` — required colon at the end (the most-forgotten character
  in Python)
- The next line is **indented** by 4 spaces — that's how Python
  knows it's inside the loop

Connect it to Scratch:

| Scratch | Python |
|---|---|
| `repeat 4` | `for i in range(4):` |
| Blocks dropped *inside* the mouth | Lines indented underneath |
| End of repeat (mouth closes) | First non-indented line |

That table is worth drawing on the whiteboard or projector.

#### The indentation moment

This is the most important pedagogical moment of the session.
**Have students intentionally break the indentation.** Take the
working square loop and dedent the second line:

```python
for i in range(4):
    t.forward(100)
t.right(90)
```

Run it. The turtle moves four times forward in a straight line,
then turns once at the end.

> "Same code, different indentation. Different program.
> Indentation in Python isn't decoration — it's how the language
> knows what's grouped together. The forward is inside the loop;
> the right is outside."

Have them put the indentation back. Run again, see the square.

This visceral demonstration of "indentation matters" lands harder
than just telling them. It's the same logic as the
"order matters" demo in Phase 1 Session 2.

#### Polygon variations

Mostly mechanical. Have them try `range(3)` + `right(120)` for a
triangle, `range(5)` + `right(72)` for a pentagon, `range(6)` +
`right(60)` for a hexagon.

Most kids will notice the 360 pattern themselves. If they don't,
ask: "What do all these turn-numbers add up to in total when you
multiply by sides? What about 360?"

This is a deliberate Phase 1 callback (Phase 1 Session 3
introduced this pattern). Some kids will get the "I remember
this!" recognition.

### Teaching Part B

#### The spiral

Walk through it at the projector. The `t.speed(0)` is genuinely
necessary — without it, the spiral takes forever to draw.

The new thing in the spiral is **using `i`**. Until now, `i` was
just required syntax. Now it's actually doing something —
`forward(i * 2)` means each iteration walks a different distance.

Don't formally explain variables yet. Just say:

> "Each time through the loop, `i` is a different number. First
> time it's 0, then 1, then 2, all the way up to 49. So
> `forward(i * 2)` walks 0, then 2, then 4, then 6... longer and
> longer."

Some kids will get it; some won't. Both are fine. Variables get
the formal treatment in Session 5.

#### Base goal

Two paths (colorful shape or row of squares) keep faster and
slower kids both engaged. Most kids should pick one and finish
it in 10 minutes.

If a kid wants to try the row of squares: they'll discover that
they need a *square-drawing pattern* inside a loop that *moves
between squares*. That's nested loops in concept, even if they
don't write them yet. Foreshadow next week's Functions session:
"What if you could write 'draw a square' once and just call it?
That's coming next week."

#### Stretch — nested loops

Walk through the flower-of-squares at the projector before
turning them loose:

- Outer loop: 12 iterations, each ending with a 30-degree turn
- Inner loop: 4 iterations, drawing a square
- Indentation: inner loop's body is indented twice (8 spaces)

The indentation hierarchy is the new wrinkle. Be ready to help
kids whose indentation gets confused — which line is inside
which loop is purely visual in Python.

#### Extension — colored spiral

The colored spiral introduces several things we haven't formally
taught: lists (`["red", "orange", ...]`), indexing (`colors[...]`),
and modulo (`i % 6`). **Don't try to teach them.** The handout
explicitly says "if confusing, just type and run."

This is a good moment to model "use it before you fully
understand it." Real programmers do this constantly — copy a
pattern they've seen, adapt it, deepen understanding later. It's
a valid skill. Worth modeling.

### Common stumbles

- **Forgot the colon.** `for i in range(4)` (no colon) → SyntaxError.
  Single most common Python mistake. Worth pointing at when it
  happens: "the colon at the end of the for line is required."
- **No indentation.** `for i in range(4):` followed by
  `t.forward(100)` at the same indent level → IndentationError.
  Thonny *should* auto-indent; if it doesn't, manually press Tab
  or 4 spaces.
- **Mixed tabs and spaces.** Subtle and confusing. Thonny
  defaults to spaces; if a student copy-pasted code from
  somewhere with tabs, it'll break. Fix: select all, retype the
  indentation manually.
- **`range(4)` vs `range(1, 4)`.** `range(4)` produces 0, 1, 2, 3
  (four numbers). `range(1, 4)` produces 1, 2, 3 (three numbers).
  Surprising. Don't formally teach unless asked.
- **Loop body not actually indented even though it looks like it
  is.** Thonny shows whitespace correctly but a copied snippet
  might use non-printing characters. If a loop "should work but
  doesn't," select the indentation, delete it, retype it.
- **`i = i * 2` (assignment) instead of `i * 2` (expression).**
  Some kids will try `t.forward(i = i * 2)`. That's a different
  thing entirely. Walk through what they want vs. what they wrote.
- **Spiral that goes off-screen and seems to vanish.** With
  `range(50)`, the spiral grows large. The window has limited
  size. Either reduce the loop count or accept that the outer
  arms go off-screen. Worth mentioning during the demo.

### Differentiation

- **Younger kids (9-10):** May find indentation genuinely
  confusing. Sit with them once or twice. Once Thonny's
  auto-indent clicks for them, they're fine. The polygon
  variations (just changing two numbers) are easy enough that
  even slow typists can keep up.
- **Older kids (12+):** Will probably finish base goals quickly.
  Push to the nested loop flower. If they finish that, suggest:
  "What does a triangle of triangles look like? An octagon of
  pentagons? Try it." Or hand them the colored spiral with
  permission to break it apart and figure out what each piece
  does.
- **Advanced (any age):** Will recognize loops from prior
  experience. Push them to write a function (foreshadowing
  Session 4) that draws a polygon — `draw_polygon(sides, length)`.
  Don't formally teach functions; let them invent it. They'll
  need to figure out `def`. They might find it; they might not.
  Either way, it primes them for next week.
- **Struggling:** A kid who can't get the basic for-loop square
  working in Part A is the kid you focus on. Common cause:
  forgot the colon, or misaligned indentation. Sit with them and
  walk through the syntax piece-by-piece.

### What to watch for

- **The "wait, that's it?" reaction** when 8 lines becomes 3
  lines. Several kids will visibly process this. Affirm: "Yep,
  that's the whole point. Imagine drawing a 100-sided shape now."
- **Kids accidentally discovering recursion / nested patterns.**
  Some kids will figure out nested loops without being shown.
  Encourage. "Yep, you can put a loop inside a loop. That's
  what we'll do in the stretch."
- **Frustration at indentation errors.** Especially the first
  time. Frame as "Python is being *helpful*. It's pointing at
  exactly where the structure is wrong."
- **The kid who tries to write `repeat 4` in Python.** Common
  Scratch-to-Python translation error. Gentle redirect: "in
  Python, repeat is called for. The syntax is different but the
  idea is the same."

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 4 (next week, Functions).** Today's loops + the
  remaining repetitive-code feeling (drawing five squares means
  copying the loop five times) is the motivation for functions.
  Mirror today's setup: "we're getting tired of copying the
  loop. Here's a way to give that loop a name and just call it."
- **Session 5 (Variables).** The `i` in `range(N)` foreshadows
  variables. The spiral's `i * 2` is the first time `i` is
  actually computed with. Variables in Session 5 generalize
  this to any name (`size = 50`).
- **Session 6 (Conditionals).** Combined with loops, conditionals
  enable any algorithmic logic. Foreshadow lightly.
- **Phase 6 (Pygame game loops).** Today's `for i in range(N)` is
  finite; the `forever`-style loops in Pygame are infinite (`while
  True:`). Same shape, different exit condition. We'll see it
  again.
- **Indentation as grammar** is forever. Every Python session
  from now on uses it. Reinforce in every session.

### Materials checklist

- [ ] Demo machine with Thonny and a manually-typed square ready
- [ ] Optional: pre-built spiral and flower-of-squares for
      "here's where we're going" previews
- [ ] Projector (helpful for the indentation demo)
- [ ] Class roster
