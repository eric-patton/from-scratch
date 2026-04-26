## Session 1: Welcome to GUIs — your first window

*Phase 5 — customtkinter · Session 1 of 8*

### What we're learning today

Phase 4 was all text. Today we go visual again — but in a
different way than Scratch or Turtle. We're building **GUIs**
(Graphical User Interfaces): apps with windows, buttons,
text fields. The kind of thing that looks like a real
program when it runs. By the end of class, you'll have a
window appear on your screen with custom text, fonts, and
colors — your first real desktop app.

### You'll need to remember from last time

- **Classes** from Phase 4 Session 4 — every widget you'll
  use today is a class.
- **`import`** — `import customtkinter as ctk` brings in
  the GUI library.
- **Functions** — we'll use them as callbacks in Session 2.

---

### Part A: Your first window

Open Thonny. Create a new file. Save it as `first_gui.py`.

#### The minimum GUI

Type this exactly:

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("My First App")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Hello, world!")
label.pack(pady=20)

app.mainloop()
```

Save. Run.

A window opens. Dark background (the default theme), a label
that says "Hello, world!" near the top. The window has a
title bar saying "My First App."

That's a real desktop app — running in its own window,
separate from Thonny.

Close the window when you're done looking at it. (Click the
X in the corner.)

#### What just happened

Walk through line by line:

- `import customtkinter as ctk` — load the library, give it
  the short name `ctk`. We'll use `ctk.` a lot today.
- `app = ctk.CTk()` — create the **main window** (also
  called the "root window"). `CTk` is a class; `CTk()` calls
  the constructor and gives you an instance.
- `app.title("My First App")` — set the title bar text.
- `app.geometry("400x300")` — set the window size: 400
  pixels wide by 300 tall.
- `label = ctk.CTkLabel(app, text="Hello, world!")` — create
  a **label widget** that lives inside `app`. `CTkLabel` is
  another class. We pass it two arguments: the parent (where
  the label lives) and the text to show.
- `label.pack(pady=20)` — make the label visible by adding it
  to the window. `pack` is a layout method — it stacks
  widgets one after another. The `pady=20` adds 20 pixels of
  vertical padding around it.
- `app.mainloop()` — run the **event loop.** The window
  appears and **stays open** until the user closes it. This
  is the magic of GUI programs.

#### The event loop

That last line is the most conceptually new thing today.

In all your previous programs, the program *ran top to
bottom* and ended. A loop kept it going if you wanted, but
when there was no more code to run, it stopped.

GUI programs are different. After `app.mainloop()`, the
program **sits there waiting.** It doesn't end. It waits for
the user to click something, type something, close the
window. When the user does, the program reacts (runs the
right code), then goes back to waiting.

This is the **event loop** — the fundamental difference
between GUI programs and text programs. You write code that
*describes the interface* and *what happens on each event.*
The event loop handles the rest.

(Phase 1's Scratch had something similar — the green flag
events, the click events. GUI programming brings that back
in Python form.)

#### Customize the window

Try a few changes:

```python
app.title("My Awesome App")
app.geometry("600x400")
```

Bigger window, different title.

Change the label:

```python
label = ctk.CTkLabel(app, text="Hello from your first GUI!", font=("Arial", 24))
```

The `font=("Arial", 24)` makes the text bigger. You can pass
many other options to widgets — color, padding, size. We'll
see more of them.

#### Multiple labels

You can add as many widgets as you want. Add another label:

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("My First App")
app.geometry("400x300")

title_label = ctk.CTkLabel(app, text="Welcome!", font=("Arial", 32))
title_label.pack(pady=20)

subtitle = ctk.CTkLabel(app, text="This is my first GUI.", font=("Arial", 14))
subtitle.pack(pady=5)

footer = ctk.CTkLabel(app, text="Made with customtkinter")
footer.pack(pady=10)

app.mainloop()
```

Run. Three labels stack vertically. `pack` adds them in the
order you call it — top to bottom by default.

**Checkpoint:** *You have a window with at least two custom
labels (different text, different fonts), a custom title,
and a custom size.* **This is the natural stop point if
class is cut short.**

---

### Part B: Customize and explore

Now make it *yours.*

#### Light vs dark theme

By default, customtkinter uses dark mode. You can switch:

```python
ctk.set_appearance_mode("light")    # or "dark", or "system"
```

Add this *before* creating the window:

```python
import customtkinter as ctk

ctk.set_appearance_mode("light")    # NEW
ctk.set_default_color_theme("blue") # also try "green", "dark-blue"

app = ctk.CTk()
# ... rest of the code ...
```

Try `"light"`, `"dark"`, and `"system"` (which follows your
OS theme). Try different color themes.

