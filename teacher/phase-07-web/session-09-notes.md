## Session 9 — Teacher Notes

*Phase 7, Web · Session 9 of 17 · Title: The DOM —
querySelector and events*

### Purpose of this session

The "JavaScript meets the page" session. Five jobs,
in priority order:

1. **Land `document.querySelector`.** The single most
   useful DOM method. Use CSS selectors (already
   familiar) to find elements.
2. **Land `addEventListener`.** The event-driven model
   of the browser. Same shape as Phase 5
   customtkinter `command=` parameter.
3. **Land `.textContent` and `.value`.** Two
   properties. Different elements, different ones.
4. **Land `classList.toggle` over `.style.X`.** Push
   the CSS-classes-control-styling discipline.
5. **Set up Session 10 (todo).** Today's patterns
   become tomorrow's app.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built counter example.
- Pre-built greeting with dark-mode toggle.
- Pre-built clickable todo list (the stretch).
- Optional: a real interactive site (search-as-you-
  type) for "see how this is used everywhere."

**Prep time:** ~20 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 8.
- **Part A: querySelector + textContent** (~15 min).
- **Part A: addEventListener + click** (~15 min).
- **Part A: counter** (~15 min). Type live.
- **Break** (~5 min).
- **Part B: input + value + live updates** (~15 min).
- **Part B: classList toggle + dark mode** (~15 min).
- **Wrap-up** (~5 min).

If running short, **drop the stretch list and
preventDefault stretch.** The greeting + dark mode
is the priority.

### Teaching Part A

#### "DOM is the bridge"

Frame:

> "The browser turns your HTML into a *tree of
> objects* in memory. JavaScript can reach into
> that tree, find elements, change them, listen for
> what the user does. That tree is the **DOM** —
> Document Object Model.
>
> Without the DOM, JS would be useless on a web
> page — just a calculator running in the
> background. With the DOM, JS becomes the
> *behavior* of the page."

#### `document.querySelector` is the workhorse

> "One method, takes a CSS selector, returns the
> first matching element. Same selectors as you
> learned in CSS — `'h1'`, `'.card'`, `'#main'`.
> One API, two purposes."

The *unified-with-CSS* part is satisfying — kids
realize they already know the selectors.

#### `.textContent` writes the page

The "wait, I just changed the page from JavaScript"
moment. Pause for it.

```javascript
document.querySelector("h1").textContent = "I changed!";
```

Type in the console of any open page (a kid's own
page is fine). The heading changes. Magic.

> "*That* is the power. JavaScript can change
> *anything* on the page."

#### `addEventListener` — Phase 5 callback

Frame:

> "Phase 5 had `command=function`. JavaScript has
> `addEventListener('click', function)`. Same idea
> — when this thing happens, run that function.
> Different syntax, same model."

The arrow function syntax `() => { ... }` may still
feel new. Walk through:

```javascript
button.addEventListener("click", () => {
    // this runs on click
});
```

The arrow function is the second argument. **The
parentheses around `()` are required even with no
arguments.**

#### Build the counter live

Type the counter on the projector. Step by step:

1. HTML — display + three buttons.
2. JS — count variable + 4 references + 3 listeners.
3. Each handler: update count, sync display.

After each step, run. After step 3, click the
buttons. Watch the count.

> "This is the pattern of *every* interactive JS
> app: state, references, listeners, sync. Memorize
> this shape."

### Teaching Part B

#### `.value` vs `.textContent`

Easy point of confusion. Frame:

> "For `<input>` and `<textarea>`, the value lives
> in `.value`. For `<p>`, `<h1>`, `<div>` — the
> visible text — use `.textContent`.
>
> Wrong one = either undefined or weird. Match the
> property to the element type."

Show:

```javascript
const inputValue = inputEl.value;          // for inputs
const headingText = headingEl.textContent;   // for displays
```

#### `input` event = live updates

The "`input` event fires on every keystroke" is the
modern reactive moment.

> "Click the button to greet — old school. Update
> *as you type* — modern. The `input` event lets
> you do that."

Demo: type a name, watch the greeting refresh
character by character.

#### `classList.toggle` over `.style.X`

The discipline:

