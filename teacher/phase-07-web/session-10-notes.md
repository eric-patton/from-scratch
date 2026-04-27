## Session 10 — Teacher Notes

*Phase 7, Web · Session 10 of 17 · Title: Build an
interactive todo list*

### Purpose of this session

The JS integration project. Five jobs, in priority
order:

1. **Land the form-submit + preventDefault pattern.**
   The standard way to wire up forms in JS.
2. **Land `createElement` + `appendChild`.** Building
   DOM dynamically. Everything from todos to chat
   messages uses this.
3. **Land per-item event listeners.** Each delete
   button gets its own listener — closures over the
   item make this clean.
4. **Phase 5 callback.** They built this same app in
   customtkinter. The shape is identical; the syntax
   differs. Drive the comparison home.
5. **Set up Session 11 (localStorage).** Today's app
   resets on reload. Next session fixes that.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built todo app (the Step 5 end-state).
- Optional: pre-built class-refactored version for
  advanced kids.
- Optional: side-by-side with Phase 5's customtkinter
  todo for comparison.

**Prep time:** ~25 minutes. Build the full todo
once before class.

### Timing and flow

Total: ~90 min — possibly tight given the breadth.

- **Welcome and recap** (~5 min). Recap Session 9.
  Today: integration.
- **Part A: HTML + first add** (~25 min). Type live.
  Steps 1-2.
- **Part A: styling + delete + toggle** (~30 min).
  Steps 3-5.
- **Break** (~5 min).
- **Part B: counter + empty state** (~20 min).
- **Wrap-up** (~5 min).

If running short, **drop empty state and counter
stretches.** The base todo (add/delete/toggle) is
the priority.

### Teaching Part A

#### "Same as Phase 5"

Open with the comparison:

> "Remember the customtkinter todo from Phase 5
> Session 6? Same app today, in the browser. Same
> shape: a form to add, a list to show, buttons to
> delete. Different language, different runtime.
>
> Compare as we build — you'll see the parallels."

#### `event.preventDefault()` is non-negotiable

> "Forms reload the page by default when submitted.
> Bad for our app — we'd lose all our JS state. So
> the *first thing* in our submit handler is
> `event.preventDefault()`. Stops the default behavior."

This is *the* most-forgotten line in the JS world.
Drill it.

#### `createElement` + `appendChild`

The two-step DOM addition pattern:

```javascript
const item = document.createElement("li");
item.textContent = "Pizza";
list.appendChild(item);
```

Frame:

> "1. Make the element. 2. Set its content. 3. Stick
> it onto the page. *Three steps.* This is how
> dynamic content works in JS — every chat message,
> every search result, every notification, gets
> created this way."

#### Closure over `item`

When the delete button is created inside the same
function that created the item, the click handler
**closes over** the `item` variable:

```javascript
deleteBtn.addEventListener("click", () => {
    item.remove();    // "item" is captured from the outer scope
});
```

> "The arrow function 'remembers' which `item` it's
> attached to, even though that variable lives in
> the outer function. This is *closure*. It's how
> we get per-item handlers without writing per-item
> code."

This is real JavaScript — closures are foundational.
Don't drill the term, but show the *behavior*.

(Phase 6 had the lambda gotcha in Pygame; this is
the *clean* JS version.)

#### `item.remove()`

Built-in DOM method. One line removes the element
from the page. Way cleaner than `parentNode.removeChild(...)`
(the old way).

### Teaching Part B

#### Counter and empty state

The pattern: any change to the list should sync the
display.

```javascript
function updateAll() {
    updateCounter();
    updateEmptyMessage();
}
```

Then call `updateAll()` after add, after delete,
after toggle.

> "The list is the truth. The counter and message
> are just *views* of it. Change the list, sync the
> views."

