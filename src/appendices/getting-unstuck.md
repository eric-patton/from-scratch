# Getting unstuck

Stuck is normal. Programmers spend most of their day stuck. The
skill isn't avoiding stuck — it's *getting unstuck*. This page is
the checklist you come back to whenever your code isn't doing what
you want.

Work through the steps in order. Don't skip ahead. Most of the
time, you'll fix the problem before you reach the end of the list,
because the act of working through the steps *is* the fix.

## Step 1: Read what you wrote, slowly

Before anything else, look at your code. Actually look at it.
Read each block (or each line, in Python) out loud if you can.

Programmers — especially programmers who are starting out — often
*think* they wrote one thing and *actually* wrote something else.
Reading slowly catches the gap.

Specifically: did you tell the computer the *exact* thing you
meant? Or did you tell it something close-ish?

> Remember the peanut butter problem from Session 1. The computer
> doesn't guess. It does what you said, even when what you said is
> wrong.

About half the time, reading slowly fixes the problem.

## Step 2: Read the error message (when there is one)

In Scratch you don't usually get error messages — things just don't
work. But once you're in Python, error messages are everywhere, and
they are almost always *trying to help*.

Find the error message. It probably has a few parts:

- **The file name** where the problem is.
- **The line number** where the problem is.
- **What kind of problem** (a name like `SyntaxError`, `TypeError`,
  `NameError`, etc.).
- **A short description** of what went wrong.

Read all of it. The most useful part is usually the **last line**
of the error.

If the error message uses a word you don't recognize — like
`indentation` or `attribute` or `iterable` — that's a real clue.
Look it up.

## Step 3: Narrow it down

When something doesn't work, your goal is to figure out *which
part* doesn't work. Usually it's not the whole program. Usually
it's one specific block or one specific line.

Two ways to narrow down:

- **Comment things out.** If your program does five things and one
  of them is broken, temporarily turn off four of them and see if
  the broken one still happens. (In Scratch, you can right-click a
  block and "Disable Block" to turn it off without deleting it.)
- **Add a `say` block (Scratch) or a `print()` (Python) at
  different points in your program.** If the message shows up,
  that part of the code ran. If it doesn't show up, the problem is
  somewhere before that point.

This is called **bisecting** — cutting the problem in half over
and over until you find the broken part.

## Step 4: Rubber-duck it

Find a friend, your buddy, your dog, or — yes — a literal rubber
duck. Explain what your program is *supposed* to do, step by step,
out loud.

Often, partway through explaining, you'll catch the bug yourself.
Saying it out loud forces your brain to think about it differently.

Programmers do this so often there's a name for it: **rubber-duck
debugging.** The duck doesn't have to understand. You're not
explaining it to the duck — you're explaining it to *yourself, with
the duck listening.*

## Step 5: Look at how you did this before

If you've done something similar in a past session and it worked,
**look at how you did it before.** Open the textbook chapter, look
at the code. Often, your current problem is the same shape as a
problem you already solved.

This is one of the highest-leverage moves in programming. Real
programmers do this all day long — they look at their old code,
or a coworker's old code, and adapt it to the current problem.
Copying-and-modifying is fine. *Copying without understanding* is
not.

(That's the explain-how-it-works rule — if you copy something, you
have to be able to explain it. Otherwise, you're not done.)

## Step 6: Ask your buddy

If you've worked through steps 1-5 and you're still stuck, ask
your buddy.

Explain to them what you're trying to do, what you've tried, and
what's not working. They might see something you missed. Or they
might be stuck on the same kind of problem and you can figure it
out together.

## Step 7: Ask Mr. Eric

Your buddy is your first line of help. Mr. Eric is your second.

When you ask Mr. Eric, **tell him what you've already tried.** This
isn't a rule for his benefit — it's a rule for yours. If you can
say "I tried X and Y and Z and none of them worked," you've already
done most of the thinking work. Often, telling him what you tried
is when you figure it out.

## Step 8: Take a break

If you've been stuck for more than about 20 minutes, your brain is
tired. Get some water, walk around for two minutes, look out a
window. Then come back.

This is not goofing off. This is one of the most-used techniques of
professional programmers. Brains find solutions when you stop
pushing them. Try it.

## What stuck *isn't*

A few things that feel like being stuck but aren't:

- **Frustration.** Frustration is normal but it isn't a clue. The
  bug doesn't care that you're frustrated. Take a breath, go back
  to step 1.
- **"It's broken."** "It's broken" isn't useful information. *What
  exactly* is broken? *What did you expect it to do?* *What did it
  actually do?* Force yourself to be specific. Half the time,
  forcing yourself to be specific is when you find the bug.
- **"I'm not smart enough for this."** No. You just haven't found
  it yet. Every programmer who has ever lived has felt this. They
  kept going. The feeling passes.

## The big idea

Getting unstuck is a *skill*, not a talent. You get better at it
the same way you get better at anything: by doing it, over and
over, until your brain learns the moves.

Every time you fix a bug, you're a slightly better programmer than
you were before. Every time. That's the whole job.
