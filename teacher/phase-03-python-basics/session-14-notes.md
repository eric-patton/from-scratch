## Session 14 — Teacher Notes

*Phase 3, Python basics · Session 14 of 16 · Title: Putting it
together — a text adventure*

### Purpose of this session

The biggest single-session integration project in Phase 3.
Same role as Phase 1 Session 7 (Apples and Rocks), Phase 2
Session 7 (garden scene), and Phase 3 Sessions 7 (number
guess) and 12 (hangman) — but bigger and more ambitious.
Five jobs, in priority order:

1. **Demonstrate that students can build a world, not just a
   game round.** Hangman is one game per run. The text
   adventure is a *world the player explores.* That's a real
   step up in scope.
2. **Showcase dictionaries.** Today is the dict moment. The
   nested dict structure (rooms inside a rooms dict) is the
   most ambitious dict use in the curriculum so far.
3. **Build the world-modeling habit.** Real games and
   simulations work like this — a data structure that
   represents the world, plus code that updates it based on
   input. Today is the prototype.
4. **Encourage personalization.** Part B's "make it your
   world" is the goal-2 (programming as a tool for *their*
   things) hook. Every kid's adventure should be different.
5. **Set up Sessions 15-16 (milestone).** Today's text
   adventure is a reasonable milestone candidate for kids
   without their own ideas — they could extend it, add
   features, or build a fundamentally similar shape with
   different content.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny open.
- Pre-built complete adventure (with items and at least one
  lock) ready to demo as the destination preview. Make it fun
  — kids should *want* to play it.
- This session is the longest of Phase 3. Plan for some
  individual help time during Part B.

**Prep time:** ~30 minutes. Build the demo adventure once.
Decide a fun small world (5-7 rooms is plenty).

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was error
  handling. Anyone retrofit hangman with try/except?
- **Part A: build the world** (~45 min) — the plan ~5 min,
  rooms dict ~10 min, current room display ~5 min, game loop
  ~20 min, checkpoint ~5 min.
- **Break** (~5 min).
- **Part B: make it yours** (~30 min) — your own world ~15
  min, items / look / locked-doors stretch and extensions ~15
  min.
- **Wrap-up** (~5 min).

If running short, **all of Part B's stretch/extensions can be
cut.** The base game with the original rooms is the goal.

### Teaching Part A

#### The plan

Walk through the four-element plan at the projector or
whiteboard:

1. Rooms (a data structure)
2. Current location (a variable)
3. Game loop (input → update → output)
4. Win condition (an `if` check)

> "Today's program has more *parts* than anything we've
> built. The trick is: each part is something you already
> know. Rooms are a dictionary. Current location is a
> variable. The game loop is `while True:`. The win check is
> `if`. We just put them together."

This decomposition framing is the goal-1 lesson made concrete.

#### Build the rooms

The dict-of-dicts structure is the new pattern. Walk through
slowly at the projector:

```python
rooms = {
    "entry": {
        "description": "You're in a dark entryway...",
        "north": "kitchen",
        "east": "library"
    },
    ...
}
```

Lots of curly braces. Worth pointing out:

> "The outer dict has room names as keys. Each value is itself
> a dict. So `rooms['entry']` gives you back the entry room's
> dict — its description, its exits. Then `rooms['entry']
> ['north']` gives you the room you'd reach by going north
> from the entry."

Indentation is critical for readability but Python doesn't
require it inside a literal dict. Be consistent in your demo.

#### Current room display

```python
current = "entry"
room = rooms[current]
print(room["description"])
```

Two lookups: `rooms[current]` then `room["description"]`. Walk
through both.

#### The game loop

The full loop is ~15 lines. Walk through at the projector:

```python
while True:
    room = rooms[current]
    print(f"\n{room['description']}")
    
    if current == "study":   # win check
        print("You won!")
        break
    
    command = input("> ").lower().strip()
    
    if command == "quit":
        print("Goodbye!")
        break
    elif command in room:    # is the command an exit?
        current = room[command]
    else:
        print("You can't go that way.")
```

The `command in room` check is clever:

> "We check if the command is a *key* in the room's dict. The
> exits are stored as keys ('north', 'east', etc.). So if the
> player typed 'north' and the room has a 'north' key, that's
> a valid exit. We use `room[command]` to look up where it
> goes."

This is the most elegant moment of the session. Several kids
will get the "ohhhh" reaction.

The `.lower().strip()` is defensive input handling — case-
insensitive, ignores leading/trailing whitespace.

The `if current == "study"` win check is hardcoded for now.
Mention:

> "Right now, `study` is hardcoded as the win room. You could
> make this a variable — `WIN_ROOM = 'study'` — and check
> against that. Cleaner."

### Teaching Part B

#### Your own world

This is the personalization moment. Encourage:

> "The example world is mine. Make yours. A house you've been
> in, a fantasy setting, a school, anywhere. Six rooms is a
> good size — enough for some real navigation, not so many
> that you get lost building it."

