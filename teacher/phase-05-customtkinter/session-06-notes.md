## Session 6 — Teacher Notes

*Phase 5, customtkinter · Session 6 of 8 · Title: Putting it
together — a complete app*

### Purpose of this session

The capstone before the milestone. Five jobs, in priority
order:

1. **Land the integration.** All five widget/layout
   sessions become one coherent app. The "aha" is that
   they already know enough to build something real.
2. **Land the redraw pattern.** State + refresh function
   is the dominant pattern in dynamic UIs. Worth
   internalizing before milestones.
3. **Land persistence as a feature.** Saving to JSON makes
   an app feel real in a way nothing else does. They will
   remember this moment.
4. **Land the class refactor as the production target.**
   Their milestone projects should aspire to this
   structure (though not required).
5. **Set up the milestone.** Today's app is the model for
   what theirs can be.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with customtkinter.
- Fully built `todos.py` (the Part A version) in case a
  kid falls behind and needs the working code to compare.
- Fully built `todos_class.py` (the Part B class version)
  for advanced kids and demo.
- A pre-existing `todos.json` to demo persistence (so the
  app opens with todos already in it).

**Prep time:** ~20 minutes. Build both versions before
class. Test the persistence flow (close → reopen).

### Timing and flow

Total: ~90 min. This is one of the longest sessions.

- **Welcome and recap** (~5 min). Recap the journey:
  Sessions 1-5 each added one piece. Today they all come
  together.
- **Part A: build the todo list** (~50 min) — Step 1
  window ~5 min, Step 2 input row ~10 min, Step 3 list
  area ~5 min, Step 4 storing/showing ~15 min, Step 5
  delete buttons ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: persistence + class refactor** (~25 min) —
  JSON save/load ~15 min, class refactor demo ~10 min.
- **Wrap-up** (~5 min).

If running short, **the class refactor can be cut.** The
JSON persistence is the second-priority goal after Part A.
The class refactor is for advanced kids and demonstration.

### Teaching Part A

#### The pacing trap

This session's biggest risk is going too fast in Part A.
Five steps, each builds on the last, each has a "save and
run" checkpoint. **Do not skip the runs.** If a step is
broken, kids need to know *now*, not at Step 5.

Walk slowly through each step. Run after each one. Have
buddies check each other's screens.

#### Step 4 is the jump

Steps 1-3 are mechanical (place widgets). Step 4 introduces
two new ideas at once:

- **State stored separately from the UI** (the `todos`
  list).
- **The redraw pattern** (`refresh_list` wipes everything
  and rebuilds).

Frame it explicitly:

> "We have two things now. The *data* — `todos`, just a
> Python list. And the *UI* — the labels showing each
> todo. Whenever the data changes, we rebuild the UI from
> scratch. That's the pattern: data is the truth, UI is
> the picture of it."

This is genuinely how React, Vue, and most modern UI
frameworks work. They're learning a real pattern.

#### `winfo_children` and `destroy`

Tkinter-ism. `winfo_children()` returns all child widgets
of a parent. `destroy()` removes a widget completely.
Worth mentioning briefly:

> "`winfo_children` gives us a list of every widget inside
> `list_frame`. We loop through and destroy each one
> before drawing fresh. Cleanup before redraw."

Don't dwell on the name (`winfo` is a Tk historical
artifact).

#### Step 5 — the lambda gotcha

This is the only genuinely hard part of the session. The
`lambda idx=i:` pattern is needed because Python closures
capture variables by reference, not by value. Without the
default argument trick, all delete buttons end up pointing
to the same `i` (the last one).

Don't try to fully explain this to younger kids. Frame it
as a recipe:

> "Whenever you create buttons in a loop, and you need each
> one to remember 'which' it was, use this pattern:
> `command=lambda idx=i: do_something(idx)`. The `idx=i`
> part is what makes each button remember its own index."

For older kids who want to know *why*, the explanation:

> "When the lambda is created, it remembers the *name* `i`,
> not the *value*. By the time you click, `i` is whatever
> it ended up as after the loop — usually the last value.
> The `idx=i` trick captures the value at lambda creation
> time as a default argument. Default arguments are
> evaluated once."

This will land for some, not for others. That's OK. The
recipe works either way.

### Teaching Part B

#### JSON persistence

Mechanically simple. The `json` module from Phase 4
Session 3 (or use a Phase 3 callback if needed). Walk
through:

