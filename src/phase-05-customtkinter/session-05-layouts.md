## Session 5: Layouts and frames

*Phase 5 — customtkinter · Session 5 of 8*

### What we're learning today

Your forms are getting *long.* Every `pack()` adds another
widget below the last — fine for a few widgets, awkward for
a real app. Today we learn **`grid()`** for arranging
widgets in rows and columns, and **`CTkFrame`** for grouping
related widgets together. By the end, you'll have a
multi-section app that *looks* like a real app, not just
a stack of widgets.

### You'll need to remember from last time

- **Widgets** — labels, buttons, entries, checkboxes,
  radios, dropdowns.
- **`pack(pady=10)`** — the layout method we've been using.
- **f-strings** for combining text.

---

### Part A: `grid()` — rows and columns

Open Thonny. Save a new file as `grid_demo.py`.

#### The motivation

`pack()` is great for one-widget-per-row. But what if you
want **two columns** — like a label *next to* an entry?

Today's first try:

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("Grid demo")
app.geometry("400x250")

# label and entry on the same "row"
name_label = ctk.CTkLabel(app, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)

name_entry = ctk.CTkEntry(app)
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_label = ctk.CTkLabel(app, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=10)

age_entry = ctk.CTkEntry(app)
age_entry.grid(row=1, column=1, padx=10, pady=10)

button = ctk.CTkButton(app, text="Submit")
button.grid(row=2, column=0, columnspan=2, pady=15)

app.mainloop()
```

Save. Run.

Two rows of label-and-entry pairs, perfectly aligned in two
columns. Then a button below that spans both columns.

#### What's new

- `widget.grid(row=R, column=C, ...)` — places the widget at
  row R, column C. Rows count from 0 (top); columns from 0
  (left).
- `padx=10, pady=10` — padding around each widget (same as
  pack).
- `columnspan=2` — makes the widget span 2 columns.
  (`rowspan=2` does the equivalent for rows.)

`grid()` and `pack()` **don't mix** in the same parent
container. Pick one per container and stick with it.

> **Important rule:** in any window or frame, use *either*
> `pack()` *or* `grid()` — not both. Mixing them breaks the
> layout in confusing ways. (You can use different ones in
> different *frames*; we'll see frames next.)

#### A bigger grid

Try a 3-column layout:

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("3-column grid")
app.geometry("500x300")

# header row spans all 3 columns
header = ctk.CTkLabel(app, text="My App", font=("Arial", 24, "bold"))
header.grid(row=0, column=0, columnspan=3, pady=10)

# row of labels
ctk.CTkLabel(app, text="Name").grid(row=1, column=0, padx=10)
ctk.CTkLabel(app, text="Age").grid(row=1, column=1, padx=10)
ctk.CTkLabel(app, text="Color").grid(row=1, column=2, padx=10)

# row of entries
ctk.CTkEntry(app).grid(row=2, column=0, padx=10, pady=5)
ctk.CTkEntry(app).grid(row=2, column=1, padx=10, pady=5)
ctk.CTkEntry(app).grid(row=2, column=2, padx=10, pady=5)

# submit button across the bottom
button = ctk.CTkButton(app, text="Submit")
button.grid(row=3, column=0, columnspan=3, pady=15)

app.mainloop()
```

Run. Three columns of input. Way more compact than
single-column pack.

Notice the inline pattern: `ctk.CTkLabel(app, text="...").
grid(...)`. We didn't save the widget in a variable because
we don't need to read or modify it later. Saves typing.

#### `sticky` — alignment within a cell

Each grid cell has a fixed size. Inside it, a widget can
align to any side. `sticky="w"` (west = left), `"e"` (east),
`"n"` (north), `"s"` (south), or combinations like `"ew"`
(stretches across).

```python
ctk.CTkLabel(app, text="Right-aligned:").grid(row=0, column=0, sticky="e", padx=5)
```

Useful for aligning labels to the right of their column so
they sit next to the entries on the left of the next.

