# Glossary

Programming words, in plain language. New words get added as they
come up in chapters. If a word here doesn't make sense yet, don't
worry — it'll show up in a session and click into place.

Words from later phases (web, etc.) get added when those phases
start. So far this glossary covers Phase 1 (Scratch) and Phase 2
(Python with Turtle).

---

## Phase 1 — Scratch words

**Block**
The colorful pieces you snap together in Scratch. Each block is
one instruction (`move 10 steps`, `wait 1 seconds`, etc.). Blocks
have shapes that fit together — that's how Scratch tells you what
goes where.

**Conditional**
A programming idea: "if something, then do this." In Scratch, the
`if` block. The "if" part is a question Scratch can answer with
yes or no. If the answer is yes, the inside runs. If no, it
doesn't.

**Costume**
A different look for a sprite. Many sprites have multiple costumes
built in (like a cat with two different walking poses). Switching
costumes is how sprites animate.

**Event**
A thing that happens *while* a program is running — a key being
pressed, a sprite being clicked, the green flag being clicked.
Each event can trigger a script to run. Sprites can have many
scripts, each listening for a different event.

**Extension**
An extra category of blocks you can add to Scratch. The most
useful one for Phase 1 is **Pen**, which lets sprites draw lines
as they move. Add an extension by clicking the "Add Extension"
button at the bottom-left of the Scratch window.

**Forever**
A loop that runs its inside over and over until you click the red
stop sign. Used a lot in games — "every fraction of a second,
check the keyboard and update the cat's position."

**If block**
The Scratch block that does conditional logic. Has a diamond-
shaped slot at the top (for the question) and a mouth (for what to
do if the answer is yes).

**Loop**
A way to do something multiple times without writing it multiple
times. Scratch has `repeat N` (do this N times) and `forever` (do
this until I stop you).

**Mouth**
The opening in some Scratch blocks (like `repeat`, `forever`, and
`if`) where other blocks go *inside*. Things in the mouth run as
part of the outer block.

**Pen**
A Scratch extension that lets sprites draw as they move. `pen
down` starts drawing; `pen up` stops. Used in Session 3 to draw
shapes.

**Script**
A stack of blocks that runs together, starting from the top
(usually a "starter" block like `when green flag clicked` or
`when [key] pressed`). One sprite can have many scripts; each one
runs when its starter block triggers.

**Sensing**
A category of Scratch blocks that *check* things in the world —
"is the space key pressed?", "am I touching another sprite?",
"what's the mouse pointer's x position?" Sensing blocks usually go
inside `if` blocks.

**Sequence**
A series of blocks that run one after another, top to bottom. The
most basic kind of program. Order matters.

**Sprite**
A character or object on the Scratch stage. The default sprite is
the orange cat. Sprites have their own scripts, costumes, and
position on the stage.

**Stage**
The big rectangle in Scratch where sprites do their thing. The
stage has a coordinate system: x goes left/right, y goes up/down,
and (0, 0) is the middle. The stage is about 480 wide × 360 tall.

**Variable**
A labeled box that holds a value (usually a number). You can put
something in (`set`), change what's in it (`change`), and read it
back (`(varname)`). Used for things that change over time, like a
score. Created with the "Make a Variable" button in the Variables
category.

**X position / Y position**
Where a sprite is on the stage. X is left-right (negative is left,
positive is right). Y is up-down (negative is down, positive is
up). The middle of the stage is x = 0, y = 0.

---

## Phase 2 — Python words

**Argument**
A value you pass to a function when you call it. In
`t.forward(100)`, the `100` is an argument — it's the
information the function uses. (See also: parameter.)

**Comment**
Text starting with `#` that Python ignores. Used to leave notes
in your code for yourself or other readers — like a label on a
section of code. Comments don't change what the program does.

**Elif**
Short for "else if." A way to check another condition after an
`if`'s condition was false. You can chain as many `elif`s as you
want before a final `else` (or no `else` at all).

**Else**
The "otherwise" part of an `if`. The body under `else` runs when
the `if`'s condition is false. Optional — you don't always need
one.

