## Session 10: Build an interactive todo list

*Phase 7 — Web · Session 10 of 17*

### What we're learning today

You built a todo list in **Phase 5 customtkinter.**
Today you build the **same app, in the browser** —
HTML for structure, CSS for style, JS for behavior.
By the end, you'll have a working todo app you can
open in any browser. Next session we make it
**remember todos between page reloads.**

This is the integration project for the JavaScript
movement.

### You'll need to remember from last time

- **`document.querySelector`** and `addEventListener`
  (Session 9).
- **`.textContent`, `.value`, `.classList`** (Session 9).
- **`document.createElement` + `appendChild`** (Session
  9 stretch).
- **`event.preventDefault()`** for form submissions.
- **JavaScript syntax** (Session 8).
- **Phase 5 todo app** — the customtkinter version is
  the same app.

---

### Part A: Build the todo list

Open Thonny. Create a folder for this project. Create
two files: `index.html` and `app.js`.

We'll build in steps. **Run after every step.**

#### Step 1 — HTML structure

`index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Todos</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main>
        <h1>My Todos</h1>
        
        <form id="todoForm">
            <input type="text" id="todoInput" placeholder="What needs doing?" required>
            <button type="submit">Add</button>
        </form>
        
        <ul id="todoList"></ul>
    </main>

    <script src="app.js"></script>
</body>
</html>
```

Save. Open in browser. **Plain page** with a heading,
a form, and an empty list.

#### Step 2 — Add the first todo

In `app.js`:

```javascript
const form = document.querySelector("#todoForm");
const input = document.querySelector("#todoInput");
const list = document.querySelector("#todoList");

form.addEventListener("submit", (event) => {
    event.preventDefault();    // stop the page reloading
    
    const text = input.value.trim();
    if (text === "") return;
    
    const item = document.createElement("li");
    item.textContent = text;
    list.appendChild(item);
    
    input.value = "";    // clear the input
});
```

Save. Reload. Type a todo. Click Add. **The todo
appears in the list.** Add another. Add several.
**It works.**

What's happening:

- **`event.preventDefault()`** — stop the form from
  reloading the page (its default behavior).
- **`input.value.trim()`** — get the typed text,
  remove leading/trailing whitespace.
- **`if (text === "") return;`** — ignore empty
  submissions.
- **`document.createElement("li")`** — make a new
  `<li>` element.
- **`item.textContent = text;`** — set its text.
- **`list.appendChild(item);`** — add it to the
  `<ul>`.
- **`input.value = "";`** — clear the input for the
  next entry.

#### Step 3 — Style it

Create `styles.css`:

```css
*, *::before, *::after {
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, sans-serif;
    background-color: #f0f0f0;
    color: #333;
    margin: 0;
    padding: 40px 20px;
}

main {
    max-width: 500px;
    margin: 0 auto;
    background-color: white;
    padding: 32px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

h1 {
    margin-top: 0;
    color: #2c3e50;
}

#todoForm {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
}

#todoInput {
    flex: 1;
    padding: 10px 12px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: inherit;
}

#todoInput:focus {
    outline: none;
    border-color: #3498db;
}

#todoForm button {
    padding: 10px 20px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

#todoForm button:hover {
    background-color: #2980b9;
}

#todoList {
    list-style: none;
    padding: 0;
    margin: 0;
}

#todoList li {
    padding: 12px;
    background-color: #fafafa;
    border: 1px solid #eee;
    border-radius: 4px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

Save. Reload. **The todo app is now styled** — a
white card with the form on top, todos below as
neat cards.

`list-style: none` removes the default bullet points
on `<ul>`s.

#### Step 4 — Delete buttons

When you create each `<li>`, also create an "×"
button inside it:

In `app.js`, replace the `addEventListener("submit",
...)` handler with this:

```javascript
form.addEventListener("submit", (event) => {
    event.preventDefault();
    
    const text = input.value.trim();
    if (text === "") return;
    
    const item = document.createElement("li");
    
    const span = document.createElement("span");
    span.textContent = text;
    
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "×";
    deleteBtn.className = "delete-btn";
    deleteBtn.addEventListener("click", () => {
        item.remove();
    });
    
    item.appendChild(span);
    item.appendChild(deleteBtn);
    list.appendChild(item);
    
    input.value = "";
});
```

Add to `styles.css`:

```css
.delete-btn {
    background: none;
    border: none;
    color: #999;
    font-size: 24px;
    cursor: pointer;
    line-height: 1;
    padding: 0 4px;
}

.delete-btn:hover {
    color: #e74c3c;
}
```

Save. Reload. **Each todo now has an × button.**
Click × to delete that todo. Add more, delete
others. Works.

What's new:

- **A wrapper `<li>`** with two children: a `<span>`
  for the text and a `<button>` for the delete.
- **`item.remove()`** — built-in DOM method to
  remove an element from the page.
- **`deleteBtn.className = "delete-btn"`** — set the
  CSS class.

#### Step 5 — Mark complete

Click the text to toggle "done" state:

In `app.js`, after creating the span:

```javascript
span.addEventListener("click", () => {
    item.classList.toggle("done");
});

