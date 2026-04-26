## Session 7: Forms — inputs, labels, buttons

*Phase 7 — Web · Session 7 of 17*

### What we're learning today

Forms are how users **send information** to a website
— sign-ups, searches, contact forms, comments, polls.
Today you learn the form-related HTML tags (input,
label, textarea, select, button) and how to style
them. By the end you'll have built a contact form
that *looks* right. Next sessions (after we learn
JavaScript) we'll make it actually *do* things.

### You'll need to remember from last time

- **HTML basics** — tags, attributes.
- **CSS basics** — selectors, properties.
- **The box model** — padding, margin, border.
- **Flexbox** — `display: flex`, `gap`,
  `align-items`.
- **Phase 5 customtkinter** (a callback) — entries,
  checkboxes, radios. Same shapes; different language.

---

### Part A: The form tags

#### `<form>` — the container

Every form is wrapped in a `<form>` tag:

```html
<form>
    <!-- inputs go here -->
    <button type="submit">Send</button>
</form>
```

A `<form>` *does something* when submitted. Without
extra setup, it tries to send the data to a URL —
which we don't have a server for, so today it'll
*look* right but not actually send anywhere. We'll
wire it up with JavaScript starting Session 9.

#### `<input>` — text fields and more

The single most useful form tag. Self-closing.

```html
<input type="text" name="username" placeholder="Your name">
```

The `type` attribute changes what kind of input:

- **`text`** — single-line text.
- **`email`** — text, but the browser will validate
  it looks like an email.
- **`password`** — text, hidden as dots.
- **`number`** — only digits. Can have `min`, `max`,
  `step`.
- **`date`** — date picker.
- **`color`** — color picker.
- **`file`** — file upload.
- **`checkbox`** — yes/no toggle.
- **`radio`** — pick one of many.
- **`range`** — slider.
- **`submit`** — a button that submits the form.

The `name` attribute is the form's *key* for that
input. The `placeholder` is grey text that shows
inside an empty field.

#### `<label>` — connect text to inputs

A label tells the user what an input is for. **Always
use one.** Two ways:

```html
<!-- Wrap the input -->
<label>
    Email:
    <input type="email" name="email">
</label>

<!-- Or use the for attribute -->
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

The second form (with `for=` matching `id=`) is more
flexible. **Both forms link the label to the input** —
clicking the label focuses the input. **Required for
accessibility** (screen readers announce the label).

#### `<textarea>` — multi-line text

For long text (comments, messages, descriptions):

```html
<textarea name="message" rows="4" cols="40" placeholder="Your message"></textarea>
```

Note: `<textarea>` has separate opening and closing
tags. Whatever's inside is the *initial value*.

`rows` and `cols` are size hints. CSS overrides them.

#### `<select>` — dropdown

```html
<label for="color">Favorite color:</label>
<select id="color" name="color">
    <option value="red">Red</option>
    <option value="green">Green</option>
    <option value="blue">Blue</option>
</select>
```

Like Phase 5's CTkOptionMenu. The `value` is what
gets sent (could differ from what's shown).

#### `<button>` — buttons

```html
<button type="submit">Send</button>
<button type="button">Reset</button>
<button type="reset">Clear all fields</button>
```

`type="submit"` submits the form. `type="button"`
does nothing on its own (you'll wire it up with JS).
`type="reset"` clears all the inputs.

`<button>` is more flexible than
`<input type="submit">` — it can contain HTML inside
(icons, multi-color text, etc.).

#### Build a contact form

Create a new HTML file (or section in your homepage):

```html
<form class="contact-form">
    <h2>Get in touch</h2>
    
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Your name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="you@example.com" required>
    
    <label for="topic">Topic:</label>
    <select id="topic" name="topic">
        <option value="general">General question</option>
        <option value="bug">Bug report</option>
        <option value="other">Other</option>
    </select>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="5" placeholder="Your message" required></textarea>
    
    <label>
        <input type="checkbox" name="newsletter">
        Subscribe to my newsletter
    </label>
    
    <button type="submit">Send</button>
</form>
```

Save. Reload. **A form appears** — but it looks raw.
CSS next.

What's new:

- **`required`** — the browser won't let the form
  submit if the field is empty. Free validation.
- **The checkbox label wraps the checkbox** so the
  whole text is clickable.
- **`<select>` with `<option>`s** for the dropdown.

**Checkpoint:** *You have a form with at least one
text input, one textarea, one select, and a submit
button.* **This is the natural stop point if class is
cut short.**

---

### Part B: Style your form

A raw form looks ugly. Time to fix that.

#### Form container

```css
.contact-form {
    max-width: 500px;
    margin: 40px auto;
    padding: 32px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    gap: 16px;
}
```

The form is a flex *column* with `gap: 16px;` between
each child. Means we don't need vertical margins on
each input — clean.

#### Labels and inputs

```css
.contact-form label {
    font-weight: 600;
    color: #2c3e50;
}

