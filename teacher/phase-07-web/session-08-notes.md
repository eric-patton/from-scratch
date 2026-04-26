## Session 8 — Teacher Notes

*Phase 7, Web · Session 8 of 17 · Title: JavaScript —
syntax compared to Python*

### Purpose of this session

The big language pivot. Five jobs, in priority order:

1. **Land "same ideas, different syntax."** Drill this
   constantly. Every JS feature has a Python
   counterpart. Don't let kids think they're learning
   from scratch.
2. **Land `console.log` and DevTools console.** Their
   primary "see what's happening" tool for the next
   four sessions.
3. **Land `let`/`const`.** Default to `const`. Avoid
   `var`.
4. **Land `===` over `==`.** Strict equality is the
   default-good in modern JS.
5. **Set up Session 9 (DOM).** Today is the language.
   Next: language *plus* the page.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- A pre-built `script-test.html` and `app.js` for
  Part B.
- The Python/JS comparison table on a printout (or on
  the board) for quick reference.
- DevTools console open and ready on the projector.

**Prep time:** ~20 minutes. Walk through the syntax
examples once before class.

### Timing and flow

Total: ~90 min — possibly tight given the breadth.

- **Welcome and pivot framing** (~10 min). Phase 7
  was HTML/CSS so far. Today: JavaScript.
- **Part A — console + variables + strings** (~20 min).
- **Part A — conditionals + loops + functions** (~20 min).
- **Part A — arrays + objects** (~10 min).
- **Break** (~5 min).
- **Part B — JS in HTML, external file, practice
  functions** (~20 min).
- **Wrap-up** (~5 min).

If running short, **drop array methods (Part B
stretch).** The base syntax is the priority.

### Teaching the framing

#### "Different syntax, same thinking"

Open the session with this. Spend 5 minutes:

> "You've been writing Python for ~50 sessions. You
> know variables, conditionals, loops, functions,
> lists, dicts. JavaScript has *all* of those.
>
> What's different: the *shapes*. Curly braces instead
> of indentation. Parens around `if` conditions.
> Semicolons. `function` instead of `def`. `===`
> instead of `==`.
>
> What's the same: the *thinking*. A `for` loop loops.
> An `if` decides. A function takes input, returns
> output. *Same thinking.* Today is mostly translation."

Drill the comparison table. Walk through it on the
projector. Pause on each row.

#### Why JavaScript exists

Brief context:

> "JavaScript was made in 1995 in *ten days* by one
> person at Netscape. It was meant to be a 'small
> scripting language' for the browser. Now it runs
> everything — websites, mobile apps, servers,
> games. Wild story.
>
> Most weirdness in JS comes from those original ten
> days. Modern JS (`let`, `const`, arrows, template
> literals) is the cleanup."

Light history; helps frame the syntax oddities.

### Teaching Part A

#### `console.log` first

Walk to the DevTools console on the projector. Type:

```javascript
console.log("Hello!")
```

Press Enter. Output appears.

> "This is your `print`. Use it constantly to debug
> JavaScript. The console is also where you can type
> arbitrary JS to try things — no need to write a
> file."

Open the console on every kid's machine if possible.

#### Variables — push `const`

Show all three:

```javascript
var oldStyle = 1;        // legacy — don't use
let changeable = 2;       // when value will change
const fixed = 3;          // default
```

> "`const` is the default. Use `let` only when you
> *know* the variable will be reassigned. `var` is
> legacy — avoid it."

#### Template literals are the f-string

> "Backtick strings with `${expression}` are JS's
> f-strings. *Always use them* for strings with
> variables — way easier than concatenation with `+`."

```javascript
// Concatenation (works but ugly):
"Hello, " + name + "! You are " + age + " years old."

// Template literal (better):
`Hello, ${name}! You are ${age} years old.`
```

#### `===` is non-negotiable

Frame:

> "JS has both `==` and `===`. The `==` does *type
> coercion* — it converts types before comparing,
> which leads to weird bugs:
>
> - `0 == ''` is `true`
> - `null == undefined` is `true`
> - `'1' == 1` is `true`
>
> `===` doesn't coerce. *Always use `===` and
> `!==`.* Modern JS style guides require it."

#### Conditionals and loops — translate

For each, show Python next to JS:

```python
# Python
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

```javascript
// JavaScript
if (x > 0) {
    console.log("positive");
} else if (x < 0) {
    console.log("negative");
} else {
    console.log("zero");
}
```

Differences:
- Parens around the condition.
- Braces around the body.
- Semicolons at the end of statements.
- `else if` (two words) instead of `elif`.

#### `for` loops have two forms

The C-style counting loop:

```javascript
for (let i = 0; i < 10; i++) {
    console.log(i);
}
```

Walk through the three parts: init, condition,
after-each. The `i++` is `i = i + 1`.

The for-of loop:

```javascript
for (const color of colors) {
    console.log(color);
}
```

> "This is closer to Python's `for x in list`. Use
> this when you don't need the index — just the
> values."

#### Functions

Two forms, both legitimate:

```javascript
// Function declaration
function add(a, b) {
    return a + b;
}

