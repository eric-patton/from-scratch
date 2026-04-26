## Session 2 — Teacher Notes

*Phase 7, Web · Session 2 of 17 · Title: HTML tags and
structure*

### Purpose of this session

The HTML deepening session. Five jobs, in priority
order:

1. **Land the block-vs-inline distinction.** This is
   foundational for understanding *anything* about
   layout (Sessions 4-5).
2. **Land semantic HTML.** `<header>`, `<nav>`,
   `<main>`, `<section>`, `<footer>` — modern best
   practice. Real sites use these.
3. **Land nesting.** HTML is a *tree*; everything
   inside everything else. Indentation reflects the
   tree.
4. **Land "tables for tabular data only."** The
   1990s-style "use tables for layout" anti-pattern
   needs to be killed before kids encounter old
   tutorials.
5. **Set up CSS (Session 3).** A well-structured page
   is much easier to style. Today's restructuring is
   the prep.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built example page using semantic tags.
- Pre-built version of the kid-target page (`index.html`
  with semantic tags + nav menu) so you can demo what
  "good" looks like.
- A real website open with View Source — point out
  the semantic tags they use.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 1.
- **Part A: nesting + block/inline** (~15 min).
- **Part A: tables** (~15 min). Real tabular data only.
- **Part A: semantic tags** (~15 min). The tour.
- **Break** (~5 min).
- **Part B: restructure personal page** (~30 min).
- **Wrap-up** (~5 min).

If running short, **tables can be cut.** They're nice-to-
have but not core. The semantic tag pass is the
priority.

### Teaching Part A

#### Block vs inline — frame on the board

```
BLOCK (stacks vertically)        INLINE (flows with text)
────────────                     ────────────
<h1>...<h6>                      <strong>
<p>                              <em>
<ul>, <ol>, <li>                 <a>
<div>                            <span>
<header>, <nav>, <main>, etc.    <code>
<table>                          <img> (kind of)
```

> "Block tags take up the *full width* and *stack
> vertically*. Headings, paragraphs, sections —
> they get their own line.
>
> Inline tags flow *with the text* — they don't break
> the line. Bold, italics, links — they're inside
> sentences."

This is the conceptual peg for everything in the next
sessions.

#### `<div>` and `<span>` — the empty containers

These are crucial to land:

> "`<div>` and `<span>` *don't mean anything*. They're
> just empty containers. Useful for *grouping* content
> for styling or layout — but not for what the content
> *is*.
>
> Compare to `<header>` — that *means* 'this is the
> header.' If you have a header, use `<header>`. If
> you have a generic group of stuff with no specific
> meaning, use `<div>`."

This sets up the "use semantic when it fits, div
otherwise" practice.

#### Tables — for data, not layout

History lesson:

> "In the 1990s, websites used `<table>` to make
> columns and rows of *content*, not data. There was no
> Flexbox yet — tables were the only way to do
> two-column layouts.
>
> Modern web doesn't do this. Tables are for *real
> tabular data* — like a schedule, a comparison chart,
> sports scores. Anything where rows × columns is the
> *meaning*.
>
> For layout — like 'sidebar on the left, content on
> the right' — we use Flexbox in Session 5."

Show what `<table>` looks like. Type the schedule
example. The borders are missing (table styling is
empty by default — we'll add CSS).

#### Semantic tags — show, don't drill

Walk through each one quickly:

- `<header>` — the top of the page or a section.
- `<nav>` — navigation links.
- `<main>` — the page's main content area.
- `<section>` — a thematic section.
- `<article>` — self-contained piece (blog post).
- `<aside>` — sidebar / related content.
- `<footer>` — the bottom of the page or a section.

Frame:

> "These are *exactly* like `<div>` to the browser —
> generic block containers. The difference: they say
> *what they are.* Search engines understand them.
> Screen readers use them. You and other developers
> can read the markup and instantly know what's what."

Show a real site with View Source — point out the
`<header>`, `<nav>`, `<main>`, `<footer>` they use.

#### Nesting — indent for clarity

```html
<body>
    <header>
        <h1>...</h1>
    </header>
    <main>
        <section>
            <h2>...</h2>
            <p>...</p>
        </section>
    </main>
</body>
```

Each level of nesting = one indent level. The browser
doesn't care, but humans do.

> "When you can't figure out which tag closes which —
> read the indentation. It's there for you. If your
> indentation is messed up, the structure is hard to
> read."

### Teaching Part B

#### "Use the page from Session 1"

The continuity matters. Today's restructure becomes
next week's styling target. Same `index.html` evolves
across the sessions.

A few kids may not have last week's file (forgot,
deleted, missed Session 1). Have a starter file ready.

#### Walk through one section's restructure