#### A personal welcome screen

Build a welcome screen for *your* app — name it after
something you'd want to make. Maybe "Caleb's Quiz Game" or
"Bible Verse of the Day" or "Sam's Drawing Tool."

Aim for at least four labels:

- A big title.
- A subtitle or description.
- Maybe an emoji or symbol (yes, customtkinter shows emojis
  in labels).
- A footer or "by you" credit.

Use different fonts and sizes to give it visual hierarchy
(big = important, small = footnote).

```python
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Bible Verse of the Day")
app.geometry("500x400")

title = ctk.CTkLabel(
    app,
    text="📖 Verse of the Day",
    font=("Arial", 32, "bold")
)
title.pack(pady=30)

verse = ctk.CTkLabel(
    app,
    text="\"For God so loved the world...\"",
    font=("Arial", 16)
)
verse.pack(pady=10)

reference = ctk.CTkLabel(
    app,
    text="John 3:16",
    font=("Arial", 14, "italic")
)
reference.pack(pady=5)

footer = ctk.CTkLabel(
    app,
    text="Made by Sam",
    font=("Arial", 10)
)
footer.pack(pady=20)

app.mainloop()
```

Save. Run. Your own little app appears.

This is the **base goal.** A personal welcome screen with
multiple labels, custom fonts, and your own theme.

#### Stretch — colored labels

Labels can have custom colors:

```python
title = ctk.CTkLabel(
    app,
    text="Important!",
    font=("Arial", 24),
    text_color="red"
)
```

Try different colors. Strings work (`"red"`, `"blue"`,
`"#FF5733"` for hex codes).

#### Stretch — backgrounds

Whole sections can have colored backgrounds. Use `fg_color`:

```python
title = ctk.CTkLabel(
    app,
    text="Important",
    font=("Arial", 24),
    fg_color="darkblue",
    corner_radius=10,
    width=300,
    height=60
)
```

`fg_color` is the background of the widget itself.
`corner_radius` makes rounded corners. `width` and `height`
set explicit size.

#### Extension — multiple themes

Add a "what theme do you want?" prompt at the start (using
plain `input()` — no GUI yet for that since we don't have
buttons until next week):

```python
import customtkinter as ctk

mode = input("Theme (light/dark/system): ")
ctk.set_appearance_mode(mode)

app = ctk.CTk()
# ... rest ...
```

Run from the terminal. Type a theme. The window opens with
that theme.

This is a tiny taste of "the user controls the appearance"
— a real feature of real apps.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built a personal welcome screen —
  what's it for? What did you call it?
- For the kids who tried different themes — which one's
  your favorite?
- Did anyone get the window to come up empty (no labels)?
  What was missing?

You learned today the foundation of every desktop app you've
ever used. **A window. Widgets inside. An event loop that
keeps it alive.** Microsoft Word, Discord, Spotify, every
game launcher — all built on the same shape.

The mental shift is real: GUI programs *describe an
interface* rather than *follow a sequence*. You're saying
"this widget here, this widget there, here's what they do."
The event loop runs everything.

### If you missed this session

Open Thonny and start a new file. Save it as `first_gui.py`.
Then:

1. Type the minimum GUI from Part A:
   ```python
   import customtkinter as ctk

   app = ctk.CTk()
   app.title("My First App")
   app.geometry("400x300")

   label = ctk.CTkLabel(app, text="Hello, world!")
   label.pack(pady=20)

   app.mainloop()
   ```
   Save. Run. A window appears.

2. Add more labels with different fonts and sizes.

3. Try `ctk.set_appearance_mode("light")` (before creating
   the window).

4. Build a personal welcome screen (Part B base).

About 30-40 minutes. If you get stuck, ask your buddy at
the start of next class.

### Stretch and extension ideas

- **Window icons** — `app.iconbitmap("icon.ico")` (Windows)
  or with a `.png` for cross-platform. Need to find or
  create an icon file first.
- **`pady` and `padx`** for spacing. `pady=(20, 5)` is
  asymmetric: 20 pixels above, 5 below. Useful for
  fine-tuning layout.
- **`anchor`** — controls how a widget aligns in its space.
  `label.pack(anchor="w")` sticks to the west (left) side.
- **Resizable windows** — the user can drag the corner to
  resize. `app.resizable(False, False)` disables resizing.
- **`destroy()`** — programmatically close the window:
  `app.destroy()`. Useful inside callbacks (next week).

### What's next

Next week we add **buttons** — interactive widgets the user
can click to make things happen. That's where the GUI gets
*alive.* Combined with today's labels, you'll have apps
that respond to the user.
