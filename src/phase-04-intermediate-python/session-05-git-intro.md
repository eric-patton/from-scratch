## Session 5: Git — saving versions of your code

*Phase 4 — Intermediate Python · Session 5 of 9*

### What we're learning today

Today we meet **Git** — the most important tool in modern
programming after the language itself. Git is a tool that
**saves versions** of your code as you work. Every time you
make a change worth keeping, you commit it. Later, if you
break something, you can go back. If you want to know what
changed yesterday, Git tells you. By the end of class, you'll
have a project with Git tracking it, several commits in its
history, and the ability to see exactly what changed at each
step.

### You'll need to remember from last time

- **The terminal** — this entire session is in the terminal.
  `cd`, `ls`, `python script.py`.
- **Multi-file projects** — Git tracks folders of files.
- **Editing files** — your normal Thonny workflow.

---

### Part A: What Git is and your first commit

#### What Git is

Git is **version control** — a system for saving snapshots of
your project as it changes over time. Think of it like the
"undo" history in a word processor, but way more powerful:

- Save snapshots whenever you want, with a message describing
  what you changed.
- Look back at any past snapshot — see what your code looked
  like a week ago.
- Compare two snapshots to see exactly what changed.
- Recover from mistakes — undo bad changes by going back to
  a known-good snapshot.

Git is what every professional programmer uses, every day, on
every project. It's not optional in the real world — and once
you've used it, you'll never want to work without it.

In this session and the next, we use Git **locally** — just
on your own machine, just for you. In Phase 6 we'll connect
to **GitHub** (the website where programmers share Git
projects), but that's not today.

#### One-time setup

Git needs to know who you are so it can label your commits.
Open a terminal and run these two commands (with your real
name and any email — for local-only Git, the email doesn't
have to be real, but use one consistently):

```
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
```

You only do this once, ever, on this machine. Git remembers.

To check it worked:

```
$ git config --global user.name
Your Name
$ git config --global user.email
you@example.com
```

#### Create a project to track

Open a terminal. Make a new folder for today's work:

```
$ cd ~                          # go home
$ mkdir version_practice
$ cd version_practice
$ pwd
/home/your_username/version_practice
```

Create a Python file. Open Thonny, type something simple,
save it as `greet.py` in the new folder:

```python
# greet.py
name = input("What's your name? ")
print(f"Hello, {name}!")
```

Save. Confirm in the terminal:

```
$ ls
greet.py
```

The folder has one file.

#### `git init` — start tracking

Tell Git to start tracking this folder:

```
$ git init
Initialized empty Git repository in /home/.../version_practice/.git/
```

Git created a hidden folder called `.git` inside your
project. That's where it'll store all the snapshots and
history. **Don't touch the `.git` folder.** Git manages it.

```
$ ls -la
total 16
drwxrwxr-x 3 you you 4096 Apr 25 14:00 .
drwxr-xr-x 4 you you 4096 Apr 25 14:00 ..
drwxrwxr-x 7 you you 4096 Apr 25 14:00 .git
-rw-rw-r-- 1 you you   76 Apr 25 14:00 greet.py
```

The `.git` folder shows up only with `ls -la` (because it's
hidden). It's the entire Git database for this project.

This folder is now a **Git repository** (or "repo" for
short). Every project tracked by Git is a Git repository.

#### `git status` — what's going on?

The most-used Git command. Run it any time to see what Git
thinks about your files:

```
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        greet.py

nothing added to commit but untracked files present (use "git add" to track)
```

Translation: "You're on the `main` branch. You have one file
that Git knows exists but isn't tracking yet. To track it,
use `git add`."

Notice Git is *helpful* — it tells you what to do next.

#### `git add` — stage a file for committing

Tell Git you want to include `greet.py` in the next snapshot:

```
$ git add greet.py
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   greet.py
```

Now `greet.py` is **staged** — ready to be included in a
commit. It's not committed yet; just *prepared* to be.

The "staging area" is one of Git's quirks. Files go through
three states:

1. **Working tree** — the actual files you're editing.
2. **Staging area** — files you've said "include this in the
   next snapshot."
3. **Committed** — saved as part of the project's history.

`git add` moves files from working tree to staging.

#### `git commit` — save the snapshot

```
$ git commit -m "Initial version of greet program"
[main (root-commit) abc1234] Initial version of greet program
 1 file changed, 2 insertions(+)
 create mode 100644 greet.py
```

You just made your first commit! Git saved a snapshot of
your project at this moment.

The `-m "..."` is the **commit message** — a short
description of what changed. Always include one. Future-you
(or any teammate) will read these messages to understand
the project's history.

> **Good commit messages.** Describe *what changed* in the
> present tense. "Add greet program," "Fix typo in
> instructions," "Make name input case-insensitive." Short
> and specific.

Now check status again:

```
$ git status
On branch main
nothing to commit, working tree clean
```

Translation: "Your working tree matches the latest commit.
Nothing has changed since."

**Checkpoint:** *You've initialized a Git repository, added a
file, made your first commit, and seen `git status` confirm
that everything's clean.* **This is the natural stop point if
class is cut short.**

---

### Part B: Iterate and track changes

A single commit doesn't show much. Let's make several
commits over time and watch the history grow.

#### Make a change

Open `greet.py` in Thonny and add a feature — maybe ask for
the user's mood:

```python
# greet.py
name = input("What's your name? ")
mood = input("How are you feeling? ")
print(f"Hello, {name}! Glad you're feeling {mood}.")
```

Save.

