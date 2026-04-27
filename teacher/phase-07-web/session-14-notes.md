## Session 14 — Teacher Notes

*Phase 7, Web · Session 14 of 17 · Title: Fetch +
JSON — talking to the internet*

### Purpose of this session

The "JS hits the internet" session. Five jobs, in
priority order:

1. **Land `fetch(url)` + `await response.json()`.**
   The standard pattern for getting data.
2. **Land `async`/`await`.** The modern,
   readable way. Skip the older `.then` chain.
3. **Land "always handle errors."** Network
   failures are real; `try`/`catch` is required.
4. **Make data exploration fun.** Free APIs are
   delightful — kids love discovering what's out
   there.
5. **Set up Session 15 (GitHub Pages).** This
   session's results are demoable to *anyone* once
   deployed.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built cat fact page.
- Pre-built dog photo page.
- Pre-built combo (dog + joke) page.
- Pre-built Pokemon search (stretch demo).
- A list of 5-10 free APIs to suggest, with their
  example URLs.
- Optional: test all chosen APIs on the network the
  class will use, *before* class. Some
  organizations block external requests.

**Prep time:** ~25 minutes. The API testing matters —
if the church/school network blocks APIs, the
session can't run.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 13.
  Today: talking to the internet.
- **Part A: what's an API + cat facts** (~25 min).
  Show the JSON in browser, then build the page.
- **Part A: dog photos + error handling** (~15 min).
- **Break** (~5 min).
- **Part B: combo + Promise.all** (~20 min).
- **Stretches** (~15 min). Other APIs, search.
- **Wrap-up** (~5 min).

If running short, **drop the combo and stretch
search.** The cat-or-dog single-API page is the
priority.

### Teaching Part A

#### "What's an API"

Frame:

> "An API is a URL that returns *data*. Visit it,
> get back JSON. There are thousands of free public
> APIs — random jokes, cat facts, dog photos,
> weather, sports scores, almost anything you can
> name.
>
> Today: your JavaScript can request data from any
> of them and use it on your page."

Show in browser: visit `https://catfact.ninja/fact`.
The raw JSON appears. **Pause.**

> "*That* is what an API returns. Just text — a
> string of JSON. Our job: get it from JS, parse
> it, display it."

#### `fetch` is async

The async concept is genuinely new. Frame:

> "Network requests take time — milliseconds at
> best, seconds at worst. JS doesn't *wait* for
> them — it keeps running, and the response comes
> back later.
>
> `fetch(url)` returns a *Promise* — an object that
> says 'I'll have the data eventually.' We use
> `await` to *wait* for it."

Don't go deep on Promises. The recipe matters more.

#### `async`/`await` recipe

```javascript
async function loadFact() {
    const response = await fetch(url);
    const data = await response.json();
    // use data
}
```

Three things to memorize:

1. **`async function`** — declares the function as
   async (allows `await` inside).
2. **`await fetch(...)`** — wait for the response.
3. **`await response.json()`** — parse the body
   (also async).

> "Think of `async`/`await` as 'pause here, wait
> for the slow thing, then continue.' Same as if
> there were no network — just with a pause."

#### Skip the old `.then` chain

Don't introduce `.then()` first. Modern JS uses
`async`/`await`. Less code, more readable.

(If a kid asks: yes, the old version exists. We're
using the modern one.)

#### Always `try`/`catch` for fetch

> "Networks fail. The API could be down. Wifi
> could drop. The URL could be wrong. *Always*
> wrap fetch in `try`/`catch`. Show the user a
> friendly error if it fails."

Same shape as Phase 3 Session 13's Python
`try/except`.

#### Explore the data first

When introducing a new API:

1. Visit the URL in browser. See the JSON.
2. Identify the field you want (e.g.,
   `data.fact`, `data.message`, etc.).
3. Then write the JS.

This sequence prevents kids from blindly typing
property names that don't exist.

### Teaching Part B

#### `Promise.all` for parallel

```javascript
await Promise.all([loadDog(), loadJoke()]);
```

