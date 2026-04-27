## Session 9: The DOM — querySelector and events

*Phase 7 — Web · Session 9 of 17*

### What we're learning today

You know JavaScript syntax. Today you learn how JS
**reaches into the page** and changes things. Click a
button → text updates. Type in a field → preview
changes. Toggle a class → theme switches. This is the
**DOM** (Document Object Model) — the bridge between
your JS and the HTML on the page. By the end of class
you'll have built an interactive counter and a
live-updating greeting.

### You'll need to remember from last time

- **JavaScript syntax** — variables, functions,
  conditionals (Session 8).
- **`console.log`** for debugging.
- **HTML structure** — IDs and classes (Sessions 2-3).
- **`<input>` and `<button>`** (Session 7).

---

### Part A: Reaching into the page

#### What's the DOM?

When the browser loads your HTML, it builds a **tree of
objects** — one for every tag, one for every text node.
This tree is called the **DOM** (Document Object
Model).

JavaScript can:

- **Find** elements in the tree.
- **Read** their content (`innerText`, `value`).
- **Change** their content.
- **Listen** for events (clicks, key presses).
- **Add or remove** classes (which triggers CSS).
- **Create or destroy** elements.

The starting object is **`document`** — JS's handle to
the page.

#### Find an element

The most common way:

```javascript
const heading = document.querySelector("h1");
```

