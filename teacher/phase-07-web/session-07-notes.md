## Session 7 — Teacher Notes

*Phase 7, Web · Session 7 of 17 · Title: Forms —
inputs, labels, buttons*

### Purpose of this session

Cover the form vocabulary. Five jobs, in priority
order:

1. **Land the form tag taxonomy.** Many shapes — text,
   checkbox, radio, select, textarea, button. Each
   for a different kind of input.
2. **Land label-input pairing.** `<label for="x">` +
   `<input id="x">` — the standard pattern. Required
   for accessibility.
3. **Land form styling fundamentals.** `font-family:
   inherit`, `:focus` states, button styling. Default
   browser styles look bad — kids must override.
4. **Set up Sessions 8-10 (JS).** Today: the form
   *looks* right but doesn't *do* anything. Next
   sessions: JS makes it actually work.
5. **Phase 5 callback.** customtkinter's
   CTkEntry/CheckBox/RadioButton/OptionMenu = today's
   `<input>`/`<input type="checkbox">`/`<input
   type="radio">`/`<select>`. Same shapes, different
   language.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with browser + Thonny.
- Pre-built styled contact form.
- Pre-built form with all input types (date, color,
  range, etc.) for variety demo.
- A real website with a styled form (sign-up page,
  contact page) for reference.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 6.
- **Part A — form tag tour** (~25 min). `<input>`
  types, `<label>`, `<textarea>`, `<select>`,
  `<button>`.
- **Part A — build contact form HTML** (~15 min).
- **Break** (~5 min).
- **Part B — style the form** (~30 min).
- **Wrap-up** (~10 min).

If running short, **drop the radio buttons stretch
and styled fieldset.** Base form + Part B is the
priority.

### Teaching Part A

#### Phase 5 callback

> "Phase 5 had CTkEntry, CTkCheckBox, CTkRadioButton,
> CTkOptionMenu. Today: same shapes, different
> language. The web's been doing this for decades —
> customtkinter copied the patterns."

This is genuinely orienting. The form vocabulary
maps directly:

- CTkEntry → `<input type="text">`
- CTkCheckBox → `<input type="checkbox">`
- CTkRadioButton → `<input type="radio">`
- CTkOptionMenu → `<select>` + `<option>`
- CTkButton → `<button>` or `<input type="submit">`
- CTkTextbox → `<textarea>`

Different syntax, same model.

#### Tour the input types

Walk through `type="text"`, `email`, `password`,
`number`, `date`, `color`, `checkbox`, `radio`,
`range`. For each, show what the input *looks like*
and *what it does* on the projector.

The "wow" types:

- **`type="color"`** — a color picker pops up.
- **`type="date"`** — a date picker pops up.
- **`type="range"`** — a slider.

Kids may not have seen these before. Real browser
features.

#### Label-input pairing

Spend time on the two-form pattern:

