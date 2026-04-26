## Session 3 — Teacher Notes

*Phase 6, Pygame · Session 3 of 14 · Title: Sprites and
images*

### Purpose of this session

The "shapes → real art" jump. Five jobs, in priority
order:

1. **Land `pygame.image.load` + `blit`.** The two-line
   pattern that puts any image on screen.
2. **Land "load once, blit every frame."** Big enough
   pitfall to call out explicitly. Reloading every frame
   tanks performance.
3. **Land the Rect class.** This is foundation for
   collision detection (Session 5) and sprite groups
   (Session 9). Master rect.x/y, center, get_rect now.
4. **Land lists-of-rects** for handling many objects.
   A coin field, a starfield, an enemy wave — all the
   same pattern.
5. **Set up Session 4 (input).** Today the sprite moves
   on its own or with the mouse. Next: keyboard control.

### Before class

**Bring:** nothing physical (assuming kids' machines
have the assets folder pre-populated).

**Set up:**

- Demo machine with Pygame.
- A folder of free game sprites — a few characters, a few
  enemies, a few collectibles. Free sources:
  [opengameart.org](https://opengameart.org),
  [kenney.nl](https://kenney.nl) (Kenney's CC0 sprites
  are perfect for this).
- Pre-built sprite-following-mouse demo.
- Pre-built multi-sprite scene (player + enemies + coins).

**Prep time:** ~25 minutes. The sprite assets need to be
on every machine before class. Either pre-installed or
distributed via USB / shared folder.

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Sessions 1-2.
  Today: real images.
- **Part A: load + blit** (~15 min). Type the minimum
  program, see the sprite appear.
- **Part A: Rect** (~20 min). `get_rect`, properties,
  `move_ip`, `center=`.
- **Break** (~5 min).
- **Part B: multiple sprites + lists** (~30 min). The
  scene + the random-coins pattern.
- **Part B: stretches** (~10 min). Scale, rotate, flip
  for kids who finish.
- **Wrap-up** (~5 min).

If running short, **scale/rotate/flip can be cut.** The
Rect mastery is the priority — it's prereq for Session 5.

### Teaching Part A

#### "Where do I get sprites?"

Distribute the pre-staged sprite folder. Each kid should
have at least 3-4 sprites available. If a kid wants to
draw their own, encourage but don't burn class time — too
slow.

For the sprites in class:

- Pick small ones (32×32 to 128×128 pixels). Bigger is
  fine but harder to position.
- Pre-test that they render correctly (transparency
  works, no weird black backgrounds).

#### File path matters

A common stumble: the image is in `Downloads/` but the
script expects it next to the .py file. Walk through:

> "Pygame looks for the file *next to your .py file*. If
> the file is in Downloads, copy it to where your script
> lives. Or use the full path: `pygame.image.load('C:/Users/...')`."

For Linux/Mac, paths use `/`. For Windows, paths can use
either `/` or `\\`. Don't use single `\` — Python sees it
as escape character.

#### Load once, draw many

Frame this clearly:

> "Loading the image *reads it from disk*. Reading from
> disk is *slow* — like, thousands of times slower than
> drawing. If you put `image.load` *inside* the loop, you
> do that slow thing 60 times a second. Your game will
> crawl.
>
> Load once, before the loop. Then `blit` over and over
> inside the loop."

Same pattern for fonts (Session 2 stretch), sounds
(Session 8), and any other resource.

#### Rect properties

The Rect's API is genuinely useful and worth teaching:

```python
rect.x, rect.y                      # top-left
rect.width, rect.height             # size
rect.left, rect.right               # x edges
rect.top, rect.bottom               # y edges
rect.center, rect.centerx, rect.centery
rect.topleft, rect.topright
rect.bottomleft, rect.bottomright
rect.midtop, rect.midbottom
rect.midleft, rect.midright
```

You can *set* any of these and the rect re-aligns. So
`rect.midbottom = (300, 400)` puts the rect's middle-bottom
point at (300, 400) — useful for "stand on the floor"
positioning.

Don't drill all of these. Show `center`, `topleft`, `right`,
`bottom`. Mention the others exist.

#### `get_rect(center=(x, y))` is the killer trick

The shortest pattern:

```python
player_rect = player_image.get_rect(center=(300, 200))
```

Three things in one line: get rect, position by center,
assign. Push this as the standard idiom.

### Teaching Part B

#### The "many sprites" insight

Same image, many rects. This is the conceptual
foundation for sprite groups (Session 9). Walk through
slowly:

> "We have *one* coin image. But we have *many* coins on
> screen — 10, 20, 100, doesn't matter. Each coin has its
> *own* rect (its own position). The image is shared.
>
> To draw all of them: loop through the list of rects,
> `blit` the same image at each."

This is real game architecture. Bullet hells, particle
systems, even simple coin collection — same shape.

#### Mouse-following sprite

Easy and engaging. The single line:

```python
player_rect.center = pygame.mouse.get_pos()
```

Notice we're calling `pygame.mouse.get_pos()` (a function
that returns the current mouse position) every frame.
Pygame's input is *poll-based* for mouse — same pattern
as `pygame.key.get_pressed()` (next session).

