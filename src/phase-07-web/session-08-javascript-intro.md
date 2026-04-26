## Session 8: JavaScript — syntax compared to Python

*Phase 7 — Web · Session 8 of 17*

### What we're learning today

You know Python. Today you meet **JavaScript** — the
language the *browser* runs. The good news: it has
the same ideas as Python (variables, conditionals,
loops, functions, arrays, objects). The bad news:
**all the syntax is different.** Today is a
side-by-side tour of "same idea, different shape."
Next session we'll use JavaScript to *change pages.*

### You'll need to remember from last time

- **Phase 3 Python** — variables, conditionals, loops,
  functions, lists, dictionaries.
- **HTML basics** — Sessions 1-2.
- **`<script>` tag** (we'll meet it today).
- **DevTools console** — Session 3 stretch.

---

### Part A: JavaScript, side by side with Python

#### Where JavaScript runs

Two ways to add JavaScript to a page:

**1. Inside a `<script>` tag in HTML:**

```html
<body>
    <h1>Hi!</h1>
    <script>
        console.log("Hello from JavaScript!");
    </script>
</body>
```

**2. In an external `.js` file (best):**

```html
<script src="app.js"></script>
```

Same idea as external CSS. Better for organization.

**For today's quick experiments:** open your browser's
**DevTools console** (Right-click → Inspect → Console
tab). You can type JavaScript directly there and run
it instantly. Like a Python REPL but in the browser.

#### Try it

Open any page in your browser. Open DevTools (F12 or
Ctrl+Shift+I). Click the **Console** tab. Type:

```javascript
console.log("Hello!")
```

Press Enter. **"Hello!" appears.** That's how you
print in JS.

`console.log(...)` is the JS equivalent of Python's
`print(...)`. Anywhere you'd `print` in Python, you
`console.log` in JS.

#### The big differences upfront

```python
# Python                          # JavaScript
x = 5                              let x = 5;
y = "hello"                        const y = "hello";
print(x)                           console.log(x);

if x > 0:                          if (x > 0) {
    print("positive")                  console.log("positive");
                                   }

for i in range(10):                for (let i = 0; i < 10; i++) {
    print(i)                           console.log(i);
                                   }

def add(a, b):                     function add(a, b) {
    return a + b                       return a + b;
                                   }

nums = [1, 2, 3]                   const nums = [1, 2, 3];
nums.append(4)                     nums.push(4);
print(len(nums))                   console.log(nums.length);

person = {"name": "Alex"}          const person = {name: "Alex"};
print(person["name"])              console.log(person.name);
```

Same shape, different syntax. Notice the patterns:

- **Variable declarations** with `let` (changeable) or
  `const` (won't change).
- **Curly braces** `{ }` instead of indentation.
- **Parentheses** around `if` / `for` / `while`
  conditions.
- **Semicolons** at the end of statements (technically
  optional, but include them).
- **No `def`** — use `function`.

#### Variables — `let` and `const`

```javascript
let x = 5;
x = 10;       // OK — let is changeable

const y = 5;
y = 10;       // Error — const can't change
```

**Use `const` by default.** Only use `let` when you
*know* the variable will change.

(Old code uses `var` — avoid it. Modern JS uses `let`
and `const`.)

#### Strings

Same idea as Python:

```javascript
const name = "Alex";
const greeting = 'Hi!';        // single quotes also OK
const message = `Hello, ${name}!`;    // template literal — like f-strings!
```

**Backticks** (`` ` ``) make a **template literal** —
the JS version of Python's f-string. `${expression}`
inserts a value. Use these for any string with
variables.

Methods feel familiar:

```javascript
"hello".length              // 5
"hello".toUpperCase()        // "HELLO"
"hello".includes("ell")      // true
"a,b,c".split(",")           // ["a", "b", "c"]
```

(Note: `length` is a *property*, not a function — no
parentheses.)

#### Numbers

```javascript
const n = 42;
const pi = 3.14;
n + 1               // 43
n / 2               // 21
n % 3               // 0 — modulo
2 ** 8              // 256 — exponent

Math.floor(3.7)     // 3
Math.round(3.7)     // 4
Math.random()        // random 0 to 1
```

JS has *one* number type for both ints and floats.
The `Math` object holds math functions.

#### Booleans

```javascript
const isReady = true;
const isDone = false;

!isReady             // false (not)
isReady && isDone    // false (and)
isReady || isDone    // true (or)
```

`!` is "not", `&&` is "and", `||` is "or". (Python uses
words; JS uses symbols.)

#### Comparison — `===` not `==`

```javascript
5 === 5              // true (strict equality)
5 === "5"            // false (different types)
5 == "5"             // true (loose — converts types)
```

**Always use `===`** (and `!==`). The `==` operator
does *type coercion* which leads to surprising bugs
(`0 == ""` is true, `null == undefined` is true).

`===` checks both *value* and *type*. Way safer.

#### Conditionals

```javascript
const score = 85;

if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else {
    console.log("C or worse");
}
```

Same shape as Python with curly braces and parens.
Note: `else if` (two words), not `elif`.

#### Loops

```javascript
// Counting loop
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// For-of (like Python's "for x in list")
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(color);
}

// While
let n = 10;
while (n > 0) {
    console.log(n);
    n = n - 1;
}
```

The `for (let i = 0; i < 10; i++)` form is the most
common counting loop. Three parts in the parens:

- **Init** — `let i = 0` (runs once, at start).
- **Condition** — `i < 10` (checked each iteration).
- **After** — `i++` (runs after each iteration).

`i++` is shorthand for `i = i + 1`. Same as `i += 1`.

The `for (const x of ...)` form is for iterating
over arrays — closer to Python's `for x in list`.

#### Functions

```javascript
function greet(name) {
    return "Hello, " + name + "!";
}

console.log(greet("Alex"));    // "Hello, Alex!"
```

The `function` keyword + name + parens with
parameters + body in braces.

There's also **arrow functions** — a shorter syntax:

```javascript
const greet = (name) => {
    return "Hello, " + name + "!";
};

// Or for one-line returns:
const greet = (name) => "Hello, " + name + "!";

const square = (n) => n * n;
```

Arrow functions are common in modern JS. We'll see
them everywhere.

#### Arrays — like Python lists

```javascript
const nums = [1, 2, 3, 4, 5];

nums[0]              // 1 — first item
nums[nums.length - 1]    // 5 — last item

nums.push(6);            // append
nums.pop();              // remove last (returns it)
nums.unshift(0);         // prepend
nums.shift();            // remove first

nums.length              // count
nums.includes(3)          // true

nums.indexOf(3)          // 2

// Iterating
for (const n of nums) {
    console.log(n);
}
```

Most Python list methods have JS equivalents with
slightly different names.

#### Objects — like Python dicts

```javascript
const person = {
    name: "Alex",
    age: 12,
    likes: ["pizza", "soccer"]
};

person.name              // "Alex" — dot syntax
person["name"]           // also "Alex" — bracket syntax
person.age = 13;          // change a value
person.email = "a@b.c";    // add a new key

Object.keys(person)      // ["name", "age", "likes", "email"]
```

JS calls them **objects** (Python calls them
**dicts**). Same idea: key-value pairs.

The dot syntax (`person.name`) is the JS norm. Use
brackets when the key is a variable or has special
characters.

#### Try it all

Try this in your browser's DevTools console:

```javascript
const person = { name: "Alex", age: 12 };

function describe(p) {
    return `${p.name} is ${p.age} years old`;
}

console.log(describe(person));    // "Alex is 12 years old"

const friends = ["Sam", "Pat", "Jordan"];
for (const friend of friends) {
    console.log(`Hi ${friend}!`);
}

const square = (n) => n * n;
console.log(square(7));    // 49
```

Type each block. Run. Verify the output.

**Checkpoint:** *You've run JavaScript in the
console — at least one variable, one function, one
loop.* **This is the natural stop point if class is
cut short.**

---

### Part B: JS in an HTML file

#### A page that uses JS

Open Thonny. Save a new file as `script-test.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>JS test</title>
</head>
<body>
    <h1>JavaScript test</h1>
    <p>Open the console to see output.</p>
    
    <script>
        console.log("Page loaded!");
        
        const colors = ["red", "green", "blue"];
        for (const color of colors) {
            console.log(`Color: ${color}`);
        }
        
        function add(a, b) {
            return a + b;
        }
        
        console.log("2 + 3 =", add(2, 3));
    </script>
</body>
</html>
```

Save. Open in browser. **Open DevTools → Console.**
You should see:

```
Page loaded!
Color: red
Color: green
Color: blue
2 + 3 = 5
```

The JS ran when the page loaded. The output went to
the console.

#### External JS file

In the same folder, create `app.js`:

```javascript
console.log("From external file!");

const numbers = [1, 2, 3, 4, 5];
let total = 0;
for (const n of numbers) {
    total = total + n;
}
console.log("Total:", total);
```

In your HTML, replace the `<script>...</script>`
block with:

```html
<script src="app.js"></script>
```

Save both. Reload. The output now comes from
`app.js`. Same as external CSS — cleaner.

#### Practice — write a few small functions

In `app.js` (or directly in the console), try
writing:

```javascript
// 1. A function that doubles a number
const double = (n) => n * 2;
console.log(double(7));    // 14

// 2. A function that joins names
function joinNames(names) {
    return names.join(" and ");
}
console.log(joinNames(["Alex", "Sam", "Pat"]));    // "Alex and Sam and Pat"

// 3. A function that filters even numbers
const evens = (numbers) => {
    const result = [];
    for (const n of numbers) {
        if (n % 2 === 0) {
            result.push(n);
        }
    }
    return result;
};
console.log(evens([1, 2, 3, 4, 5, 6]));    // [2, 4, 6]

// 4. An object describing yourself
const me = {
    name: "Alex",
    age: 12,
    hobbies: ["coding", "soccer"]
};
console.log(`I'm ${me.name}, age ${me.age}.`);
console.log(`My hobbies: ${me.hobbies.join(", ")}`);
```

Each one mirrors something you've done in Python.
Try writing more — a max function, a function that
counts vowels, anything from Phase 3.

#### Stretch — array methods

JS arrays have powerful methods. The big ones:

```javascript
const nums = [1, 2, 3, 4, 5];

nums.map(n => n * 2)              // [2, 4, 6, 8, 10]
nums.filter(n => n > 2)           // [3, 4, 5]
nums.reduce((sum, n) => sum + n, 0)    // 15

nums.forEach(n => console.log(n))    // logs each
```

These come up *constantly* in real JS. They're like
Python's `map`, `filter`, `sum` — but more idiomatic
in JS.

#### Stretch — try/catch (like Python's try/except)

```javascript
try {
    const data = JSON.parse("not json");
} catch (error) {
    console.log("Couldn't parse:", error.message);
}
```

Same idea as Python's `try/except`, different syntax.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show one JavaScript thing you wrote.
  A function? An object? Something funky?
- Did the syntax differences (braces, parens,
  semicolons) feel weird at first?
- Which is harder to type — Python or JavaScript?
- Anyone discover an array method that felt magical?

Today you learned:

- **JavaScript runs in the browser.** Open DevTools
  console to try things.
- **`console.log(...)`** = `print(...)` from Python.
- **Variables** with `let` (changeable) and `const`
  (constant). Default to `const`.
- **Strings** with single, double, or backticks.
  Backticks support `${...}` interpolation.
- **`===` not `==`** for comparison.
- **Conditionals** with parens around the condition,
  braces around the body.
- **Loops** — `for (let i = 0; i < N; i++)` and
  `for (const x of arr)`.
- **Functions** — `function name() { ... }` or
  arrow `(a, b) => a + b`.
- **Arrays** — `push`, `pop`, `length`, etc.
- **Objects** — `{key: value}` with dot or bracket
  access.
- **External `.js` files** with `<script
  src="...">`.

The *thinking* is the same as Python. Just the
shapes are different.

Next week: **the DOM** — using JavaScript to *reach
into the page* and change what's there. Click a
button, change the page. The web's secret power.

### If you missed this session

Open your browser. Open DevTools (F12). Click the
Console tab.

1. Try the syntax examples in Part A. Run each in
   the console. Notice the output.

2. Build the test HTML page from Part B with the
   `<script>` block.

3. Move the JS to an external `app.js` file.

4. Write a few small functions. Run them in the
   console.

About 45-60 minutes. By the end you should be
comfortable writing simple JS.

### Stretch and extension ideas

- **Array methods** — `map`, `filter`, `reduce`,
  `forEach`. Practice converting Python loops to
  these.
- **`try/catch`** for error handling.
- **`JSON.parse` and `JSON.stringify`** — convert
  between objects and JSON strings.
- **`setTimeout(fn, 1000)`** — run a function after
  1 second. (Async, sort of.)
- **Read [MDN's JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)**
  — the canonical reference.

### What's next

Next week: **the DOM** — Document Object Model.
JavaScript's interface to the page. We'll use
`document.querySelector(...)` to find elements,
`addEventListener(...)` to react to clicks, and
`element.textContent = ...` to change what's on the
page. **This is where JS gets exciting.**
