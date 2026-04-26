## Session 3 — Teacher Notes

*Phase 5, customtkinter · Session 3 of 8 · Title: Inputs —
entries and text boxes*

### Purpose of this session

Inputs are the second-most-common widget category after
buttons. Five jobs, in priority order:

1. **Land `CTkEntry` and `entry.get()`.** The single-line
   text input + the read-the-value pattern.
2. **Land the read-then-use pattern.** Callback does
   `entry.get()` first, then uses the value. Same shape
   they'll see all phase.
3. **Build a real form.** Multi-input → submit → display
   results is the canonical small-app pattern.
4. **Touch input cleanup.** `.lower()`, `.strip()`,
   eventually validation. Real apps process input.
5. **Set up Session 4 (choices).** Today's `entry.get()`
   pattern generalizes to checkbox/radio/dropdown's
   read-the-state methods.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with customtkinter.
- Pre-built quiz or form for destination preview.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min) — last week was buttons.
- **Part A: first entry** (~35 min) — build greeter ~10
  min, walk through new pieces ~10 min, customize and
  delete/insert ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: form** (~40 min) — about-me form ~15 min, quiz
  stretch ~15 min, textbox extension ~10 min.
- **Wrap-up** (~5 min).

If running short, **the textbox extension can be cut.** The
form is the goal.

### Teaching Part A

#### The greeter

Walk through at the projector. The new pieces:

- `CTkEntry` — text input
- `entry.get()` — read the value
- The pattern: callback reads, then updates

> "Same loop as the counter — user does something → callback
> runs → display updates. The new piece is `entry.get()` to
> read the user's text."

The "placeholder text" is the faded prompt text. Mention:

> "The placeholder shows when the entry is empty. Vanishes
> when the user starts typing. Standard form pattern."

#### Read pattern

The standard sequence:

```python
def callback():
    value = widget.get()    # read
    # ... use value ...
    other_widget.configure(text=value)    # update
```

This pattern shows up *everywhere* in GUI programming.
Naming it explicitly helps students recognize it.

#### Customize

Mechanical. `width=300` to make the entry wider. Different
fonts. Different placeholders.

#### Delete / insert

```python
entry.delete(0, "end")
entry.insert(0, "default text")
```

The `(0, "end")` arguments are tkinter's way of saying
"from the start to the end." Delete removes that range;
insert adds at the position.

> "Two common uses: clear the entry after the user submits
> (so they're ready for the next input), or provide a
> default value at startup."

### Teaching Part B

#### About-me form

Walk through. The structure scales naturally:
- One entry per field
- One submit button
- One callback that reads all entries, updates one label

The `wraplength=350` is new and useful. Mention:

> "By default labels go on one line and might run off the
> window. `wraplength` makes them wrap to multiple lines."

#### Quiz stretch

Walk through. The `.lower()` and `.strip()` are real input-
processing moves:

> "Real apps clean up input before checking it. `.lower()`
> handles 'NOAH' vs 'noah'. `.strip()` handles 'Moses '
> with a trailing space. Without these, the user has to
> match exactly — frustrating."

This is "input validation lite." Phase 4 Session 7 covered
real validation with try/except; Phase 5 reinforces it
visually.

#### Textbox extension

`CTkTextbox` is the multi-line variant. The `("1.0", "end")`
syntax for `.get()` is genuinely weird. Mention:

> "tkinter has a quirky way of indexing text. Row 1, column
> 0 is the start. 'end' is, well, the end. Just memorize
> the recipe `textbox.get('1.0', 'end')` to get all the
> text."

Don't dwell. Just show.

The `.split()` call divides the string into words. `len()`
counts them. Practical use of Phase 3 string methods.

### Common stumbles

- **`widget.get` instead of `widget.get()`** — without parens,
  you're getting the method object, not its return value.
- **`entry.text` or `entry.value`** — neither works. Use
  `.get()`.
- **Entry empty when reading** — user didn't type. Always
  check `if value:` before using if it might be empty.
- **`delete(0, "end")` not clearing fully** — sometimes
  cursor weirdness on multi-line text. For Entry (single
  line), `delete(0, "end")` works.
- **Numeric entry but `.get()` returns string** — same as
  Phase 3's `int(input())` pattern. Convert with `int(...)`
  if doing math. Also handle ValueError.
- **The "I typed but the label didn't change" bug** — usually
  forgot to call the callback (no button, or button without
  command). Or callback doesn't reference the entry by name.

### Differentiation

- **Younger kids (9-10):** Stick with the basic greeter and
  about-me form. The quiz stretch may be too much.
- **Older kids (12+):** Will pick this up fast. Push to the
  quiz stretch and textbox extension.
- **Advanced (any age):** Suggest:
  - Input validation with try/except (Phase 3 callback)
  - Enter key binding (`entry.bind("<Return>", ...)`)
  - StringVar for two-way binding
  - Multi-page forms (using frames — preview Session 5)
- **Struggling:** A kid who can't get the basic greeter
  working is the kid you focus on. Most common cause:
  forgot `.get()`, or button doesn't have `command`, or
  variable name typo.

### What to watch for

- **The "real form!" reaction.** Forms feel like real apps.
  Several kids will get excited.
- **Buddies trading quiz topics.** Encourage. Personal
  trivia (sports, Bible, family lore) is fun.
- **Frustration with input that "doesn't match."** Real
  problem; intro to validation. The `.lower()` / `.strip()`
  cleanup is the lesson.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 4 (choices).** Same `widget.get()` pattern for
  reading state.
- **Session 6 (integration).** Forms become bigger apps.
- **Phase 8 (Flask).** Web forms — same conceptual model.
- **Peanut butter callback opportunity:** the
  `entry.get` (no parens) bug is a precision moment.

### Materials checklist

- [ ] Demo machine with customtkinter
- [ ] Pre-built quiz or form for preview
- [ ] Projector
- [ ] Class roster
