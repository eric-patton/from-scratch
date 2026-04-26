## Session 5 — Teacher Notes

*Phase 4, Intermediate Python · Session 5 of 9 · Title: Git
— saving versions of your code*

### Purpose of this session

Git is the most important workflow tool in modern programming
after the language itself. Six jobs, in priority order:

1. **Land Git as a real, useful tool.** Many kids will be
   skeptical at first ("why do I need this for my little
   project?"). Lean on the "you can always undo" framing.
2. **Land the four-command loop: status, add, commit, log.**
   ~80% of daily Git usage. Drill until automatic.
3. **Land the three-state model: working tree, staging,
   committed.** The staging area is Git's most-confusing
   feature. Make it concrete with the demos.
4. **Build the commit-as-you-go habit.** Multiple commits
   today, with thoughtful messages, is the goal. Establishes
   the rhythm.
5. **Land `git diff` as a debugging tool.** "What did I
   change?" is a question that comes up constantly.
6. **Set up Session 6 (recovery + branches).** Today's
   foundation makes recovery possible.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with terminal open and Git pre-configured
  (`git config --global user.name`, `user.email`).
- Verify Git is installed on every student machine: `git
  --version`. Should be 2.x. (Pre-installed on Linux Mint.)
- Verify your machine has the Git config set; double-check
  by running `git config --list`.
- Plan to demo Git on the projector — running individual
  commands and pointing at the output is essential.

**Prep time:** ~20 minutes. Test the full demo flow on a
student machine before class. Especially: confirm `git init`
works, the staging-and-commit flow works, etc.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was classes.
  Anyone build something with their own class at home?
- **Part A: setup + first commit** (~45 min) — what Git is
  ~10 min, one-time config ~5 min, create project ~5 min,
  init ~5 min, status/add/commit walkthrough ~15 min,
  checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: iterate** (~30 min) — make a change ~5 min, diff
  ~10 min, commit + iterate ~10 min, log ~5 min.
- **Wrap-up** (~5 min).

If running short, **`.gitignore` and the existing-project
extension can be cut.** The base "init + multiple commits +
log" workflow is the goal.

### Teaching Part A

#### What Git is

Open with the framing:

> "Git is *version control*. Think of it like saving a video
> game — you can save your progress, and if you mess up,
> you can go back to a save point. Git does that for your
> code, with way more power. Every commit is a save point.
> You can have hundreds of save points and look at any of
> them."

The save-points analogy lands well with kids who play games.

Address the "why" explicitly:

> "Why do you need this for a small project? Three reasons.
> One: you'll mess up. Sometimes you'll change something
> and break the program and not remember what you did. Git
> lets you go back. Two: you'll work on bigger projects.
> Multi-file programs with many changes — Git keeps them
> organized. Three: every job that involves writing code
> uses Git. Learning it now means you can join any project
> tomorrow."

#### One-time setup

Walk through `git config --global user.name` and `user.email`
at the projector. Have students do it on their own machines.

Worth pointing out:

> "These get used to label your commits. For local Git, the
> email doesn't have to be real — but use one consistently.
> When we get to GitHub later, you'll want a real email so
> things connect."

Some kids will worry about the "real name" for privacy.
Reassure: this is on their own machine, not shared anywhere
yet.

#### Create the project

Walk through `mkdir`, `cd`, creating `greet.py`. Familiar
terminal moves from Session 1.

#### `git init`

Demo at the projector:

```
$ git init
Initialized empty Git repository in /.../greet/.git/
```

Then `ls -la` to show the `.git` folder appearing.

> "Git made a hidden `.git` folder. That's where it'll
> store all the snapshots and history. *Don't touch it.*
> Git manages it; you manage your own files."

The "don't touch .git" warning is real. Kids who edit files
inside .git can corrupt their repo. Just don't.

#### `git status` — the daily driver

Demo and explain. Point out that Git is **friendly** —
status messages tell you what to do next.

> "When you don't know what's going on, run `git status`. It
> tells you what state your files are in and usually
> suggests the command to use next. It's the friendliest
> command in Git."

This habit is huge. New users panic when they're confused;
status is always the answer.

#### `git add`

The staging-area concept needs explicit treatment. Draw on
the whiteboard or projector:

```
WORKING TREE  →  STAGING  →  COMMITTED
   (edit)       (git add)  (git commit)
```

> "Three places. Working tree is the files you actually
> edit. Staging is a holding area for changes you want to
> include in the next commit. Committed means saved into
> Git's history."

The staging area is genuinely confusing. The "holding area"
mental model helps.

> "Why have a staging area? It lets you make several changes
> and decide which ones to include in a single commit. You
> might change three things, then add only two of them
> because they're related, leaving the third for a
> different commit."

Don't dwell. Most kids will use `git add file` to add the
file and then commit. The fancier uses come later.

#### `git commit`

Demo at the projector. The `-m "message"` is required
syntax (or Git opens an editor, which we don't want).

> "Always include `-m` with a message. Without it, Git tries
> to open a text editor — usually Vim, which is hard to
> exit. Just always do `-m`."

This saves you from the eternal "how do I exit Vim?"
question.

Talk about good commit messages:

> "Describe what changed, in the present tense, in a short
> sentence. 'Add login feature.' 'Fix bug in score
> calculation.' 'Update README.' Future-you will read these
> to understand the project's history."

Bad message examples: `"asdf"`, `"changes"`, `"updates"`,
`"work"`. Good message examples: `"Add greet program"`, `"Fix
typo"`, `"Make name input case-insensitive"`.

#### Status after commit

Demo `git status` after commit. The "working tree clean"
message is satisfying — it confirms everything's saved.

### Teaching Part B

#### Make a change

Have students open `greet.py` in Thonny and modify it. Save.

Then run `git status` again. The "modified" message appears.

> "Git noticed the file changed. But it's not staged yet —
> not ready for commit. We have to add it again."

Worth noting: even tracked files that change have to be
re-added. Each commit is a fresh staging.

#### `git diff`

This is the most useful new command. Demo at the projector:

```
$ git diff
```

The output is initially confusing (the +/- markers, the
@@ section). Walk through:

> "Lines starting with `-` were in the old version,
> removed. Lines starting with `+` are new. Lines without
> marks are unchanged context — Git shows them so you can
> see where the change is in the file."

The header lines (`diff --git`, `index`, `+++`, `---`) are
metadata. Skip them.

> "When you've been coding for an hour and want to remember
> what you changed since the last commit, `git diff`
> answers it. One of the most-used Git commands."

#### Commit and iterate

Have students commit, then make another change, status,
diff, commit. Repeat 2-3 times.

After several iterations, run `git log` and `git log --oneline`.
Show the history.

> "Look at this. Every snapshot you took is in here. You
> could go back to any of them. You could see exactly what
> changed in each one."

The "real history" moment lands here. Several kids will
visibly process this — they have a real, multi-step history
of their project.

#### Stretch — `.gitignore`

Mostly mechanical. Show:

```
# .gitignore
__pycache__/
*.pyc
```

> "Some files shouldn't be tracked. Temporary stuff. Caches.
> Personal secrets. The `.gitignore` file lists patterns
> Git should ignore."

The `.gitignore` topic comes back when kids hit
`__pycache__` (Python's auto-cache folder). Useful to
introduce now.

#### Extension — existing project

Have kids `git init` an old project (their hangman, text
adventure, etc.). One commit for "existing version", then a
small improvement and another commit.

This makes Git feel less like a "new tool just for today" and
more like "something I can use on everything I've built."

### Common stumbles

- **`git config` confusion.** The `--global` flag sets
  config for all repos on this machine. Without `--global`,
  config is per-repo (must be inside a repo). For kids,
  always use `--global`.
- **`fatal: not a git repository`** when running git in a
  non-repo folder. Use `pwd` and `ls -la` to confirm
  you're in the right place. If no `.git` folder, run
  `git init` first.
- **Forgot `-m`** — Git tries to open an editor. On Linux
  Mint that's usually Nano (which is at least exitable
  with Ctrl-X). On other systems it might be Vim (which is
  legendarily hard to exit — `Esc :q!` and Enter).
- **Staged but not committed.** `git status` shows "Changes
  to be committed" — they added but didn't commit yet.
- **Committed but the message was bad.** Messages can be
  changed (`git commit --amend -m "new message"`) but only
  for the most recent commit. Don't dwell.
- **Tried to delete .git folder.** Lost their entire
  history. Recovery is hard. The "don't touch .git"
  warning is real.
- **Working in the wrong folder.** `git status` in the
  parent of their project gives "not a git repository."
  `cd` into the right folder.
- **`git add .` confusion.** The `.` means "all files in
  current directory." Convenient but can add things you
  didn't mean. Mention but encourage `git add filename`
  for clarity.

### Differentiation

- **Younger kids (9-10):** May find Git's vocabulary
  (commit, staging, working tree) overwhelming. Lean on
  the save-point analogy. Simplify to: "edit, add, commit,
  repeat."
- **Older kids (12+):** Will pick up the workflow fast.
  Push them through the iterate-and-diff loop with
  multiple commits.
- **Advanced (any age):** Suggest:
  - `git commit --amend` to edit the last commit
  - `git log --graph` for visual history
  - `git stash` to temporarily set aside changes
  - Aliases for common commands
- **Struggling:** A kid who can't get a basic commit
  through is the kid you focus on. Most common cause:
  forgot `-m`, in the wrong folder, or hit a config issue.
  Walk through.

### What to watch for

- **The "I have a history!" moment** when `git log` first
  shows multiple commits. Affirm.
- **The "git diff is amazing" reaction** when they realize
  they can see exactly what changed. Note who lights up.
- **Buddies trading commit messages.** Encourage —
  especially silly or honest messages ("Fix dumb bug",
  "Make it work better, sort of"). The culture of
  commits is being formed.
- **The "I'm scared I'll break something" reaction.**
  Reassure: "Git is forgiving. We'll learn how to undo
  things next week."

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **Git muscle memory check** — note any kid who's still
  fumbling the basic commit loop; they'll need extra
  support before Session 6.

### Connections forward

- **Session 6 (next week, Git in practice).** Builds on
  today's foundation. Recovery, branches, undo.
- **Session 7 (testing).** Tests are typically committed
  alongside code. Today's commit habit applies.
- **Sessions 8-9 (milestone).** Milestone projects should
  use Git from day one. Today's habit becomes the default.
- **Phase 6 (Pygame).** GitHub introduced. Today's local Git
  becomes shared Git.
- **Every later phase.** Git used throughout. The habit is
  permanent.
- **The peanut butter callback opportunity:** the "wait, I
  forgot to add the file before committing" bug is a
  precision moment. Git did exactly what was asked; you
  said "commit" but didn't say "commit this file"; nothing
  got committed.

### Materials checklist

- [ ] Demo machine with terminal + Git config set
- [ ] Verified Git installed on student machines
- [ ] Whiteboard for the "three states" diagram
- [ ] Projector (essential for showing terminal output)
- [ ] Class roster