// Arrow function (modern, common in libraries)
const add = (a, b) => a + b;
```

> "Modern JS uses arrows everywhere. They're shorter,
> and they have a slightly different `this` binding
> (which we won't worry about for now). For our
> purposes, both work."

#### Arrays and objects

Briefly:
- Array creation, indexing, methods (push, pop,
  length).
- Object creation, dot access, bracket access.

Compare to Python lists and dicts at every step. The
mental model is identical.

### Teaching Part B

#### `<script>` placement

Mention briefly:

> "Scripts can go in `<head>` or at the end of
> `<body>`. End of body is more common — by then,
> all the HTML is loaded and the script can find
> elements (Session 9). For now, end of body."

Avoid the `defer` / `async` attributes for now —
deeper than needed.

#### External JS

Same pattern as external CSS. One line:

```html
<script src="app.js"></script>
```

Push toward external files for any non-trivial JS.

#### Practice functions

Walk through one or two on the projector. Then have
kids write their own. Some good targets:

- A function that triples a number.
- A function that picks max of three numbers.
- A function that counts items in an array.
- A function that builds a greeting from an object.

Push them to type and run, not just read.

### Common stumbles

- **Forgot semicolons.** JS is forgiving — usually
  works without them. But sometimes (especially with
  functions returning objects) breaks subtly. Drill
  including them.
- **Confused parens with braces.** `if x > 0:` from
  Python becomes `if (x > 0) {`. Forgetting either
  errors.
- **Used `=` instead of `===`.** `=` is assignment,
  `==`/`===` are comparison. Walk through.
- **`var` instead of `let`/`const`.** Old habit from
  tutorials. Push toward modern.
- **String concatenation with `+`.** Works, but
  template literals are cleaner. Push toward
  backticks.
- **Forgot `return`.** Function logs but doesn't
  return — calling code gets `undefined`.
- **Arrow function syntax wrong.** `n => n * 2` (no
  parens for one arg) vs `(n) => n * 2` (parens
  always work). Either is fine.
- **Used Python operators.** `and` instead of `&&`.
  `or` instead of `||`. `not` instead of `!`. JS
  uses symbols.
- **Indented but no braces.** `if (x > 0) console.log(x);`
  works but `if (x > 0)\n    console.log(x);\n
  console.log("done");` looks like both lines are
  inside the if — but only the first is. *Always
  use braces.*
- **`console.log` vs `print`.** Several kids will
  type `print(...)` and wonder why nothing happens.

### Differentiation

- **Younger kids (9-10):** Goal is variables +
  console.log + simple if + simple for loop.
  Functions are a stretch.
- **Older kids (12+):** Push for full Part A + Part
  B practice functions.
- **Advanced (any age):** Suggest:
  - Array methods (`map`, `filter`, `reduce`)
  - `try/catch` for error handling
  - `JSON.parse` and `JSON.stringify`
  - Reading MDN's JavaScript Guide
- **Struggling:** A kid who can't translate one
  Python program to JS is the kid you focus on.
  Take a Phase 3 program (Hangman, number guessing)
  and translate together.

### What to watch for

- **The "wait, this is exactly like Python" reaction.**
  Once the syntax friction wears off, the *thinking*
  is identical. Acknowledge.
- **The "why is JS so weird" reaction.** Yes. The
  language has history. Reassure that modern JS is
  reasonable.
- **Comparing array methods to Python.** Some kids
  who know Python's list comprehensions will love
  JS's `map`/`filter`. Encourage.
- **Buddies pair-translating.** Encourage. Real
  programming work.
- **Frustration with semicolons.** Some kids will
  forget; let them. The interpreter usually
  recovers. Drill the rule but don't dwell.
- **Excitement about the console.** Some kids
  realize they can type JS into *any* website's
  console. (Discourage messing with real sites
  destructively, but encourage exploration.)

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 9 (DOM).** Today's language + page
  manipulation = real JavaScript.
- **Session 10 (todo).** Build an interactive todo
  in JS. Phase 5 callback (built same in
  customtkinter).
- **Session 13 (canvas game).** Pygame patterns in
  JS. Same loops, same conditionals.
- **Session 14 (fetch).** Talking to APIs from JS.
- **Phase 8 (Flask).** Python on the server, JS on
  the client. Both languages, both jobs.
- **Career-long callback:** JavaScript is everywhere
  — browsers, mobile (React Native), servers (Node),
  games (Phaser). Today's foundation matters.
- **Peanut butter callback opportunity:** the `==`
  vs `===` confusion is a precision moment. Computer
  does *exactly* what you write — even when the
  type-coercion result is unexpected.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built script-test.html + app.js
- [ ] Python/JS comparison table (printed or
      board-ready)
- [ ] DevTools console open on projector
- [ ] Projector
- [ ] Class roster
