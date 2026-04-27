## Session 11 — Teacher Notes

*Phase 7, Web · Session 11 of 17 · Title: localStorage
— make state survive*

### Purpose of this session

The persistence session. Five jobs, in priority
order:

1. **Land `localStorage` API** — four methods, one
   key-value store. Easy.
2. **Land JSON serialization.** `JSON.stringify` /
   `JSON.parse` for non-string data. The standard
   pattern.
3. **Land "save on change, load on start."** The
   standard persistence pattern.
4. **Phase 5 callback.** customtkinter Session 6's
   JSON file save → today's localStorage. Same
   shape, different storage backend.
5. **Set up Sessions 12-13 (canvas).** Persistence
   sessions tend to be lighter; gives breathing
   room before the canvas content.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built settings example (Part A).
- Pre-built todo app with localStorage (Part B
  end-state).
- DevTools Application/Storage tab open and ready
  to demo.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 10.
  "Reload erases everything — let's fix that."
- **Part A: localStorage basics** (~15 min). Demo in
  console, then build settings.
- **Part A: settings example** (~20 min).
- **Break** (~5 min).
- **Part B: persist the todo** (~35 min).
- **Wrap-up** (~10 min).

If running short, **drop the settings example** —
go straight to persisting the todo. The todo is
the higher-payoff outcome.

### Teaching Part A

#### "Reload erases everything"

Open with the frustration:

> "Last week we built a todo app. Awesome. Reload
> the page... gone. *That's not how real apps
> work.* Today we fix it."

#### Demo in the DevTools console first

Before any HTML/JS file work:

1. Open any page.
2. Open DevTools console.
3. Type `localStorage.setItem("test", "hello")`.
4. Type `localStorage.getItem("test")` — see
   "hello".
5. **Reload the page.** Type `getItem` again. Still
   "hello".
6. Show DevTools → Application → Local Storage.
   See the key.

> "*Persistence in your browser.* The simplest API
> in JS. Four methods. That's it."

#### Strings only — JSON solves it

> "localStorage stores strings. If you stuff an
> array in, it converts it to a string — and you
> can't easily get the array back.
>
> Solution: `JSON.stringify` to save, `JSON.parse`
> to load. Universal pattern for any data more
> complex than a single string."

Demo:

```javascript
const arr = [1, 2, 3];
localStorage.setItem("nums", arr);
localStorage.getItem("nums");    // "1,2,3" — string!

localStorage.setItem("nums", JSON.stringify(arr));
JSON.parse(localStorage.getItem("nums"));    // [1, 2, 3] — array!
```

The contrast is illuminating.

#### Settings example

A simpler example than the todo. Two settings:
checkbox + text input. Save on change, load on
start.

The pattern is **canonical** for persistence:

```javascript
// Load on start
const saved = localStorage.getItem("key");
if (saved) {
    // apply
}

// Save on change
input.addEventListener("input", () => {
    localStorage.setItem("key", input.value);
});
```

Walk through. Show the reload "still there" moment.

#### `getItem` returns `null`, not `undefined`

If the key doesn't exist, `getItem` returns `null`.
Worth mentioning:

```javascript
const x = localStorage.getItem("nope");    // null
```

Use `||` for default:

```javascript
const name = localStorage.getItem("name") || "Anonymous";
```

### Teaching Part B

#### Refactor required

The Session 10 todo's add logic is inline in the
form handler. To support loading saved todos, we
need to extract it into a function.

> "We need *one* function that creates an item with
> given text and done state. Then the form-submit
> can call it with the typed text, and the load
> can call it for each saved todo. *Same code,
> two callers.* That's the refactor."

```javascript
function addItem(text, done = false) {
    // ... build the item, attach listeners
    list.appendChild(item);
}
```

The `done = false` is a default parameter — same as
Python.

#### Save on every change

> "When does the data change? Add. Delete. Toggle
> done. Every one of those should call `saveTodos()`."