On the projector, take one kid's page (or your own
example) and demo:

```html
<!-- Before -->
<h1>Alex's homepage</h1>
<p>Welcome to my page.</p>
<h2>About me</h2>
<p>...</p>
<h2>Projects</h2>
<p>...</p>

<!-- After -->
<header>
    <h1>Alex's homepage</h1>
    <p>Welcome to my page.</p>
</header>
<main>
    <section>
        <h2>About me</h2>
        <p>...</p>
    </section>
    <section>
        <h2>Projects</h2>
        <p>...</p>
    </section>
</main>
<footer>
    <p>&copy; 2026 Alex</p>
</footer>
```

Show the page in the browser before and after. **Looks
identical.** Frame: "Same look, but the markup is
*meaningful* now."

#### Fragment links

The `href="#about"` + `id="about"` pattern is satisfying
because it works *immediately* — click the nav link,
the page scrolls. No JavaScript needed.

> "Browser does this for free. Just match the `id` to
> the `href`."

#### Stretch — multi-page

For kids who finish quickly, push the multi-page
stretch. Three files, each linking to the others. Real
website shape.

Watch for: kids forgetting to update the nav links on
*every* page. Walk through the duplication problem
(every page has its own nav). Mention briefly that
templating systems (Phase 8) solve this.

### Common stumbles

- **Mismatched closing tags.** `<section>...</div>`.
  Walk through.
- **Closing the wrong-level tag.** `</body>` before
  `</main>` or similar. The indentation reveals it.
- **`<header>` confused with `<head>`.** Different
  things. `<head>` is invisible metadata; `<header>`
  is visible top-of-page.
- **`<section>` without a heading.** Semantic
  convention says `<section>` should contain a heading.
  Not a hard error, but worth mentioning.
- **Tables with `<th>` and `<td>` mixed up.** `<th>`
  for headers (bold), `<td>` for data cells.
- **Fragment link doesn't scroll.** The `id` doesn't
  match the `href`, or the section is too high to
  scroll to. Walk through.
- **Multi-page nav inconsistent.** Each page's nav is
  its own copy. Easy to update one and forget the
  others.
- **Table renders without borders.** Default style.
  Mention CSS is coming next week.
- **Special characters render literally.** Forgot to
  use `&lt;` for `<`. Walk through HTML entities.

### Differentiation

- **Younger kids (9-10):** Goal is restructure with
  `<header>`, `<main>`, `<footer>` (drop `<nav>` and
  `<section>` if it's too much). Tables are a stretch.
- **Older kids (12+):** Push for the full restructure
  + multi-page stretch.
- **Advanced (any age):** Suggest:
  - `<figure>` and `<figcaption>` for images
  - `<details>` and `<summary>` for collapsibles
  - Meta tags in head
  - Read MDN HTML elements list
- **Struggling:** A kid who can't get past Session 1's
  basic structure is the kid you focus on. Most common
  cause: typo in tag names, or didn't reload the
  browser.

### What to watch for

- **The "I see why semantic tags matter" moment.**
  Some kids get it from the View Source demo. Others
  from the multi-page stretch. Most from screen-reader
  framing.
- **Buddies sharing nav menu styles.** Encourage —
  good page structure is contagious.
- **Kids over-nesting.** Wrapping every paragraph in
  a `<section>` inside an `<article>` inside a
  `<div>`. Push back: nest only when it adds meaning.
- **Kids resisting semantic tags** ("but `<div>` works
  fine"). Re-frame: yes for browser; no for humans
  and search engines and accessibility.
- **Excitement about multi-page sites.** A few kids
  will go big — 5 pages, full nav, real content.
  Encourage; great prep for Session 6.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 3 (CSS).** Today's well-structured page
  becomes much easier to style.
- **Session 5 (Flexbox).** Today's `<header>`,
  `<main>`, `<footer>` become the layout targets.
- **Session 6 (homepage).** Today's restructured page
  becomes the polished homepage.
- **Sessions 9-10 (DOM).** Today's IDs and semantic
  tags become the *targets* of `document.querySelector(...)`.
- **Phase 8 (Flask).** Templates produce HTML
  structures like today's. Same shape; generated by
  Python.
- **Career-long callback:** semantic HTML is universal.
  React, Vue, Angular — they all produce HTML at the
  end. The structure matters.
- **Peanut butter callback opportunity:** mismatched
  open/close tags + browser silently rendering = the
  precision moment. Browser does what you wrote, even
  when it's wrong.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built semantic-tags example page
- [ ] A real website with semantic tags for View Source
      demo
- [ ] Optional: starter `index.html` for kids who lost
      last week's
- [ ] Projector
- [ ] Class roster
