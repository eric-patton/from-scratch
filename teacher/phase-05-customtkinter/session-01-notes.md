## Session 1 — Teacher Notes

*Phase 5, customtkinter · Session 1 of 8 · Title: Welcome to
GUIs — your first window*

### Purpose of this session

The fifth major transition session in the curriculum. The
shift from text programs to GUI programs is a real
conceptual leap — programs become event-driven rather than
sequential. Six jobs, in priority order:

1. **Land the visual payoff.** A real window opens. Real
   labels show. Several kids will be visibly excited — this
   feels like "real software."
2. **Land the minimum GUI template.** Five lines covers
   90% of what they need to start. Drill until automatic.
3. **Land the event loop concept.** `mainloop()` is the
   most important conceptual new thing today. The "the
   program waits for the user" mental model needs to land.
4. **Reinforce classes from Phase 4.** Every widget is a
   class. `CTkLabel(app, text="...")` is class
   instantiation. The Phase 4 callback bridges to Phase 5.
5. **Establish the customtkinter visual style.** Dark mode
   default, themes, modern look. Kids will appreciate the
   aesthetic vs. raw tkinter.
6. **Set up Session 2 (buttons + events).** Today is
   passive (just labels); next week is interactive
   (buttons that do things). Foreshadow.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny + customtkinter pre-installed.
  Verify by running a one-line test (`import customtkinter`)
  in the shell.
- **Verify customtkinter is installed on every student
  machine.** This is the big setup risk for Phase 5. If
  any machine doesn't have it: `pip install customtkinter`
  (may need `pip3` on some systems, or `--user` flag).
- Pre-built finished welcome screen for destination preview.
- Projector helpful — windows opening and closing make sense
  better when seen.

**Prep time:** ~30 minutes. Especially: test customtkinter
on EVERY machine before class. The "import error" bug at
the start of Phase 5 wastes class time if not caught.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — Phase 4 done; today is a
  visual return.
- **Part A: first window** (~40 min) — minimum GUI ~10 min,
  walk through line-by-line ~10 min, event loop concept ~5
  min, customize (title, geometry, labels) ~10 min,
  checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: personal welcome screen** (~35 min) — themes ~10
  min, build personal screen ~15 min, stretch (colors,
  backgrounds) ~10 min.
- **Wrap-up** (~5 min).

If running short, **the stretches and extension can be
cut.** The base personal welcome screen is the goal.

### Teaching Part A

#### The minimum GUI

Type at the projector:

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("My First App")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Hello, world!")
label.pack(pady=20)

