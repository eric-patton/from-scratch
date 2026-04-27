## Session 14: Fetch + JSON — talking to the internet

*Phase 7 — Web · Session 14 of 17*

### What we're learning today

Your JS lives in your browser. **The internet is full
of services** that respond to requests with data —
weather, jokes, dog photos, sports scores, almost
anything. Today you'll learn the **`fetch`** API to
ask for data, **`async`/`await`** to wait for the
response, and **JSON** to read what you get back.
By the end you'll have a page that fetches random
content from a public API.

This is **the web's actual superpower** — your tiny
JavaScript can talk to anything online.

### You'll need to remember from last time

- **JavaScript syntax** (Session 8).
- **DOM manipulation** (Session 9).
- **`JSON.parse` / `JSON.stringify`** (Session 11).
- **Functions and arrow functions** (Session 8).

---

### Part A: Fetching data

#### What's an API?

An **API** (Application Programming Interface) is a
URL you can request data from. Visit the URL — you
get back data, usually in JSON format. Examples:

- `https://dog.ceo/api/breeds/image/random` →
  `{"message": "https://...", "status": "success"}` —
  random dog photo URL.
- `https://catfact.ninja/fact` →
  `{"fact": "...", "length": 79}` — random cat fact.
- `https://official-joke-api.appspot.com/random_joke`
  → `{"setup": "...", "punchline": "..."}` —
  random joke.

These are **free public APIs.** No login, no payment,
just request and respond. There are thousands of
them.

Try one in the browser. Visit
`https://catfact.ninja/fact`. You see raw JSON. **The
data is there.** Now we make JS request it from your
page.

#### `fetch(url)`

The basic call:

```javascript
fetch("https://catfact.ninja/fact")
```

This sends a request. But — wait, did anything
happen? Yes, but it takes *time*. Network requests
are **asynchronous** — your code keeps running while
the data is on its way.

`fetch` returns a **Promise** — an object that says
"I'll have the data eventually." To get the data,
you wait for the promise.

#### Async / await — the modern way

The cleanest pattern:

```javascript
async function getCatFact() {
    const response = await fetch("https://catfact.ninja/fact");
    const data = await response.json();
    console.log(data.fact);
}

getCatFact();
```

What's happening:

- **`async function`** — declares the function as
  asynchronous. Means it can use `await` inside.
- **`await fetch(...)`** — wait for the network
  response.
- **`response.json()`** — convert the response body
  to a JavaScript object (parse the JSON). This
  also takes time, so we `await` it too.
- Then `data.fact` is the value we want.

Try it. Open `cat.html` in Thonny:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Cat facts</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 60px auto;
            padding: 20px;
            text-align: center;
        }
        button {
            font-size: 18px;
            padding: 10px 20px;
            cursor: pointer;
        }
        #fact {
            font-size: 22px;
            margin: 30px 0;
            min-height: 50px;
        }
    </style>
</head>
<body>
    <h1>🐱 Random Cat Fact</h1>
    <p id="fact">Click the button to learn something.</p>
    <button id="btn">Get a fact</button>

    <script>
        const btn = document.querySelector("#btn");
        const fact = document.querySelector("#fact");

        async function loadFact() {
            const response = await fetch("https://catfact.ninja/fact");
            const data = await response.json();
            fact.textContent = data.fact;
        }

        btn.addEventListener("click", loadFact);
    </script>