Walk through where to add `saveTodos()`:

- After the new item is added in the form handler.
- Inside the delete button click handler.
- Inside the toggle (span click) handler.

Three places. Miss one and that change isn't saved.

#### Load on start

```javascript
loadTodos();
```

One line at the bottom of `app.js`. Reads from
localStorage, calls `addItem` for each.

#### The "wow" moment

After it works:

1. Add several todos.
2. Mark some as done.
3. Close the browser tab.
4. Open `index.html` in a fresh tab.
5. **Todos are still there.**

Pause for the reaction. Some kids will *visibly*
process it. They'll close the laptop and reopen it
to confirm.

### Common stumbles

- **Forgot `JSON.stringify`/`JSON.parse`.** Saves
  weird strings, loads weird data.
- **`getItem` returns null and code crashes.**
  Forgot the null check or `|| default`.
- **Save not called everywhere.** A change happens
  but isn't persisted. Walk through: every list
  modification needs `saveTodos()`.
- **Save called too early.** Inside the form
  submit, called *before* `addItem` — saves the
  list state from *before* the add.
- **`addItem` with no `done` parameter.** Old code
  doesn't pass it, gets `undefined`, weird state.
  Default parameter `done = false` solves this.
- **Loaded todos don't have working delete buttons.**
  `addItem` not attaching listeners properly.
  Trace through.
- **`localStorage` quota exceeded.** ~5MB per
  origin. Won't be an issue for todos but worth
  knowing.
- **Different browser, no data.** Each browser has
  separate localStorage. Reassure: this is
  expected.
- **Incognito mode storage.** localStorage works in
  incognito but is wiped when window closes.
- **Old `var` issues.** Same as before — push
  `let`/`const`.

### Differentiation

- **Younger kids (9-10):** Goal is the basic
  persistent todo (add only). Skip the toggle and
  delete persistence.
- **Older kids (12+):** Push for full persistent
  todo + at least one stretch.
- **Advanced (any age):** Push for:
  - Multiple lists
  - Export/import as JSON
  - Auto-save drafts
  - Different storage (sessionStorage comparison)
  - Real practice: refactor previous projects
    (counter from Session 9, etc.) to persist
    state.
- **Struggling:** A kid who can't get save-and-
  reload working is the kid you focus on. Most
  common cause: forgot JSON, forgot to call save in
  one of the handlers.

### What to watch for

- **The "my todos came back!" reaction.** Real,
  visible. Pause for it.
- **Buddies showing each other persisted state.**
  "Look, I closed it and they're still here."
  Encourage.
- **Kids checking DevTools Application tab.** Real
  inspection. Show that they can edit values
  there.
- **Kids hitting the "different browser, no data"
  realization.** Affirm — explain that real apps
  use server-side storage to share across devices.
- **The "wait, what happens if I store a million
  todos?" curiosity.** Real performance question.
  ~5MB limit; hundreds of todos easy.
- **Kids realizing they could persist any state.**
  Counter, settings, score... yes. Encourage them
  to retrofit Session 9's counter to persist.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 13 (canvas game).** Save high score
  to localStorage.
- **Session 14 (fetch).** localStorage for client-
  side, fetch for server-side. Both are real
  patterns.
- **Phase 8 (Flask).** Server-side persistence
  (databases) for data that needs to be shared
  across devices/users.
- **Phase 5 callback.** customtkinter's JSON file
  save did the same job for desktop apps.
- **Career-long callback:** localStorage is *the*
  client-side persistence API. Used everywhere.
  Often combined with server-side storage for
  best-of-both.
- **Peanut butter callback opportunity:** the
  forgot-to-save in one handler → "why aren't my
  changes persisting?" debugging is a precision
  moment. Computer saves only when you call save.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built settings example
- [ ] Pre-built todo app with localStorage
- [ ] DevTools Application/Storage tab familiar
- [ ] Projector
- [ ] Class roster