`document.querySelector(...)` takes a **CSS selector**
(any selector you'd use in CSS) and returns the
**first matching element**. So:

```javascript
document.querySelector("h1")           // first <h1>
document.querySelector(".card")         // first .card
document.querySelector("#main-title")   // the #main-title
document.querySelector(".card h2")      // first h2 inside a card
```

Same selectors as CSS. **One API for both.**

For all matches, use `querySelectorAll`:

```javascript
const cards = document.querySelectorAll(".card");
```

Returns a list-like thing (a `NodeList`) of all
matching elements.

#### Try it

Open Thonny. Save a new file as `dom-test.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>DOM test</title>
</head>
<body>
    <h1 id="title">Hello!</h1>
    <p>This is a paragraph.</p>
    <button id="changeBtn">Change the title</button>

    <script>
        const heading = document.querySelector("#title");
        console.log(heading);
        console.log(heading.textContent);
    </script>
</body>
</html>
```

Save. Open in browser. **Open DevTools console.**

You see two outputs:

1. `<h1 id="title">Hello!</h1>` — the actual HTML
   element.
2. `Hello!` — its text content.

`textContent` is the text inside an element. You can
**also write to it**:

```javascript
heading.textContent = "I changed!";
```

Type that in the console. **The page updates
immediately.** The `<h1>` now says "I changed!"

You just changed the page from JavaScript. **That's the
power.**

#### Listen for events

Right now the button does nothing. Add a click handler:

```javascript
const button = document.querySelector("#changeBtn");

button.addEventListener("click", () => {
    heading.textContent = "Button was clicked!";
});
```

Save. Reload. Click the button. **The heading
changes.**

What's happening:

- **`addEventListener("click", fn)`** attaches a
  function to the button.
- When the button is clicked, the function runs.
- The function changes `heading.textContent`.

The function is an **arrow function** — Session 8. The
`() => { ... }` is shorthand for "a function that
takes no arguments and runs this code."

#### Common events

```javascript
element.addEventListener("click", handler);      // mouse click
element.addEventListener("dblclick", handler);    // double-click
element.addEventListener("input", handler);       // user typed in input
element.addEventListener("submit", handler);      // form submit
element.addEventListener("change", handler);      // input value changed
element.addEventListener("mouseenter", handler);  // mouse entered
element.addEventListener("mouseleave", handler);  // mouse left
element.addEventListener("keydown", handler);     // key pressed
```

Most user interactions have an event you can listen
for. **`click`** and **`input`** are the two you'll
use most.

#### Counter — a complete tiny app

Open Thonny. Save a new file as `counter.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Counter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 400px;
            margin: 80px auto;
            text-align: center;
        }
        #count {
            font-size: 80px;
            margin: 20px 0;
        }
        button {
            font-size: 24px;
            padding: 10px 20px;
            margin: 0 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Counter</h1>
    <div id="count">0</div>
    <button id="minus">-1</button>
    <button id="reset">Reset</button>
    <button id="plus">+1</button>

    <script>
        let count = 0;
        const display = document.querySelector("#count");
        const plusBtn = document.querySelector("#plus");
        const minusBtn = document.querySelector("#minus");
        const resetBtn = document.querySelector("#reset");

        plusBtn.addEventListener("click", () => {
            count = count + 1;
            display.textContent = count;
        });

        minusBtn.addEventListener("click", () => {
            count = count - 1;
            display.textContent = count;
        });

        resetBtn.addEventListener("click", () => {
            count = 0;
            display.textContent = count;
        });
    </script>
</body>
</html>
```

Save. Open in browser. Click the buttons. **The
counter goes up and down.** Reset returns to 0.

This is your **first interactive web app.**

The pattern:

1. **State** — a variable (`count`).
2. **DOM references** — find elements (`display`,
   buttons).
3. **Event listeners** — wire up buttons.
4. **In each handler:** update state, sync DOM.

This is the **fundamental shape of every interactive
JS app.** Phase 5 customtkinter had the same shape
with different syntax. The DOM is the JS version of
"reach into the UI and change it."

**Checkpoint:** *You have a working counter with three
buttons that change a displayed number.* **This is the
natural stop point if class is cut short.**

---

### Part B: Reading inputs and changing classes

#### Reading from an input

For text inputs, the value lives in `.value` (not
`.textContent`):

```html
<input type="text" id="nameInput" placeholder="Your name">
<button id="greetBtn">Greet me</button>
<p id="greeting"></p>

<script>
    const input = document.querySelector("#nameInput");
    const button = document.querySelector("#greetBtn");
    const greeting = document.querySelector("#greeting");

    button.addEventListener("click", () => {
        const name = input.value;
        greeting.textContent = `Hello, ${name}!`;
    });
</script>
```

Type a name. Click the button. **Your name shows up.**

Note: `.textContent` for paragraphs and headings;
`.value` for input fields and textareas.

#### Live updates with the `input` event

```javascript
input.addEventListener("input", () => {
    greeting.textContent = `Hello, ${input.value}!`;
});
```

Now the greeting updates **as you type** — no button
needed. Try it.

The `input` event fires on every keystroke. Modern
reactive apps work this way.

#### Toggling a class

The most common DOM trick — add or remove a CSS class
to change appearance:

```html
<div id="box" class="box">A box</div>
<button id="toggleBtn">Toggle dark mode</button>

<style>
    .box {
        padding: 30px;
        background-color: white;
        color: black;
        transition: all 0.3s;
    }
    .box.dark {
        background-color: black;
        color: white;
    }
</style>

<script>
    const box = document.querySelector("#box");
    const toggleBtn = document.querySelector("#toggleBtn");

    toggleBtn.addEventListener("click", () => {
        box.classList.toggle("dark");
    });
</script>
```

Click the button. Box turns dark. Click again. Light.

`classList` has these methods:

- **`add("classname")`** — add the class.
- **`remove("classname")`** — remove it.
- **`toggle("classname")`** — flip (add if absent,
  remove if present).
- **`contains("classname")`** — true/false.

> **Strong recommendation:** Toggle CSS classes from
> JS, don't change `.style.X` directly. Why? CSS keeps
> the visual decisions; JS keeps the *what changed*
> decisions. Cleaner separation.

#### Build it — a live-updating greeting

Open Thonny. Save as `greeting.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Greeting</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 80px auto;
            text-align: center;
            transition: background-color 0.3s, color 0.3s;
        }
        body.dark {
            background-color: #1a1a2e;
            color: white;
        }
        input, button {
            font-size: 18px;
            padding: 10px;
            margin: 5px;
        }
        #greeting {
            font-size: 36px;
            margin: 30px 0;
        }
    </style>
</head>
<body>
    <h1>Greeting</h1>
    <input type="text" id="nameInput" placeholder="Your name">
    <button id="darkBtn">Toggle dark mode</button>
    <p id="greeting">Hello, ?</p>

    <script>
        const input = document.querySelector("#nameInput");
        const greeting = document.querySelector("#greeting");
        const darkBtn = document.querySelector("#darkBtn");

        input.addEventListener("input", () => {
            const name = input.value || "?";
            greeting.textContent = `Hello, ${name}!`;
        });

        darkBtn.addEventListener("click", () => {
            document.body.classList.toggle("dark");
        });
    </script>
</body>
</html>
```

Save. Reload. **Type a name** — greeting updates
live. **Click "Toggle dark mode"** — page goes dark.
Click again — back to light.

The `input.value || "?"` trick: if input is empty,
use "?" instead. Real little touch.

#### Stretch — multiple list items

Show a list with class toggles:

```html
<ul id="todo-list">
    <li>Pizza</li>
    <li>Soccer</li>
    <li>Reading</li>
</ul>

<style>
    li { cursor: pointer; transition: color 0.2s; }
    li.done { color: gray; text-decoration: line-through; }
</style>

<script>
    const items = document.querySelectorAll("#todo-list li");

    items.forEach(item => {
        item.addEventListener("click", () => {
            item.classList.toggle("done");
        });
    });
</script>
```

`querySelectorAll` returns multiple. `.forEach` runs a
function on each. Click any item — it gets struck
through. Click again — restored.

This is the *seed* of the todo list we build properly
next session.

#### Stretch — preventDefault on form submit

```javascript
const form = document.querySelector("form");
form.addEventListener("submit", (event) => {
    event.preventDefault();    // stop the default form submit
    // now do whatever you want with the form data
    const name = document.querySelector("#name").value;
    console.log("Submitted with name:", name);
});
```

`event.preventDefault()` stops the form from doing its
default behavior (submitting to a URL). Now your JS
handles it. **Crucial for forms in JS.**

#### Extension — element creation

You can build elements from JS:

```javascript
const newItem = document.createElement("li");
newItem.textContent = "New thing!";
document.querySelector("#todo-list").appendChild(newItem);
```

Three lines:

1. `createElement("li")` — make a new `<li>` element
   (not yet in the page).
2. Set its content.
3. `appendChild` adds it to the parent.

This is how todo apps add new items dynamically. We'll
use this constantly next session.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your counter or greeting.
- Did the live-updating-as-you-type feel different?
  More "modern"?
- For the kids who tried the toggleable list — how
  satisfying was the strikethrough-on-click?
- Is the DOM what you expected?

Today you learned:

- **The DOM** — JavaScript's interface to the page.
- **`document.querySelector(...)`** — find one
  element.
- **`document.querySelectorAll(...)`** — find all
  matches.
- **`.textContent`** — read or change text.
- **`.value`** — read or change input value.
- **`.classList.add/remove/toggle`** — change CSS
  classes (preferred over `.style.X`).
- **`addEventListener("event", handler)`** — react to
  user actions.
- **Common events:** click, input, submit, change.
- **`event.preventDefault()`** — stop default
  behaviors.
- **`document.createElement(...)`** + `appendChild`
  for new elements.

The pattern: **state + DOM references + event
listeners + sync.** Same as customtkinter, different
language.

Next week: a full **interactive todo list** — combining
everything. Add items, delete, mark complete. Real app.

### If you missed this session

Open Thonny.

1. Build the basic `dom-test.html` from Part A.
   Get the title to change when you click the button.

2. Build the counter from Part A. Plus, minus, reset.

3. Build the greeting from Part B with live updates
   and dark mode.

4. (Stretch) Build the toggleable list.

About 45-60 minutes. By the end you should have at
least two interactive pages.

### Stretch and extension ideas

- **Inline editing** — click text to edit it.
- **Multiple themes** — buttons for dark, sepia, blue,
  etc.
- **Keyboard shortcuts** — listen for keys. Press
  Space to count up; press R to reset.
- **A small calculator** — two number inputs, four
  operation buttons, a result display.
- **A color picker** that updates the page's
  background:
  ```javascript
  colorInput.addEventListener("input", () => {
      document.body.style.backgroundColor = colorInput.value;
  });
  ```
  (One time when `.style.X` is fine — the color is
  truly dynamic.)
- **A character counter for textarea** — show
  "500/1000 characters" as the user types.

### What's next

Next week: **build a real todo list** — add items,
mark them done, delete them. Combine everything from
Sessions 1-9. Your first JS-powered app.