span.style.cursor = "pointer";    // hint that it's clickable
```

In `styles.css`, add:

```css
#todoList li.done span {
    color: #999;
    text-decoration: line-through;
}
```

Save. Reload. Click any todo's text. **It gets struck
through.** Click again. Restored.

Now you can add, complete, and delete. **Real todo
app shape.**

**Checkpoint:** *You have a working todo app — add,
complete, delete.* **This is the natural stop point if
class is cut short.**

---

### Part B: Polish

Time to make it nicer.

#### Empty state

When there are no todos, show a friendly message
instead of a blank list. Add to your HTML, just
inside `<main>` after the form:

```html
<p id="emptyMessage">Nothing to do! Add a todo above.</p>
```

Add CSS:

```css
#emptyMessage {
    color: #aaa;
    text-align: center;
    margin: 20px 0;
}
```

Manage the message from JS. After every change to the
list:

```javascript
function updateEmptyMessage() {
    const message = document.querySelector("#emptyMessage");
    if (list.children.length === 0) {
        message.style.display = "block";
    } else {
        message.style.display = "none";
    }
}
```

Call `updateEmptyMessage()` after adding and after
deleting. **Or** wrap the change-and-update in a
single function so you always sync.

#### Counter

How many todos do you have? How many are done?
Add a header above the list:

```html
<p id="counter"></p>
```

```javascript
function updateCounter() {
    const total = list.children.length;
    const done = document.querySelectorAll("#todoList li.done").length;
    document.querySelector("#counter").textContent = `${done}/${total} done`;
}
```

Call `updateCounter()` whenever you add, delete, or
toggle.

```css
#counter {
    text-align: right;
    color: #666;
    margin: 0 0 10px 0;
}
```

Save. Reload. **The counter updates live.**

#### Stretch — clear all

A button to wipe the list:

```html
<button id="clearBtn">Clear all</button>
```

```javascript
const clearBtn = document.querySelector("#clearBtn");
clearBtn.addEventListener("click", () => {
    if (confirm("Are you sure?")) {
        list.innerHTML = "";
        updateCounter();
        updateEmptyMessage();
    }
});
```

`confirm("...")` shows a built-in OK/Cancel dialog.
Returns true if user clicked OK.

`list.innerHTML = ""` removes all children at once.

#### Stretch — Enter to add

Already works! Forms submit on Enter by default.
Type a todo, press Enter — added. Try it.

#### Stretch — show added time

Add a timestamp:

```javascript
const timeSpan = document.createElement("small");
const now = new Date();
timeSpan.textContent = now.toLocaleTimeString();
timeSpan.className = "time";
item.appendChild(timeSpan);
```

```css
.time {
    color: #999;
    font-size: 12px;
    margin-left: 8px;
}
```

Each new todo shows when it was added.

#### Extension — refactor with a class

If your `app.js` is getting long, wrap it in a
TodoApp class (like Phase 5 Session 6's class
refactor):

```javascript
class TodoApp {
    constructor() {
        this.list = document.querySelector("#todoList");
        this.form = document.querySelector("#todoForm");
        this.input = document.querySelector("#todoInput");
        
        this.form.addEventListener("submit", (e) => this.add(e));
    }
    
    add(event) {
        event.preventDefault();
        const text = this.input.value.trim();
        if (text === "") return;
        this.createItem(text);
        this.input.value = "";
    }
    
    createItem(text) {
        const item = document.createElement("li");
        // ... build item, attach listeners ...
        this.list.appendChild(item);
    }
}

new TodoApp();
```

Same code, organized as a class. Real production
shape.

#### Extension — push to GitHub

Treat this todo as a real project. Commit it. Push
to a GitHub repo. (You did this in Phase 6 Session
7 with Pong — same flow.)

You're building a portfolio.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your todo app. How many todos
  did you add to test?
- For the kids who added the counter — does the
  live update feel modern?
- For the kids who tried `confirm()` — fun built-in
  dialog, right?
- Anyone notice you have to *re-add* todos every
  time you reload? **Next week we fix that.**

Today you built **a real interactive web app.** Not a
toy. The kind of thing you could actually use to track
real tasks (in this single browser tab, until next
session adds storage).

You used:

- **Form submit** with `preventDefault`.
- **Reading input** with `.value`.
- **Creating elements** with `createElement` and
  `appendChild`.
- **Deleting elements** with `.remove()`.
- **Toggling state** with `classList.toggle`.
- **Built-in dialogs** like `confirm()`.
- **The pattern** — state in DOM, JS reads/changes,
  events drive updates.

This is the **production shape of every interactive
web app.** Same patterns power the apps you use every
day — Trello, Slack, Twitter (each is a more
elaborate version).

Next week: **localStorage** — make your todos persist
between page reloads. Real persistence in the
browser.

### If you missed this session

Open Thonny.

1. Create a folder. Inside, `index.html`, `app.js`,
   `styles.css`.

2. Build the HTML shell from Step 1.

3. Build the add-todo logic from Step 2.

4. Style with the CSS from Step 3.

5. Add delete buttons (Step 4) and complete-toggle
   (Step 5).

About 60-90 minutes — this is a substantial session.

### Stretch and extension ideas

- **Counter** — show "X/Y done."
- **Empty state** — friendly message when list is
  empty.
- **Clear all** with `confirm()`.
- **Timestamp** on each todo.
- **Refactor as a class.**
- **Edit a todo** — double-click to make it editable.
  Replace span with input on dblclick; save on Enter
  or blur.
- **Filter** — show all / active / completed.
- **Drag to reorder** — advanced (uses `dragstart`,
  `dragover`, `drop` events).
- **Push to GitHub.**

### What's next

Next week: **localStorage** — your todos *survive*
between page reloads. Close the tab, come back
later, todos are still there. The "wow" moment of
the JavaScript movement.
