## Session 10 — Teacher Notes

*Phase 3, Python basics · Session 10 of 16 · Title: Dictionaries
— key-value pairs*

### Purpose of this session

Dictionaries are the second pillar of Python data (lists are the
first). Five jobs, in priority order:

1. **Land "key-value pairs."** The mental model: instead of
   indexing by number, index by name. The framing matters more
   than the syntax.
2. **Connect to the parallel-lists problem from Session 8.**
   "Remember the awkward favorites + categories thing? Dicts
   are the cleaner solution."
3. **Land basic operations: create, lookup, add/update,
   `in`, `.items()`.** That's enough for most programs.
4. **Land the count-into-a-dict pattern.** One of the most
   common Python idioms; lots of real programs use it.
5. **Set up Session 11 (file I/O).** A file gives you data;
   what do you put it into? Often a dict. Foreshadow.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: pre-built contact book and word counter as
  destination previews.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was deeper lists.
  Anyone build a menu-driven anything at home?
- **Part A: dict basics** (~40 min) — the parallel-lists
  callback ~5 min, dict creation ~5 min, lookup ~10 min, `in`
  for safety ~5 min, iteration ~10 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: contact book** (~35 min) — base ~15 min, delete
  stretch ~5 min, word counter extension ~15 min.
- **Wrap-up** (~5 min).

If running short, **the word counter extension can be cut.**
The contact book is the goal.

### Teaching Part A

#### The parallel-lists callback

Open with the Session 8 callback explicitly:

> "Two weeks ago we did favorites with categories — two parallel
> lists, indexes lined up. It worked but was awkward. Today
> we'll see the cleaner way."

Show the parallel lists:

```python
favorites = ["pizza", "soccer", "blue"]
categories = ["food", "activity", "color"]
```

Then the dict:

```python
favorites = {
    "pizza": "food",
    "soccer": "activity",
    "blue": "color"
}
```

> "Same information, one structure. The names ('pizza',
> 'soccer', 'blue') are *keys*. The values are what they point
> to. Together they're *key-value pairs*."

The "they go together" insight is the lesson. Drive it home.

#### Creating dicts

The syntax variations:

```python
# all at once
person = {"name": "Sam", "age": 12}

# empty then add
person = {}
person["name"] = "Sam"
person["age"] = 12
```

Both work. The empty-then-add pattern is what kids will use
most (mirrors `[]` then `.append()` for lists).

The colon between key and value is a new symbol in this
context. Don't dwell — just show the pattern.

#### Lookup

The `[key]` syntax is the bridge from lists. Same brackets,
different content — strings (or sometimes other types) instead
of integers.

The KeyError demo is important:

```python
print(person["color"])   # KeyError if color isn't a key
```

Run. Show the error. Then introduce `in`:

```python
if "color" in person:
    print(person["color"])
else:
    print("Not set.")
```

The `in` operator generalizes from strings (Session 3) and
lists (Session 8). Same idea, just checking dict keys now.

#### Iteration

Two patterns:

```python
# just keys
for key in person:
    print(key)

# keys and values
for key, value in person.items():
    print(f"{key}: {value}")
```

The `.items()` form is the standard. Show both; lean on the
two-variable form.

The `enumerate`-style two-variable unpacking should be
familiar from Session 9. Make the connection:

> "Same syntax as `for i, item in enumerate(...)` — two
> variables, separated by comma, each gets a value."

### Teaching Part B

#### Base — contact book

Walk through the structure once. The menu pattern is familiar
from Session 9. The new content is the dict operations:

- Add: `contacts[name] = phone`
- Lookup: `if name in contacts: print(contacts[name])`
- Show all: `for name, phone in contacts.items():`

Note: the same `contacts[name] = phone` line both *adds new*
and *updates existing*. Worth pointing out:

> "If the name is already in the dict, this *updates* the
> phone. If not, it *adds* a new entry. Same syntax. Python
> figures out which one based on whether the key exists."

This is convenient but can also be a bug source — kids might
overwrite something they didn't mean to.

#### Stretch — delete

`del contacts[name]` is the new piece. Mechanical.

The protective `if name in contacts:` check is good practice.
Without it, deleting a non-existent key raises KeyError.

#### Extension — word counter

