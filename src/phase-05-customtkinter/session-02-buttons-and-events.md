## Session 2: Buttons and events

*Phase 5 — customtkinter · Session 2 of 8*

### What we're learning today

Last week your window just *sat there* — labels, but nothing
to click. Today we add **buttons** that react when the user
clicks them. By the end, you'll have built a counter app: a
button that, when clicked, makes a number go up on the
screen. Tiny but real — and the same pattern that powers
*every* interactive app you've ever used.

### You'll need to remember from last time

- **`import customtkinter as ctk`** — the GUI library.
- **`ctk.CTk()`** — main window.
- **`ctk.CTkLabel(parent, text="...")`** — a text label.
- **`.pack()`** — add a widget to the window.
- **`app.mainloop()`** — start the event loop.
- **The event loop** — the program waits for the user to do
  something.
- **Functions** — we'll write functions called when the
  button is clicked.

---

### Part A: Your first button

Open Thonny. Save a new file as `button_app.py`.

#### A button that does one thing

```python
import customtkinter as ctk

def say_hello():
    print("Hello!")

app = ctk.CTk()
app.title("Button App")
app.geometry("400x200")

button = ctk.CTkButton(app, text="Click me!", command=say_hello)
button.pack(pady=50)

app.mainloop()
```

Save. Run.

A window opens with a button. Click it. Look at the **shell
in Thonny** — "Hello!" appears. Click again. Another
"Hello!". The button calls the function every time you click.

Walk through what's new:

- `def say_hello():` — a function. Same as Phase 2-3
  functions. No parameters.
- `ctk.CTkButton(app, text="Click me!", command=say_hello)`
  — a button widget. The new parameter is `command`. It
  takes a *function* (not a function call — just the name).
- The function gets called every time the button is clicked.

#### `command=` is special

Notice: `command=say_hello`, **not** `command=say_hello()`.

The `()` would *call* the function and pass its return
value (which would be None) to `command`. We don't want
that. We want to give the button the function itself, so
the button can call it later when it needs to.

This is one of the most common Python beginner mistakes.
**Pass the function name, not a call.**

```python
command=say_hello       # CORRECT — pass the function
command=say_hello()     # WRONG — calls it now, passes the result
```

If you ever click your button and nothing happens (or it
runs once when the program starts and never again), check
this.

#### Multiple buttons

You can have as many buttons as you want, each with its own
function:

```python
import customtkinter as ctk

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

def make_a_noise():
    print("BEEP BEEP")

app = ctk.CTk()
app.title("Multi-button App")
app.geometry("400x300")

button1 = ctk.CTkButton(app, text="Hello", command=say_hello)
button1.pack(pady=10)

button2 = ctk.CTkButton(app, text="Goodbye", command=say_goodbye)
button2.pack(pady=10)

button3 = ctk.CTkButton(app, text="Make noise", command=make_a_noise)
button3.pack(pady=10)

app.mainloop()
```

Three buttons. Three functions. Each button calls its own.

**Checkpoint:** *You have a window with at least two
buttons, each calling a different function that prints
something different.* **This is the natural stop point if
class is cut short.**

---

### Part B: A counter app

Printing to the shell is fine, but real apps update the
*window itself.* Let's build a counter — a number on the
screen that goes up when you click a button.

#### Build it

```python
import customtkinter as ctk

count = 0

def increment():
    global count
    count = count + 1
    label.configure(text=f"Count: {count}")

app = ctk.CTk()
app.title("Counter")
app.geometry("400x200")

label = ctk.CTkLabel(app, text="Count: 0", font=("Arial", 32))
label.pack(pady=20)

button = ctk.CTkButton(app, text="Click me!", command=increment)
button.pack(pady=10)

app.mainloop()
```

Save. Run. Click the button. The number goes up *on the
screen.* Each click adds 1.

This is what every app does. Counter, score, message
display, timer — all variations of "user does something →
update the display."

#### What's new

A few things:

- `count = 0` at the top — a regular variable that starts
  at 0.
- `def increment():` — the callback function.
- `global count` inside the function — tells Python that
  when we say `count`, we mean the variable up top, not a
  new local one. Without `global`, Python would create a
  new local `count` and the outer one would never change.
- `label.configure(text=...)` — this is how you *change* a
  widget's properties after creating it. The `.configure()`
  method takes the same parameters as the constructor.

#### About `global`

The `global count` line is a Python wrinkle worth
explaining. By default, when a function assigns to a
variable, Python treats it as a *new local variable.* So:

```python
count = 0

def increment():
    count = count + 1   # This makes a NEW local count
```

The `count = count + 1` line creates a new local variable
called `count`, sets it to (outer count) + 1, then throws
it away when the function ends. The outer `count` is never
changed.

To modify the outer `count`, you need `global count`:

```python
count = 0

def increment():
    global count       # "use the outer count"
    count = count + 1
```

This is one of those Python quirks. In bigger programs,
`global` is considered bad style — better solutions exist
(using classes, or returning values). For a small app, it
works.

