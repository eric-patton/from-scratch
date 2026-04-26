## Session 6: Putting it together — a complete app

*Phase 5 — customtkinter · Session 6 of 8*

### What we're learning today

You've met every basic widget: labels, buttons, entries,
checkboxes, radios, dropdowns, frames. You've learned `pack`
and `grid`. Today we put it all together and build a
**complete, real app** — a todo list. Add tasks, see them
in a scrollable list, delete them, and (stretch) save them
to a file so they survive between runs.

By the end you'll have something that looks and feels like
real software — the kind of thing you could actually use.

### You'll need to remember from last time

- **`grid()` and `CTkFrame`** — Session 5.
- **`CTkEntry` and `entry.get()`** — Session 3.
- **`CTkButton` with callbacks** — Session 2.
- **`label.configure(text=...)`** — Session 2.
- **Lists in Python** — Phase 3 Session 8.
- **Reading and writing files** — Phase 3 Session 11.
- **Light classes** — Phase 4 Session 4.

---

### Part A: Build the todo list

Open Thonny. Save a new file as `todos.py`.

We'll build this in steps. Run after each step to make sure
each piece works before moving on.

#### Step 1 — The window and the title

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("My Todos")
app.geometry("400x500")

title = ctk.CTkLabel(app, text="My Todos", font=("Arial", 24, "bold"))
title.pack(pady=10)

app.mainloop()
```

Save. Run. A window with a title. So far, nothing new.

#### Step 2 — The input row

We want an entry on the left and an "Add" button on the
right, sitting in a row across the top. That's a frame with
two widgets in it, packed left and right.

Add this **before** `app.mainloop()`:

```python
input_frame = ctk.CTkFrame(app)
input_frame.pack(fill="x", padx=10, pady=10)

entry = ctk.CTkEntry(input_frame, placeholder_text="What needs doing?")
entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

add_button = ctk.CTkButton(input_frame, text="Add", width=80)
add_button.pack(side="right", padx=5, pady=5)
```

Save. Run. The entry stretches across; the Add button sits
on the right. Click "Add" — nothing happens yet (no
callback). That's next.

#### Step 3 — The list area

Below the input row, we want a scrollable area where the
todos will appear. customtkinter has a built-in widget for
this: `CTkScrollableFrame`. Widgets inside it scroll
automatically once they overflow.

Add this below the input frame setup:

```python
list_frame = ctk.CTkScrollableFrame(app)
list_frame.pack(fill="both", expand=True, padx=10, pady=10)
```

Save. Run. The window now has a scrollable area in the
middle. Empty for now. We'll fill it with todo rows.

#### Step 4 — Storing and showing todos

Now the meat. We need:

- A list to **store** the todos.
- A function to **add** a todo (called when Add is clicked).
- A function to **redraw** the list area whenever it changes.

Add this near the top of your file (right after the
`import`):

```python
todos = []

def add_todo():
    text = entry.get().strip()
    if not text:
        return
    todos.append(text)
    entry.delete(0, "end")
    refresh_list()

def refresh_list():
    # First, clear out the existing rows
    for widget in list_frame.winfo_children():
        widget.destroy()
    
    # Then re-create one row per todo
    for todo in todos:
        row = ctk.CTkFrame(list_frame)
        row.pack(fill="x", pady=2)
        
        label = ctk.CTkLabel(row, text=todo, anchor="w")
        label.pack(side="left", fill="x", expand=True, padx=5)
```

Then connect the Add button to `add_todo`. Change the
`add_button` line to:

```python
add_button = ctk.CTkButton(input_frame, text="Add", command=add_todo, width=80)
```

Save. Run. Type something. Click Add. Your todo appears
in the list. Type another. Click Add. Both appear.

There's a lot going on here — let's break it down:

- **`text = entry.get().strip()`** reads what the user typed
  and removes leading/trailing spaces.
- **`if not text: return`** ignores empty entries (clicking
  Add with nothing typed does nothing).
- **`todos.append(text)`** adds to the list.
- **`entry.delete(0, "end")`** clears the entry box.
- **`refresh_list()`** redraws the list area from scratch.

The "redraw from scratch" pattern is useful: instead of
trying to add or remove just the right widget, we wipe
everything and rebuild. Simpler to think about, and
performance is fine for small lists.

**`winfo_children()`** gives us all widgets inside a parent
— here, all the rows we previously created in `list_frame`.
We loop through and destroy each one before drawing the new
list.

#### Step 5 — Delete buttons

Each row should have a delete button (an "×") on the right.
Click it, that todo is gone.

This is trickier than it looks because each row needs its
*own* delete callback that knows *which* todo to delete.
We'll use a trick: a `lambda` that captures the index.

Add a delete function:

```python
def delete_todo(index):
    todos.pop(index)
    refresh_list()
