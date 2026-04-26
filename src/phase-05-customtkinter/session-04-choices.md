## Session 4: Choices — checkboxes, radio buttons, dropdowns

*Phase 5 — customtkinter · Session 4 of 8*

### What we're learning today

You've got buttons and text input. Today we add the rest of
the basic widget toolbox: **checkboxes** (yes/no
multi-select), **radio buttons** (pick one of several), and
**dropdowns** (pick from a list). By the end, you'll have
built a "build your character" form using all three.

### You'll need to remember from last time

- **`CTkButton`** with callbacks.
- **`CTkEntry`** and `entry.get()`.
- **`label.configure(text=...)`** to update widgets.
- **f-strings** for combining text and variables.

---

### Part A: Checkboxes, radios, dropdowns

Open Thonny. Save a new file as `choices_app.py`.

#### Checkboxes

A checkbox is yes/no. The user clicks to toggle. You can
have many checkboxes, each with its own state.

```python
import customtkinter as ctk

def show_choices():
    likes = []
    if pizza_check.get() == 1:
        likes.append("pizza")
    if soccer_check.get() == 1:
        likes.append("soccer")
    if reading_check.get() == 1:
        likes.append("reading")
    
    if len(likes) == 0:
        result.configure(text="You like nothing? :(")
    else:
        result.configure(text=f"You like: {', '.join(likes)}")

app = ctk.CTk()
app.title("What do you like?")
app.geometry("400x350")

title = ctk.CTkLabel(app, text="Pick what you like:", font=("Arial", 16))
title.pack(pady=10)

pizza_check = ctk.CTkCheckBox(app, text="Pizza")
pizza_check.pack(pady=5)

soccer_check = ctk.CTkCheckBox(app, text="Soccer")
soccer_check.pack(pady=5)

reading_check = ctk.CTkCheckBox(app, text="Reading")
reading_check.pack(pady=5)

button = ctk.CTkButton(app, text="Show choices", command=show_choices)
button.pack(pady=10)

result = ctk.CTkLabel(app, text="", font=("Arial", 14), wraplength=350)
result.pack(pady=10)

app.mainloop()
```

Save. Run. Check some boxes. Click button. The label shows
your choices.

What's new:

- `CTkCheckBox(app, text="Label")` — the checkbox widget.
- `checkbox.get()` returns `1` if checked, `0` if not.
- The pattern: build up a list based on which boxes are
  checked.

Each checkbox is **independent** — they don't affect each
other. The user can check zero, one, two, or all of them.

#### Radio buttons

Radio buttons are different — only **one** can be selected
at a time. Like a multiple-choice question. Click one and
any previously selected one unchecks.

To make several radio buttons share state, you give them
all the same `variable` argument:

```python
import customtkinter as ctk

def show_pick():
    pick = pet_choice.get()
    result.configure(text=f"You picked: {pick}")

app = ctk.CTk()
app.title("Pick a pet")
app.geometry("400x300")

title = ctk.CTkLabel(app, text="What kind of pet?", font=("Arial", 16))
title.pack(pady=10)

# all three radios share this variable
pet_choice = ctk.StringVar(value="dog")    # default selection

dog_radio = ctk.CTkRadioButton(app, text="Dog", variable=pet_choice, value="dog")
dog_radio.pack(pady=5)

cat_radio = ctk.CTkRadioButton(app, text="Cat", variable=pet_choice, value="cat")
cat_radio.pack(pady=5)

fish_radio = ctk.CTkRadioButton(app, text="Fish", variable=pet_choice, value="fish")
fish_radio.pack(pady=5)

button = ctk.CTkButton(app, text="Submit", command=show_pick)
button.pack(pady=10)

result = ctk.CTkLabel(app, text="", font=("Arial", 14))
result.pack(pady=10)

app.mainloop()
```

Save. Run. Pick a pet. Click submit. The label shows your
choice.

What's new:

- `ctk.StringVar(value="dog")` — a special variable for
  sharing state between widgets. We give it a starting
  value (`"dog"` is selected at startup).
- `variable=pet_choice` on each radio — connects the radio
  to the shared variable.
