## Session 3 — Teacher Notes

*Phase 3, Python basics · Session 3 of 16 · Title: Strings —
text in Python*

### Purpose of this session

Strings are the most common data type in everyday Python. Today
goes deep enough to make them useful. Five jobs, in priority
order:

1. **Land f-strings.** Promised in Session 2 as the upgrade from
   `+ str(...) +` concatenation. Today is the payoff. Once kids
   see f-strings, they'll never go back.
2. **Land string methods (lower/upper/strip).** Mechanical. Just
   show them and use them. Methods on values is a new pattern
   (the `.method()` syntax) — worth pointing out explicitly.
3. **Land indexing and slicing.** The `[0]`, `[-1]`, `[0:3]`
   syntax is genuinely new. Some kids will find it intuitive
   immediately; others need to see it visually.
4. **Land `for letter in name:` (string iteration).** Foreshadows
   list iteration in Session 8. Today's vowel-counter stretch
   is the first encounter; lists make it general.
5. **Land `len()` and the membership operator (`in`).** Both
   short, both useful, both come back constantly.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Optional: have the name analyzer pre-built so you can show
  the destination if energy flags.

**Prep time:** ~10 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was types. Anyone
  build something with their age calculator at home?
- **Part A: f-strings + methods** (~40 min) — the f-string reveal
  ~10 min, methods ~10 min, len ~5 min, hands-on practice ~10
  min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: indexing + name analyzer** (~35 min) — indexing ~10
  min, slicing ~10 min, name analyzer build ~10 min, stretch
  for fast finishers ~5 min.
- **Wrap-up** (~5 min).

If running short, **the palindrome extension can be cut.** The
name analyzer is the goal.

### Teaching Part A

#### The f-string reveal

Open with last week's awkward concatenation:

```python
print("In " + str(years) + " years, you'll be " + str(future_age) + ".")
```

Then the f-string version:

```python
print(f"In {years} years, you'll be {future_age}.")
```

Run them side by side. Same output. One is gross; one isn't.

> "Both work. F-strings are way easier to read and write. From
> today onward, we use f-strings whenever we mix variables into
> output."

The three rules (f prefix, curly braces, done) are all kids need
to know. Don't get into formatting specifiers (`:.2f`, etc.)
yet — they'll discover them when they need them.

The "expressions inside curly braces" thing is worth showing:

```python
print(f"Next year you'll be {age + 1}.")
```

The `age + 1` runs first, the result goes into the string. This
unlocks more concise output.

#### String methods

The `.method()` syntax is genuinely new. Worth pointing out
explicitly:

> "When we write `name.upper()`, the `name.` part means 'this
> belongs to the string in name.' Different types have different
> methods — strings have upper, lower, strip; numbers have
> different ones. We've actually used methods before — `t.forward(100)`
> in Phase 2 was a method on the turtle."

The Phase 2 callback ties together what's otherwise a confusing
new syntax. The `.method()` pattern is the same as `t.forward(100)`
— just different objects.

The "methods don't change the original" point is important:

```python
name = "Sam"
name.upper()
print(name)   # still "Sam"
```

vs.

```python
name = "Sam"
name = name.upper()
print(name)   # "SAM"
```

This is a confusing pattern for beginners. The string methods
return a *new* string; they don't modify the original. Worth a
minute at the projector.

#### `len()`

Mechanical. `len(name)` returns the count of characters.