- `json.dump(todos, f)` — write list to file as JSON text.
- `json.load(f)` — read JSON text back into a Python list.
- `os.path.exists(SAVE_FILE)` — only load if the file
  exists (first run, no file yet).

The "wow" moment is closing the app, reopening it, and
seeing the list still there. Pause for it. Let kids react.

> "Your app has memory now. Close it. Open it. Your todos
> are still there. *That* is what makes an app feel real."

#### When to call `save()`

Three places: after `add_todo`, after `delete_todo`, and
nowhere else (state hasn't changed otherwise). Frame it:

> "Save whenever the data changes. Not before, not after
> on a timer. Right when something changes — write to
> disk."

For larger apps this gets more nuanced (debouncing, etc.),
but for now: change → save.

#### Class refactor

Show, don't drill. Run the class version side by side with
the global version. Same app, different organization.

> "Same behavior. Same widgets. But look how it's
> organized. State on the instance. Methods grouped. The
> `if __name__` block at the bottom. *This* is what
> production GUI code looks like."

Point out the bind:

> "I added one new thing — pressing Enter in the entry
> box adds the todo. Real apps do this. Two lines of code:
> `self.entry.bind('<Return>', lambda e: self.add_todo())`."

Encourage advanced kids to use the class version as a
template for their milestones.

### Common stumbles

- **Skipped a step.** Most failures here. Diagnose by
  asking: "Which step did you last save and run
  successfully?" Go back to there.
- **Forgot to update Add button to use `command=add_todo`.**
  Click does nothing. Walk through Step 4 again.
- **`refresh_list` not called from the right place.**
  Adds a todo but the UI doesn't update. Diagnose: where
  is `refresh_list()` called?
- **Lambda gotcha.** All delete buttons delete the same
  todo (usually the last). Walk through the recipe again.
- **Indentation errors in `refresh_list`.** Easy to mess
  up the nested loop and the row creation. Pair-debug.
- **JSON file in the wrong place.** Look for `todos.json`
  next to `todos.py`. If running from a different working
  directory, JSON might be elsewhere.
- **`json.load` errors on first run.** Should be guarded
  by `os.path.exists`. If they removed the guard,
  `FileNotFoundError`.
- **Forgot to call `refresh_list()` before `mainloop()`**
  after adding load. Loaded todos exist in memory but
  don't show until first add.
- **`winfo_children` returning more than expected.** If
  there are widgets in `list_frame` that aren't rows, they
  get destroyed too. (Shouldn't happen with this design,
  but watch for it if a kid adds extras.)

### Differentiation

- **Younger kids (9-10):** Goal is finishing Part A. The
  class refactor is way too much. JSON persistence is
  optional but worth trying.
- **Older kids (12+):** Push to finish persistence in Part
  B. Class refactor as a stretch.
- **Advanced (any age):** Push through the full class
  refactor. Suggest the "mark complete" extension. They
  might also try multiple lists with `CTkTabview`.
- **Struggling:** A kid who can't get Step 1 working is
  the kid you focus on first. Most common cause: typo, or
  Thonny pointing at wrong file.

### What to watch for

- **The "I built a real app!" moment** at the end of Part
  A. Visible. Some kids will immediately start using the
  todo app for actual things.
- **Frustration with the lambda gotcha.** Reassure — it's
  hard. Walk through the recipe.
- **The "wait, my list saved!" moment** when persistence
  works. The "wow" of Part B.
- **Buddies pair-debugging.** Encourage. This is real
  collaboration.
- **Kids tempted to add features instead of finishing.**
  Redirect: "Get the base working, then add features."

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sessions 7-8 (milestone).** Today's app is the model.
  Many kids will build something todo-shaped. That's fine.
- **Phase 7 (web).** The same patterns appear in web JS
  with localStorage instead of JSON files. Today's mental
  model transfers directly.
- **Phase 8 (Flask).** The redraw pattern resembles how
  Flask renders templates after data changes.
- **Peanut butter callback opportunity:** the lambda
  gotcha is a precision moment. Python did exactly what
  they wrote, not what they meant.

### Materials checklist

- [ ] Demo machine with customtkinter
- [ ] Pre-built `todos.py` (Part A version)
- [ ] Pre-built `todos_class.py` (Part B class version)
- [ ] Pre-existing `todos.json` for persistence demo
- [ ] Projector
- [ ] Class roster