```

Then update `refresh_list` to also create a delete button on
each row. Replace the inner `for todo in todos:` loop with:

```python
for i, todo in enumerate(todos):
    row = ctk.CTkFrame(list_frame)
    row.pack(fill="x", pady=2)
    
    label = ctk.CTkLabel(row, text=todo, anchor="w")
    label.pack(side="left", fill="x", expand=True, padx=5)
    
    delete_button = ctk.CTkButton(
        row,
        text="×",
        width=30,
        command=lambda idx=i: delete_todo(idx)
    )
    delete_button.pack(side="right", padx=5)
```

Save. Run. Add a few todos. Click the "×" next to one. It
disappears. Add more. Delete others. The list updates each
time.

What's new:

- **`enumerate(todos)`** gives `(index, item)` pairs as you
  loop. We need both — the index for deletion, the item for
  the label.
- **`lambda idx=i: delete_todo(idx)`** is the tricky part.
  We capture the current value of `i` as `idx`, then call
  `delete_todo(idx)` when the button is clicked. Without
  the `idx=i` part, all buttons would end up calling
  `delete_todo` with the *last* value of `i`. (This is a
  classic Python gotcha. Don't dwell on it — just remember
  the pattern.)

**Checkpoint:** *You have a todo app — add, view, delete.*
**This is the natural stop point if class is cut short.**

---

### Part B: Save to a file (and a class refactor)

The app works great — until you close it. Then everything
disappears. Real apps **persist** state between runs. Let's
fix that.

#### Save and load to JSON

We'll use the `json` module from Phase 4 Session 3. JSON is
the standard format for saving structured data like lists.

Add to the top of your file:

```python
import json
import os

SAVE_FILE = "todos.json"
```

Add two functions:

```python
def save():
    with open(SAVE_FILE, "w") as f:
        json.dump(todos, f)

def load():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []
```

Now call them from the right places. At the top, change
`todos = []` to:

```python
todos = load()
```

In `add_todo` and `delete_todo`, add `save()` after the
list change:

```python
def add_todo():
    text = entry.get().strip()
    if not text:
        return
    todos.append(text)
    entry.delete(0, "end")
    save()
    refresh_list()

def delete_todo(index):
    todos.pop(index)
    save()
    refresh_list()
```

And finally, **call `refresh_list()` once before
`app.mainloop()`** so any todos from a previous run show
up immediately:

```python
refresh_list()
app.mainloop()
```

Save. Run. Add some todos. Close the app. Open a file
explorer — you should see `todos.json` next to your script.
Run the app again. Your todos are back!

This is what makes an app feel **real**. State that survives
the program closing.

#### Stretch — class refactor

Phase 4 Session 4 introduced classes. Phase 5 Session 5
showed a class refactor. This is the same pattern, applied
to your todo app.

A new file, `todos_class.py`:

```python
import customtkinter as ctk
import json
import os

SAVE_FILE = "todos.json"