#### Stretches by interest

Push the right kid to the right stretch:

- Visual kid → scale, rotate, flip
- Procedural kid → random coin field
- Animation kid → background image + foreground sprite

### Common stumbles

- **`FileNotFoundError` from `image.load`.** File isn't
  next to the script. Walk through file paths. On Linux
  Mint, the working directory matters — running from
  Thonny vs terminal can change it.
- **Black box around sprite.** PNG didn't have
  transparency, or `convert_alpha()` not called. Use
  `pygame.image.load(...).convert_alpha()` for proper
  transparency. (We skip this in the handout to keep
  it simple, but mention it for advanced kids.)
- **Sprite at wrong position.** `(x, y)` is the top-left
  *corner*, not the center. Confusing for a 64×64 sprite
  centered around the wanted point. Use `get_rect(center=...)`
  instead.
- **"Why isn't my image moving?"** Forgot to update the
  rect inside the loop. Or updated `x` variable but
  blitted with `(300, 200)` hardcoded.
- **Multiple sprites blit but only one shows.** They're
  all at the same position. Sprite below is hidden by
  sprite above. Move them apart.
- **Image too big / too small.** Use `pygame.transform.scale`
  to fit to the screen.
- **`AttributeError: 'tuple' object has no attribute 'x'`.**
  Used a tuple where a Rect was expected. Walk through:
  rect comes from `get_rect()`, not directly.
- **`move_ip` confusion.** `(2, 0)` moves right; `(0, 2)`
  moves down. Some kids try `(2)` (single value) which is
  not a tuple.

### Differentiation

- **Younger kids (9-10):** Goal is one sprite that follows
  the mouse. Multiple sprites is a stretch.
- **Older kids (12+):** Push for the multi-sprite scene
  with the random-coins pattern.
- **Advanced (any age):** Suggest:
  - A background image + multiple foreground sprites
  - Sprite that grows/shrinks based on mouse position
  - Walking animation (alternate between two pose images
    every few frames)
  - A starfield (50+ sprites at random positions, each
    moving slowly)
- **Struggling:** A kid who can't get one sprite on screen
  is the kid you focus on. Most common cause: file path
  wrong, or forgot to put image in the right folder.

### What to watch for

- **The "wait, that's MY character?" reaction.** Some kids
  bring their own art (drew it in Paint, downloaded
  something). Encourage; their game becomes *theirs*
  immediately.
- **The temptation to make their game *look* impressive
  before it works.** Some kids will spend 30 minutes
  picking sprites instead of coding. Gentle nudge: "Get
  one sprite working first, then pick the perfect art
  later."
- **Buddies trading sprites.** Encourage. Sharing assets
  is real game-dev practice.
- **Confusion with the Rect class.** A few kids will
  struggle with "is this a tuple or a Rect?" Walk through
  the difference patiently.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 4 (input).** Today's mouse-follow becomes
  keyboard control.
- **Session 5 (collision).** Today's "the coins don't
  react" becomes "now they do." Rects are the mechanism.
- **Session 9 (sprite classes).** Today's "image + rect +
  position" pattern wraps into a `Sprite` class.
  Multiple sprites become a `Group`.
- **Phase 7 (web).** Browser canvas API also has
  `drawImage(image, x, y)`. Same conceptual model.
- **Peanut butter callback opportunity:** loading the
  image inside the loop instead of outside is a precision
  moment. The computer does what you say — and if you say
  "load the image 60 times a second," it does.

### Materials checklist

- [ ] Demo machine with Pygame
- [ ] Sprite asset folder distributed to all student
      machines (or available on shared drive)
- [ ] Pre-built mouse-follow demo
- [ ] Pre-built multi-sprite scene
- [ ] Optional: Kenney's CC0 sprite pack URL printed for
      students who want to use them at home
- [ ] Projector
- [ ] Class roster