> "You *could* set `element.style.backgroundColor =
> 'black'` directly from JS. Don't.
>
> Better: define the visual change in CSS as a
> class (`.dark { background: black; ... }`), then
> toggle the class from JS. CSS keeps the visual
> decisions; JS keeps the *what changed* decisions.
> Cleaner separation."

Demo the dark mode toggle. The CSS does all the
work; JS just toggles the class.

#### `event.preventDefault()` (stretch)

For forms, the default submit reloads the page. JS
needs to stop it:

```javascript
form.addEventListener("submit", (event) => {
    event.preventDefault();
    // ... handle the form here
});
```

Mention as a teaser for Session 10. Don't drill
unless time.

### Common stumbles

- **`querySelector` returns null.** Selector doesn't
  match anything. Check the ID/class spelling.
- **Trying to use selector before page loads.**
  `<script>` in `<head>` runs before the body.
  Either move script to end of body, or wait for
  `DOMContentLoaded`. For our curriculum: end of
  body is simpler.
- **Used `.value` on a `<p>`** (or `.textContent` on
  an `<input>`). Wrong property for the element
  type.
- **Changed `.textContent` and lost child elements.**
  `.textContent = "..."` replaces *everything*
  inside. If the element had child elements, they're
  gone.
- **Used `==` not `===`.** Same precision moment as
  Session 8.
- **Forgot `.value`.** `input.textContent` is empty;
  the value comes from `.value`.
- **Listener attached but not firing.** Wrong element
  selected, or wrong event name (`click` vs
  `clicked`).
- **Listener fires multiple times.** Attached
  multiple times (e.g., inside a loop). Each call to
  `addEventListener` adds a new listener.
- **Using `onclick=` HTML attribute.** Older style.
  Works but mixes HTML and JS. Use
  `addEventListener` from JS.
- **Forgot the function in `addEventListener`.**
  `button.addEventListener("click")` errors —
  needs the second arg.
- **Reading `.value` of a non-existent input.**
  Returns undefined. Always verify the selector.

### Differentiation

- **Younger kids (9-10):** Goal is the counter or
  greeting. One working interactive page.
- **Older kids (12+):** Push for both Part A and
  Part B. Try the toggleable list stretch.
- **Advanced (any age):** Suggest:
  - Calculator (two inputs, four operations)
  - Character counter for textarea
  - Color picker that changes background
  - Typewriter effect (text appears letter by letter)
  - Multiple themes (light/dark/sepia)
- **Struggling:** A kid who can't get one click to
  change one thing is the kid you focus on. Most
  common cause: wrong selector, or script in head
  before body.

### What to watch for

- **The "I changed the page from code!" reaction.**
  First successful DOM change is real. Pause for
  it.
- **Buddies trading dark-mode demos.** Encourage.
- **Kids over-using `.style.X`.** Push toward
  classList.toggle. Real practice.
- **Excitement about `input` event.** "It updates
  as I type!" Yes. That's the modern web.
- **Comparing to Phase 5 customtkinter.** "This is
  the same as `command=function`!" Yes — affirm.
- **The "what else can I select?" curiosity.** Some
  kids will start querying everything. Encourage —
  this is real DOM exploration.
- **DevTools console abuse on real sites.** Some kids
  will type `document.querySelector("h1").textContent
  = "lol"` on Wikipedia or similar. Mention briefly
  that those changes are *local* (vanish on
  refresh) — they're not actually changing the
  internet.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 10 (todo).** Today's pattern (state +
  references + listeners) becomes the todo app.
- **Session 11 (localStorage).** Same DOM, but state
  *survives reloads*.
- **Session 13 (canvas game).** Canvas is also DOM
  manipulation — but for graphics instead of HTML
  elements.
- **Session 14 (fetch).** Async data loading +
  updating the DOM = real web app pattern.
- **Phase 8 (Flask).** JS handles the front-end
  interactivity; Flask handles the back-end. Today's
  skills transfer.
- **Career-long callback:** the DOM is the foundation
  of *all* web JS — including React, Vue, etc.
  (those frameworks just *automate* DOM
  manipulation under the hood).
- **Peanut butter callback opportunity:** the
  `.value` vs `.textContent` confusion is a
  precision moment. Wrong property = `undefined` or
  empty.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built counter
- [ ] Pre-built greeting with dark mode
- [ ] Pre-built clickable list
- [ ] DevTools console open on projector
- [ ] Projector
- [ ] Class roster