Walk the room and help kids who:
- Have grand ideas they can't finish (push to scope down)
- Have no idea (suggest something concrete: "what's a place
  you know well?")
- Are typing room data without testing (push to test as they
  go — add 2 rooms, run, navigate, then add 2 more)

The "test as you build" advice is a real engineering practice
worth reinforcing today.

#### Items stretch

The items mechanic is the first real "game state beyond
location." Walk through:

```python
inventory = []

elif command.startswith("take "):
    item = command[5:]
    if "items" in room and item in room["items"]:
        room["items"].remove(item)
        inventory.append(item)
        print(f"You picked up the {item}.")
```

Several new things in one block:
- `command.startswith("take ")` — string method check
- `command[5:]` — string slicing to extract the item name
- Nested `if`: check if room has items AND the item is one
- `.remove()` from the room (Session 9 callback), `.append()`
  to inventory

Also worth explaining `', '.join(inventory)`:

> "`.join()` is a string method, not a list method. The
> *separator string* — in this case `", "` — calls `.join()`
> on the list. Weird Python choice, but the syntax is
> `separator.join(list)`. Result: a single string with the
> separator between items."

Don't dwell — just teach the recipe.

#### `look` command

Two versions in the handout — the simple one (just `pass`,
since the description re-prints next iteration) and the
elaborate one (lists exits explicitly). The elaborate one
introduces dict iteration that filters out non-exit keys.

The `for key in room:` then `if key not in ("description",
"items"):` is straightforward but worth walking through. Some
kids will want to know why we hardcode the skipped keys
("description", "items"). Honest answer: "we'd have to track
this somehow; this is the simple way. A more elegant version
would store exits in their own sub-dict, but that's more
complex."

#### Locked doors extension

The `west_requires` mechanism is a clever data extension.
Walk through:

> "We add a key like `west_requires` to the room dict. The
> value is what you need to use that exit. Before letting the
> player move, we check if there's a `_requires` for the
> direction they're going, and if so, whether they have it."

This is the first "stateful puzzle" mechanic — solving the
puzzle requires the right items in the right order.

#### Extension — JSON file loading

For very advanced kids only. JSON is genuinely useful, but
introducing it today is a lot. The handout includes the
syntax for kids who want to try.

Don't formally teach JSON. Mention as a stretch and let
curious kids figure it out.

### Common stumbles

- **Misnamed exit.** `"north": "kitchnen"` (typo) — going
  north errors with KeyError. Type carefully or use the
  debugger.
- **Missing room.** Exit points to `"libary"` but no such
  room defined. Same KeyError. Walk through the data.
- **Win check before display.** If win check is *before*
  printing the room's description, the player never sees the
  win room. Order matters.
- **Forgot `.lower()` on command.** Player types "North"
  (capital), check fails. Add `.lower()`.
- **Item commands don't work.** Common: forgot `command.
  startswith("take ")`, used `command == "take"` instead.
  The space matters.
- **Inventory persists between game restarts.** Yes — within
  one run of the program. To reset, restart the program. (To
  persist across runs, save to a file — Session 11.)
- **The room description has a typo and breaks immersion.**
  No code fix; just edit the description string. Kids notice
  this when they play their own games.

### Differentiation

- **Younger kids (9-10):** May find the dict-of-dicts
  structure intimidating. Focus on the base game with simple
  rooms. Skip items.
- **Older kids (12+):** Will probably finish the base game
  quickly. Push them through items + look. If they finish:
  locked doors. If they finish that: JSON loading.
- **Advanced (any age):** Suggest:
  - NPCs (characters with dialog)
  - Multiple win conditions
  - A scoring system
  - A `map` command (advanced)
  - Save/load with JSON
- **Struggling:** A kid who can't get the base game working
  is the kid you focus on. Most common cause: typo in a room
  name or exit. Use the debugger to find which lookup fails.

### What to watch for

- **The "I built a world" reaction.** Several kids will
  visibly process this. Affirm — they didn't just write a
  game with rules; they wrote a *place.*
- **Buddies playing each other's adventures.** Encourage.
  Real testing — buddies will find unintended dead ends and
  typos.
- **Personalization explosion.** Adventures will get
  surprisingly creative. Bible-themed, school-themed,
  fantasy, scifi, reality TV — kids will run with this.
  Encourage all of it.
- **The "I want to keep working on this at home" moment.**
  Many kids will want to extend their adventures between
  sessions. Encourage. This could become their milestone.

### After class

*(Leave this section blank until after the session. Fill in then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:
- **Notable adventures** — anyone build something especially
  creative?

### Connections forward

- **Sessions 15-16 (milestone).** Today's text adventure is
  one of the suggested milestone shapes for kids without
  ideas. Several will choose to extend or remix today's work.
- **Phase 4 (intermediate Python).** Refactoring the
  adventure into multiple files (one for the game logic, one
  for the rooms data, etc.) is exactly what Phase 4's
  multi-file Python intro is about.
- **Phase 5 (customtkinter).** A graphical version of today's
  adventure — buttons for directions, text area for
  descriptions — is a perfect customtkinter project.
- **Phase 6 (Pygame).** A graphical adventure with sprites
  and a tile-based map is the natural Pygame extension.
  Today's data structure (dict of locations) directly maps
  to a 2D grid.
- **Phase 8 (Flask).** A web-based text adventure is a
  reasonable Flask milestone. Same logic, HTTP requests
  instead of console input.
- **Peanut butter callback opportunity:** the misnamed-room
  KeyError is a precision moment. The computer looked up
  exactly what was written; the typo'd name doesn't exist;
  KeyError.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Pre-built complete adventure with items and a locked
      door for the destination preview
- [ ] Projector (essential — long session, lots to walk
      through)
- [ ] Class roster
