## Session 2 — Teacher Notes

*Phase 5, customtkinter · Session 2 of 8 · Title: Buttons
and events*

### Purpose of this session

Buttons are the canonical interactive widget. Five jobs, in
priority order:

1. **Land `CTkButton` with `command=function`.** The button
   widget plus its callback parameter — the heart of GUI
   interaction.
2. **Land "pass the function, don't call it" (no parens).**
   Most common GUI beginner mistake. Establish the rule
   early.
3. **Land `widget.configure()` for updating widgets after
   creation.** This is what makes UIs feel alive.
4. **Touch the `global` keyword carefully.** Necessary for
   today's pattern; bad style for real code. Mention the
   class-based "right way" without forcing it.
5. **Set up Session 3 (input widgets).** Buttons take input
   too (the click); next week is text input.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with customtkinter verified.
- Pre-built counter app for destination preview.
- Plan to demo the "no-parens" mistake explicitly.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was first
  windows. Anyone build a personal welcome screen at home?
- **Part A: first button** (~40 min) — basic button + callback
  ~10 min, the no-parens explanation ~10 min, multiple buttons
  ~15 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: counter app** (~35 min) — build the counter ~15
  min, global keyword explanation ~5 min, customizations
  ~10 min, clicker game stretch ~5 min.
- **Wrap-up** (~5 min).

If running short, **the class-based extension can be cut.**
The counter app with multiple buttons is the goal.

### Teaching Part A

#### Build the basic button

Walk through at the projector:

```python
def say_hello():
    print("Hello!")

button = ctk.CTkButton(app, text="Click me!", command=say_hello)
button.pack(pady=50)
```

Run. Click. "Hello!" in the shell.

Walk through what's new:
- The function definition (familiar from Phase 2+)
- `command=say_hello` — the callback parameter

#### The no-parens rule

This is the most important pedagogical moment of the
session. **Demo the mistake explicitly:**

```python
button = ctk.CTkButton(app, text="Click me", command=say_hello())  # WRONG
```

Run. The shell shows "Hello!" *immediately when the program
starts* — because `say_hello()` got called right then to get
its return value (None) for `command`. Then click the
button. Nothing happens. Because `command` is `None`, not a
function.

Make the rule explicit:

> "When you pass a function to `command`, don't add the
> parens. The parens *call* the function. We don't want to
> call it now — we want to give it to the button so the
> button can call it later. Pass the *name*, not a *call*."

This bug is the #1 GUI beginner trap. By making it explicit
now, you save kids future confusion.

#### Multiple buttons

Mechanical. Each button has its own function. The pattern
generalizes: any number of buttons, any number of callbacks.

### Teaching Part B

#### The counter

Walk through at the projector. The new pieces:

- A module-level variable (`count = 0`) for state.
- A function that modifies it.
- The `global count` line.
- `label.configure(text=...)` to update the display.

#### `global` carefully

The `global` keyword needs explicit explanation:

> "Without `global`, when a function says `count = something`,
> Python makes a NEW local count. Doesn't touch the outer
> one. Bizarre but that's the rule. To modify the outer
> variable, you have to say `global count` first. Then
> assignments inside the function affect the outer
> variable."

Demo what happens *without* `global`:

```python
def increment():
    count = count + 1   # ERROR or doesn't work
```

Without `global`, this errors with `UnboundLocalError`
because Python sees the assignment and makes a local — but
then the right-hand side tries to read it before it's set.

Then with `global`:

```python
def increment():
    global count
    count = count + 1   # Works
```

Mention the trade-off:

> "`global` works for small apps but is bad style for big
> ones. The 'right' way is to wrap state in a class —
> `self.count` instead of `count`. We'll see that in the
> extension and use it more in later sessions."

This honest framing prepares them for "we're using a
shortcut for now" without lying about it.

#### `label.configure()`

The new mechanic for updating widgets. Walk through:

> "`configure` lets you change a widget's properties after
> it's been created. Pass the same arguments you'd pass to
> the constructor. Most often used to change `text` on
> labels and buttons."

The "after it's been created" framing matters. Until now,
widgets were "set and forget." Now they can change.

#### Customize

Have students add Reset, Decrement, etc. The same pattern
applied to different functions. Reinforces the loop:
button → callback → state → configure.

#### Clicker game stretch

The conditional logic on score milestones is fun and
visual. Several kids will get really into the "what should
happen at score 100?" question. Encourage.

#### Extension — class version

Show the class-wrapped version at the projector for kids
who finish stretches. Don't drill — it's the
"production-quality" version, and we're not requiring it
yet. Just establish that it exists and is better:

> "When your app gets bigger, the global pattern breaks
> down. The proper way is to wrap everything in a class —
> state lives on the instance, methods access it via
> `self`. This is what real production GUI code looks like.
> You can use this pattern any time you want; we'll do more
> of it in later sessions."

### Common stumbles

- **`command=function()` instead of `command=function`.**
  Demo'd above. Most-common mistake.
- **`UnboundLocalError` from missing `global`.** Walk through
  the rule.
- **`AttributeError: 'NoneType' object has no attribute
  'configure'`.** Usually means `label = label.pack(...)`
  — `pack()` returns None, so the variable becomes None.
  Fix: separate lines.
- **Forgot to update label after changing state.** Counter
  goes up but display doesn't change. The callback needs
  `label.configure(text=...)` after the state change.
- **Button text doesn't change visually.** Spelled
  `.config()` (older tkinter) instead of `.configure()`.
  Either works in tkinter; customtkinter prefers
  `.configure()`.
- **Multiple buttons, only the last works.** Usually the
  variable name is reused. `button = ...` then `button = ...`
  — the second one overwrote the first. Use different names
  (`button1`, `button2`).

### Differentiation

- **Younger kids (9-10):** Focus on the basic button + the
  counter. Skip the global discussion (use globals; don't
  fuss about the keyword) — just say "we need this line; it
  makes the variable change."
- **Older kids (12+):** Will pick up callbacks fast. Push
  to the clicker game stretch and the class extension.
- **Advanced (any age):** Push hard to the class extension.
  Suggest:
  - `lambda` for one-line callbacks
  - `after()` for delayed execution
  - State machines (different button behavior based on
    current state)
  - Multiple windows
- **Struggling:** A kid who can't get the basic button
  working is the kid you focus on. Most common cause:
  `command=function()` (with parens), or forgot `.pack()`
  the button.

### What to watch for

- **The "I made it interactive!" reaction.** Several kids
  will visibly process this. Affirm.
- **The "wait, no parens?" surprise.** When the no-parens
  rule lands, several kids will gasp. Real moment.
- **Buddies playing each other's clickers.** Encourage.
- **Frustration with `global`.** Some kids will find it
  weird. Acknowledge: "yes, this is weird. Python made this
  decision a long time ago. We work around it."

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 3 (next week, inputs).** Today's button takes
  input (the click); next week's `CTkEntry` takes typed
  text input.
- **Session 6 (integration).** Today's pattern (button →
  callback → state → configure) is the heart of every
  interactive app.
- **Phase 6 (Pygame).** Game programming is event-driven
  too — keyboard events, mouse clicks. Today's mental
  model transfers.
- **Phase 8 (Flask).** Web forms have a similar pattern —
  user submits, server callback runs, response sent.
- **The peanut butter callback opportunity:** the no-parens
  bug is a precision moment. The computer did exactly what
  was written; you said "call this function and pass me the
  result" — the result is None — None is what got stored.

### Materials checklist

- [ ] Demo machine with customtkinter
- [ ] Pre-built counter app for destination preview
- [ ] Projector (helpful for the no-parens demo)
- [ ] Class roster
