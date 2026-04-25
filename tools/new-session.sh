#!/usr/bin/env bash
#
# new-session.sh — scaffold a new session's three artifacts
#
# Creates:
#   src/phase-XX-name/session-NN-name.md       (student handout)
#   teacher/phase-XX-name/session-NN-notes.md  (teacher notes)
#   code/phase-XX-name/session-NN-name/{starter,exercises,solutions}/
#   assets/phase-XX-name/session-NN/
#
# Refuses to overwrite existing files. Reminds you to update
# src/SUMMARY.md afterward.

set -euo pipefail

usage() {
    cat <<'USAGE'
Usage: tools/new-session.sh <phase-num> <phase-name> <session-num> <session-name> [title]

Arguments:
  phase-num     2-digit phase number, e.g. 01
  phase-name    kebab-case phase name, e.g. scratch
  session-num   2-digit session number, e.g. 03
  session-name  kebab-case session name, e.g. loops
  title         (optional) human-readable title for the session.
                Defaults to "TODO: session title goes here".

Example:
  tools/new-session.sh 01 scratch 03 loops "Loops: doing things over and over"

After running, add the new session to src/SUMMARY.md under the
appropriate phase header.
USAGE
    exit 1
}

[ "$#" -ge 4 ] || usage

PHASE_NUM="$1"
PHASE_NAME="$2"
SESSION_NUM="$3"
SESSION_NAME="$4"
TITLE="${5:-TODO: session title goes here}"

# Validate the numeric arguments are exactly 2 digits.
case "$PHASE_NUM" in
    [0-9][0-9]) ;;
    *) echo "Error: phase-num must be 2 digits (e.g. 01), got: $PHASE_NUM" >&2; exit 2 ;;
esac
case "$SESSION_NUM" in
    [0-9][0-9]) ;;
    *) echo "Error: session-num must be 2 digits (e.g. 03), got: $SESSION_NUM" >&2; exit 2 ;;
esac

# Validate kebab-case names (lowercase letters, digits, hyphens only).
case "$PHASE_NAME" in
    *[!a-z0-9-]*|"") echo "Error: phase-name must be kebab-case, got: $PHASE_NAME" >&2; exit 2 ;;
esac
case "$SESSION_NAME" in
    *[!a-z0-9-]*|"") echo "Error: session-name must be kebab-case, got: $SESSION_NAME" >&2; exit 2 ;;
esac

# Display numbers strip leading zero safely (handles 10, 11, etc.).
PHASE_DISPLAY=$((10#$PHASE_NUM))
SESSION_DISPLAY=$((10#$SESSION_NUM))

# Repo root is the parent of tools/.
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

PHASE_DIR="phase-${PHASE_NUM}-${PHASE_NAME}"
SESSION_BASE="session-${SESSION_NUM}-${SESSION_NAME}"

STUDENT_FILE="${REPO_ROOT}/src/${PHASE_DIR}/${SESSION_BASE}.md"
TEACHER_FILE="${REPO_ROOT}/teacher/${PHASE_DIR}/session-${SESSION_NUM}-notes.md"
CODE_DIR="${REPO_ROOT}/code/${PHASE_DIR}/${SESSION_BASE}"
ASSETS_DIR="${REPO_ROOT}/assets/${PHASE_DIR}/session-${SESSION_NUM}"

# Refuse to overwrite either of the two markdown files. Code/asset
# directories may already exist from a partial earlier run; that's
# fine and we just create what's missing.
for f in "$STUDENT_FILE" "$TEACHER_FILE"; do
    if [ -e "$f" ]; then
        echo "Error: $f already exists; refusing to overwrite." >&2
        exit 3
    fi
done

mkdir -p "$(dirname "$STUDENT_FILE")"
mkdir -p "$(dirname "$TEACHER_FILE")"
mkdir -p "${CODE_DIR}/starter" "${CODE_DIR}/exercises" "${CODE_DIR}/solutions"
mkdir -p "${ASSETS_DIR}"

touch "${CODE_DIR}/starter/.gitkeep"
touch "${CODE_DIR}/exercises/.gitkeep"
touch "${CODE_DIR}/solutions/.gitkeep"
touch "${ASSETS_DIR}/.gitkeep"

# Student handout template — 9-section structure from CLAUDE.md.
cat > "$STUDENT_FILE" <<EOF
## Session ${SESSION_DISPLAY}: ${TITLE}

*Phase ${PHASE_DISPLAY} — ${PHASE_NAME} · Session ${SESSION_DISPLAY} of N*

### What we're learning today

TODO: 2-3 sentences in student voice. Talk *to* the student.

### You'll need to remember from last time

- TODO
- TODO
- TODO

---

### Part A: TODO concept name

TODO: introduce the concept, then a guided exercise.

**Checkpoint:** TODO — describe what every student should be able
to do before moving on. **This is the natural stop point if class
is cut short.**

---

### Part B: TODO project or extended practice

TODO: extended practice or mini-project. Tier when relevant:

- **Base:** TODO (everyone aims for this)
- **Stretch:** TODO (try it)
- **Extension:** TODO (for kids who finish early)

---

### Wrap-up

TODO: a few questions for the room.

### If you missed this session

TODO: ~20-30 minute self-paced catch-up. Reads cold without having
been in class.

### Stretch and extension ideas

TODO

### What's next

TODO: one sentence.
EOF

# Teacher notes template — 11-section structure from CLAUDE.md.
cat > "$TEACHER_FILE" <<EOF
## Session ${SESSION_DISPLAY} — Teacher Notes

*Phase ${PHASE_DISPLAY}, ${PHASE_NAME} · Session ${SESSION_DISPLAY} of N · Title: ${TITLE}*

### Purpose of this session

TODO: 2-4 jobs this session is doing, in priority order.

### Before class

TODO: materials, setup, prep time estimate.

### Timing and flow

TODO: rough minute-by-minute. Mark which half is cuttable if
running short.

### Teaching Part A

TODO: specific moves, lines to land, things to model.

### Teaching Part B

TODO

### Common stumbles

TODO: student misconceptions and how to address them.

### Differentiation

- **Younger kids (9-10):** TODO
- **Older kids (12+):** TODO
- **Advanced:** TODO
- **Struggling:** TODO

### What to watch for

TODO: behavioral signals, kids who might need extra attention.

### After class

*(Leave blank until after teaching. Then jot quick notes for next
year's run. This section is the highest-compound-interest part of
the file.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

TODO: callbacks, future references.

### Materials checklist

- [ ] TODO
EOF

cat <<INFO

Created:
  ${STUDENT_FILE}
  ${TEACHER_FILE}
  ${CODE_DIR}/{starter,exercises,solutions}/
  ${ASSETS_DIR}/

Next steps:
  1. Add an entry to src/SUMMARY.md under the "${PHASE_DIR}" header:
       - [Session ${SESSION_DISPLAY}: ${TITLE}](${PHASE_DIR}/${SESSION_BASE}.md)
  2. Fill in the student handout and teacher notes.
INFO
