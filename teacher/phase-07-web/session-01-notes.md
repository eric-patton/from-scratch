## Session 1 — Teacher Notes

*Phase 7, Web · Session 1 of 17 · Title: Welcome to the
web — your first HTML page*

### Purpose of this session

Phase 7 opener. Five jobs, in priority order:

1. **Land the three-language model** (HTML/CSS/JS) and
   what each one does. Even just naming them sets up
   every future session.
2. **Land the browser-as-runtime shift.** No `python`
   command. No install. File + browser + reload.
3. **Land the HTML skeleton.** `<!DOCTYPE>`, `<html>`,
   `<head>`, `<body>`. Every page has it. Memorize.
4. **Land tag syntax.** Open tag, content, close tag.
   Some tags are self-closing (`<img>`, `<br>`).
   Attributes inside the open tag.
5. **Get every kid to a real saved-and-reloaded page.**
   Hands-on. The "edit → save → reload" loop is the
   muscle memory of web dev.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Firefox/Chrome and Thonny.
- A pre-built example "personal page" to demo as the
  Part B target.
- A real website open in another tab — for the View
  Source demo at the end. Pick something visually
  recognizable (the class church website if it exists,
  Wikipedia, a kid-friendly site).
- The MDN URL bookmarked / printed for the handout
  reference.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and Phase 7 framing** (~10 min). Phase 6
  was games, Phase 7 is the web. Three languages.
  Browser as runtime.
- **Part A: HTML skeleton + first page** (~25 min).
  Type the minimal HTML on the projector. Save. Open
  in browser. Reload after edits.
- **Part A: more tags** (~20 min). Lists, images, links.
- **Break** (~5 min).
- **Part B: personal page** (~25 min). Each kid builds.
- **Wrap-up + view source demo** (~5 min). Show one real
  website's HTML.

If running short, **the personal page can be cut to
"add 2-3 things to the demo page."** The skeleton + tag
mechanics are the priority.

### Teaching the framing

#### "Three languages, one page"

Spend 5 minutes on the conceptual frame:

> "Every web page is *three things*:
> - **HTML** is the *structure* — what's there.
> - **CSS** is the *style* — how it looks.
> - **JavaScript** is the *behavior* — what it does.
>
> Today: just HTML. Next sessions: CSS. Then JavaScript.
> By the end you can do all three."

Show a real website. Point at things:

- The text? HTML.
- The colors and fonts and layout? CSS.
- The dropdown menu, the search-as-you-type? JavaScript.

This frame becomes the spine of the next 7 sessions.

#### "Browser is your runtime"

Frame the shift from Python:

> "In Pygame, you ran `python game.py`. The Python
> interpreter ran your code. Here, the *browser* is the
> runtime. The browser reads the HTML, applies the CSS,
> runs the JavaScript. You don't run your code; the
> browser does.
>
> What this means: **anyone with a browser can use your
> work.** No Python install. No 'pip install pygame.'
> Just send them the file (or a URL).
>
> That's the magic of the web."

### Teaching Part A

#### Type the skeleton on the projector

```html
<!DOCTYPE html>
<html>
<head>
    <title>My first page</title>
</head>
<body>
    <h1>Hello, web!</h1>
    <p>This is my first HTML page.</p>
</body>
</html>
```

Type *every line* on the projector with the kids
watching. Pause between lines:

- `<!DOCTYPE html>` — "Tells the browser this is HTML5."
- `<html>` — "The outer envelope."
- `<head>` — "Invisible stuff *about* the page."
- `<title>` — "Shows in the browser tab."
- `</head>` — "End of head section."
- `<body>` — "The visible stuff."
- `<h1>` — "Big heading."
- `<p>` — "Paragraph."

Save as `index.html`. Open in browser. **Pause.** "We
made a web page."

The "we made a web page" moment matters. Some kids
have built websites with drag-and-drop tools — making
one *from text* is a different feeling.

#### File path / opening in browser

This is where many kids stumble. Three approaches:

1. Double-click the file in file manager.
2. File → Open in browser.
3. Drag the file into the browser window.

Walk through whichever works on the class machines
best. Mention the URL bar shows `file:///...` — that's
the local file protocol.

#### Edit → save → reload loop

Demo this explicitly. Change the heading. Save. Reload
in browser. The change appears.

> "This is the web dev loop. Edit the file, save, reload
> the browser. You'll do this thousands of times. Get
> comfortable with it."

For Linux Mint / Thonny: F5 (run) doesn't run anything
useful here. Ctrl+S saves. Then switch to browser, F5
to reload.

#### Lists and images

`<ul>` containing `<li>` items is the structural
pattern of every list on the web. Frame:

> "Lists are *containers* (`<ul>`) of *items* (`<li>`).
> The container goes around all the items. Just like
> Python lists, but in HTML."

For images: file path matters. The `src="me.png"`
expects `me.png` to be in the same folder as
`index.html`. If kids put the image elsewhere, it won't
load — they see a broken image icon.