**Checkpoint:** *You've built a layout with `grid()` that
has at least two columns and at least two rows.* **This is
the natural stop point if class is cut short.**

---

### Part B: Frames — grouping widgets

When forms get bigger, they need *sections* — visual
groupings of related widgets. That's a `CTkFrame`.

#### What a frame is

A `CTkFrame` is a **container** widget. It holds other
widgets inside it. You can pack/grid widgets *inside* a
frame, then pack/grid the frame inside the main window.

Frames give you:
- Visual grouping (you can color the background).
- Layout flexibility (one frame can use grid, another can
  use pack).
- Easier reorganization (move a frame and everything in it
  moves together).

#### A two-section app

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("Two-section app")
app.geometry("600x400")

# Left frame — input
left_frame = ctk.CTkFrame(app)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(left_frame, text="Input", font=("Arial", 18, "bold")).pack(pady=10)
ctk.CTkEntry(left_frame, placeholder_text="Name").pack(pady=5)
ctk.CTkEntry(left_frame, placeholder_text="Age").pack(pady=5)
ctk.CTkButton(left_frame, text="Submit").pack(pady=10)

# Right frame — output
right_frame = ctk.CTkFrame(app)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(right_frame, text="Output", font=("Arial", 18, "bold")).pack(pady=10)
ctk.CTkLabel(right_frame, text="(submit something to see results)").pack(pady=5)

app.mainloop()
```

Save. Run.

Two frames side by side. Left holds inputs; right holds
output. Inside each frame, widgets stack with `pack()`.

What's new:

- `CTkFrame(app)` — a frame that lives in the main window.
- `pack(side="left", fill="both", expand=True)` — packs the
  frame to the left side; fills available space; expands as
  the window grows.
- Widgets inside the frame are children of the frame, not
  of the app. So `ctk.CTkLabel(left_frame, ...)` puts the
  label inside `left_frame`, not the main window.

The `side="left"` and `side="right"` is `pack()`'s way of
doing horizontal layout (instead of the default vertical).
You can also use `"top"` and `"bottom"`.

> **Inside a frame**, use `pack()` or `grid()` independently
> of the parent. The "no mixing" rule applies *within each
> container*, not across the whole app.

#### A real layout — header, sidebar, content

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("App with sections")
app.geometry("700x500")

# Header (top)
header = ctk.CTkFrame(app, height=60)
header.pack(side="top", fill="x", padx=5, pady=5)
ctk.CTkLabel(header, text="My App", font=("Arial", 24, "bold")).pack(pady=10)

# Body — sidebar + content
body = ctk.CTkFrame(app)
body.pack(side="top", fill="both", expand=True, padx=5, pady=5)

# Sidebar (left part of body)
sidebar = ctk.CTkFrame(body, width=150)
sidebar.pack(side="left", fill="y", padx=5, pady=5)
ctk.CTkLabel(sidebar, text="Menu", font=("Arial", 14, "bold")).pack(pady=10)
ctk.CTkButton(sidebar, text="Home").pack(pady=5)
ctk.CTkButton(sidebar, text="Settings").pack(pady=5)
ctk.CTkButton(sidebar, text="About").pack(pady=5)

# Content (right part of body)
content = ctk.CTkFrame(body)
content.pack(side="right", fill="both", expand=True, padx=5, pady=5)
ctk.CTkLabel(content, text="Welcome!", font=("Arial", 32)).pack(pady=30)
ctk.CTkLabel(content, text="This is a real-looking app layout.").pack(pady=5)

app.mainloop()
```

Save. Run.

A header bar across the top. A sidebar on the left with
buttons. A main content area on the right. **This actually
looks like a real app.**

Frames within frames. Each one organizes its part of the
window.

That's the **base goal** — a multi-frame layout that looks
like a real app.

#### Stretch — make the sidebar do something

Add callbacks to the sidebar buttons so they update the
content area:

