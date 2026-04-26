## Session 6 — Teacher Notes

*Phase 4, Intermediate Python · Session 6 of 9 · Title: Git
in practice — recovering and exploring*

### Purpose of this session

Last week was the basics. This week is the *useful* stuff —
recovery, branches, the things that make Git valuable. Five
jobs, in priority order:

1. **Land "mistakes are recoverable."** This is the
   confidence Git gives you. Once kids feel it, they'll try
   bigger things.
2. **Land `git restore` (and the alternative `git checkout
   -- file`) for working-tree undo.** Most-needed recovery
   tool.
3. **Land `git revert` for committed undo.** Safer than
   `reset --hard`. Establish habit.
4. **Land branches as "alternate timelines."** Conceptually
   tricky but fundamental. Light intro today; serious use
   next week.
5. **Set up the "feature branch" mental model** for
   Sessions 8-9 milestone. Real workflows use this.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with terminal + last week's `version_practice`
  repo (or be ready to create a fresh one).
- Verify branch operations work on your demo machine before
  class.
- Plan to use the projector heavily — branch switching is a
  visual thing.

**Prep time:** ~20 minutes. Practice the branch demo flow
yourself once — switching branches, seeing the file change,
merging.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was Git basics.
  Anyone use Git on their own at home?
- **Part A: undoing** (~40 min) — set up ~5 min, restore for
  working tree ~10 min, restore --staged for staging ~5
  min, revert HEAD ~10 min, recover old file version ~5
  min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: branches** (~35 min) — branch concept ~5 min,
  branch + checkout ~5 min, make changes on branch ~5 min,
  switch back to main ("file changed!") ~10 min, merge or
  delete ~10 min.
- **Wrap-up** (~5 min).

If running short, **the "branches for daily work" extension
can be cut.** The basic create-branch + switch + merge cycle
is the goal.

### Teaching Part A

#### The framing

Open with the most-asked question:

> "The thing every new Git user asks: 'I made a change. It's
> bad. How do I undo it?' The answer depends on where the
> change is — still being edited, staged, or already
> committed. Different undo for each. Today we cover all
> three."

This sets up the three scenarios.

#### Scenario 1: working tree restore

Walk through making a deliberately bad change:

```python
GARBAGE GARBAGE GARBAGE
```

Then `git status` to confirm Git noticed. Then:

```
$ git restore greet.py
```

The file is back to its last-committed state. The garbage is
gone.

> "`git restore` throws away your edits and gives you back
> the file from the last commit. It's permanent — no undo
> for the undo. Be sure before you use it."

The "no undo for the undo" warning is real. Some kids will
restore and then realize they actually wanted those changes.
Too late.