class TodoApp:
    def __init__(self):
        self.todos = self._load()
        
        self.app = ctk.CTk()
        self.app.title("My Todos")
        self.app.geometry("400x500")
        
        self._build_ui()
        self._refresh_list()
    
    def _build_ui(self):
        title = ctk.CTkLabel(self.app, text="My Todos", font=("Arial", 24, "bold"))
        title.pack(pady=10)
        
        input_frame = ctk.CTkFrame(self.app)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        self.entry = ctk.CTkEntry(input_frame, placeholder_text="What needs doing?")
        self.entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        self.entry.bind("<Return>", lambda e: self.add_todo())
        
        add_button = ctk.CTkButton(input_frame, text="Add", command=self.add_todo, width=80)
        add_button.pack(side="right", padx=5, pady=5)
        
        self.list_frame = ctk.CTkScrollableFrame(self.app)
        self.list_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    def add_todo(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.todos.append(text)
        self.entry.delete(0, "end")
        self._save()
        self._refresh_list()
    
    def delete_todo(self, index):
        self.todos.pop(index)
        self._save()
        self._refresh_list()
    
    def _refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        
        for i, todo in enumerate(self.todos):
            row = ctk.CTkFrame(self.list_frame)
            row.pack(fill="x", pady=2)
            
            label = ctk.CTkLabel(row, text=todo, anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=5)
            
            delete_button = ctk.CTkButton(
                row, text="×", width=30,
                command=lambda idx=i: self.delete_todo(idx)
            )
            delete_button.pack(side="right", padx=5)
    
    def _save(self):
        with open(SAVE_FILE, "w") as f:
            json.dump(self.todos, f)
    
    def _load(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                return json.load(f)
        return []
    
    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    TodoApp().run()
```

Save. Run. Same app — same behavior. But the code is
**organized** differently:

- All state (`self.todos`, `self.entry`, `self.list_frame`)
  lives on the instance. No `global`. No magic top-level
  variables.
- All behavior is methods. Related code sits next to
  related code.
- Underscore prefix (`_build_ui`, `_save`, `_load`,
  `_refresh_list`) signals "internal helper, don't call
  from outside the class." A convention, not enforced.
- The `if __name__ == "__main__"` block creates the app and
  runs it. If you imported this file from another module,
  the app would *not* automatically start.

Also new: **`self.entry.bind("<Return>", lambda e: self.add_todo())`**
— pressing Enter in the entry box adds the todo without
clicking the button. Real apps do this. Try it.

This structure is what real production GUI code looks like.
You're writing real code now.

#### Extension — mark complete

Add a checkbox to each row. When checked, the todo is
"done" — show it greyed out or with different text.

Hint: store todos as `{"text": "...", "done": False}`
dictionaries instead of plain strings. Then in
`_refresh_list`, render the label differently when
`todo["done"]` is True (try `text_color="gray"`).

---

### Wrap-up

Before we leave, share with the room:

- For the kids who finished Part A — show your todo list.
  How many todos did you add to test it?
- For the kids who got persistence working — close the app
  and reopen it. Magical, right?
- For the kids who refactored to a class — does the code
  feel more organized?

Today you built a **real, useful app.** Not a toy. The kind
of thing you could actually run on your own machine and
use to track real tasks. That's the goal of Phase 5 — and
you're there.

You used:

- **Layouts** — frame inside a frame, side-packing.
- **Widgets** — labels, entries, buttons.
- **State** — a list that the UI reflects.
- **Callbacks** — functions that run on user action.
- **The redraw pattern** — wipe and rebuild on every
  change.
- **Persistence** — save to JSON, load on startup.
- **Classes (stretch)** — production-style organization.

Next two weeks are **your** project — your design, your
code. You're ready.

### If you missed this session

Open Thonny. Then:

1. Build the todo list step by step from Part A. Don't
   skip steps — each one builds on the last.

2. Test with a few todos. Add some, delete some.

3. (Stretch) Add the JSON save/load from Part B. Verify
   that closing and reopening keeps your list.

4. (Stretch) Read through the class refactor. Try running
   it. Notice how the code is organized.

About 60-90 minutes total — this is a long, substantial
session.

### Stretch and extension ideas

- **Mark complete** (extension above) — checkbox per row,
  greyed-out when done.
- **Edit a todo** — click on the label to make it editable.
  Use a `CTkEntry` that swaps in for the label.
- **Sort or filter** — show only undone todos; sort
  alphabetically; sort by date added.
- **Multiple lists** — a "shopping" list and a "homework"
  list, switchable via tabs (`CTkTabview`).
- **Due dates** — store a date with each todo, color old
  ones red.
- **Categories or tags** — group todos by category.
- **A header bar** with "Clear completed" or "Clear all"
  buttons.
- **Better styling** — different colors, better fonts,
  icons in the buttons.

Each of these is a small project. Pick one or two for
fun. Or save them as ideas for your milestone project.

### What's next

Next week is **milestone planning + work day 1.** You'll
design *your* desktop app — your idea, your design. You'll
spend the rest of the session building the simplest version.
Week after that, you'll finish, polish, and **demo** to the
class.

Bring an idea or two next week. (Or come empty-handed —
we have a seed list ready.)