</body>
</html>
```

Save. Open in browser. Click the button. **A random
cat fact appears.** Click again. New fact.

You just made your page **talk to the internet.**

#### Error handling

What if the network is down, or the API is broken?
Wrap with `try`/`catch`:

```javascript
async function loadFact() {
    try {
        const response = await fetch("https://catfact.ninja/fact");
        const data = await response.json();
        fact.textContent = data.fact;
    } catch (error) {
        fact.textContent = "Couldn't load a fact. Try again?";
        console.error(error);
    }
}
```

Same `try/except` pattern as Python (Phase 3 Session
13), with `try/catch` instead.

Always include error handling for fetches. Networks
fail.

#### What does the data look like?

Add a `console.log(data)` line to see the full
structure:

```javascript
const data = await response.json();
console.log(data);
fact.textContent = data.fact;
```

In the DevTools console you see the full object —
a dictionary-like thing with `fact` and `length`
keys. JSON is just objects and arrays.

Different APIs return different shapes. Always
explore the data first before using it.

#### Try a dog photo API

Open `dog.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dog photos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }
        img {
            max-width: 500px;
            max-height: 500px;
            margin: 20px 0;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <h1>🐶 Random Dog</h1>
    <button id="btn">New dog</button>
    <div>
        <img id="dogImg" src="" alt="A dog">
    </div>

    <script>
        const btn = document.querySelector("#btn");
        const dogImg = document.querySelector("#dogImg");

        async function loadDog() {
            try {
                const response = await fetch("https://dog.ceo/api/breeds/image/random");
                const data = await response.json();
                dogImg.src = data.message;
            } catch (error) {
                console.error(error);
            }
        }

        btn.addEventListener("click", loadDog);
        loadDog();    // load on page open
    </script>
</body>
</html>
```

Save. Open. **A random dog photo loads
automatically.** Click the button for another. A
new dog every time.

The Dog API returns `{"message": "<url>", "status":
"success"}`. `data.message` is the URL of the dog
photo. We assign it to the `<img src>`.

**Checkpoint:** *You have a page that fetches data
from a public API and displays it.* **This is the
natural stop point if class is cut short.**

---

### Part B: Combine multiple fetches

Time to build something more interesting.

#### Joke + dog combo

A page that shows a random dog photo and a random
joke side by side, with one button to refresh both.

Save as `combo.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dogs & Jokes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            text-align: center;
        }
        .row {
            display: flex;
            gap: 20px;
            margin: 30px 0;
            align-items: center;
        }
        .col {
            flex: 1;
        }
        img {
            max-width: 100%;
            max-height: 400px;
            border-radius: 8px;
        }
        button {
            font-size: 18px;
            padding: 12px 24px;
            cursor: pointer;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
        }
        #joke {
            font-style: italic;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>Dog + Joke combo</h1>
    <button id="btn">Refresh</button>
    <div class="row">
        <div class="col">
            <img id="dogImg" src="" alt="A random dog">
        </div>
        <div class="col">
            <p id="joke">Click the button.</p>
        </div>
    </div>

    <script>
        const btn = document.querySelector("#btn");
        const dogImg = document.querySelector("#dogImg");
        const joke = document.querySelector("#joke");

        async function loadDog() {
            const response = await fetch("https://dog.ceo/api/breeds/image/random");
            const data = await response.json();
            dogImg.src = data.message;
        }

        async function loadJoke() {
            const response = await fetch("https://official-joke-api.appspot.com/random_joke");
            const data = await response.json();
            joke.textContent = `${data.setup} — ${data.punchline}`;
        }

        async function refresh() {
            try {
                await Promise.all([loadDog(), loadJoke()]);
            } catch (error) {
                console.error(error);
            }
        }

        btn.addEventListener("click", refresh);
        refresh();
    </script>
</body>
</html>
```

Save. Open. **A dog photo and a joke load.** Click
"Refresh." Both update.

What's new:

- **`Promise.all([a, b])`** — runs both fetches
  *in parallel* and waits for both to finish.
  Faster than waiting for one, then the other.

#### List response — multiple results

Some APIs return arrays. Try the JokeAPI:

```javascript
const response = await fetch("https://official-joke-api.appspot.com/jokes/ten");
const jokes = await response.json();    // array of 10 jokes
console.log(jokes.length);    // 10
```

Then loop and add to the page:

```javascript
const list = document.querySelector("#jokeList");
list.innerHTML = "";    // clear
for (const j of jokes) {
    const li = document.createElement("li");
    li.textContent = `${j.setup} — ${j.punchline}`;
    list.appendChild(li);
}
```

Renders 10 jokes as a list.

#### Stretch — loading state

Network requests aren't instant. While waiting, show
a loading message:

```javascript
async function loadDog() {
    dogImg.src = "";
    dogImg.alt = "Loading...";
    
    try {
        const response = await fetch("https://dog.ceo/api/breeds/image/random");
        const data = await response.json();
        dogImg.src = data.message;
        dogImg.alt = "A random dog";
    } catch (error) {
        dogImg.alt = "Failed to load";
    }
}
```

Or a spinner / "loading..." text. Real apps always
show feedback.

#### Stretch — explore other APIs

Public APIs to try:

- **Bored API** — `https://www.boredapi.com/api/activity`
  → returns a random activity to do.
