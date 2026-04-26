## Session 6: Git in practice — recovering and exploring

*Phase 4 — Intermediate Python · Session 6 of 9*

### What we're learning today

Last week you learned the core Git workflow: edit, add,
commit. Today we tackle the *real* questions: **how do I
undo a mistake?**, **how do I see what my code looked like
last week?**, and **how do I try out an experiment without
breaking my main code?** By the end of class, you'll have
recovered a "broken" file from a previous commit and used a
branch to safely experiment with code changes.

### You'll need to remember from last time

- **`git status`** — what's going on right now.
- **`git add`** + **`git commit -m "message"`** — save a
  snapshot.
- **`git log`** — see the history.
- **`git diff`** — see what changed since last commit.
- **The three states** — working tree, staging, committed.

---

### Part A: Undoing mistakes

The most-asked question by new Git users: "I made a change.
It's bad. How do I undo it?"

The answer depends on **where the change is** — working tree,
staging, or committed. Different undo tools for each.

#### Set up: the project

Open a terminal. Find your `version_practice` folder from
last week (or make a fresh one with `git init` and a
`greet.py` file with a few commits — same setup as last
week).

Make sure `git status` shows "working tree clean":

```
$ cd ~/version_practice
$ git status
On branch main
nothing to commit, working tree clean
```

We start clean.

#### Scenario 1: I edited a file and want to throw away the changes

Open `greet.py` in Thonny. Make a deliberately bad change —
delete a line, add some garbage, whatever:

```python
# greet.py
name = input("What's your name? ")
GARBAGE GARBAGE GARBAGE
print(f"Hello, {name}!")
```

Save. Now `git status`:

```
$ git status
On branch main
Changes not staged for commit:
        modified:   greet.py
```

You changed it but haven't staged or committed. To **throw
away** these changes and go back to the last committed
version:

```
$ git restore greet.py
```

Open the file in Thonny. The garbage is gone. The file is
back to what it was at the last commit.

> **Be careful with `git restore` (or its older cousin `git
> checkout -- file`).** It *throws away* your changes
> permanently. There's no undo. Use it only when you're
> sure you want to lose the changes.

#### Scenario 2: I staged a change but want to unstage it

Make a small change to `greet.py` and *stage* it:

```
$ git add greet.py
$ git status
Changes to be committed:
        modified:   greet.py
```

Wait — you wanted to stage something else first. To
**unstage** without losing the change:

```
$ git restore --staged greet.py
$ git status
Changes not staged for commit:
        modified:   greet.py
```

The change is still there in your working tree, but no
longer in staging. Now you can stage what you actually
wanted, or `git restore greet.py` to throw away the change
entirely.

#### Scenario 3: I committed something, want to back up

Hardest case. You already committed. Two main options:

**a) Make a new commit that undoes the last one** — safest:

```
$ git revert HEAD
```

This creates a *new* commit that undoes whatever the most
recent commit did. The history shows both the original and
the undo. Safe because you don't lose any history.

`HEAD` is Git's name for "the most recent commit." `HEAD~1`
is "one before that," `HEAD~2` is "two before that," etc.

**b) Actually delete the last commit** — risky:

```
$ git reset --hard HEAD~1
```

This *removes* the most recent commit and resets your files
to the previous one. Like the commit never happened.

> **`git reset --hard` is dangerous.** It loses commits *and*
> any uncommitted work. Only use when you're sure. For most
> situations, `git revert` is safer.

#### Recovering an old version of a file

Sometimes you don't want to undo a commit — you just want to
get the old version of *one specific file*:

```
$ git log --oneline greet.py
def5678 Add mood question
abc1234 Initial version
```

To pull `greet.py` from a specific commit into your working
tree:

```
$ git restore --source=abc1234 greet.py
```

Now `greet.py` matches what it was in commit `abc1234`. The
file is changed in your working tree (you'd `git status`,
then `git add` and `git commit` to make it official).

This is useful when you've been refactoring for hours and
want to start over from a known-good state.

**Checkpoint:** *You've used `git restore` to undo at least
one type of change (working tree, staged, or pulling an old
version of a file).* **This is the natural stop point if
class is cut short.**

---

### Part B: Branches — alternate timelines

Branches let you **experiment without affecting your main
code.** You make a branch, mess around on it, and either keep
the changes or throw them away — without touching the main
version.

This sounds abstract; the demo makes it concrete.

#### What's a branch?

You've actually been on a branch the whole time. Run:

```
$ git branch
* main
```

You're on the `main` branch. The asterisk shows which one.

A branch is a **named line of commits** — a separate history
that diverged from another branch at some point. By default,
all your work has been on `main`.

#### Make a new branch

Suppose you want to try a big change to `greet.py` but don't
want to mess up your main version. Make a branch to try it
on:

```
$ git branch experiment
$ git branch
  experiment
* main
```

You created a branch called `experiment` but you're still on
`main`. Switch to it:

```
$ git checkout experiment
Switched to branch 'experiment'
$ git branch
* experiment
  main
```

Now you're on `experiment`. Any commits you make here go to
the `experiment` branch, not `main`.

(There's a shortcut: `git checkout -b experiment` creates and
switches to a new branch in one step.)

#### Make experimental changes

Open `greet.py` in Thonny. Make a wild change — translate
the prompts to pirate-speak, or add a song lyric, or ask
seventeen questions, or whatever:

```python
# greet.py — experimental pirate version
name = input("Yarrr! What be yer name? ")
print(f"Ahoy, {name}! Welcome aboard, matey!")
```

Save. Status:

```
$ git status
On branch experiment
Changes not staged for commit:
        modified:   greet.py
```

You're on `experiment`. Add and commit:

```
$ git add greet.py
$ git commit -m "Pirate-themed greeting"
```

#### Switch back to main

Now switch to `main`:

```
$ git checkout main
$ git branch
  experiment
* main
```

Open `greet.py` in Thonny. **Your pirate changes are gone.**
The file is back to what it was on `main`. Your experiment
is safe on the `experiment` branch — but `main` is unchanged.

This is the magic of branches. **Each branch has its own
files.** Switching branches changes what's in your working
tree.

#### Switch back to experiment

```
$ git checkout experiment
```

Open `greet.py`. The pirate version is back.

Switch to main, switch to experiment, switch back. The file
changes each time. Two parallel "alternate timelines" of
your project, each with its own state.

#### Decide what to do

Two outcomes:

**You like the experiment** and want it on main:

```
$ git checkout main
$ git merge experiment
```

`git merge experiment` brings the `experiment` branch's
changes into `main`. Now `main` has the pirate version too.
The experiment "succeeded" and got promoted.

**You hate the experiment** and want to abandon it:

```
$ git checkout main
$ git branch -D experiment
```

`git branch -D experiment` *deletes* the experiment branch.
Its commits are gone. `main` is untouched.

(Note the capital `-D`. Lowercase `-d` only deletes branches
that have already been merged. Capital `-D` deletes anything,
including unmerged work. Use carefully.)

#### Try the full cycle

Set up another experiment. This time, pick a real
improvement you'd want to make to your program. Maybe:

- Add input validation
- Try a different greeting style
- Add a `try/except` for robustness
- Refactor into functions

Branch:

```
$ git checkout -b improve-greeting
```

Make your changes. Commit them on the branch. Test them.

Like the result? Merge to main:

```
$ git checkout main
$ git merge improve-greeting
$ git branch -d improve-greeting
```

Don't like it? Throw it away:

```
$ git checkout main
$ git branch -D improve-greeting
```

That's the **base goal** — you've made a branch, made
changes on it, and either merged or discarded.

#### Stretch — visualize branches

`git log --oneline --graph --all` shows all branches as a
visual tree:

```
$ git log --oneline --graph --all
* abc1234 (experiment) Pirate-themed greeting
| * def5678 (HEAD -> main) Add mood question
|/
* 123abcd Initial version
```

The lines and asterisks show the branching. Useful when you
have multiple branches.

#### Extension — branches for daily work

Real workflow: don't work directly on `main`. For every
feature or experiment, make a branch. Work there. When it's
done and tested, merge to `main`.

This keeps `main` always in a working state. Try it for a
week:

- Need to add a feature? `git checkout -b add-feature-name`.
- Done? Test, then merge to main.
- Discovered a bug? `git checkout -b fix-bug-name`. Fix it.
  Test. Merge.

Real teams use this exact pattern (often called "feature
branch workflow"). You're using professional practices.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who used `git restore` — was it scary to
  throw away changes? Did it work as expected?
- For the kids who made a branch — was it weird to see the
  file change when you switched branches?
- For the kids who merged — did the merge work the first
  time, or did anything go wrong?

You learned today the **safety net** of professional
programming. **Mistakes are recoverable.** Experiments are
isolated. The main version is always intact unless you
deliberately change it. This is what gives professional
developers the confidence to try things — they know the worst
case is "throw it away."

Three big takeaways:

1. **`git restore`** undoes uncommitted changes (use carefully).
2. **`git revert`** safely undoes a committed change (creates
   a new commit; doesn't lose history).
3. **Branches** let you experiment without affecting `main`.

Combined with last week's commit basics, that's enough Git
to handle most real-world situations.

### If you missed this session

You need a Git repository (your `greet` project from last
week, or a fresh one). Then:

1. Make a change to a file. Try `git restore filename` to
   throw it away.

2. Make another change, `git add` it. Try `git restore
   --staged filename` to unstage.

3. Make and commit a change you'll want to undo. Try `git
   revert HEAD` to create an undoing commit.

4. Make a branch with `git checkout -b experiment`. Make
   changes, commit. Switch back with `git checkout main`.
   Notice the file changes.

5. Either merge with `git merge experiment` or delete with
   `git branch -D experiment`.

About 40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- **`git stash`** — temporarily set aside uncommitted
  changes. Useful when you need to switch branches but have
  unsaved work.
- **Conflict resolution** — when you merge two branches that
  changed the same lines, Git sometimes can't auto-merge.
  You have to resolve the conflict by hand. Genuinely
  tricky; a real-world Git skill.
- **`.gitconfig` aliases** — `git config --global alias.co
  checkout` makes `git co` mean `git checkout`. Tons of
  good aliases on the internet.
- **`git blame filename`** — shows who last changed each
  line of a file (and in which commit). Useful for "wait,
  who wrote this code?"
- **`git tag v1.0`** — name a specific commit (like a
  release). Tags are fixed labels; branches move as you
  commit.

### What's next

Next week we learn about **testing** — `assert` statements
and simple test functions that verify your code does what
you think. After that, you'll plan and build your milestone
project using *all* the Phase 4 tools — multi-file structure,
Git tracking, tests verifying your work. Real
software-engineering muscle.
