## Session 11: localStorage — make state survive

*Phase 7 — Web · Session 11 of 17*

### What we're learning today

Last session your todo app worked great — until you
reloaded the page. Then everything vanished. Today
we **fix that** with **localStorage** — a tiny
key-value store the browser provides for every
website. Save your todos to localStorage; load them
on page open. Close the browser, come back tomorrow,
todos are still there. **Real persistence.**

### You'll need to remember from last time

- **Your todo app** from Session 10.
- **`JSON.stringify` and `JSON.parse`** (Session 8
  stretch — we'll cover them properly today).
- **DOM manipulation** — `createElement`,
  `appendChild`, `remove`.
- **Phase 5 Session 6 stretch** — JSON file persistence
  in customtkinter. Same idea, different storage.

---

### Part A: localStorage basics

#### What's localStorage?

`localStorage` is a **key-value store** built into
every browser. It stores **strings** (and only
strings) under string keys, and the data **persists
forever** (until explicitly cleared, or until the
user clears browser data).

It's:

- **Per-site.** Each website has its own
  localStorage; sites can't read each other's.
- **Per-browser.** Different browsers have separate
  storage. Chrome's localStorage is separate from
  Firefox's.
- **Limited size.** ~5-10 MB per site (tons for
  text; not for big images).
- **Synchronous and instant.** No callbacks, no
  await — just call and use.

#### The API — three methods

```javascript
localStorage.setItem("key", "value");    // save
const value = localStorage.getItem("key");    // load
localStorage.removeItem("key");           // delete
localStorage.clear();                     // delete everything
```

That's it. Four methods. Easy.

#### Try it

Open any HTML file (or the homepage you've been
building) in your browser. Open the **DevTools
console** (F12 → Console).

Type:

```javascript
localStorage.setItem("name", "Alex");
```

Press Enter. **Saved.**

Now:

```javascript
localStorage.getItem("name");    // "Alex"
```

Returns the value. **Reload the page.** Try
`getItem("name")` again. **Still "Alex".** The data
survived the reload.

Close the browser tab. Reopen the page in a fresh
tab. `getItem("name")` still returns "Alex". The
data survives across sessions.

This is **local persistent storage** in the browser.

#### See it in DevTools

In DevTools, switch to the **Application** tab (in
Chrome) or **Storage** tab (in Firefox). Find
**Local Storage** in the left sidebar. Click it.

You see all the keys you've stored, with their
values. **You can edit or delete them directly here.**
Useful for debugging.

#### Strings only

`localStorage` only stores strings. **What if you
want to save a list?**

```javascript
const todos = ["pizza", "soccer", "reading"];
localStorage.setItem("todos", todos);    // saves "pizza,soccer,reading" — actually a string
localStorage.getItem("todos");           // "pizza,soccer,reading"
```

It works, but you got a string back, not an array.

#### JSON to the rescue

The standard way to save complex data is **JSON
serialization**:

```javascript
// Save (object → string)
const todos = ["pizza", "soccer", "reading"];
localStorage.setItem("todos", JSON.stringify(todos));

// Load (string → object)
const loaded = JSON.parse(localStorage.getItem("todos"));
console.log(loaded);    // ["pizza", "soccer", "reading"]
```

`JSON.stringify(value)` turns any object/array into
a JSON string. `JSON.parse(string)` turns it back.

JSON works for any combination of:

- Strings, numbers, booleans, null.
- Arrays.
- Objects (with string keys).

Functions, undefined, and circular references break
JSON. Stick to plain data.

#### Build a settings example

Open Thonny. Save a new file as `settings.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Settings demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 60px auto;
            padding: 20px;
            transition: all 0.3s;
        }
        body.dark {
            background-color: #1a1a2e;
            color: white;
        }
        label {
            display: block;
            margin: 12px 0;
        }
    </style>
</head>
<body>
    <h1>Settings</h1>
    
    <label>
        <input type="checkbox" id="darkToggle">
        Dark mode
    </label>
    
    <label>
        Your name:
        <input type="text" id="nameInput">
    </label>

    <script src="settings.js"></script>
</body>
</html>
```

`settings.js`:

```javascript
const darkToggle = document.querySelector("#darkToggle");
const nameInput = document.querySelector("#nameInput");

// Load saved settings
const isDark = localStorage.getItem("dark") === "true";
const savedName = localStorage.getItem("name") || "";

// Apply them
darkToggle.checked = isDark;
nameInput.value = savedName;
if (isDark) document.body.classList.add("dark");

// Save on change
darkToggle.addEventListener("change", () => {
    localStorage.setItem("dark", darkToggle.checked);
    document.body.classList.toggle("dark", darkToggle.checked);
});

nameInput.addEventListener("input", () => {
    localStorage.setItem("name", nameInput.value);
});
```

Save. Reload. Set dark mode. Type your name. **Reload
the page** (or close and reopen the tab). Dark mode
is still on. Name is still there. **Settings
persist.**

A few details:

- **`localStorage.getItem("dark") === "true"`** —
  localStorage returns strings, so we compare to
  the string `"true"`.
- **`localStorage.getItem("name") || ""`** — if no
  saved name (returns `null`), default to empty
  string.
- **`darkToggle.checked`** — checkbox state (true/
  false).
- **`classList.toggle("dark", darkToggle.checked)`**
  — second arg forces add if true, remove if false.

**Checkpoint:** *You have a page with at least one
setting that persists across reloads.* **This is the
natural stop point if class is cut short.**

---

### Part B: Persist the todo list

Open your todo app from Session 10. Add persistence.

#### The pattern

After every change to the list, save. On page load,
restore.

Add to the **top of `app.js`:**

```javascript
function saveTodos() {
    const items = list.querySelectorAll("li");
    const todos = [];
    items.forEach(item => {
        const text = item.querySelector("span").textContent;
        const done = item.classList.contains("done");
        todos.push({ text, done });
    });
    localStorage.setItem("todos", JSON.stringify(todos));
}

function loadTodos() {
    const data = localStorage.getItem("todos");
    if (!data) return;
    const todos = JSON.parse(data);
    todos.forEach(({ text, done }) => {
        addItem(text, done);
    });
}
```

**Refactor your add-item code into a function** so
both the form submit and load can use it:

```javascript
function addItem(text, done = false) {
    const item = document.createElement("li");
    if (done) item.classList.add("done");
    
    const span = document.createElement("span");
    span.textContent = text;
    span.style.cursor = "pointer";
    span.addEventListener("click", () => {
        item.classList.toggle("done");
        saveTodos();
    });
    
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "×";
    deleteBtn.className = "delete-btn";
    deleteBtn.addEventListener("click", () => {
        item.remove();
        saveTodos();
    });
    
    item.appendChild(span);
    item.appendChild(deleteBtn);
    list.appendChild(item);
}
```

Update the form handler:

```javascript
form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value.trim();
    if (text === "") return;
    addItem(text);
    saveTodos();
    input.value = "";
});
```

Call `loadTodos()` once on page load:

```javascript
loadTodos();
```

Save. Reload. Add some todos. Toggle done on a few.
**Close the browser tab.** Reopen the page. **Your
todos are still there**, in their done/not-done
states.

**This is real persistence.** The app remembers
between sessions. You could close your laptop, come
back tomorrow, and see your todos.

#### Stretch — a "clear all" with persistence

```javascript
clearBtn.addEventListener("click", () => {
    if (confirm("Clear all todos?")) {
        list.innerHTML = "";
        saveTodos();    // saves an empty list
    }
});
```

`saveTodos()` after the clear writes the (now
empty) list to localStorage. Otherwise reload would
restore them.

#### Stretch — show storage usage

```javascript
const data = localStorage.getItem("todos") || "";
console.log(`Storage: ${data.length} bytes`);
```

Tiny inspection of how much you're storing.

#### Extension — settings + todos in one app

Combine the settings (dark mode toggle) with the
todo persistence. Two separate keys in localStorage
(`"darkMode"` and `"todos"`).

#### Extension — multiple lists

Save an object that holds *multiple lists*:

```javascript
const allLists = {
    "Today": ["pizza", "soccer"],
    "Tomorrow": ["doctor", "homework"],
    "Sometime": ["learn french", "build robot"]
};
localStorage.setItem("lists", JSON.stringify(allLists));
```

Lets your app handle multiple categories. UI gets
more complex (need to switch between lists), but the
storage pattern is the same.

#### Extension — export/import

Add buttons to export the data (download as a JSON
file) and import (upload a JSON file). Useful for
moving data between machines.

```javascript
function exportTodos() {
    const data = localStorage.getItem("todos") || "[]";
    const blob = new Blob([data], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "todos.json";
    a.click();
}
```

Advanced. Real-app feature.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your persistent todo. Add
  some, reload, see them survive.
- For the kids who tried clearing — does it now
  *stay* clear after reload?
- Did seeing your data in DevTools' Application
  panel feel cool? Like seeing inside?
- Anyone notice that this only works on *your*
  browser? Different browser = different storage.

Today you learned:

- **`localStorage`** — browser-built-in key-value
  store.
- **Four methods:** `setItem`, `getItem`,
  `removeItem`, `clear`.
- **Strings only** — use `JSON.stringify` /
  `JSON.parse` for objects and arrays.
- **`getItem` returns `null`** if no key — use `||`
  fallback.
- **DevTools Application/Storage tab** to inspect.
- **Pattern:** save on every change, load on page
  start.

This is **the simplest browser persistence** — no
backend, no database, just your code and the
browser. Real apps use this for:

- Settings (dark mode, language preference).
- Drafts (auto-save what the user is typing).
- "Recent searches" / "recently viewed."
- Authentication tokens.
- Game saves (the kid's sidequest).

For data that needs to be *shared across devices*,
you'd need a real backend (server + database). That's
Phase 8 (Flask).

Next week: **Canvas** — drawing graphics in the
browser. The Pygame patterns transfer directly.

### If you missed this session

Open Thonny. You need your Session 10 todo app.

1. Open `app.js`. Add the `saveTodos()` and
   `loadTodos()` functions from the handout.

2. Refactor add logic into an `addItem(text, done)`
   function that both form-submit and load can use.

3. Call `saveTodos()` after every change. Call
   `loadTodos()` once at startup.

4. Add some todos, reload, see them persist.

5. (Stretch) Add the settings example or any
   extension.

About 45-60 minutes. By the end your todo app should
persist across reloads.

### Stretch and extension ideas

- **Settings + todos** in one app.
- **Multiple lists** with names.
- **Export / import** as JSON files.
- **Storage size display** — tiny info bar showing
  current usage.
- **"Last edited" timestamp** — save when each todo
  was last changed.
- **Auto-save drafts** — save the input field as you
  type, restore on reload (in case you closed
  by accident).
- **Different storage:** `sessionStorage` (same API,
  but only lives for the current tab — clears on
  close).

### What's next

Next week: **Canvas** — JavaScript's drawing
surface. Lines, shapes, images, animation. The
Pygame mental model directly transfers — same frame
loop, same drawing primitives, in the browser.
Followed by Session 13's canvas mini-game.