This is a baby version of the "data + redraw"
pattern from Phase 5 Session 6 (the customtkinter
todo's `refresh_list()`). Same idea.

#### `confirm("Are you sure?")`

Built-in browser dialog. Returns true/false.

```javascript
if (confirm("Are you sure?")) {
    // ... do the destructive thing
}
```

Quick way to add a "are you sure" check. Real apps
often use custom modals; for kids, `confirm` is
fine.

Note: also `alert("...")` and `prompt("...", "default")`
exist. The trio of built-in dialogs.

#### Class refactor (advanced)

For kids who finish early or want the production
shape, suggest the TodoApp class. Same pattern as
Phase 5 Session 6's class refactor. Real production
JS uses classes (or modules) for organization.

### Common stumbles

- **Forgot `preventDefault`.** Page reloads on
  submit, app resets. Walk through.
- **Empty submission.** No `trim` and `if (text
  === "")` guard — empty todos appear.
- **Delete button doesn't work.** Wrong element
  selected. Or attached the listener to the wrong
  element. Walk through.
- **All delete buttons delete the same item.**
  Closure issue — but in this design it shouldn't
  happen because each `item` is local to its
  iteration. But if a kid uses a `for` loop with
  `var i`, they hit the classic closure gotcha. Use
  `let` or arrow functions.
- **Element appears but unstyled.** New `<li>` doesn't
  inherit the styling because... it does. CSS for
  `#todoList li` applies to all children including
  newly added ones. If unstyled: check that JS
  appends to the right parent.
- **Layout wrong because no flex.** Default `<li>`
  display doesn't put text and button side-by-side.
  The CSS uses `display: flex; justify-content:
  space-between;` to lay them out.
- **Click on text doesn't toggle.** `span` not
  selected, or listener attached to `item` instead
  of `span`.
- **Counter shows wrong number.** Counter not called
  in all the right places (forgot one of add/delete/
  toggle).
- **Empty message doesn't disappear.** Forgot to
  call `updateEmptyMessage` after add. Or the logic
  is inverted.

### Differentiation

- **Younger kids (9-10):** Goal is the basic add-
  todo + delete (Steps 1-4). Skip the toggle, empty
  state, counter.
- **Older kids (12+):** Push for full Part A + at
  least counter or empty state from Part B.
- **Advanced (any age):** Push for class refactor +
  multiple Part B stretches. Suggest:
  - Edit todo on double-click
  - Filter (all/active/done)
  - Push to GitHub
  - Drag-to-reorder (`dragstart`/`dragover`/`drop`)
- **Struggling:** A kid who can't get one todo to
  add is the kid you focus on. Most common cause:
  forgot `preventDefault`, wrong selector, or
  forgot to clear input.

### What to watch for

- **The "I built a real app" reaction.** First
  successful add-and-delete moment is real. Pause
  for it.
- **Buddies showing each other todos they added.**
  Encourage. The collaborative testing is real.
- **Kids adding silly todos.** "Pet the cat", "Rule
  the world", etc. Fine — let them have fun.
- **Kids reaching for the "delete" experience first.**
  They'll add a todo just to test deletion. Real UX
  testing.
- **Comparison to Phase 5.** "This is way more code
  than customtkinter!" Yes. customtkinter wraps a
  lot. JS gives more control. Reframe.
- **The "reload erases everything" frustration.**
  Real moment — set up Session 11.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 11 (localStorage).** Today's app +
  persistence = real, useful app.
- **Session 13 (canvas game).** Different DOM
  manipulation, same event-driven shape.
- **Session 14 (fetch).** Today's app + a server =
  shareable across devices.
- **Phase 8 (Flask).** Server-side todo with form
  POSTs. Combine with today's JS for live updates.
- **Career-long callback:** the create-element +
  append-child + per-item-listener pattern powers
  *every* interactive list on the web. Tabs, news
  feeds, comments, notifications, dropdowns — all
  same shape.
- **Peanut butter callback opportunity:** the
  forgot-preventDefault → page reload bug is a
  precision moment. Default behavior happens unless
  you stop it.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built todo app (Step 5 end-state)
- [ ] Optional: class-refactored version
- [ ] Optional: Phase 5 customtkinter todo open for
      comparison
- [ ] Projector
- [ ] Class roster
