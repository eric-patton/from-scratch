## Session 4 — Teacher Notes

*Phase 5, customtkinter · Session 4 of 8 · Title: Choices —
checkboxes, radio buttons, dropdowns*

### Purpose of this session

Completes the basic widget vocabulary. Five jobs, in
priority order:

1. **Land the three choice widget types.** Different
   patterns for different decisions: many-out-of-many
   (checkboxes), one-of-many (radios), pick-from-list
   (dropdown).
2. **Land `StringVar` for shared state.** Required for
   radios; introduces a Python concept that comes up later.
3. **Land the read pattern for each widget type.** Each
   widget has its own `.get()` mechanic.
4. **Build a substantial form.** The character builder is
   the integration of all widget types so far.
5. **Set up Session 5 (layouts).** Today's forms get long
   and crowded with `pack()`; layouts will fix that.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with customtkinter.
- Pre-built character form for destination preview.

**Prep time:** ~15 minutes. The character form is bigger;
build it once before class.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min).
- **Part A: choice widgets** (~40 min) — checkboxes ~10
  min, radio buttons ~15 min (StringVar concept), dropdowns
  ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: character form** (~35 min) — build base ~20
  min, real-time updates stretch ~10 min, save extension
  ~5 min.
- **Wrap-up** (~5 min).

If running short, **the real-time stretch and save extension
can be cut.** The character form is the goal.

### Teaching Part A

#### Checkboxes — independent yes/no

Walk through. The `.get()` returns `1` (checked) or `0`
(unchecked). Use `if check.get() == 1:` or `if check.get():`
(0 is falsy, 1 is truthy).

The pattern: a list of checked items, built by checking
each.

#### Radio buttons — pick exactly one

The conceptual difference from checkboxes:

> "Checkboxes: pick any number, including zero. Radios: pick
> exactly one. They're for different kinds of questions."

The `StringVar` is the new mechanic. Frame it:

> "Radio buttons need to *share* state — only one can be
> selected. To do that, we make a special variable called
> `StringVar` that all the radios reference. When one is
> clicked, the variable updates to that radio's value.
> When you read the variable, you know which is selected."

The syntax is fiddly. Walk through carefully:

```python
pet_choice = ctk.StringVar(value="dog")    # the shared variable

dog_radio = ctk.CTkRadioButton(
    app,
    text="Dog",
    variable=pet_choice,    # shared variable
    value="dog"             # what to set it to
)
```

Three things to remember:
1. Make a `StringVar` first.
2. All radios in the group use `variable=that_var`.
3. Each radio has a unique `value=...`.

#### Dropdowns — pick from a list

Mechanically simpler than radios. Just `values=[list]`.
`.get()` returns the selected string.

The two flavors (`CTkOptionMenu` vs `CTkComboBox`) — option
menu is fixed list, combo box allows typing too. Most apps
use option menu.

> "OptionMenu when the list is fixed. ComboBox when the
> user might want to type something not in the list. For
> kids' apps, OptionMenu usually."

### Teaching Part B

#### Build the character form

Walk through structure. Lots of widgets. The point is the
combination — all four widget types working together.

The output uses an f-string with newlines (`\n`) for
multi-line output. Worth pointing out:

> "F-strings can have `\n` for newlines. Multi-line output
> reads cleanly when the label has `wraplength`."

#### Real-time updates stretch

The `command=` parameter on choice widgets calls a function
when the user changes the selection. No submit button
needed.

For the OptionMenu, the command receives the selected value
as a parameter (different from buttons which receive
nothing). Hence the `lambda x: update()` to ignore it.

For Entry widgets, you `bind("<KeyRelease>", ...)` since
they don't have a `command` parameter.

> "Real-time updates feel modern. The user sees their choice
> reflect immediately. This is how most reactive web apps
> work."

#### Save extension

File I/O callback. The "characters.txt" file persists across
runs. Same pattern as Phase 3 Session 11's notes program.

### Common stumbles

- **Checkbox state confusion.** `.get()` returns 1/0, not
  True/False. `if check.get() == 1:` or `if check.get():`
  both work; first is more explicit.
- **Radios all checked at once.** Forgot the shared
  `StringVar`. Without `variable=`, each radio is
  independent (which defeats the purpose).
- **Radio variable wrong type.** `IntVar(value=1)` instead
  of `StringVar(value="dog")`. Match the type to your
  values.
- **OptionMenu callback gets unexpected argument.**
  `command=update` errors because OptionMenu passes the
  value. Use `command=lambda x: update()`.
- **Default radio not selected.** Forgot `value=` on the
  StringVar. With no default, no radio appears selected
  initially.
- **Forgot to read shared variable.** Used `dog_radio.get()`
  thinking it returns the radio's state. Should be
  `pet_choice.get()` (the shared variable).

### Differentiation

- **Younger kids (9-10):** Checkboxes are easiest, then
  dropdowns. Radio buttons (with StringVar) are the
  trickiest concept. Make sure they get checkboxes
  working before pushing to radios.
- **Older kids (12+):** Will pick up all three quickly.
  Push through real-time updates and save extension.
- **Advanced (any age):** Suggest:
  - Multiple radio groups in one form (different StringVars)
  - SegmentedButton, Slider, Switch as alternatives
  - Validation: disable Submit until name is filled in
  - Custom widget classes
- **Struggling:** A kid who can't get checkboxes working is
  the kid you focus on. Most common cause: confused
  `.get()` syntax or callback issues.

### What to watch for

- **The "wait, only one radio at a time?" reaction.** Some
  kids initially try to fight it ("I want both!"). Frame
  the difference: "checkboxes are for 'any of these';
  radios are for 'exactly one of these.'"
- **Buddies trading character ideas.** Encourage. Creative
  characters are fun.
- **Kids who try to use radio buttons as checkboxes.**
  Rare; gentle redirect.
- **Frustration with StringVar.** It's a real conceptual
  hurdle. Walk through patiently.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 5 (layouts).** Today's forms get long with
  `pack()`. Layouts solve the organization problem.
- **Session 6 (integration).** Forms become full apps.
- **Phase 8 (Flask).** HTML forms have the same shapes —
  text inputs, checkboxes, radios, selects. Today's
  conceptual model transfers.
- **Peanut butter callback opportunity:** the "radio buttons
  all check at once" bug is a precision moment. They
  weren't told to share state, so they didn't.

### Materials checklist

- [ ] Demo machine with customtkinter
- [ ] Pre-built character form
- [ ] Projector
- [ ] Class roster