- `value="dog"` (etc.) — what the variable becomes when
  this radio is selected.
- `pet_choice.get()` — reads the current value.

The `StringVar` is the new piece. Think of it as a "shared
text variable" that multiple widgets can reference. When one
radio is clicked, the variable updates to that radio's
`value`. Reading the variable tells you which is selected.

#### Dropdowns

A dropdown shows one item but lets the user expand to pick
from a list. Compact for many options.

```python
import customtkinter as ctk

def show_color():
    chosen = color_dropdown.get()
    result.configure(text=f"Color: {chosen}", text_color=chosen)

app = ctk.CTk()
app.title("Pick a color")
app.geometry("400x250")

title = ctk.CTkLabel(app, text="Pick a color:", font=("Arial", 16))
title.pack(pady=10)

color_dropdown = ctk.CTkOptionMenu(
    app,
    values=["red", "blue", "green", "purple", "orange", "pink"]
)
color_dropdown.pack(pady=10)

button = ctk.CTkButton(app, text="Show", command=show_color)
button.pack(pady=10)

result = ctk.CTkLabel(app, text="", font=("Arial", 18))
result.pack(pady=10)

app.mainloop()
```

Save. Run. Click the dropdown. Pick a color. Click "Show."
The label updates with the color name AND in that color.

What's new:

- `CTkOptionMenu(app, values=[...])` — the dropdown widget.
  The list is what shows when you click it.
- `dropdown.get()` returns the currently-selected string.

There's also `CTkComboBox` which is similar but lets the
user *type* a custom value (in addition to picking from
the list). Use that when the options aren't fixed.

**Checkpoint:** *You've used at least one of each: a
checkbox, a radio button group, and a dropdown.* **This is
the natural stop point if class is cut short.**

---

### Part B: A "build your character" form

Time to combine everything into one form.

#### Build it

```python
import customtkinter as ctk

def build_character():
    name = name_entry.get()
    char_class = class_choice.get()
    weapon = weapon_dropdown.get()
    
    abilities = []
    if magic_check.get() == 1:
        abilities.append("magic")
    if stealth_check.get() == 1:
        abilities.append("stealth")
    if strength_check.get() == 1:
        abilities.append("strength")
    
    abilities_text = ", ".join(abilities) if abilities else "none"
    
    result.configure(
        text=f"Meet {name} the {char_class}!\n"
             f"Wields a {weapon}.\n"
             f"Special abilities: {abilities_text}.",
        wraplength=350
    )

app = ctk.CTk()
app.title("Build a Character")
app.geometry("500x600")

title = ctk.CTkLabel(app, text="🗡️ Build Your Character", font=("Arial", 22, "bold"))
title.pack(pady=15)

# Name input
name_label = ctk.CTkLabel(app, text="Name:")
name_label.pack()
name_entry = ctk.CTkEntry(app, placeholder_text="Enter character name", width=300)
name_entry.pack(pady=5)

# Class (radio buttons)
class_label = ctk.CTkLabel(app, text="Class:")
class_label.pack(pady=(15, 0))

class_choice = ctk.StringVar(value="warrior")
warrior_radio = ctk.CTkRadioButton(app, text="Warrior", variable=class_choice, value="warrior")
warrior_radio.pack()
mage_radio = ctk.CTkRadioButton(app, text="Mage", variable=class_choice, value="mage")
mage_radio.pack()
rogue_radio = ctk.CTkRadioButton(app, text="Rogue", variable=class_choice, value="rogue")
rogue_radio.pack()

# Weapon (dropdown)
weapon_label = ctk.CTkLabel(app, text="Weapon:")
weapon_label.pack(pady=(15, 0))
weapon_dropdown = ctk.CTkOptionMenu(
    app,
    values=["sword", "staff", "dagger", "bow", "hammer"]
)
weapon_dropdown.pack(pady=5)

# Abilities (checkboxes)
abilities_label = ctk.CTkLabel(app, text="Special abilities:")
abilities_label.pack(pady=(15, 0))
magic_check = ctk.CTkCheckBox(app, text="Magic")
magic_check.pack()
stealth_check = ctk.CTkCheckBox(app, text="Stealth")
stealth_check.pack()
strength_check = ctk.CTkCheckBox(app, text="Strength")
strength_check.pack()

# Submit button
button = ctk.CTkButton(app, text="Build!", command=build_character)
button.pack(pady=15)

# Result
result = ctk.CTkLabel(app, text="", font=("Arial", 14), wraplength=350)
result.pack(pady=10)

app.mainloop()
```

