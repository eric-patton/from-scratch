## Session 6: Build a personal homepage

*Phase 7 — Web · Session 6 of 17*

### What we're learning today

You have HTML, CSS, the box model, Flexbox. Today
we **put it all together** and build your real
personal homepage — the one that'll go on GitHub Pages
in Session 15 with a public URL anyone can visit. We
build it step by step. By the end you'll have a
polished site you'd be proud to share.

### You'll need to remember from last time

- **HTML structure** — semantic tags (Session 2).
- **CSS** — selectors, colors, fonts (Session 3).
- **The box model** — padding, margin, border (Session 4).
- **Flexbox** — `display: flex`, `justify-content`,
  `align-items`, `gap`, `flex: 1` (Session 5).
- **`box-sizing: border-box`** at the top of every
  stylesheet.

---

### Part A: Plan and build the structure

#### What's a personal homepage?

A page about *you*. What you make, what you like, who
you are. Modern professionals (developers, artists,
writers) all have one. Yours has these jobs:

- **Tell visitors who you are.**
- **Show what you've made** (Phase 6 games, Phase 5
  apps, anything you're proud of).
- **Be visually interesting** without being chaotic.

We'll build a single-page version today. (You can
expand to multiple pages later.)

#### Sketch first

Take 5 minutes. On paper, sketch what your page should
look like. Think about:

- **Top:** a navbar (logo + links) and/or a big hero
  area with your name.
- **Middle:** sections — about you, projects, hobbies,
  whatever.
- **Bottom:** a footer (copyright, contact links).

Most pages roughly follow this shape:

```
┌─────────────────────────┐
│   navbar (logo + nav)   │
├─────────────────────────┤
│                         │
│       hero (name +      │
│      tagline + intro)   │
│                         │
├─────────────────────────┤
│                         │
│     about section       │
│                         │
├─────────────────────────┤
│                         │
│  ┌────┐ ┌────┐ ┌────┐  │
│  │card│ │card│ │card│   projects
│  └────┘ └────┘ └────┘  │
│                         │
├─────────────────────────┤
│      footer             │
└─────────────────────────┘
```

#### Step 1 — Skeleton

Open Thonny. Create a new folder for your homepage if
you want. Create `index.html` and `styles.css` inside
it.

`index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Alex's Homepage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="navbar">
        <div class="logo">Alex</div>
        <nav>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    
    <section class="hero">
        <h1>Hi, I'm Alex.</h1>
        <p class="tagline">Programmer, gamer, future game dev.</p>
    </section>
    
    <main>
        <section id="about" class="content-section">
            <h2>About me</h2>
            <p>I'm 12 years old. I'm in From Scratch Programming Class. I've shipped six projects so far.</p>
        </section>
        
        <section id="projects" class="content-section">
            <h2>Projects</h2>
            <div class="card-row">
                <article class="card">
                    <h3>Pong</h3>
                    <p>My first complete game. Two paddles, one ball.</p>
                    <a href="#" class="btn">See on GitHub</a>
                </article>
                <article class="card">
                    <h3>Fruit Catcher</h3>
                    <p>Catch fruit. Don't catch bombs.</p>
                    <a href="#" class="btn">See on GitHub</a>
                </article>
                <article class="card">
                    <h3>Todo App</h3>
                    <p>My customtkinter project — add tasks, save to disk.</p>
                    <a href="#" class="btn">See on GitHub</a>
                </article>
            </div>
        </section>
        
        <section id="contact" class="content-section">
            <h2>Contact</h2>
            <p>Find me on <a href="https://github.com/...">GitHub</a>.</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2026 Alex</p>
    </footer>
</body>
</html>
```

Save. Open in browser. **Looks plain** — that's
expected. CSS is next.

#### Step 2 — Reset and base styles

`styles.css`:

```css
*, *::before, *::after {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #333;
    background-color: #f7f7f7;
    line-height: 1.6;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

main {
    flex: 1;
}
```