Mention `alt` text genuinely:

> "Always include `alt`. Real-world: it's how blind
> users (with screen readers) experience the page. Also
> shows up if the image fails to load. Real
> accessibility."

#### Links

`<a href="...">` introduces attributes formally. Frame:

> "Some tags need *extra info*. The `<a>` tag needs to
> know where the link goes. That extra info is an
> *attribute*. `href="https://..."` is the attribute.
> Tags can have many attributes."

Show clicking the link in the browser to navigate. The
back button works.

#### Open external links in a new tab (mention only)

Real sites use `target="_blank"` to open in a new tab:

```html
<a href="..." target="_blank">link</a>
```

Mention but don't drill. Useful trick.

### Teaching Part B

#### Encourage personality, not perfection

> "Tell us things. Real things. What do you actually
> like? What's a weird opinion you have? What did you
> do this weekend?
>
> A page that says *real you* beats a page that says
> 'I am a student. I like cars and music.'"

A few kids will be paralyzed by "what should I write?"
Suggest topics:

- Their favorite Pygame project from Phase 6.
- A book they're reading.
- A sport / activity they like.
- A weird food preference.

#### Walking around

This is the hands-on time. Common help moments:

- Forgot to close a tag.
- Image won't load (wrong file path / wrong filename).
- Saved as `index.html.txt` (Windows hiding the
  extension).
- Wrong file open in browser (still showing the
  pre-edit version).

#### Don't get too fancy yet

A few kids will want to "make it look good" right now.
Redirect:

> "We'll style it next week. For today: get the
> *content* right. The colors and layout come later."

### Common stumbles

- **Typed `<h1>` content `<h2>`** (mismatched closing
  tag). Walk through: open and close must match.
- **Forgot the closing tag.** Page renders weirdly —
  everything inside the unclosed tag.
- **Quotes around attribute values missing.**
  `<img src=me.png>` *might* work in some browsers but
  is wrong. Use quotes.
- **Wrong quote type.** Curly/smart quotes from a word
  processor break HTML. Use straight quotes only.
  (Thonny uses straight quotes by default.)
- **File saved with `.html.txt` extension on Windows.**
  Hidden extension. Show "show file extensions" in
  Windows Explorer or rename in terminal.
- **Browser caching old version.** Hard reload
  (Ctrl+Shift+R / Cmd+Shift+R) bypasses cache.
- **Image not in same folder.** Won't load. Walk
  through file paths.
- **Can't find the file in browser.** Ctrl+O / Cmd+O
  to open file dialog from browser.
- **HTML auto-correction by Thonny.** Generally fine,
  but watch for indentation oddities.

### Differentiation

- **Younger kids (9-10):** Goal is the basic page with
  heading + paragraph + image. The full personal page
  is a stretch.
- **Older kids (12+):** Push for the full personal page
  with multiple sections. Try `<strong>`, `<em>`.
- **Advanced (any age):** Suggest:
  - Multiple linked pages (`index.html`, `about.html`)
  - Special characters (`&copy;`, `&hearts;`)
  - Tables (`<table>`, `<tr>`, `<td>`)
  - HTML5 semantic tags (`<header>`, `<nav>`, `<main>`,
    `<footer>`) — pre-load Session 2
- **Struggling:** A kid who can't get a basic page
  open is the kid you focus on. Most common cause:
  file not saved correctly, or wrong file open in
  browser.

### What to watch for

- **The "I made a web page" reaction.** First page in
  browser = real moment. Pause for it.
- **Buddies trading personal page contents.**
  Encourage. Sharing taste is real.
- **Kids over-typing.** The skeleton is repetitive but
  necessary; some kids try to skip the head section.
  Push back gently.
- **Kids reaching for fancy formatting** (colors,
  fonts) before CSS. Redirect.
- **Kids who view-source on real websites.** Encourage.
  This is one of the great learning resources of the
  web.
- **Kids who notice their changes don't appear.**
  Browser caching, or wrong file open. Walk through.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 2 (HTML structure).** Today's tags expand
  to the semantic ones (`<header>`, `<main>`, `<footer>`).
- **Sessions 3-5 (CSS).** Today's plain page becomes
  styled.
- **Session 6 (homepage).** Today's personal page
  becomes the polished homepage we host on GitHub
  Pages.
- **Sessions 9-10 (DOM).** Today's tags become the
  *targets* of JavaScript queries — `document.querySelector('h1')`.
- **Phase 8 (Flask).** Flask templates produce HTML.
  Today's understanding is foundational.
- **Career-long callback:** view-source on the web is a
  *forever* learning resource. Real site source =
  real teacher.
- **Peanut butter callback opportunity:** mismatched
  open/close tags + browser silent rendering = a
  precision moment. Browser does what you wrote, even
  when wrong.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built "personal page" example
- [ ] A real website open for view-source demo
- [ ] MDN URL printed / bookmarked
- [ ] A few sample images (png/jpg) for kids who don't
      have one ready
- [ ] Projector
- [ ] Class roster