#### `git status` again

```
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   greet.py

no changes added to commit but untracked files present (use "git add" to track)
```

Git noticed `greet.py` changed. It's "modified" but not
staged.

#### `git diff` — see what changed

```
$ git diff
diff --git a/greet.py b/greet.py
index abc1234..def5678 100644
--- a/greet.py
+++ b/greet.py
@@ -1,2 +1,3 @@
 name = input("What's your name? ")
-print(f"Hello, {name}!")
+mood = input("How are you feeling? ")
+print(f"Hello, {name}! Glad you're feeling {mood}.")
```

This is a **diff** — a view of the differences between the
file as it is now and the file as it was in the last commit.
Lines starting with `-` were removed; lines starting with `+`
were added. Lines without those marks were unchanged.

`git diff` is one of the most-used Git commands once you're
working on real projects. "What did I change since last
commit?" → `git diff`.

#### Commit the change

```
$ git add greet.py
$ git commit -m "Ask the user about their mood"
[main def5678] Ask the user about their mood
 1 file changed, 2 insertions(+), 1 deletion(-)
```

Now you have *two* commits in your history.

#### Make a few more changes

Iterate a few times. Each time:

1. Make a change in Thonny.
2. Save.
3. `git status` to see what changed.
4. `git diff` to see the actual differences.
5. `git add` to stage.
6. `git commit -m "..."` with a clear message.

Examples of changes you could make:

- Add a third question (favorite color, favorite food).
- Validate the input (no empty answers).
- Print multiple lines of output.
- Use `if/else` to give different greetings based on mood.

Make at least three more commits. You'll have a real history
to look at.

#### `git log` — see the history

```
$ git log
commit def567...
Author: Your Name <you@example.com>
Date:   Wed Apr 25 14:32:18 2026

    Add a third question

commit abc234...
Author: Your Name <you@example.com>
Date:   Wed Apr 25 14:25:00 2026

    Ask the user about their mood

commit 123abc...
Author: Your Name <you@example.com>
Date:   Wed Apr 25 14:20:00 2026

    Initial version of greet program
```

Each commit shows:

- A unique ID (the long hex string)
- Who made it (you)
- When
- The message you wrote

Newest commits are at the top.

A useful one-line variant:

```
$ git log --oneline
def5678 Add a third question
abc2345 Ask the user about their mood
123abc4 Initial version of greet program
```

Compact view. Just the IDs (shortened) and messages. Most
useful for quick "what's in this project's history?"

That's the **base goal** for today — a project tracked by
Git, with several commits showing the project's evolution
over time.

#### Stretch — log with diffs

`git log -p` shows each commit *with* its diff:

```
$ git log -p
```

Press `space` to scroll, `q` to quit. Now you can see
every change in every commit.

#### Stretch — `.gitignore`

Some files shouldn't be tracked by Git — temporary files,
caches, secrets. Create a file called `.gitignore` in your
project folder:

```
# .gitignore — files Git should ignore
__pycache__/
*.pyc
secrets.txt
```

Each line is a pattern. `__pycache__/` ignores a folder Python
sometimes creates. `*.pyc` ignores compiled Python files.
`secrets.txt` ignores a specific file.

Now `git status` won't bug you about those files even if
they exist in your folder.

Most real projects have a `.gitignore`. The
[github.com/github/gitignore](https://github.com/github/gitignore)
repo has templates for common languages.

#### Extension — track an existing project

Pick a project from a previous session (your text adventure,
your hangman, anything). Initialize Git in its folder. Make
a first commit ("Existing project as of today"). Then make a
small improvement, commit. Make another, commit.

Now even your old projects have version history. From now
on, *every* project you work on can use Git.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the greet program — what's the
  weirdest commit message you wrote?
- For the kids who used `git diff` — was it useful to see
  exactly what you changed?
- For the kids who tried `.gitignore` — what did you ignore?

You learned today the foundation of professional version
control. **Every commit is a permanent snapshot.** You can
always go back. You can always see what changed. You can
work confidently because mistakes are recoverable.

The four commands you'll use the most:

- `git status` — what's going on?
- `git add filename` — stage a file
- `git commit -m "message"` — save the snapshot
- `git log --oneline` — see the history

Memorize that loop. You'll use it every day.

Next week we go further — recovering from mistakes, looking
at old versions, and lightly touching branches.

### If you missed this session

You need a terminal and Git installed (it's pre-installed on
your class machine). Then:

1. Run the one-time setup:
   ```
   $ git config --global user.name "Your Name"
   $ git config --global user.email "you@example.com"
   ```

2. Create a folder, put a Python file in it.

3. In the folder:
   ```
   $ git init
   $ git status
   $ git add yourfile.py
   $ git commit -m "Initial version"
   ```

4. Make some changes, repeat steps 2-4 a few times.

5. Run `git log --oneline` to see your history.

About 40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- **`git log --graph`** shows commits in a visual tree.
- **`git show <commit-id>`** shows the details of a specific
  commit (use the short ID from `git log --oneline`).
- **`git diff --staged`** shows what's about to be
  committed (already staged but not yet committed).
- **`git commit -am "message"`** combines `git add` and `git
  commit` for already-tracked files (won't add new files
  though).
- **Aliases** — Git lets you create shortcuts. `git config
  --global alias.s status` makes `git s` mean `git status`.

### What's next

Next week we use Git for the things people *really* care
about: **recovering from mistakes**, looking at old versions,
and using **branches** to try out experiments without
breaking your main code. The full Git workflow.
