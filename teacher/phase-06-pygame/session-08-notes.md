## Session 8 — Teacher Notes

*Phase 6, Pygame · Session 8 of 14 · Title: Sound and
music*

### Purpose of this session

The "feel" session. Five jobs, in priority order:

1. **Land the two-API split.** `mixer.Sound` for short
   effects, `mixer.music` for long tracks. Different
   APIs, different use cases.
2. **Land "load once, play many."** Same as images.
   Loading audio every frame would be terrible.
3. **Land sound triggered from game events.** Sound
   isn't ambient — it's tied to what's happening
   (bounce, score, win).
4. **Make the games feel alive.** Sound is the highest
   signal-to-code-volume polish in any game.
5. **Encourage iteration.** Push the new sound version
   to GitHub (Session 7 callback) — "iterate and
   re-push" is a real workflow.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Pygame and pre-distributed sound
  asset folder.
- Pre-built Pong with sound (bounce, wall, score) for
  comparison.
- Pre-built Pong with sound + music for the "wow" demo.
- A WAV/OGG file collection on every student machine
  (free CC0 sounds from freesound.org or kenney.nl).

**Prep time:** ~25 minutes. Sound assets need to be on
every machine. Pre-test that audio actually plays on
the class hardware (Pygame audio on Linux can be flaky
if PulseAudio isn't running).

### Timing and flow

Total: ~90 min.

- **Welcome and recap** (~5 min). Recap Session 7 (push
  to GitHub).
- **Part A: sound effects** (~30 min). Two-API split,
  load + play, add to a game.
- **Break** (~5 min).
- **Part B: background music** (~25 min). Load, play,
  loop, mute toggle.
- **Stretches** (~15 min). Random variations, recorded
  sounds, push to GitHub.
- **Wrap-up** (~10 min).

If running short: **stretches can be cut.** The base
goal — at least one sound playing in their game — is
the priority.

### Teaching Part A

#### The two-API split

Worth time on the board:

```
mixer.Sound                   mixer.music
────────────                  ────────────
Short clips                   Long tracks
Many at once                  One at a time
Loaded fully                  Streamed
Effects: bounces, dings       Background music
.wav (best)                   .ogg (best)
sound.play()                  music.play(-1)
```

Frame:

> "Sound effects are short and you might play many at
> the same time. Music is long and you only have one
> playing at a time. Different APIs because they have
> different jobs."

#### Load once, play many

Same teaching as Session 3 (images). Reinforce:

> "Loading sound is slow. If you put the load inside
> the loop, your game crawls. Load once, before the
> loop. Play as many times as you want inside."

Walk to confirm every kid has loads outside the loop.

#### Where to trigger sounds

Sounds tie to **game events.** Show the pattern: find
the line where the event happens (`if colliderect:`),
add `sound.play()` right after.

Common in Pong:

- Wall bounce: `if ball.top < 0 or ball.bottom > HEIGHT:`
- Paddle bounce: `if ball.colliderect(paddle):`
- Score: `if ball.right < 0 or ball.left > WIDTH:`

The sound is *part* of the event handler.

#### Volume

Sounds default to full volume — usually *too loud*
relative to background music. Suggest defaults:

- Background music: 0.3-0.5
- Sound effects: 0.5-0.8

Mention but don't drill — kids will tune.

#### Linux audio gotchas

Pygame audio on Linux can fail if:

- PulseAudio not running.
- Wrong audio device (HDMI vs analog).
- ALSA conflicts.

Symptoms: program runs, no error, no sound. Or audio
crackling.

Quick fixes:

- `pulseaudio --start` from terminal.
- Check audio device in system settings.
- Restart Thonny / restart the script.

If audio is flaky on a kid's machine, troubleshoot
briefly. If not fixable in class, the kid can still
write the code (it just won't make noise). Catch up
next session.

### Teaching Part B

#### Music is one line difference from sound

Frame:

> "Music is even easier. One line to load, one line to
> play. The trick: `play(-1)` means *loop forever.*
> Without that, music plays once and stops."

Run a "no -1" demo: music plays through once, then
silence. Then add the -1: continuous loop.

#### Mute key

Real games have one. Show the toggle pattern:

```python
if event.key == pygame.K_m:
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
```

`get_busy()` returns True if music is currently
playing (vs paused or stopped). Useful check.

#### Random variation is the polish

The "list of bounce sounds, random.choice each time"
trick is *the* small upgrade that makes a game feel
professional. Real Pong (and pinball, and fighting
games) all do this.

Frame:

> "Real game audio doesn't repeat the *same* sound on
> every bounce. It picks from a small variety. Three
> slightly different bounce sounds, randomly chosen,
> feels way more alive than one repeating sound."

### Common stumbles

- **No sound at all.** Most often a Linux audio issue
  (above). Sometimes wrong file path. Sometimes wrong
  format.
- **`pygame.error: Unable to open file`.** Filename
  typo, file not in the right folder.
- **`pygame.error: ModPlug_Load failed`.** Bad file
  format. Convert to standard WAV/OGG.
- **Sound plays but distorted.** Sample rate mismatch.
  Resample to 44100 Hz (or whatever the file should be).
- **Sound effects too loud.** Set lower volume.
- **Music plays once and stops.** Forgot the `-1` in
  `play(-1)`.
- **Music interrupts itself.** Multiple `play()` calls
  with `mixer.music`. It should only be triggered once.
- **Mute key works but unmute doesn't.** `get_busy()`
  returns False when paused — kids might confuse the
  states. Walk through.
- **Sound repeats every frame.** Trigger condition stays
  true for multiple frames (e.g., paddle and ball
  overlap for 2-3 frames). Sound plays 60 times per
  second. Solution: add a flag or check that prevents
  re-triggering until the condition resolves. Or use a
  cooldown. (For Pong, the ball bounces away after one
  frame so this rarely happens.)

### Differentiation

- **Younger kids (9-10):** Goal is *one* sound playing
  in their game. Music + variations is a stretch.
- **Older kids (12+):** Push for sound + music. Mute
  toggle as a stretch.
- **Advanced (any age):** Suggest:
  - Random sound variations
  - Recording own voice as game sound
  - Music switches based on game state
  - Volume control with keyboard
  - Sound channel pinning
- **Struggling:** A kid who can't get any sound playing
  is the kid you focus on. Most common cause: file path
  or audio system issue.

### What to watch for

- **The "wait, my game has SOUND now?" reaction.** First
  successful bounce sound. Visible delight.
- **Kids playing each other's games.** Sound makes games
  more fun to share — encourage.
- **Annoying sound spam.** Some kids will set everything
  to volume 1.0 and wonder why their game is unbearable.
  Suggest tuning.
- **Buddies recording each other for sounds.** Real game
  development practice. Encourage if there's time.
- **Kids tempted to spend the whole session picking the
  perfect sound from freesound.org.** Redirect: "Use
  any sound that works. Polish later."
- **Pushing to GitHub.** Encourage kids who got Session
  7 working to commit and push the sound update.
  "Iterate and ship" is a real workflow habit.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked / didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Session 9 (sprite classes).** Sound effects can live
  *on* the sprite (the `Bullet` sprite plays its own
  fire sound). Cleaner organization.
- **Sessions 10-11 (grid-world).** Sound for puzzle
  solved, character moved, victory.
- **Session 12 (game state).** Different music per state
  — title screen music, gameplay music, game-over music.
- **Sessions 13-14 (milestone).** Their milestone games
  benefit hugely from sound. Push them to add at least
  one sound.
- **Phase 7 (web).** HTML5 Audio API has the same
  conceptual split (short clips vs music). Today's mental
  model transfers.
- **Peanut butter callback opportunity:** the `play(-1)`
  vs `play()` distinction is a precision moment. The
  computer plays *exactly* the number of times you say.

### Materials checklist

- [ ] Demo machine with Pygame + sound asset folder
- [ ] Sound asset folder on every student machine
- [ ] Pre-built Pong with sound effects
- [ ] Pre-built Pong with music + effects
- [ ] Audio working on demo machine (test before class)
- [ ] Optional: Audacity installed for kids who want to
      record their own sounds
- [ ] Projector
- [ ] Class roster
