## Session 3: Inputs — entries and text boxes

*Phase 5 — customtkinter · Session 3 of 8*

### What we're learning today

Last week your buttons made things happen — but the user
couldn't *type* anything. Today we add **input widgets** —
text fields the user types into. Combined with buttons,
you'll be able to build apps that take real input from the
user and respond with personalized output. By the end of
class, you'll have a "form" app that asks for several pieces
of info and uses them in a custom message.

### You'll need to remember from last time

- **`CTkButton`** with `command=function`.
- **Callback functions.**
- **`label.configure(text=...)`** to update widgets.
- **Phase 3 strings** — f-strings for combining text and
  variables.

---

### Part A: Your first entry

Open Thonny. Save a new file as `entry_app.py`.

#### Build it

```python
import customtkinter as ctk

def greet():
    name = entry.get()
    label.configure(text=f"Hello, {name}!")

app = ctk.CTk()
app.title("Greeter")
app.geometry("400x250")

entry = ctk.CTkEntry(app, placeholder_text="Type your name")
entry.pack(pady=20)

button = ctk.CTkButton(app, text="Greet me", command=greet)
button.pack(pady=10)

label = ctk.CTkLabel(app, text="", font=("Arial", 18))
label.pack(pady=20)

app.mainloop()
```

Save. Run.

A window opens with a text field, a button, and an empty
label below. Type your name into the text field. Click the
button. The label updates: "Hello, [your name]!"

#### What's new

- `ctk.CTkEntry(app, placeholder_text="Type your name")` —
  a single-line text input. The `placeholder_text` is the
  faded text that shows when empty.
- `entry.get()` — reads the current text in the entry.
  Returns a string.
- The callback `greet()` calls `entry.get()`, then
  `label.configure(text=...)` to update the display.

The pattern: **type into entry → click button → callback
reads entry value → callback updates display.** Same loop as
the counter, just with text input instead of a click.

#### Customize and try variations

Try:

- An empty starting label (`text=""`) so nothing shows
  until the button is clicked.
- A different greeting in the f-string ("Welcome, ___!"
  or "Hi there, ___!").
- Make the entry bigger: `width=300`.
- Make the font of the entry bigger: `font=("Arial", 16)`.

#### Setting and clearing the entry

You can also *set* the entry's text from code:

```python
entry.delete(0, "end")          # clear it
entry.insert(0, "default")      # put text in
```

Useful when you want to clear after the user submits, or
provide a default.

Try adding `entry.delete(0, "end")` at the end of `greet()`:

```python
def greet():
    name = entry.get()
    label.configure(text=f"Hello, {name}!")
    entry.delete(0, "end")    # clear after greeting
```

Now the entry empties out after each greeting. More
form-like.

**Checkpoint:** *You have a window with at least one entry,
one button, and a label that updates with the entry's
content when the button is clicked.* **This is the natural
stop point if class is cut short.**

---

### Part B: A multi-input form

Real apps usually have *several* fields. Build a small form
that takes multiple pieces of info.

#### Base goal — about-me form

```python
import customtkinter as ctk

def submit():
    name = name_entry.get()
    age = age_entry.get()
    color = color_entry.get()
    
    output_label.configure(
        text=f"Hi {name}! You're {age} years old and your favorite color is {color}.",
        wraplength=350
    )

app = ctk.CTk()
app.title("About Me Form")
app.geometry("450x400")

title = ctk.CTkLabel(app, text="Tell me about you!", font=("Arial", 20, "bold"))
title.pack(pady=15)

name_entry = ctk.CTkEntry(app, placeholder_text="Name", width=300)
name_entry.pack(pady=5)

age_entry = ctk.CTkEntry(app, placeholder_text="Age", width=300)
age_entry.pack(pady=5)

color_entry = ctk.CTkEntry(app, placeholder_text="Favorite color", width=300)
color_entry.pack(pady=5)

submit_button = ctk.CTkButton(app, text="Submit", command=submit, width=200)
submit_button.pack(pady=15)

output_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
output_label.pack(pady=20)

app.mainloop()
```

Save. Run. Fill in the three fields. Click submit. A
personalized message appears.

What's new:

- **Multiple entries** — each one is its own widget with its
  own variable name.
- **`wraplength=350`** on the label — wraps the text after
  350 pixels so long messages don't run off the side.
- **The pattern scales** — one callback that reads several
  entries and updates one label.