Save. Run. Fill out the form — name, class, weapon, any
abilities you want. Click Build. The label shows your
character.

That's the **base goal** — every choice widget type plus
text input plus a button, all combined into one form.

#### Stretch — react in real-time

Make the result update *as the user changes choices* —
no submit button needed. Use `command=` on the choice
widgets:

```python
def update():
    name = name_entry.get() or "(no name)"
    char_class = class_choice.get()
    # ... build the result string ...
    result.configure(text=...)

# attach update to each widget:
warrior_radio = ctk.CTkRadioButton(app, ..., command=update)
mage_radio = ctk.CTkRadioButton(app, ..., command=update)
weapon_dropdown = ctk.CTkOptionMenu(app, ..., command=lambda x: update())
magic_check = ctk.CTkCheckBox(app, ..., command=update)
# ... etc.
```

(For OptionMenu, the command takes one argument — the
selected value — so we use `lambda x: update()` to ignore
it.)

For text entries, you'd `bind` to the keypress event:

```python
name_entry.bind("<KeyRelease>", lambda e: update())
```

Now the character description updates in real time as the
user changes anything. That's how modern reactive apps feel.

#### Extension — save the character

Add a "Save" button that writes the character to a file
(callback to Phase 3 Session 11):

```python
def save():
    name = name_entry.get()
    char_class = class_choice.get()
    weapon = weapon_dropdown.get()
    
    with open("characters.txt", "a") as f:
        f.write(f"{name}, {char_class}, {weapon}\n")
    
    result.configure(text=f"Saved {name} to characters.txt!")

# add another button:
save_button = ctk.CTkButton(app, text="Save", command=save)
save_button.pack(pady=5)
```

Now characters persist between runs of the app. A real
mini-app.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the character form — what's your
  best character?
- For the kids who tried real-time updates — does it feel
  more "alive" than clicking submit?
- Did anyone get the radio buttons to work without a
  StringVar? (Trick question — they need it.)

You learned today the **complete form vocabulary** —
text input, choice widgets, buttons. Combined with last
week's labels and update patterns, you can now build *any*
form an app might need. Login pages, settings, surveys,
configuration — all the same shapes.

You also met **`StringVar`** (and the related `IntVar`,
`DoubleVar`, `BooleanVar`) — special variables that let
multiple widgets share state. Required for radio buttons;
useful for many other things.

### If you missed this session

Open Thonny. Then:

1. Build the basic checkbox example from Part A. Check
   some boxes. Click submit. See the result.

2. Build the radio button example. Notice how only one can
   be selected.

3. Build the dropdown example.

4. Build the character form (Part B base) using all three
   widget types plus an entry.

About 40-50 minutes — this is a long session.

### Stretch and extension ideas

- **`SegmentedButton`** — like radio buttons but as a row
  of buttons. `ctk.CTkSegmentedButton(app, values=[...])`.
- **`Slider`** — for numeric input. `ctk.CTkSlider(app,
  from_=0, to=100)`.
- **`Switch`** — like a checkbox but styled as a toggle
  switch. `ctk.CTkSwitch(app, text="...")`.
- **`ProgressBar`** — for showing progress.
- **Disable widgets based on choices** — e.g., the magic
  checkbox is only available if class is "Mage." Use
  `widget.configure(state="disabled")` and `state="normal"`.

### What's next

Next week we tackle **layouts** — how to organize all these
widgets so they look good together. So far we've used
`pack()` which just stacks vertically. Next week we'll use
`grid()` and `CTkFrame` to make multi-column, multi-section
layouts that look like real apps.