Note the syntax: `len()` is a *function* (you pass the string
in), not a *method* (you'd call `name.len()`). Python has both
patterns. Don't try to explain why — just say "len works on
lots of things and it's a function."

### Teaching Part B

#### Indexing

The "boxes numbered starting from 0" framing is the right model.
Draw it on the whiteboard or projector:

```
C a l e b
0 1 2 3 4
```

Have students try `name[0]` and `name[1]` themselves. The
zero-based indexing is the surprise — most kids would guess
`name[1]` is the first character. The "it starts at 0" rule is
universal in programming and worth landing now.

Negative indexing (`name[-1]`) is a small Python kindness: it
counts from the end. Useful for "the last character" without
needing to know the length.

#### Slicing

Slicing `[start:end]` is genuinely tricky. The "includes start,
excludes end" rule trips kids up every time. Demo:

```python
name = "Caleb"
print(name[0:3])    # Cal — three characters
```

> "Notice — we asked for `0:3`, and we got 3 characters. The
> end number is *not included.* It's like saying 'from index 0
> up to but not including 3.' This is one of the most-confusing
> things in Python; everyone has to learn it once."

Show the omitted-end and omitted-start variants:
- `name[2:]` — from index 2 to the end
- `name[:3]` — from the start to index 3

The `[::-1]` reverse trick is magic. Don't try to explain why
in detail (the third number is a "step"). Just say:

> "This is a Python idiom for 'reverse a string.' Don't worry
> about why; just remember it works."

Some kids will be curious about the underlying mechanic. Brief
honest answer: "the third number in slicing is the step; -1
means step backward by 1, which means reverse." Don't dwell.

#### Name analyzer

Mechanical assembly of everything in Parts A and B:
- An f-string with `len(name)` inside
- F-strings with `name[0]` and `name[-1]`
- F-strings with `name.upper()` and `name[::-1]`

Five output lines, all using f-strings. Have students customize
their analyzer — add their own facts about the name.

#### Stretch — vowel counter

The vowel counter introduces:
- `for letter in name:` — string iteration (new)
- `letter in "aeiou"` — membership check (new)
- A counter variable

Worth walking through the loop body at the projector:

> "Each iteration of this loop, `letter` becomes the next
> character of `name`. So if `name` is 'caleb', the loop runs
> five times. First iteration `letter` is 'c'; second 'a'; etc.
> Each iteration, we check if that letter is in the string
> 'aeiou'. If so, count it."

The `for X in collection:` pattern is the foundation for list
iteration in Session 8. Today is foreshadowing.

#### Extension — palindrome

The palindrome checker combines:
- `.lower()` for case-insensitive comparison
- `[::-1]` for reversal
- `==` for equality
- `if/else` for the decision
- F-strings for output

Five concepts, four lines of meaningful code. Worth pointing out
how concise Python can be once you have the right tools.

Test cases worth trying: `mom`, `racecar`, `level`, `taco` (not),
`wasitacaroracatisaw` (yes — read it carefully).

### Common stumbles

- **`print(name.upper)` instead of `print(name.upper())`.**
  Without parens, you're printing the function itself, not the
  result. Easy fix; common typo.
- **Forgot the `f` in front of the f-string.** Variables in
  `{}` don't get replaced; they print literally. Fix: add
  the `f`.
- **String methods that should chain don't.** `name.upper().lower()`
  works fine; chained method calls return new strings each time.
  Mention if asked.
- **Trying to modify the original string.** `name[0] = "X"` is
  an error — strings are immutable. To "change" a string, build
  a new one.
- **Off-by-one on slicing.** `name[0:5]` for a 5-character
  string is the whole thing. `name[0:4]` skips the last
  character. The "end is exclusive" rule trips everyone up
  initially.
- **`len(name)` returning 0 unexpectedly.** Usually means `name`
  is the empty string `""`. If kid did `name = input("Name: ")`
  and just hit Enter, `name` is empty.
- **Vowel counter that double-counts.** Some kids add to the
  counter without indenting under the `if`, or forget to
  initialize the counter to 0. Walk through the loop body
  carefully.

### Differentiation

- **Younger kids (9-10):** May find slicing genuinely confusing.
  Spend extra time on the visual "boxes with numbers" model.
  Once they see `name[0]` is the first character because Python
  starts at 0, the rest follows.
- **Older kids (12+):** Will pick up f-strings and indexing
  fast. Push them to the palindrome extension. If they finish:
  ask them to write a function `is_palindrome(word)` that
  returns True or False (foreshadows return values in Session 6).
- **Advanced (any age):** May know strings from prior
  experience. Push them on f-string formatting (`f"{x:.2f}"`
  for 2 decimals, etc.) or on `.split()`/`.join()` (which lead
  into lists in Session 8). Or have them tackle a Caesar
  cipher — shift each letter by N positions in the alphabet.
- **Struggling:** A kid who can't get the basic f-string
  working in Part A is the kid you focus on. Most common
  cause: forgot the `f` prefix, or used wrong brace types
  (curly `{}` not square `[]`).

### What to watch for

- **The "wait, that's so much easier" reaction to f-strings.**
  Most kids will visibly process this. Affirm.
- **The "boxes start at 0" surprise.** Some kids find this
  weird, some find it natural. Either way, it's universal in
  programming so the sooner it's normalized, the better.
- **Frustration with slicing.** The end-exclusive rule will
  trip kids up. When it does, walk them through the boxes
  visualization. Don't rush.
- **The vowel-counter "loop ran but counter didn't update"
  bug.** Usually missing indentation. Common; fix gently.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 4 (next week, deeper conditionals).** The `in`
  operator from today's vowel counter generalizes — `if name in
  ["Sam", "Alex", "Jordan"]:` — when we have lists in Session 8.
- **Session 7 (number-guessing game).** Heavy f-string usage for
  output; basic conditionals on the user's guess.
- **Session 8 (lists).** The `for letter in name:` pattern from
  today is the *exact same syntax* as `for item in list:`.
  Foreshadow lightly.
- **Session 12 (hangman).** String indexing, `in` for membership
  ("is this letter in the word?"), `.lower()` for normalization
  — all today's tools, scaled up.
- **Phase 7 (web).** F-strings are how you build HTML in
  Python (Flask uses templates which are basically f-strings
  under the hood). Today's syntax transfers directly.
- **Peanut butter callback opportunity:** the f-string-without-f
  bug is a precision moment. The computer did exactly what was
  written; you wrote `"{name}"` instead of `f"{name}"`, which
  is a literal string with curly braces.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built name analyzer
- [ ] Whiteboard or projector for the indexing/slicing visuals
- [ ] Class roster