This is the count-into-a-dict pattern, which is *the* dict
idiom. Walk through it carefully.

```python
counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
```

The mental model: "for each word, if I've seen it before, add
1 to its count; otherwise, start its count at 1."

There's a one-line version using `.get()`:

```python
counts[word] = counts.get(word, 0) + 1
```

`.get(word, 0)` returns the current count or 0 if not there.
Add 1. Assign. Don't formally teach today — but mention it as
a stretch idea.

The `sentence.lower().split()` chain is also new:

- `.lower()` — convert to lowercase (string method from
  Session 3)
- `.split()` — split into list of words by whitespace (new)

Method chaining (`a.b().c()`) is genuinely useful but takes
practice to read. Walk through it slowly.

### Common stumbles

- **KeyError when looking up a non-existent key.** Use `in`
  to check first, or `.get()` for safety.
- **Mutable keys.** Dict keys must be immutable (strings,
  numbers, tuples). Lists can't be keys. Most kids won't hit
  this; mention if asked.
- **Confusing list syntax `[]` with dict syntax `{}`.** New
  curly braces vs old square brackets. Watch for mix-ups
  early.
- **`person["age"] = "12"` (string instead of int).** Subtle;
  works fine until you try to do math. Same type-confusion
  issue from Session 2.
- **`for key, value in person:` (without `.items()`).**
  Symptom: error or unexpected behavior. The dict iterates
  over keys by default; you need `.items()` to get pairs.
- **Forgot to call `.items()` (no parens).** `for key, value
  in person.items` — no parens — gives you the method object,
  not the items. Confusing error. Add parens.
- **Word counter that double-counts.** Forgot the `if...else`,
  so they always add 1 even on first encounter (works) but
  with `counts[word] = 1` always (so always 1). Walk through
  the if/else.

### Differentiation

- **Younger kids (9-10):** May find dicts genuinely abstract.
  Lean on the contact book — it's concrete (names → phone
  numbers, like a real address book). Skip the word counter
  if they're struggling.
- **Older kids (12+):** Will pick up dicts fast. Push them
  through the word counter. If they finish: ask them to find
  the most-frequent word using `max(counts, key=counts.get)`
  (advanced, but doable).
- **Advanced (any age):** Suggest:
  - `.get(key, default)` for safe lookup
  - Dict comprehensions: `{x: x*x for x in range(5)}`
  - Nested dicts: `people = {"sam": {"age": 12}, ...}`
  - Counting with `collections.Counter` — Python's built-in
    counting class
- **Struggling:** A kid who can't get the basic dict working in
  Part A is the kid you focus on. Most common cause: confused
  brackets and braces, or forgot the colon.

### What to watch for

- **The "ohhh, it's like a real dictionary" insight.** When
  kids see lookup-by-name, several get the connection to
  paper dictionaries (word → definition). Affirm.
- **The "this is way better than parallel lists" reaction**
  for kids who remember Session 8's awkward version.
- **The word counter "wow" moment** — when they run it and
  see actual frequencies. Counting is satisfying.
- **Buddies trading dict-application ideas.** "What else could
  you store in a dict?" is a great brainstorming pattern.
  Encourage.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 11 (next week, file I/O).** A file gives you raw
  data; you'll often want to process it into lists or dicts.
  Today's count-into-a-dict pattern shows up immediately
  when you read a file of words.
- **Session 12 (hangman).** Could use a dict to track letter
  guesses (letter → True/False) but lists also work. Either
  pattern.
- **Session 13 (error handling).** Dict KeyError is one of the
  errors `try/except` handles cleanly. Today's "use `in` to
  check" is the alternative.
- **Phase 4 (CLI tools).** Configuration is often a dict.
  Every CLI tool that has settings uses dict-like structures.
- **Phase 7 (web).** JSON — the format used by web APIs — is
  basically dicts and lists. Today's syntax maps almost
  directly.
- **Phase 8 (Flask).** HTTP requests come as dicts (the form
  fields). Database results often come as lists of dicts.
  Today's mental model carries the entire web.
- **The peanut butter callback opportunity:** the KeyError on
  missing key is a precision moment. The computer looked up
  exactly what was asked; the key wasn't there; that's an
  error.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built contact book + word counter
- [ ] Projector (helpful for the parallel-lists callback)
- [ ] Class roster
