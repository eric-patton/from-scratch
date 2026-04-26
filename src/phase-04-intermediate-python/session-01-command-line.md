## Session 1: The command line — your first `cd`, `ls`, `python`

*Phase 4 — Intermediate Python · Session 1 of 9*

### What we're learning today

Until now, you've run Python by clicking the green button in
Thonny. Today we learn another way: **the command line.** You
open a terminal window, type a command, and the computer does
what you said. By the end of class, you'll be running Python
scripts from the terminal — the way every professional
programmer in the world does it.

### You'll need to remember from last time

- **Thonny** — the editor where you've been writing and
  running Python.
- **The shell** at the bottom of Thonny — where output
  appeared when your programs ran.
- A few of your **own .py files** from earlier sessions —
  we'll run them today.

---

### Part A: Open a terminal

Find the **Terminal Emulator** on your computer. On Linux
Mint XFCE, it's usually:

- Applications menu → System → Terminal Emulator, OR
- Right-click on the desktop → Open Terminal Here

A black (or sometimes white) window opens. There's a blinking
cursor and some text — probably your username and a `$` or
`%` symbol. That's the **prompt.** It's the terminal saying
"type a command."

#### What this is

The terminal lets you talk to your computer **without using
a mouse.** You type a command, press Enter, the computer does
something, and the result shows up in the same window.

The terminal is also called:
- **The command line** (because you type one line at a time)
- **The shell** (because it's a "shell" around the operating
  system)
- **The console**
- **bash** (the specific shell program most Linuxes use)

These all mean roughly the same thing in our class.

#### Your first command — `pwd`