- **Pokemon** — `https://pokeapi.co/api/v2/pokemon/charizard`
  → returns Pokemon data. Try different names.
- **NASA APOD** — `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`
  → astronomy picture of the day.
- **Open-Meteo** — weather data (more complex).
- **OpenLibrary** — book search.
- **Star Wars API** — `https://swapi.dev/api/people/1`
  → character data.

For each: visit the URL in your browser to see the
JSON, then write JS to fetch and display it.

#### Stretch — search interface

Build a "search Pokemon" page:

```html
<input id="nameInput" type="text" placeholder="Pokemon name">
<button id="searchBtn">Search</button>
<div id="result"></div>
```

```javascript
async function search() {
    const name = nameInput.value.trim().toLowerCase();
    if (!name) return;
    
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);
        const data = await response.json();
        
        result.innerHTML = `
            <h2>${data.name}</h2>
            <img src="${data.sprites.front_default}" alt="${data.name}">
            <p>Height: ${data.height}, Weight: ${data.weight}</p>
        `;
    } catch (error) {
        result.textContent = "Pokemon not found.";
    }
}
```

A real search interface. Type "pikachu", "charmander",
"mew" — different Pokemon load.

The `${name}` in the URL is template literal
substitution — building dynamic URLs from input.

#### Extension — display saved API responses

Combine fetch with localStorage. Save the last 10
fetched items. Display history.

#### Extension — error handling polish

Try cutting your wifi. Click the button. Right now,
the error goes to the console — silent failure for
the user. Fix it: show a friendly error message in
the UI when fetch fails.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show what you fetched. Cat facts?
  Dogs? Jokes?
- Did the wait-for-the-response delay feel
  noticeable?
- For kids who explored other APIs — show the
  weirdest one you found.
- For the Pokemon-searcher kids — what's your
  favorite Pokemon's name?

Today you learned:

- **APIs** — URLs that return data.
- **`fetch(url)`** — JS's HTTP request.
- **`async`/`await`** — the modern way to wait for
  async results.
- **`response.json()`** — parse the response body
  as JSON.
- **`try`/`catch`** — error handling for failures.
- **`Promise.all([...])`** — parallel fetches.
- **Template literals** in URLs for dynamic
  requests.

Your JavaScript can now **talk to the world.** Any
public API. Any data on the internet. **That's the
foundation of every modern web app** — Twitter,
Instagram, weather apps, news sites — all hit APIs
behind the scenes.

Next week: **GitHub Pages.** Your work becomes
*publicly accessible* with a real URL anyone can
visit. After that: your milestone.

### If you missed this session

Open Thonny.

1. Build the cat-fact page from Part A. Click the
   button, see facts.

2. Build the dog-photo page. Click for new dogs.

3. Build the combo (dog + joke).

4. (Stretch) Try one other API from the list.

About 30-45 minutes. By the end you should have at
least one page that fetches and displays API data.

### Stretch and extension ideas

- **Loading state** — show "Loading..." while
  waiting.
- **Error handling polish** — friendly UI on
  failure.
- **Multiple APIs combined** in one page.
- **Search interface** — input + button + display.
- **Save fetched data** to localStorage.
- **Display fetch history.**
- **A weather widget** — fetch from Open-Meteo.
- **A news headline ticker** — fetch periodically.
- **Auto-refresh** every N seconds with
  `setInterval`.

### What's next

Next week: **GitHub Pages.** All this work you've
been building? Push it to GitHub, flip a setting,
and **anyone with the link can use it.** Your
homepage, your todo app, your canvas game, your
fetch experiments — all hostable for free.