Frame:

> "If you `await` two fetches in sequence, you wait
> for one, *then* the other. With `Promise.all`,
> they run in parallel — start both, wait for the
> slowest. Faster total time."

Demo the difference if you have time. Two `await`s
sequentially might take 600ms; in parallel, maybe
350ms.

#### Search interface — template literals in URLs

```javascript
const url = `https://pokeapi.co/api/v2/pokemon/${name}`;
```

Frame:

> "Build URLs dynamically. Take user input, drop it
> in. Now your page can search across millions of
> entries — type a name, get the data."

The Pokemon search is delightful for kids who know
Pokemon. Charizard, Pikachu, Mew, Mewtwo — all
work. Encourage exploration.

### Common stumbles

- **Forgot `await`.** `const data = response.json()`
  returns a Promise, not the actual data. Walk
  through.
- **Forgot to make function `async`.** Can't use
  `await`. Add `async` before `function`.
- **CORS errors.** Some APIs block requests from
  arbitrary origins. The APIs in the handout work
  from any browser. If a kid finds an API that
  errors with "blocked by CORS policy," try a
  different one.
- **Network blocks.** Some school/church networks
  block external requests. **Test before class.**
- **`response.json()` errors.** Response wasn't
  JSON. Maybe the URL returned HTML (404 page).
  `response.ok` check before parsing helps:
  ```javascript
  if (!response.ok) throw new Error(`Status ${response.status}`);
  ```
- **Wrong field name.** `data.facts` vs
  `data.fact`. Always log the data first.
- **Image src not updating.** Forgot to wait, or
  set src wrong.
- **HTML chars in API responses.** Some APIs return
  text with `<` or `&`. `textContent` is safe;
  `innerHTML` would interpret as HTML. **Use
  `textContent`** for untrusted data.
- **Mixed content errors.** If your page is HTTPS
  but the API is HTTP, browser blocks. Use HTTPS
  APIs.

### Differentiation

- **Younger kids (9-10):** Goal is one fetched
  thing on the page. The cat-fact page is enough.
- **Older kids (12+):** Push for the combo + at
  least one stretch.
- **Advanced (any age):** Suggest:
  - Search interface
  - Multiple API combinations
  - Auto-refresh with `setInterval`
  - Save fetched history to localStorage
  - Loading states with spinner CSS
  - Display 10+ items from a list-returning API
- **Struggling:** A kid who can't get fetch
  working is the kid you focus on. Most common
  cause: forgot `async`/`await`, or wrong URL.

### What to watch for

- **The "I just talked to the internet" reaction.**
  First successful fetch is real. Pause for it.
- **Buddies sharing API URLs.** Encourage. Each
  kid finding a new one expands the class's pool.
- **Excitement over Pokemon API.** Some kids will
  go deep — fetching all 1000+ Pokemon. Encourage.
- **Frustration with first network failure.**
  "Why isn't it working?" Walk through console
  errors.
- **Discovery of more APIs.** Some kids will
  search for "free public API" and bring back
  weird ones. Generally encourage; verify the
  results aren't inappropriate before showing
  the class.
- **CORS / network blocks frustration.** If
  network blocks fetches, switch to a different
  API or use a CORS proxy (advanced).

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 15 (GitHub Pages).** Their fetch
  pages can go on the internet. Anyone can use.
- **Sessions 16-17 (milestone).** Many kids will
  build API-driven apps for their milestone.
- **Phase 8 (Flask).** Backend that serves *its
  own* APIs. JS can fetch from those.
- **Career-long callback:** every modern web app
  uses fetch (or its successors). React, Vue —
  all hit APIs behind the scenes.
- **Peanut butter callback opportunity:** the
  forgot-await issue is a precision moment. Code
  runs but data is a Promise, not a value.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built cat / dog / combo pages
- [ ] Pre-built Pokemon search
- [ ] List of 5-10 free APIs (in handout, but
      have specific recommendations)
- [ ] Network tested in advance — APIs accessible
- [ ] Projector
- [ ] Class roster