.contact-form input,
.contact-form textarea,
.contact-form select {
    padding: 10px 12px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: inherit;
}
```

`font-family: inherit` makes form inputs use the
same font as the page. By default, browsers use a
system default that doesn't match.

#### Focus state

When the user clicks an input, the border should
*change* to indicate focus:

```css
.contact-form input:focus,
.contact-form textarea:focus,
.contact-form select:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}
```

`:focus` is a pseudo-class (like `:hover`). The
`outline: none;` removes the browser's default focus
ring; the box-shadow gives a softer one.

#### Button

```css
.contact-form button {
    padding: 12px 24px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s;
    align-self: flex-start;    /* don't stretch full width */
}

.contact-form button:hover {
    background-color: #2980b9;
}
```

`align-self: flex-start` is a Flexbox trick — overrides
the default `stretch` for *just this one item*.
The button doesn't stretch to full width.

Save. Reload. **A polished form** — clean inputs,
focus indicators, styled button.

#### Checkbox row

The checkbox label wrapping looks weird with the rest
of the column. Style it as a horizontal row:

```css
.contact-form label.checkbox-label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: normal;
}
```

Update the HTML:

```html
<label class="checkbox-label">
    <input type="checkbox" name="newsletter">
    Subscribe to my newsletter
</label>
```

Checkbox and text now sit side by side.

#### Stretch — radio buttons

For "pick one of these":

```html
<fieldset>
    <legend>How did you find me?</legend>
    <label><input type="radio" name="source" value="google"> Google</label>
    <label><input type="radio" name="source" value="friend"> A friend told me</label>
    <label><input type="radio" name="source" value="other"> Other</label>
</fieldset>
```

`<fieldset>` groups related form fields with a
border; `<legend>` is the title for the group.

```css
fieldset {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 16px;
}

legend {
    padding: 0 8px;
    font-weight: 600;
    color: #2c3e50;
}
```

#### Stretch — input validation hints

The browser auto-validates `required` fields and
`type="email"` formats. You can also use:

- **`minlength="3"`** on text inputs.
- **`maxlength="100"`** on text inputs.
- **`min="0" max="100"`** on number inputs.
- **`pattern="[A-Za-z]+"`** for regex matching.

When the user tries to submit with invalid data,
the browser shows a popup. **No JavaScript needed.**

#### Stretch — placeholder vs label

`placeholder="Your name"` shows grey text inside
the empty input. **Doesn't replace the label** —
it disappears as soon as you type. Use both:

- Label: what the field *is*.
- Placeholder: example or format hint.

#### Extension — disabled and readonly

```html
<input type="text" name="username" value="alex" readonly>
<button type="submit" disabled>Send</button>
```

`readonly` — user can't change the value but can
focus / copy.
`disabled` — user can't interact at all (greyed out).

Useful for "you can't submit until X is true" or
"you can't change your username here."

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your form. Did the styling
  click?
- Did you discover the focus state? (Click in a
  field; watch the border change.)
- Did anyone notice the form *almost works* — pressing
  submit reloads the page with the data in the URL?
  We'll fix that with JavaScript.
- Anyone use `required` and try to submit empty?
  Free validation.

Today you learned:

- **`<form>`** — the container.
- **`<input>`** — many types (text, email, number,
  checkbox, radio, etc.).
- **`<label>`** — connect text to inputs (use `for=`/
  `id=`, or wrap).
- **`<textarea>`** — multi-line text.
- **`<select>` + `<option>`** — dropdowns.
- **`<button>`** — buttons.
- **`required`, `placeholder`, `disabled`,
  `readonly`** — useful attributes.
- **CSS form styling** — focus states, padding,
  consistent fonts.
- **`:focus` pseudo-class** for visible feedback.

You can now build any form a website might need —
sign-up, login, search, contact, survey, settings.
The shapes are the same.

Next week: **JavaScript** — making the form *do*
something when submitted (and making the page do
all sorts of things on demand).

### If you missed this session

Open Thonny.

1. Build the basic contact form from Part A.

2. Style it (Part B steps). Make sure focus states
   work.

3. (Stretch) Add radio buttons in a fieldset.

About 30-45 minutes. By the end you should have a
styled form.

### Stretch and extension ideas

- **Different input types** — date, color, range,
  number, file. Each one has unique behavior.
- **Required field validation** — the browser handles
  it.
- **`fieldset` + `legend`** for grouping.
- **Custom validation messages** — `pattern=`,
  `minlength=`, etc.
- **Multi-step forms** — show some fields, hide
  others until they're filled. Advanced (uses JS).
- **Search bar** — a simple `<form>` with one
  `<input type="search">` and a button. Common
  pattern.
- **Real form on your homepage** — add a contact
  form below your projects.

### What's next

Next week is **the big language pivot:** JavaScript.
We move from HTML/CSS (structure and style) to *JS
(behavior)*. Variables, loops, functions — but
**different syntax** from Python. We'll compare
side-by-side.