app.mainloop()
```

Save. Run.

A window appears. Several kids will gasp or laugh. This is
the visual moment.

Then walk through line by line. The new pieces:

- `import customtkinter as ctk` — `as ctk` is the
  shortname-on-import pattern from Phase 4.
- `app = ctk.CTk()` — instantiating a class. Phase 4
  callback.
- `app.title(...)` and `app.geometry(...)` — methods on the
  app instance.
- `label = ctk.CTkLabel(app, text="...")` — another class
  instance. The first argument (`app`) is the parent — where
  the label lives.
- `label.pack(...)` — layout method.
- `app.mainloop()` — the event loop. The new big concept.

#### The event loop

This is the most important conceptual moment of the session.
Frame explicitly:

> "Every program until now ran top to bottom and ended.
> GUI programs don't. After `mainloop()`, the program just
> sits there. It waits for the user to do something — click,
> type, close. When the user does, the program reacts.
> Then it goes back to waiting. That's the *event loop* —
> the fundamental difference between GUI programs and text
> programs."

Some kids will nod immediately; others will need to see it
to understand. Let them experiment with closing and reopening
the window — it really does just sit there.

If any kid asks "what runs after `app.mainloop()`?": the
answer is "nothing, until the user closes the window. Then
mainloop returns and any code after runs."

The Scratch callback is worth making explicit:

> "Phase 1 had something like this. Remember `when green
> flag clicked` and `when sprite clicked`? Those were
> events. The Scratch program waited for events and reacted.
> GUI programming is the same idea, in Python."

#### Customize

Mechanical. Different titles, sizes, fonts. The font is
specified as a tuple `("Arial", 24)` — the parentheses can
be confusing. Walk through:

> "The font is a tuple — three values usually: family,
> size, style. `("Arial", 24)` is just family and size.
> `("Arial", 24, "bold")` adds the style."

#### Multiple labels

Each `pack()` adds the next label below the previous one.
The order in your code is the order on screen.

Worth pointing out:

> "We're stacking labels with `pack()`. It puts each one
> under the last by default. Later we'll see other ways to
> arrange widgets."

### Teaching Part B

#### Themes

`set_appearance_mode("light")` and
`set_default_color_theme("blue")` should be called *before*
creating the window. Demo:

```python
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
# ...
```

Run. Look. Different.

> "Three modes: light, dark, system. System follows your
> OS theme — switches automatically if your OS does. Color
> themes are blue (default), green, dark-blue, and a few
> others."

Have students try a few combinations. Visual exploration is
fun and easy at this stage.

#### Personal welcome screen

This is the personalization moment. Encourage:

> "Make it about something you'd want to build. A quiz
> game. A Bible app. A drawing tool. A pet care app. Just
> the welcome screen for now — buttons and behavior come
> next week."

Walk the room. Help with:
- Font sizing (visual hierarchy)
- Padding (spacing between widgets)
- Theme choices

Several kids will spend lots of time on aesthetics — that's
fine. Visual design is a real skill and they're discovering
they care about it.

#### Stretch — colors and backgrounds

The `text_color` and `fg_color` options let kids further
customize. Walk through quickly. The hex code option
(`"#FF5733"`) is worth mentioning:

> "Colors can be names like 'red' or hex codes like
> '#FF5733'. Hex codes give you any color you want — there
> are color picker tools online if you want a specific
> shade."

The `corner_radius` is the modern-look feature. customtkinter
makes everything look like 2024+ apps with rounded corners
and clean styling.

#### Extension — input prompt for theme

The terminal-input-then-GUI pattern is a small but real
taste of "the user controls things." Until next week's
buttons, this is the only way to take input.

### Common stumbles

- **`ImportError: No module named 'customtkinter'`.** Not
  installed. `pip install customtkinter` (or `pip3` or
  `pip install --user customtkinter` depending on system).
- **Window doesn't appear.** Forgot `app.mainloop()`. The
  program creates the widgets but doesn't show them.
- **Window appears blank.** Created widgets but didn't
  `.pack()` them. Widgets exist but aren't in the layout.
- **Window appears, doesn't have the right text.** Wrong
  parameter name. `text=` not `txt=` or `label=`.
- **Multiple windows appear.** Called `ctk.CTk()` more
  than once. The first one is the main window; only one
  is needed.
- **Window flashes and closes immediately.** Forgot
  `mainloop()` (or it's being called somewhere unreachable
  — under a `def`, after a `return`, etc.).
- **Font tuple syntax confusion.** `font=("Arial", 24)` —
  the parentheses make a tuple. Different from a list (`[]`).
- **Theme call after window creation.** `set_appearance_mode`
  must come before `CTk()` to take effect cleanly.

### Differentiation

- **Younger kids (9-10):** Will spend a lot of time on
  visual customization. Encourage. Less time on the event-
  loop concept; they'll absorb it gradually.
- **Older kids (12+):** Will pick up the syntax fast. Push
  through stretches.
- **Advanced (any age):** Suggest:
  - Reading the customtkinter docs
  - Building a multi-window app (they don't have buttons
    yet but can use `ctk.CTkToplevel` for second windows)
  - Custom widgets (advanced — `class MyWidget(ctk.CTkFrame):`)
  - Image labels (`CTkImage`)
- **Struggling:** A kid who can't get the first window
  open is the kid you focus on. Most common cause:
  customtkinter not installed, or forgot mainloop, or
  forgot `.pack()`.

### What to watch for

- **The "a real window!" reaction.** Several kids will
  visibly process this. Affirm.
- **Frustration when widgets don't appear.** Usually missing
  `.pack()`. Walk through.
- **Kids who go wild with themes and colors.** Encourage —
  they're discovering visual design.
- **The "I want to build [specific app]" moment.** Note
  what kids want to build; useful for milestone planning
  later.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **customtkinter installed cleanly?** — flag any machine
  that had import issues so they're fixed before Session 2.

### Connections forward

- **Session 2 (next week, buttons + events).** Today is
  passive labels; next week is interactive buttons.
- **Session 5 (layouts).** Today's `pack()` is the simplest
  layout; `grid()` and `CTkFrame` come in Session 5.
- **Sessions 6-8.** Today's mental model carries forward.
- **Phase 6 (Pygame).** Game programming has a similar
  event loop. Today's mental model transfers.
- **Phase 7 (web).** Web frontends are also event-driven.
  Today is the mental foundation.
- **Phase 8 (Flask).** Web servers wait for HTTP requests
  the way GUIs wait for clicks. Same pattern, different
  context.
- **Peanut butter callback opportunity:** the "window
  appears blank" bug (forgot `.pack()`) is a precision
  moment. The widget exists; you didn't tell the layout
  about it; nothing appears.

### Materials checklist

- [ ] Demo machine with customtkinter verified
- [ ] EVERY student machine verified to have customtkinter
- [ ] Optional: pre-built welcome screen for destination
      preview
- [ ] Projector (helpful for showing the window appearing)
- [ ] Class roster