Save. Reload. The page now has:

- The universal `box-sizing` (set once, forever).
- `margin: 0` on body kills the default 8px browser
  margin.
- A clean font stack.
- The body is a flex column, so the footer will stick
  to the bottom (Session 5 pattern).

#### Step 3 — The navbar

```css
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 32px;
    background-color: #2c3e50;
    color: white;
}

.logo {
    font-size: 24px;
    font-weight: bold;
}

.navbar nav {
    display: flex;
    gap: 24px;
}

.navbar a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}

.navbar a:hover {
    color: #3498db;
}
```

Save. Reload. **Real navbar** — logo on the left, nav
links on the right, dark background, hover effect.

#### Step 4 — Hero section

```css
.hero {
    background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
    color: white;
    padding: 80px 32px;
    text-align: center;
}

.hero h1 {
    font-size: 56px;
    margin: 0 0 16px 0;
}

.hero .tagline {
    font-size: 24px;
    opacity: 0.9;
    margin: 0;
}
```

Save. Reload. **A hero section** with a gradient
background and big centered text. Looks like a real
modern site.

`linear-gradient(135deg, color1, color2)` makes a
diagonal gradient between two colors. Try other angles
(`90deg`, `180deg`, `to right`) and other colors.

#### Step 5 — Content sections

```css
.content-section {
    max-width: 1000px;
    margin: 0 auto;
    padding: 60px 32px;
}

.content-section h2 {
    font-size: 36px;
    color: #2c3e50;
    margin-top: 0;
    border-bottom: 3px solid #3498db;
    padding-bottom: 8px;
    margin-bottom: 32px;
}
```

Save. Reload. Each section has good spacing, max
width that keeps text readable, and a styled heading
with an accent underline.

#### Step 6 — Cards

```css
.card-row {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.card {
    flex: 1 1 250px;    /* grow, shrink, base width */
    background-color: white;
    border-radius: 8px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
}

.card h3 {
    margin-top: 0;
    color: #2c3e50;
}

.btn {
    display: inline-block;
    padding: 8px 16px;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 500;
    transition: background-color 0.2s;
}

.btn:hover {
    background-color: #2980b9;
}
```

Save. Reload. **Project cards in a row, with a
satisfying hover lift.**

The `transform: translateY(-4px)` on hover lifts the
card up 4 pixels. Combined with the bigger shadow,
it feels like the card is rising. Real-modern-web
polish.

`flex: 1 1 250px;` means: grow to fill, shrink if
needed, with a base of 250px. On wide screens the
cards spread out; on narrower screens they wrap.

#### Step 7 — Footer

```css
footer {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 24px;
    margin-top: 60px;
}
```

Save. Reload. **Done.** A complete, polished personal
homepage.

**Checkpoint:** *Your homepage has a navbar, hero
section, about, project cards, and footer — all
styled.* **This is the natural stop point if class is
cut short.**

---

### Part B: Make it yours

The structure is the same for everyone. The **content**
should not be.

#### Real content

Replace every word with *yours*:

- The name in the navbar/hero.
- The tagline (one sentence about you — interest,
  hobby, vibe).