#### Stretch — a quiz that grades you

Ask a few questions, check the answers, give a score:

```python
import customtkinter as ctk

def grade():
    score = 0
    if answer1.get().lower() == "noah":
        score = score + 1
    if answer2.get().lower() == "12":
        score = score + 1
    if answer3.get().lower().strip() == "moses":
        score = score + 1
    
    result_label.configure(text=f"Score: {score} / 3")

app = ctk.CTk()
app.title("Bible Quiz")
app.geometry("500x400")

title = ctk.CTkLabel(app, text="Bible Quiz", font=("Arial", 24, "bold"))
title.pack(pady=10)

q1 = ctk.CTkLabel(app, text="1. Who built the ark?")
q1.pack()
answer1 = ctk.CTkEntry(app, width=300)
answer1.pack(pady=5)

q2 = ctk.CTkLabel(app, text="2. How many disciples did Jesus have?")
q2.pack()
answer2 = ctk.CTkEntry(app, width=300)
answer2.pack(pady=5)

q3 = ctk.CTkLabel(app, text="3. Who led the Israelites out of Egypt?")
q3.pack()
answer3 = ctk.CTkEntry(app, width=300)
answer3.pack(pady=5)

button = ctk.CTkButton(app, text="Submit answers", command=grade)
button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 18))
result_label.pack(pady=15)

app.mainloop()
```

Run. Answer the questions. See your score.

The `.lower()` and `.strip()` calls handle different ways
the user might type the answer (capital, lowercase, with or
without trailing spaces).

#### Extension — a textbox for longer input

Sometimes you want the user to write *paragraphs*, not just
single lines. That's a `CTkTextbox`:

```python
import customtkinter as ctk

def count_words():
    text = textbox.get("1.0", "end")
    word_count = len(text.split())
    label.configure(text=f"Word count: {word_count}")

app = ctk.CTk()
app.title("Word Counter")
app.geometry("500x400")

title = ctk.CTkLabel(app, text="Type something:", font=("Arial", 16))
title.pack(pady=10)

textbox = ctk.CTkTextbox(app, width=400, height=200)
textbox.pack(pady=10)

button = ctk.CTkButton(app, text="Count words", command=count_words)
button.pack(pady=5)

label = ctk.CTkLabel(app, text="", font=("Arial", 14))
label.pack(pady=10)

app.mainloop()
```

`CTkTextbox` is for multi-line text. To read its content,
use `textbox.get("1.0", "end")` — the `"1.0"` means "row 1,
column 0" (yes, rows count from 1, columns from 0; weird
but that's tkinter). `"end"` means to the end.

The `.split()` on the result divides into words by
whitespace. `len()` counts them.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the form — what fields did you
  ask about?
- For the kids who built the quiz — what subject did you
  pick?
- Did anyone hit the "user typed something weird and it
  broke" issue? How did you handle it?

You learned today the foundation of **forms** — the
interface element that powers every signup page, every
search box, every comment field, every login. Plus
buttons, plus output labels, plus updating widgets — that's
the entire shape of *most* productivity apps.

You also met the input pattern: **`widget.get()` reads what
the user typed; the callback uses it.** Same shape for
entries, textboxes, and (next week) checkboxes / radio
buttons / dropdowns.

### If you missed this session

Open Thonny. Then:

1. Build the basic greeter from Part A — entry + button +
   label that updates on click.

2. Try `entry.delete(0, "end")` to clear after greeting.

3. Build the about-me form (Part B base) with three
   entries.

About 30-40 minutes. If you get stuck, ask your buddy at
the start of next class.

### Stretch and extension ideas

- **Validation** — check that input is a number before
  using it. `if not age.isdigit(): ...`. Use `try/except
  ValueError` for converting strings to integers.
- **`bind` to Enter key** — `entry.bind("<Return>",
  lambda e: submit())` makes pressing Enter submit the
  form (instead of having to click the button).
- **`focus_set()`** — `entry.focus_set()` puts the cursor
  in the entry. Useful at startup or after submission.
- **`StringVar`** — a special variable type that
  automatically syncs with widgets. More advanced; powerful
  for two-way binding.

### What's next

Next week we add **choice widgets** — checkboxes, radio
buttons, and dropdowns. Combined with today's text inputs,
you'll have every common form element. After that, layouts
to organize them all nicely.