```html
<!-- Wrap form -->
<label>
    Email:
    <input type="email" name="email">
</label>

<!-- For/id form -->
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

> "Both link the label to the input. Click the label,
> the input gets focus. *Required for accessibility*
> — screen readers use the label to describe the
> input."

The `for/id` form is more flexible (the label and
input don't have to be next to each other in HTML).

Some kids will skip labels because the placeholder is
sufficient *visually*. Push back:

> "Placeholder isn't enough. It disappears as soon as
> you type. Labels stay. *Always* use labels."

#### `<button>` vs `<input type="submit">`

Both submit a form. `<button>` is more flexible
(can contain HTML). Push toward `<button>` as the
modern default.

> "`<input type="submit">` is older. `<button>` is
> the modern choice — and it can have HTML inside,
> like an icon next to text."

#### Form does GET/POST by default

Demo: build the form, hit submit. The page reloads
with the form data in the URL (`?name=Alex&email=...`).
This is the default form submission — which we'll
*intercept with JavaScript* in Session 9.

> "By default, submitting a form sends the data
> somewhere — usually a URL on a server. We don't
> have a server, so today the form *looks* right but
> the data goes nowhere useful. Next sessions, JS
> will catch the submit and *do something* with the
> data."

This hint points forward to Sessions 9-10.

### Teaching Part B

#### Default styles look terrible

Show the form before any CSS. Default browser styles
are inconsistent and ugly. Frame:

> "Browsers each style forms slightly differently.
> Without CSS, your form looks 1995. We need to
> override defaults."

#### `font-family: inherit` is the unsung hero

```css
.contact-form input,
.contact-form textarea,
.contact-form select {
    font-family: inherit;
}
```

> "Browsers default form inputs to a system monospace
> or 'serif Times' — clashes with the page font.
> `inherit` makes them match the page. Tiny detail,
> huge difference."

Demo: comment it out, see the inputs in a different
font. Add it back, watch them match.

#### Focus states are critical for UX

```css
.contact-form input:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}
```

> "When a user clicks an input, they need *visual
> feedback* that the input is selected. Without it,
> they're typing blind. The default browser focus
> ring works but looks dated; many sites replace it.
>
> Don't remove `outline` without adding *something*
> in its place — accessibility-wise, blind keyboard
> users need the focus indicator."

#### Flex column for the form

The form-as-flex-column with `gap` is clean:

```css
.contact-form {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
```

> "Each input + its label = one row. Vertical stack.
> `gap: 16px` between them. Way cleaner than margins
> on every input."

#### `align-self: flex-start` on the button

```css
.contact-form button {
    align-self: flex-start;
}
```

> "By default flex items in a column stretch to full
> width. The button shouldn't — it's a button, not a
> banner. `align-self: flex-start` overrides for just
> this one item."

A real Flexbox detail kids will use later.

### Common stumbles

- **No label connection.** `<label>Name:</label>` then
  `<input>` — they're separate. Use `for/id` or wrap.
- **Multiple inputs sharing same `name`.** Form data
  gets confused. Each text input needs its own
  `name`.
- **Radio buttons not exclusive.** All checkable.
  Forgot to give them all the *same* `name` — that's
  what groups them.
- **Form submit reloads page.** That's the default.
  Will fix in Session 9 with JS.
- **Inputs not styled.** Forgot the selector. Walk
  through.
- **`<input>` with closing tag.** Self-closing. Don't
  write `</input>`.
- **Button outside form.** Doesn't submit anything.
  Make sure submit button is inside the `<form>`.
- **Hidden focus indicator.** They removed `outline`
  but didn't replace it. Walk through.
- **`<textarea>` with `value="..."`** — doesn't work.
  Initial value goes between open/close tags.
- **Select option `value`s misaligned with display
  text.** `<option value="r">Red</option>` — sends
  "r", shows "Red". Often confusing.

### Differentiation

- **Younger kids (9-10):** Goal is the basic contact
  form (Part A) + minimal styling (just inputs and
  button). Skip radios.
- **Older kids (12+):** Push for full styled form +
  one of the stretches.
- **Advanced (any age):** Suggest:
  - All input types (try date, color, range, file)
  - Custom validation with `pattern=`
  - `fieldset` + `legend` for grouping
  - Form on their homepage from Session 6
  - Accessible focus styling
- **Struggling:** A kid who can't get a label-input
  to pair is the kid you focus on. Most common
  cause: missing `for/id`, or typo'd one.

### What to watch for

- **The "wait, color picker is built into the
  browser?" reaction.** Kids didn't know.
- **Buddies trading form designs.** Encourage.
- **Kids skipping labels because "the placeholder
  works."** Push back.
- **Excitement about `required`.** "I don't have to
  write the validation?" Right.
- **Kids trying to submit and getting confused by the
  URL change.** Use as a teaser for Sessions 9-10.
- **Kids playing with `type="color"` for 5 minutes.**
  Let them. Color pickers are fun.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 8 (JS intro).** The language. Today's
  form sits idle; soon it'll do things.
- **Session 9 (DOM).** `document.querySelector('input')`
  + `addEventListener('submit', ...)` reaches into
  forms.
- **Session 10 (todo app).** The integration with JS
  + form input.
- **Phase 8 (Flask).** Real server-side form
  handling. Today's `<form action="/submit"
  method="POST">` would post to a Flask route.
- **Career-long callback:** every site has forms.
  Every web framework eventually deals with HTML
  forms. Today is foundational.

### Materials checklist

- [ ] Demo machine with browser + Thonny
- [ ] Pre-built styled contact form
- [ ] Pre-built form with all input types
- [ ] Real website with styled form for reference
- [ ] Projector
- [ ] Class roster