```python
def show_home():
    content_label.configure(text="🏠 Home")

def show_settings():
    content_label.configure(text="⚙️ Settings")

def show_about():
    content_label.configure(text="ℹ️ About this app")

# ...

ctk.CTkButton(sidebar, text="Home", command=show_home).pack(pady=5)
ctk.CTkButton(sidebar, text="Settings", command=show_settings).pack(pady=5)
ctk.CTkButton(sidebar, text="About", command=show_about).pack(pady=5)

# in the content frame:
content_label = ctk.CTkLabel(content, text="🏠 Home", font=("Arial", 32))
content_label.pack(pady=30)
```

Now clicking a sidebar button changes the content. That's
how every navigation-based app works.

#### Extension — wrap the whole thing in a class

If you've got time, refactor the whole app into a class
(callback to Phase 4 Session 4):

```python
import customtkinter as ctk

class MyApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("My App")
        self.app.geometry("700x500")
        
        self._build_header()
        self._build_sidebar_and_content()
    
    def _build_header(self):
        header = ctk.CTkFrame(self.app, height=60)
        header.pack(side="top", fill="x", padx=5, pady=5)
        ctk.CTkLabel(header, text="My App", font=("Arial", 24, "bold")).pack(pady=10)
    
    def _build_sidebar_and_content(self):
        body = ctk.CTkFrame(self.app)
        body.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        
        sidebar = ctk.CTkFrame(body, width=150)
        sidebar.pack(side="left", fill="y", padx=5, pady=5)
        
        ctk.CTkButton(sidebar, text="Home", command=self.show_home).pack(pady=5)
        ctk.CTkButton(sidebar, text="Settings", command=self.show_settings).pack(pady=5)
        
        content = ctk.CTkFrame(body)
        content.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        
        self.content_label = ctk.CTkLabel(content, text="🏠 Home", font=("Arial", 32))
        self.content_label.pack(pady=30)
    
    def show_home(self):
        self.content_label.configure(text="🏠 Home")
    
    def show_settings(self):
        self.content_label.configure(text="⚙️ Settings")
    
    def run(self):
        self.app.mainloop()

app = MyApp()
app.run()
```

Same app, organized as a class. State (`self.content_label`)
lives on the instance. Methods access it via `self`. No
`global` needed. This is how *real* GUI apps are organized.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the two-section app — does
  side-by-side feel cleaner than stacked?
- For the kids who built the header-sidebar-content layout
  — does it feel like a real app?
- For the class refactor — does the class version feel
  more organized, or just longer?

You learned today the **organizational toolkit** for GUI
apps. **`grid()`** for precise rows-and-columns layouts.
**`CTkFrame`** for grouping related widgets. Combined,
they let you build interfaces that look like real software
— not just stacked widgets.

Most real apps are built as **frames within frames** — a
header frame, a body frame, a sidebar frame, a content
frame. Each one self-contained. Each one easy to
rearrange. That's the structural pattern of every GUI app
you've ever used.

### If you missed this session

Open Thonny. Then:

1. Build the basic 2-column form from Part A using `grid()`
   instead of `pack()`.

2. Try `columnspan` to make a button span multiple columns.

3. Build the two-section app with frames from Part B.

4. Build the header-sidebar-content layout (Part B base).

About 50 minutes — this is a long session. If you get
stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- **`grid_rowconfigure(weight=1)`** — makes a row grow
  when the window resizes. Useful for "expand this row to
  fill space."
- **`grid_columnconfigure(weight=1)`** — same for columns.
- **`place()`** — a third layout method that puts widgets
  at exact pixel positions. Almost never used in practice
  (windows resize and pixel positions break). Mention as
  "exists; usually don't."
- **Border styles on frames** — `CTkFrame(app, border_width=2,
  border_color="gray")` for visible borders.
- **Scrollable frames** — `CTkScrollableFrame` for content
  that's bigger than the window.

### What's next

Next week we **put it all together** — building a complete
app using everything from Phase 5 so far. After that, you
have one milestone planning session and one demo session,
then Phase 5 is done.
