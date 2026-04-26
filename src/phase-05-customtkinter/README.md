# Phase 5 — customtkinter (desktop apps)

You can write CLI tools. You can save versions of your work
with Git. Now we go visual again — building **desktop apps**
with windows, buttons, forms, and other widgets that look
like real software.

## What this phase is

Eight focused sessions on building GUI (Graphical User
Interface) apps with Python. Less new programming syntax,
more *new ways to think about programs.* Programs with
GUIs aren't sequential — they sit there waiting for the user
to do something, then react. That's a different mental model
from the text-based programs of Phases 3-4.

By the end, you'll have built a desktop app of your own
design — something with windows, buttons, inputs, and real
behavior. The kind of thing you could install on someone
else's computer and they'd know how to use.

## What you'll learn

| Session | Idea | What's new |
|---|---|---|
| 1 | Welcome to GUIs — your first window | `CTk()`, `CTkLabel`, `mainloop` |
| 2 | Buttons and events | `CTkButton` + `command` callbacks |
| 3 | Inputs — entries and text boxes | `CTkEntry`, text input from the user |
| 4 | Choices — checkboxes, radios, dropdowns | choice widgets |
| 5 | Layouts and frames | `grid`, `CTkFrame` for organized UIs |
| 6 | Putting it together — a complete app | guided build of a real app |
| 7 | Milestone project work day 1 | plan + build |
| 8 | Milestone project work day 2 + demo | finish + showcase |

The Python skills here build on Phase 4's classes (every
widget is a class) and multi-file structure (real apps are
multi-file). What's new is the *event-driven* model — the
program waits for the user, then reacts.

## What you'll build

Smaller widgets-and-callbacks experiments throughout the
phase, then bigger apps:

- **Sessions 1-4:** small examples — counters, greeters,
  forms.
- **Session 5:** an organized multi-frame layout (a
  settings panel, a multi-section form, etc.).
- **Session 6:** a complete app together — a todo list,
  notes app, or simple calculator.
- **Sessions 7-8:** *your* milestone app — your design,
  your code.

## What you'll need

- The same machine as before. **customtkinter** is
  pre-installed on the class machine.
- For working at home, install with:
  ```
  $ pip install customtkinter
  ```
- Thonny still works as your editor.

## How sessions work

Same shape as before:

- **Part A** introduces a new widget or concept with a
  guided exercise.
- **Part B** is open practice or a project.
- **Wrap-up** to share what you did.

## A note about GUI programs

GUI programs are different from the text programs you've
been writing. A GUI program **sits there waiting** for the
user to click a button or type something. When the user
does, the program reacts (runs a callback function). Then it
goes back to waiting.

This is called the **event loop**, and it's a fundamentally
different mental model. You're not writing a sequence of
steps — you're describing widgets and what happens when the
user interacts with each one.

Phase 1's Scratch had something similar (the `when green
flag clicked` and `when sprite clicked` blocks were
events). GUI programming brings that back, this time in real
Python with real windows.

## A note about classes

Per Phase 4 Session 4: "every widget is a class." That's
literally true here. `CTkButton` is a class. `CTkLabel` is
a class. When you write `button = ctk.CTkButton(...)` you're
creating an instance, just like Pet from Phase 4.

Your own apps will often *also* use classes — your code
becomes a class that *contains* widgets. We'll touch this
in later sessions.

## Where to start

[Session 1: Welcome to GUIs](session-01-welcome.md) opens
your first window.

When you're stuck, the [Getting unstuck](../appendices/getting-unstuck.md)
appendix has the checklist. The [Glossary](../appendices/glossary.md)
will grow as Phase 5 introduces new terms.

Welcome to building real desktop apps. Let's go.