(Phase 4 Session 4 covered classes. The "right" way to do
this is to wrap the counter in a class. We'll touch that
later.)

#### Customize the counter

Try variations:

- Add a "Reset" button that sets `count` back to 0.
- Add a "Decrement" button that goes down.
- Add a "Multiply by 2" button.
- Make the font huge and the buttons big.

That's the **base goal** — a counter app with at least
three buttons (increment, reset, and one more of your
choice).

#### Stretch — a tiny clicker game

Build a "clicker game" — every click adds points; certain
milestones trigger messages:

```python
import customtkinter as ctk

score = 0

def click():
    global score
    score = score + 1
    score_label.configure(text=f"Score: {score}")
    
    if score == 10:
        message_label.configure(text="🎉 You hit 10!")
    elif score == 50:
        message_label.configure(text="🌟 50 points! Amazing!")
    elif score == 100:
        message_label.configure(text="🏆 100! You're a champion!")

app = ctk.CTk()
app.title("Clicker")
app.geometry("400x300")

title = ctk.CTkLabel(app, text="Click as fast as you can!", font=("Arial", 18))
title.pack(pady=10)

score_label = ctk.CTkLabel(app, text="Score: 0", font=("Arial", 32))
score_label.pack(pady=20)

button = ctk.CTkButton(app, text="CLICK", command=click, font=("Arial", 24), height=60)
button.pack(pady=10)

message_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
message_label.pack(pady=10)

app.mainloop()
```

Run. Click fast. Hit 10, 50, 100 — different messages
appear.

That's a real little game. Two state variables (score,
which message), conditional logic, multiple labels updating.
The same pattern scales to bigger games.

#### Extension — buttons that change buttons

Make a button that *changes its own text* each time it's
clicked:

```python
import customtkinter as ctk

texts = ["Click me", "Again", "Once more", "Last time", "Click me"]
index = 0

def change_text():
    global index
    index = (index + 1) % len(texts)
    button.configure(text=texts[index])

app = ctk.CTk()
app.title("Changing button")
app.geometry("400x200")

button = ctk.CTkButton(app, text=texts[0], command=change_text)
button.pack(pady=50)

app.mainloop()
```

The button's text cycles through a list. Same pattern —
state variable + callback that updates a widget — but the
widget being updated is the *same one* being clicked.

#### Extension — wrap in a class

If you want to do this the "right way" (per Phase 4 Session
4), put everything in a class:

```python
import customtkinter as ctk

class CounterApp:
    def __init__(self):
        self.count = 0
        
        self.app = ctk.CTk()
        self.app.title("Counter (class version)")
        self.app.geometry("400x200")
        
        self.label = ctk.CTkLabel(self.app, text="Count: 0", font=("Arial", 32))
        self.label.pack(pady=20)
        
        self.button = ctk.CTkButton(self.app, text="Click me!", command=self.increment)
        self.button.pack(pady=10)
    
    def increment(self):
        self.count += 1
        self.label.configure(text=f"Count: {self.count}")
    
    def run(self):
        self.app.mainloop()

# create and run
counter = CounterApp()
counter.run()
```

Notice — no more `global`. The count lives on the class
instance (`self.count`). Methods access it via `self`. This
is real-world structure for non-trivial GUI apps.

We'll do more of this in later sessions.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the counter — what other buttons
  did you add?
- For the clicker game — did anyone get to 100?
- Did anyone get the "button does nothing" bug? Was it the
  `command=function()` mistake?

You learned today the heart of GUI programming:
**user does something → callback runs → display updates.**
That single loop is what every interactive app does. Word
processors, games, web pages, mobile apps — all variations
of that pattern.

You also met `.configure()` for *changing widgets after
creation.* Until now, widgets were fixed once made; now
they can update. That's how interfaces feel alive.

### If you missed this session

Open Thonny and start a new file. Save as `button_app.py`.
Then:

1. Build the basic button + callback from Part A. Click
   it; see the shell output.

2. Build the counter app from Part B base. Notice how
   `label.configure(text=...)` updates the display.

3. Try adding a Reset button.

About 30-40 minutes. If you get stuck, ask your buddy at
the start of next class.

### Stretch and extension ideas

- **Disable a button** — `button.configure(state="disabled")`
  grays it out. Re-enable with `state="normal"`.
- **Hide a widget** — `label.pack_forget()` removes it from
  view (it still exists; can `.pack()` it again later).
- **`after()`** — schedule a function to run after a
  delay. `app.after(1000, my_function)` runs `my_function`
  in 1000 milliseconds (1 second). Useful for animations
  and timers.
- **`destroy()`** — close the window with `app.destroy()`.
  Call it inside a callback for a "Quit" button.
- **Lambda functions** — `command=lambda: print("hi")`
  defines a tiny one-line function inline. Useful when the
  callback is trivial.

### What's next

Next week we add **input widgets** — text fields the user
can type into. Combined with today's buttons, you'll be
able to build apps that take real text input and respond to
it. Real forms!