- About paragraph(s).
- Project cards — your actual Phase 6 projects, their
  real GitHub URLs (if you've pushed), your real
  descriptions.
- Footer — your real name and year.

**Don't leave any "Alex" or "lorem ipsum."** Make
every word real.

#### Pick a personality

Customize colors. Pick 2-3 that work together:

```css
/* Calm — blue/grey */
--primary: #2c3e50;
--accent: #3498db;
--bg: #f7f7f7;

/* Warm — orange/terra */
--primary: #6b3838;
--accent: #d35400;
--bg: #fdf6e3;

/* Dark — modern dev vibe */
--primary: #1a1a2e;
--accent: #e94560;
--bg: #0f3460;
--text: #f0f0f0;

/* Soft — pastel */
--primary: #6c5b7b;
--accent: #c06c84;
--bg: #f8e7e7;
```

Then in CSS:

```css
:root {
    --primary: #2c3e50;
    --accent: #3498db;
    --bg: #f7f7f7;
}

body { background-color: var(--bg); }
.navbar { background-color: var(--primary); }
.btn { background-color: var(--accent); }
```

`:root` defines CSS variables. `var(--name)` uses
them. Change one variable, the whole page changes.

#### Real images

Find or take real images:

- A photo (or avatar / cartoon you).
- Screenshots of your Pygame projects.
- Hobby photos.

Add `<img src="..." alt="...">` where it fits. Style:

```css
img {
    max-width: 100%;    /* never wider than its container */
    border-radius: 8px;
}

.hero img {
    width: 200px;
    height: 200px;
    border-radius: 50%;    /* circle */
    border: 4px solid white;
}
```

#### Stretch — multi-page

Add real `about.html` and `projects.html` pages.
Update the nav to link to them. Each page has the
same navbar (copy-paste). Real multi-page site.

#### Stretch — favicon

A favicon is the tiny icon in the browser tab. Find a
small PNG (or use one of your sprite assets), save as
`favicon.png` in your folder, and add to `<head>`:

```html
<link rel="icon" type="image/png" href="favicon.png">
```

Reload. Your icon shows in the tab. **Tiny detail,
big "real site" feeling.**

#### Extension — responsive design

Real sites adjust to phone screens. You can add this:

```css
@media (max-width: 600px) {
    .navbar {
        flex-direction: column;
        gap: 12px;
    }
    
    .hero h1 {
        font-size: 36px;
    }
    
    .content-section {
        padding: 40px 16px;
    }
}
```

`@media (max-width: 600px)` says "these rules apply
**only when the screen is 600 pixels or narrower**."
Resize your browser window to test.

This is **mobile-first / responsive design.** A real
modern web skill.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your homepage. Tour us through
  it.
- What's the personality you went for?
- For the kids who used CSS variables — how did the
  one-place-changes-everything feel?
- For the kids who tested at narrow widths — does
  it look OK on phone-ish screens?

Today you built **a real, polished website.** Not a
toy. The kind of thing you could actually share with
people. (And you will — Session 15 puts it on a
public URL.)

You used:

- **Semantic HTML** (`<header>`, `<main>`, `<section>`,
  `<footer>`).
- **External CSS** with `box-sizing: border-box`.
- **Flexbox** for navbar and card layouts.
- **The box model** — padding, margin, borders, shadows.
- **Custom typography and colors** — your style.
- **Hover transitions** — real polish.

Next week we add **forms** — text inputs, checkboxes,
buttons that look right. Then comes JavaScript.

### If you missed this session

Open Thonny.

1. Create a folder for your homepage. Create
   `index.html` and `styles.css`.

2. Type the HTML structure (navbar, hero, sections,
   footer) from Part A.

3. Type the CSS in steps 2-7. Reload after each
   step.

4. Customize content and colors to be *yours*.

About 60-90 minutes — this is a long, integrated
session.

### Stretch and extension ideas

- **CSS variables** for a centralized color palette.
- **Multi-page site** — about.html, projects.html.
- **Favicon** in the browser tab.
- **Responsive design** with `@media` queries.
- **Smooth scroll** on nav clicks:
  ```css
  html { scroll-behavior: smooth; }
  ```
- **Sticky navbar** — stays at the top while
  scrolling:
  ```css
  .navbar { position: sticky; top: 0; z-index: 10; }
  ```
- **Animations** — subtle fade-in on scroll. Advanced
  (uses JS), but a stretch.
- **Real screenshots** of your projects in the cards.

### What's next

Next week: **forms** — input fields, text areas,
checkboxes, dropdowns, buttons. The web's input
controls. Then we tackle JavaScript and make
everything *do* things.
