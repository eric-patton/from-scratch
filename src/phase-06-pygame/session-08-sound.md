## Session 8: Sound and music

*Phase 6 — Pygame · Session 8 of 14*

### What we're learning today

Your games have been **silent.** Today changes that.
Pygame's `mixer` plays sound effects (short clips like
a "bounce" or a "ding") and music (longer tracks that
loop in the background). By the end of class, your Pong
will *sound* like a game — paddle bounces, scoring, and
maybe even background music.

Sound is the smallest amount of code with the biggest
"feel" change in any game.

### You'll need to remember from last time

- **Your Pong project** from Session 6 (or any other
  game).
- **Loading resources outside the loop** — Session 3.
  Same idea applies to sounds.
- **`pygame.event.KEYDOWN`** — Session 4. Sounds usually
  trigger from events.

### What you'll need today

- Some **sound files.** In class, there's a folder of
  free game sounds for you. At home, you can grab free
  sounds from [freesound.org](https://freesound.org) or
  [opengameart.org](https://opengameart.org).
- A working game (Pong, fruit catcher, collector — any
  one works).

---

### Part A: Sound effects

#### Two kinds of audio

Pygame splits audio into two APIs:

- **`pygame.mixer.Sound`** — short clips (a beep, a
  bounce, a click). Can play many at once. Loaded fully
  into memory.
- **`pygame.mixer.music`** — long tracks (background
  music, a song). Streamed from disk, only one at a
  time.

Use **Sound** for game effects. Use **music** for
background tracks.

#### Loading and playing a sound

The basic pattern. Open a copy of your Pong (or any
game). Add at the top:

```python
pygame.init()
# ... existing setup ...

# Load sounds — once, outside the loop
bounce_sound = pygame.mixer.Sound("bounce.wav")
score_sound = pygame.mixer.Sound("score.wav")
```

Inside the loop, where the relevant thing happens:

```python
if ball_rect.colliderect(left_paddle):
    ball_dx = -ball_dx
    bounce_sound.play()    # ← here
```

```python
if ball_rect.right < 0:
    right_score += 1
    reset_ball()
    score_sound.play()     # ← here
```

Save. Run. **You should hear a sound when the ball
bounces.** And a different one when someone scores.

That's it. Two lines per sound.

#### Sound formats

Pygame supports `.wav`, `.ogg`, and `.mp3` (with the
right system libraries — sometimes spotty on Linux).

- **WAV** — uncompressed. Big files, instant load,
  perfect quality. Best for sound effects.
- **OGG** — compressed, open format. Smaller files,
  good quality. Best for music.
- **MP3** — compressed, common. Sometimes works,
  sometimes doesn't. Convert to OGG if you have issues.

For sound effects (short clips), **stick to WAV.**

#### Volume

Sounds can be quieter. Set volume from `0.0` (silent)
to `1.0` (full):

```python
bounce_sound.set_volume(0.4)
```

Per-sound, set once after loading. Or change at runtime
to make a sound fade.

You can also set the *channel*'s volume — but for most
games, per-sound is enough.

#### Sound + boundaries

Add a "wall bounce" sound for when the ball hits the top
or bottom:

```python
wall_sound = pygame.mixer.Sound("wall.wav")

# in update:
if ball_rect.top < 0 or ball_rect.bottom > HEIGHT:
    ball_dy = -ball_dy
    wall_sound.play()
```

The two-tone "bonk-bing" of a Pong bounce comes from
having different sounds for paddle vs wall hits.

**Checkpoint:** *Your game plays sounds when at least
two different things happen.* **This is the natural
stop point if class is cut short.**

---

### Part B: Background music

Now the long-form audio. Music plays continuously while
the game runs.

#### Load and play

```python
pygame.mixer.music.load("background.ogg")
pygame.mixer.music.set_volume(0.3)    # quieter than effects
pygame.mixer.music.play(-1)            # -1 means loop forever
```

The `play(-1)` is the key — it loops the track
indefinitely. `play(1)` plays it once. `play(3)` plays
it three times, then stops.

Add this **once, near the start of your program** (after
`pygame.init()`). The music starts playing immediately.

Run. Background music plays. Sound effects (paddle
bounces, scores) play *over* the music. Both work.

#### Pausing and stopping music

Common controls:

```python
pygame.mixer.music.pause()    # pause
pygame.mixer.music.unpause()  # resume
pygame.mixer.music.stop()     # stop completely
pygame.mixer.music.set_volume(0.0)    # silent (without stopping)
```

Often games have a key to mute. In your event handling:

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_m:
        # toggle music
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
```

Press **M** to toggle music.

#### Stretch — switch tracks for game over

When the game ends, switch from upbeat music to
something more dramatic. You'll need a second track:

```python
# at game over:
pygame.mixer.music.load("game_over.ogg")
pygame.mixer.music.play()    # play once
```

You can `load` a new track at any time.

#### Stretch — sound channels

For more advanced control, Pygame uses *channels.* By
default sounds play on whichever channel is free; you
can also pin a sound to a specific channel:

```python
channel = pygame.mixer.Channel(0)
channel.play(bounce_sound)
channel.set_volume(0.5)
```

Useful for "I want this kind of sound to never overlap
itself" or "I want music in one channel and effects in
another." Don't drill — mention only if asked.

#### Extension — record your own sound

Free apps like Audacity (or any phone voice recorder)
let you record short clips. Save as WAV. Use as game
sounds. **Your game now has *your voice* or *your tap*
in it.**

If you have a buddy nearby, record them saying "score!"
or "ouch!" and use it. Suddenly it's *your* game.

#### Extension — sound for every event

Add a sound for everything:

- Game start: an intro sound.
- Each score: a different ding.
- Bouncing off a wall vs paddle: two sounds.
- Each paddle: different sounds (left vs right).
- A "warning" sound when one player is one point from
  losing.

Each one is two lines of code (load + play). Add up to
a *very* polished feel.

---

### Wrap-up

Before we leave, share with the room:

- For everyone — show your game with sound. Did the
  feel change?
- For the kids who added music — what music?
- Anyone find or record a particularly satisfying sound?
- (Honest question:) Is your game more fun with sound?
  Or just *louder*?

Today you learned:

- **Two audio APIs:** `mixer.Sound` (effects) and
  `mixer.music` (music).
- **Load once, play many times** — same pattern as
  images.
- **`.set_volume(0.0 - 1.0)`** for individual sounds.
- **`.play(-1)` for looping** background music.
- **Sound triggers from events or game state** — bounce,
  score, lose.

Sound is the **smallest amount of code with the biggest
feel change** in any game. Two lines per sound. Huge
difference.

Next up: **sprite classes and groups** — using Phase 4's
classes properly. Your games have many objects — bullets,
enemies, particles. Today you'd track each in a list.
Next session, sprites become real *Sprite* instances,
and Pygame's `Group` handles them all at once.

### If you missed this session

Open Thonny. Get a sound effect (any short WAV) and
optionally a music file (any OGG).

1. Open one of your games (Pong, fruit catcher, etc.).

2. Load the sound: `bounce_sound = pygame.mixer.Sound("bounce.wav")`.

3. Play it where appropriate (collision, score, etc.):
   `bounce_sound.play()`.

4. (Stretch) Add background music:
   ```python
   pygame.mixer.music.load("background.ogg")
   pygame.mixer.music.play(-1)
   ```

5. (Stretch) Add a mute key (M).

About 30-45 minutes. By the end your game should make
noise.

### Stretch and extension ideas

- **Different sound per event** — wall bounce vs paddle
  bounce vs score vs win.
- **Volume control** — keys to turn music up/down.
- **Mute toggle.**
- **Music switches** for different game states (intro,
  playing, game over).
- **Random sound variety** — instead of one bounce
  sound, pick from a list of three each time.
  ```python
  bounce_sounds = [
      pygame.mixer.Sound("bounce1.wav"),
      pygame.mixer.Sound("bounce2.wav"),
      pygame.mixer.Sound("bounce3.wav"),
  ]
  random.choice(bounce_sounds).play()
  ```
- **Recorded sounds** — your voice, your tap, your
  whatever. WAV files work fine.
- **Sound chiptune music** — search "chiptune music free"
  for retro game-style tracks.
- **Push the new sound version to GitHub** (Session 7
  callback). `git add`, `commit -m "Add sound effects"`,
  `git push`.

### What's next

Next week: **sprite classes and groups.** Your games
have lots of objects. Tracking them in raw lists
(`fruits = []`, `enemies = []`) works for a while but
gets messy fast. Pygame's `Sprite` class and `Group`
container make organizing many objects *much* cleaner.
This is where Phase 4's classes really pay off.