**Error message**
What Python tells you in red text when something goes wrong.
Error messages are *trying to help.* They usually tell you the
file, the line number, and what kind of problem (`SyntaxError`,
`NameError`, `AttributeError`, etc.). Read them slowly.

**Float**
A number with a decimal point, like `5.0` or `3.14`. Division
in Python (`/`) always gives a float, even when the answer is
whole (`15 / 3` is `5.0`, not `5`).

**For loop**
The Python version of Scratch's `repeat`. `for i in range(N):`
runs the indented body N times. The `i` is a loop variable that
takes the values 0, 1, 2, ..., N-1.

**Function**
A named chunk of code you can call by name. You define it with
`def name():` and the indented body underneath. You call it by
writing `name()` somewhere later. The biggest new idea in
Phase 2.

**IDE**
Short for **Integrated Development Environment.** A program for
writing code. Thonny is an IDE. So are VS Code, PyCharm, and
many others. We use Thonny in this class.

**Import**
A Python statement that brings in a *module* (a toolbox of code
written by someone else) so you can use it. `import turtle`
brings in the turtle module so you can do `t = turtle.Turtle()`.

**Indentation**
Spaces at the start of a line. In Python, indentation is part
of the grammar — it's how Python knows which lines belong inside
a `for` loop, `if`, `def`, etc. Lines indented underneath are
"inside"; lines not indented are "outside." Standard is 4
spaces.

**Module**
A bundle of Python code you can `import` and use. Comes from
Python's standard library (like `turtle`) or from the internet
(like Pygame, later in the class). Sometimes also called a
**library**.

**Operator**
A symbol that does something. Math operators: `+ - * /`.
Comparison operators: `< > == != <= >=`. The `=` sign is the
*assignment* operator (gives a variable a value).

**Parameter**
A placeholder name in a function definition. In
`def draw_square(size):`, `size` is the parameter. When you call
the function with `draw_square(50)`, the parameter `size` gets
the value `50` for that call. (See also: argument.)

**Print**
A Python function (`print(...)`) that displays text or values in
the shell. Useful for showing output to the user, and especially
useful for debugging — `print(size)` shows what `size` is right
now.

**Python**
The programming language we use after Scratch. Real,
general-purpose, used by professional developers, scientists,
data analysts, web developers — almost everyone. We use it
through Thonny.

**range**
A built-in Python function that gives a sequence of numbers.
`range(5)` is the numbers 0, 1, 2, 3, 4. Almost always used
inside a `for` loop: `for i in range(5):` runs five times.

**Run**
To execute your program. In Thonny, click the green Run button
or press F5. Python reads your code top to bottom and does what
it says.

**Save**
To write your code to a file on your computer. Files end in
`.py`. Save before you Run, or Thonny will sometimes complain.
Use Ctrl-S as a shortcut.

**Shell**
The bottom panel of Thonny. Where Python prints messages, where
errors appear, and where you can type one-line Python
experiments interactively (without saving a file).

**SyntaxError**
A Python error that means "your code's grammar is wrong."
Usually a missing colon, missing parenthesis, or wrong
indentation. Python points at where it noticed the problem
(which is sometimes a line *after* the actual mistake).

**Thonny**
The Python editor we use in class. Has an editor (top), a shell
(bottom), and a green Run button. Pre-installed on every class
machine.

**Turtle**
The Python module we use in Phase 2 to draw on the screen.
Imported with `import turtle`. The turtle is a little arrow
(or actual turtle shape) that moves around drawing lines.

---

## General programming words

**Bug**
A mistake in code that makes it do the wrong thing. Named after a
real moth that got stuck in an early computer in 1947 and stopped
it from working.

**Code**
A general word for "instructions you wrote for the computer."
Scratch blocks are code. Python lines are code. HTML tags are
code.

**Debugging**
Fixing bugs. Half of programming.

**Program**
A complete set of instructions that does something. Your Scratch
projects are programs. So is every app on your phone.

**Programmer**
A person who writes programs. Also: you, after about three weeks
of class.

---

*This glossary will grow as the curriculum moves into Python and
beyond. If a word should be here and isn't, ask Mr. Eric to add it.*
