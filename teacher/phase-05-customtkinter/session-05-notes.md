## Session 5 — Teacher Notes

*Phase 5, customtkinter · Session 5 of 8 · Title: Layouts
and frames*

### Purpose of this session

Layouts elevate apps from "widget stack" to "real software
look." Five jobs, in priority order:

1. **Land `grid()` for 2D layouts.** rows and columns.
2. **Land "don't mix pack and grid in the same container."**
   The single most common layout bug.
3. **Land `CTkFrame` for grouping.** Frames within frames.
   Each frame is its own layout context.
4. **Land "real apps look like header-sidebar-content."**
   The structural pattern of most modern apps.
5. **Set up Session 6 (integration).** Today's layouts are
   the structural foundation for tomorrow's full app.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with customtkinter.
- Pre-built header-sidebar-content app for destination
  preview.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min).
- **Part A: grid** (~35 min) — motivation ~5 min, basic
  grid example ~15 min, columnspan + sticky ~10 min,
  checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: frames** (~40 min) — concept + two-section
  app ~15 min, header-sidebar-content ~15 min, sidebar
  callbacks stretch ~5 min, class refactor extension ~5
  min.
- **Wrap-up** (~5 min).

If running short, **the class refactor extension can be
cut.** The header-sidebar-content layout is the goal.

### Teaching Part A

#### Motivation

Show a `pack()`-only form with 8 widgets. Awkward — long
vertical strip. Then show the same with `grid()` — labels
next to entries, button at the bottom. Better.

#### Build the basic grid

Walk through:

```python
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
```

Same row (0), different columns (0 and 1). They appear side
by side.

> "`row` and `column` start at 0. Same idea as list
> indexing. Each widget claims a cell at (row, column)."

The `padx=10, pady=10` is the same padding from `pack`.

#### The "don't mix" rule

Demo the problem. In a `pack()`-using app, try to add a
`grid()` widget. Nothing happens (or app freezes).

> "In a single container, use one or the other. Not both.
> If you do, weird things happen — sometimes the program
> just hangs. Different containers can use different
> methods, but inside one container, pick one."

This rule saves real bugs. Drill it.

#### `columnspan`

For widgets that should span multiple columns (like a
button under a 2-column form):

```python
button.grid(row=2, column=0, columnspan=2)
```

Button takes both columns at row 2.

#### `sticky`

For alignment within a cell:

```python
label.grid(row=0, column=0, sticky="e")    # east = right
```

Useful for right-aligning labels next to left-aligned
entries.

Don't drill all directions. The "e" / "w" / "ew" cases
cover most needs.

### Teaching Part B

#### What's a frame

> "A frame is a container — it holds other widgets. Inside
> the frame, you use pack or grid like normal. Then the
> frame itself is packed or gridded into its parent."

The "frames within frames" model is the structural insight.

#### Two-section app

Walk through:

```python
left_frame = ctk.CTkFrame(app)
left_frame.pack(side="left", fill="both", expand=True)

# widgets inside left_frame
ctk.CTkLabel(left_frame, ...).pack(...)
```

The `side="left"` is new — `pack()` can do horizontal too.

The `fill="both", expand=True` makes the frame stretch to
fill available space. Worth explaining briefly:

> "`fill` says how the widget should stretch in its
> available space. `expand=True` says the widget should
> grab any extra space in its container. Together: this
> frame fills the available space and grows with the
> window."

#### Header-sidebar-content

The canonical "real app" layout. Walk through.

> "This is the shape of most modern apps. Header at the
> top with the title. Sidebar on the left with navigation.
> Content area on the right. The user clicks a sidebar
> button, the content area updates."

This is genuinely satisfying for kids — their app looks
like a real app, not just a form.

#### Sidebar callbacks stretch

Mechanical addition. Each button's callback updates the
content. Same pattern as Phase 5 Session 2's counter, just
in a structured layout.

#### Class refactor extension

Show the class version. Don't drill — it's for advanced
kids. The point: state (`self.content_label`) lives on the
instance, no `global` needed.

> "When apps get bigger, the class structure pays off
> hugely. State organized. Methods grouped. Reusable. Real
> production GUI code looks like this."

### Common stumbles

- **Mixed pack and grid.** App freezes or behaves
  weirdly. Debug: pick one method per container.
- **Forgot `pack()` or `grid()` on a widget.** Widget
  exists but doesn't show. Same as Session 1.
- **`grid()` cells in wrong positions.** Walk through the
  row/column numbers. Use a piece of paper to plan grids
  if needed.
- **Frame doesn't appear.** Forgot to pack the frame
  itself, only the widgets inside it.
- **Widget added to wrong frame.** `ctk.CTkButton(app, ...)`
  when meant `ctk.CTkButton(left_frame, ...)`. The first
  argument is the parent.
- **Frames don't size as expected.** `expand=True` and
  `fill="both"` are usually what you want. If a frame
  appears too small, those are missing.

### Differentiation

- **Younger kids (9-10):** Focus on the basic grid in Part
  A and the two-section app in Part B. The header-sidebar-
  content might be too much.
- **Older kids (12+):** Push through the full
  header-sidebar-content layout. Stretch goal: sidebar
  callbacks.
- **Advanced (any age):** Push to the class refactor.
  Suggest:
  - Multiple "screens" via swapping content frames
  - Scrollable frames for long content
  - Grid weight (rows/columns that grow with window)
  - Multi-window apps with `CTkToplevel`
- **Struggling:** A kid who can't get the basic 2-column
  grid working is the kid you focus on. Most common cause:
  mixed pack/grid in one container, or wrong row/column
  numbers.

### What to watch for

- **The "this looks like a real app!" reaction** at the
  header-sidebar-content layout. Visible processing.
- **Frustration with the "don't mix" rule.** Some kids will
  try anyway. Reinforce.
- **Buddies designing layouts together.** Encourage. Real
  UX practice.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 6 (integration).** Layouts + widgets + state.
  Today's structure becomes tomorrow's app.
- **Sessions 7-8 (milestone).** Milestone projects use
  layouts.
- **Phase 7 (web).** HTML layouts (CSS Grid, Flexbox) have
  similar concepts. Today's mental model transfers.
- **Peanut butter callback opportunity:** the "mixed pack
  and grid" bug is a precision moment.

### Materials checklist

- [ ] Demo machine with customtkinter
- [ ] Pre-built header-sidebar-content app
- [ ] Projector
- [ ] Class roster