Type `pwd` and press Enter. (Stands for "print working
directory.")

```
$ pwd
/home/your_username
```

It tells you **where you are** in the file system. By
default, you start in your "home" directory.

The `$` is the prompt; you don't type it. Just the `pwd`.
Throughout this chapter, lines starting with `$` are
commands you type; the rest is what the terminal prints back.

#### `ls` — what's here?

Type `ls` (LS — for "list"):

```
$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Videos
```

You see the things in your home directory — folders and files.

Try `ls -la`:

```
$ ls -la
total 96
drwxr-xr-x 18 you you  4096 Apr 25 09:00 .
drwxr-xr-x  3 root root 4096 Apr  1 12:00 ..
drwxr-xr-x  2 you you  4096 Apr 25 09:00 Desktop
...
```

The `-la` is a **flag** — extra options. `-l` means "long
format" (more details). `-a` means "include hidden files"
(files starting with `.`).

Most commands have flags. You don't need to memorize them;
you'll learn the ones you use.

#### `cd` — go somewhere else

`cd` means "change directory." Try:

```
$ cd Desktop
$ pwd
/home/your_username/Desktop
```

You moved to the Desktop folder. Now `ls` shows what's on
the desktop.

To go *back up* to your home directory:

```
$ cd ..
$ pwd
/home/your_username
```

The `..` means "the parent folder." It's a special name that
always means "one level up."

To jump straight back home from anywhere:

```
$ cd
$ pwd
/home/your_username
```

`cd` with no argument always takes you home.

#### Try this on your own

Spend a few minutes navigating around. Try:

- `cd Documents` then `ls`
- `cd Pictures` then `ls`
- `cd ..` to go back
- `cd ../Music` to go up and over

Get comfortable moving around. The terminal is just a way of
walking through your folders.

**Checkpoint:** *You've used `pwd` to see where you are,
`ls` to list files, and `cd` to navigate to a different
folder.* **This is the natural stop point if class is cut
short.**

---

### Part B: Running Python from the terminal

Time for the actual point of all this — running Python
without the green button.

#### Find one of your old programs

You have lots of `.py` files saved from previous sessions —
hangman, the contact book, the text adventure. Pick one.

In the terminal, navigate to the folder where that file is.
For example, if your hangman is in `Documents/python`:

```
$ cd Documents/python
$ ls
hangman.py  notes.txt  words.txt
```

You see your file.

#### Run it

Type:

```
$ python hangman.py
```

(On some systems it's `python3` instead of `python`. Try
`python` first; if "command not found", use `python3`.)

The program runs — same as if you'd hit the green button in
Thonny. Same input, same output, same everything. But now
you're running it from the terminal.

When the program ends, you're back at the `$` prompt, ready
for another command.

#### Why this matters

Three reasons:

1. **No editor required.** You can run a Python script
   anywhere, anytime, without opening Thonny.
2. **Other tools work the same way.** Most professional
   tools (Git, Node.js, web servers, you name it) are
   command-line first. Learning the terminal opens up *all*
   of them.
3. **It's faster.** Once you're used to it, running a
   script with `python myscript.py` is faster than clicking
   through menus.

#### Try a few

Pick three different `.py` files you've written. Navigate to
each and run it from the terminal:

```
$ cd Documents/python
$ python hangman.py
[play hangman]
$ python adventure.py
[explore the adventure]
$ python contacts.py
[manage contacts]
```

This is your new daily workflow.

#### Stretch — useful CLI commands

Some other commands you'll use over and over:

| Command | What it does |
|---|---|
| `mkdir new_folder` | make a new folder |
| `rm filename` | delete a file (be careful — no undo) |
| `cp source destination` | copy a file |
| `mv source destination` | move (or rename) a file |
| `cat filename` | show the contents of a text file |
| `clear` | clear the terminal screen |

Try `cat words.txt` in your hangman folder — your word list
prints out.

Try `mkdir test_folder` then `cd test_folder` then `ls`.

> **Be careful with `rm`.** It's permanent — there's no
> trash can. If you delete a file by accident, it's gone.
> Always look at what you're deleting first.

#### Stretch — `python -i`

`python -i myscript.py` runs your script and then drops you
into an **interactive shell** with all your variables still
defined. Useful for poking at your program after it runs.

#### Extension — make your script feel like a real command

Add this line at the very top of one of your scripts:

```python
#!/usr/bin/env python3
```

(Yes, that exact text — including the `#!`.)

Then in the terminal:

```
$ chmod +x myscript.py
$ ./myscript.py
```

Now you can run it like a normal command. The first line
tells your system "use Python to run this." The `chmod +x`
makes the file *executable.* The `./` says "run this from
the current folder."

This is how real programmers package their tools. Phase 4's
later sessions will use this pattern.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who ran one of your earlier programs from
  the terminal — did it feel different from clicking the
  green button?
- Did anyone get lost in the file system? How did you find
  your way back?
- For the stretch commands — anyone use `mkdir` or `cat`?
  What for?

You learned today the most-used tool in all of professional
programming. **Every developer uses the terminal every day.**
You don't have to like it; you do have to be comfortable with
it.

The terminal is also how you'll use **Git** in a few sessions
— Git is a command-line tool. Today's `cd` and `ls` and
`python` are the foundation; Git's commands will feel natural
once these do.

### If you missed this session

Open a terminal on your computer (Applications → Terminal,
or right-click desktop → Open Terminal). Then:

1. Type `pwd` and press Enter. See where you are.
2. Type `ls`. See what's in this folder.
3. Type `cd Documents` (or wherever your `.py` files are).
   Then `ls` again.
4. Type `python yourfile.py` to run a Python file from the
   terminal.

About 20-30 minutes of practice. The more you use it, the
faster it gets.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- **Tab completion** — start typing a folder or file name,
  press Tab. The terminal completes it for you. Saves a lot
  of typing.
- **Up arrow** — recalls previous commands. Useful for
  re-running something.
- **`history`** — shows your command history.
- **Pipes** — `cat words.txt | wc -l` counts the lines in
  the file. The `|` pipes the output of one command into
  another. Powerful and confusing; mention if curious.
- **Output redirection** — `python myscript.py > output.txt`
  saves the output to a file instead of printing it.

### What's next

Next week we'll learn how to **split a Python program into
multiple files** — because real programs don't fit in one
file. We'll learn how to `import` your own files, just like
you've been importing `random` and `turtle`.