(Older Git versions used `git checkout -- filename` for
this. Mention briefly: "if you see `git checkout` for this in
older tutorials, it's the same idea. We use the newer
`restore` command.")

#### Scenario 2: unstage

Have students make a change, `git add` it, then realize they
didn't want to stage. `git restore --staged filename`
unstages without losing the change.

> "The change is still there in your file — just no longer
> staged for commit. You can stage something else, or
> restore the file entirely if you decide to throw the
> change away."

#### Scenario 3: revert a committed change

Have students make a change, commit it, then decide they
want to undo. Two paths:

**`git revert HEAD`** — creates a new commit that undoes the
old one. Walk through:

```
$ git revert HEAD
[main abc1234] Revert "your message"
```

A new commit appears. The file is back to before the change,
but the history shows both commits — the original and the
revert.

> "This is the safest way to undo. The original commit is
> still in history; we just added a new one that undoes it.
> If you change your mind, you can revert the revert."

**`git reset --hard HEAD~1`** — actually deletes the most
recent commit. Demo briefly with strong warning:

> "This *removes* the commit. Like it never happened. Also
> throws away any uncommitted work. Only use this when
> you're absolutely sure. For most cases, `git revert` is
> safer."

The `HEAD`, `HEAD~1`, `HEAD~2` notation is worth mentioning
once:

> "`HEAD` is the most recent commit. `HEAD~1` is one back.
> `HEAD~2` is two back. Useful for 'undo the last N
> commits.'"

#### Recover an old version of a file

The `git restore --source=abc1234 greet.py` pattern is
useful for "I refactored for hours, want to start over from
yesterday's version."

Walk through:

```
$ git log --oneline greet.py
def5678 Add mood question
abc1234 Initial version

$ git restore --source=abc1234 greet.py
```

The file in your working tree is now the version from
commit `abc1234`. You'd `git status`, then `git add` and
commit if you want to keep that version.

This is genuinely useful and not obvious. Demo carefully.

### Teaching Part B

#### What's a branch

Open with a check:

```
$ git branch
* main
```

> "You've been on the `main` branch the whole time. The
> asterisk shows which branch you're on. A branch is a
> named line of commits. Multiple branches let you have
> multiple versions of your code at once."

Draw a simple diagram on the whiteboard:

```
A — B — C   (main)
        \
         D — E   (experiment)
```

> "Both branches share commits A, B, C. Then they diverge —
> main stays at C; experiment has D and E on top. They're
> two parallel timelines."

#### Create and switch

Walk through:

```
$ git branch experiment       # create branch
$ git branch                  # see all branches
$ git checkout experiment     # switch to it
$ git branch                  # confirm
```

Or the shortcut `git checkout -b experiment` (create + switch
in one).

#### Make changes on the branch

Have students make a deliberately wild change (pirate
greeting, song lyrics, anything). Save. Add. Commit.

#### Switch back to main — the magic moment

```
$ git checkout main
```

Open the file in Thonny. **The wild changes are gone.** The
file is back to what main has.

This is the moment the lesson lands. Several kids will go
"whoa." Affirm:

> "Look. You did all that work on the experiment branch.
> When we switched to main, the file changed. Your
> experiment is still saved on the experiment branch — but
> main is untouched. Two parallel timelines."

#### Switch back to experiment

```
$ git checkout experiment
```

Open the file. The wild version is back.

Switch back and forth a few times. The visceral "the file
changes" is the lesson.

#### Decide: merge or delete

Two paths:

**Merge** to incorporate the experiment into main:

```
$ git checkout main
$ git merge experiment
```

Demo: file now has the experiment's content, even on main.

**Delete** to throw the experiment away:

```
$ git checkout main
$ git branch -D experiment
```

The branch is gone. Its commits are unreachable (technically
still in Git's database for a while, but functionally gone).

> "Make a branch when you want to try something. If it
> works, merge. If not, delete. Either way, main stays
> safe."

#### Full cycle practice

Have students do the full cycle on their own — make a
branch, change something real, decide to merge or delete.
Walk the room and help.

#### Stretch — visualize

`git log --oneline --graph --all` shows the branch tree.
Mostly for kids who like visuals.

#### Extension — feature branch workflow

The "real" workflow:

1. Need to do something? Make a branch.
2. Work on the branch. Commit as you go.
3. When done and tested, merge to main.

> "This is how teams work. Nobody commits directly to
> main. Every change is a branch that gets merged when
> it's ready. Main stays clean and working."

### Common stumbles

- **`git restore` confused with `git restore --staged`.**
  Different things. Restore alone throws away working-tree
  changes. Restore --staged unstages without throwing away.
- **Tried to checkout a branch with uncommitted changes.**
  Git refuses if the changes would conflict. Either
  commit first, stash, or restore.
- **`git branch -d` won't delete unmerged branch.** Says
  "branch is not fully merged." Use `-D` (capital) to force,
  but be sure you want to lose the work.
- **Forgot which branch they're on.** Always `git status`
  or `git branch` to check.
- **Made changes meant for main on a feature branch (or
  vice versa).** Common. Stash, checkout the right branch,
  pop the stash. Or cherry-pick. Don't formally teach;
  fix individually.
- **Merge conflict.** When two branches changed the same
  lines, Git can't auto-merge. The file gets `<<<<<<<`
  markers and they have to manually pick. Don't formally
  teach today; mention as a stretch idea.

### Differentiation

- **Younger kids (9-10):** May find branches confusing. Lean
  on the visual demo of switching and seeing the file
  change. Skip merges if they're struggling — just
  experiment with branch creation and switching.
- **Older kids (12+):** Will pick up branches fast. Push
  through the full cycle and the feature branch workflow
  extension.
- **Advanced (any age):** Suggest:
  - `git stash` for temporarily setting aside changes
  - Multi-branch experiments (3+ branches)
  - Merge conflicts (intentionally cause one and resolve)
  - `git cherry-pick` for moving a single commit between
    branches
- **Struggling:** A kid who can't get the basic restore
  working in Part A is the kid you focus on. Most common
  cause: ran restore in the wrong folder, or forgot the
  filename argument.

### What to watch for

- **The "the file CHANGED!" reaction** when first switching
  branches. The branch concept lands here.
- **Kids who use `git revert` and immediately understand
  why it's safer than `reset --hard`.** Note them — they
  get the "history matters" insight.
- **Buddies trading branch experiments.** Encourage. Real
  workflow practice.
- **Kids panicking about deleting things.** Reassure. With
  Git, almost nothing is truly lost (commits stay in the
  reflog for ~90 days even after branch deletion). But
  `--hard` and `-D` are the dangerous combos.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 7 (next week, testing).** Tests are committed
  alongside code. Today's commit habit applies.
- **Sessions 8-9 (milestone).** Milestone projects use Git
  from day one. Branch for features; commit often. The
  workflow is now in place.
- **Phase 6 (Pygame).** GitHub introduced. Today's local
  branches become collaborative branches with `git push`,
  `git pull`, pull requests.
- **Every later phase.** Git used throughout. Today's
  branching skills mean students can experiment confidently.
- **The peanut butter callback opportunity:** the "deleted
  the wrong file with `git restore`" mistake is a precision
  moment. Git did exactly what was asked; you said
  "restore this file from last commit"; the file now
  matches last commit, including erasing your work.

### Materials checklist

- [ ] Demo machine with terminal + Git repo from last week
- [ ] Whiteboard for the branch diagram
- [ ] Projector (essential for branch switching demos)
- [ ] Class roster
