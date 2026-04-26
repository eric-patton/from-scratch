## Session 14: Putting it together — a text adventure

*Phase 3 — Python basics · Session 14 of 16*

### What we're learning today

Today we build the **biggest project of Phase 3** — a **text
adventure game.** The player walks through a small world
(rooms connected by exits), reads descriptions, types commands
like "north" or "look", and tries to find their way to the
goal. Everything from Phase 3 comes together: dictionaries
(for the rooms), loops (the game loop), conditionals (handling
commands), strings, input/output, error handling, and
optionally file I/O. By the end of class, you'll have a
playable adventure of your own design.

### You'll need to remember from last time

- **Dictionaries** — `{"key": "value"}`, lookup with `[key]`,
  the `in` operator, `.items()`.
- **Lists** — for inventories or anything ordered.
- **`while True:` and `break`** for game loops.
- **`if/elif/else`** for handling different commands.
- **f-strings** for output.
- **`try/except`** for handling unexpected input.

---

### Part A: Build the world

Open Thonny and start a new file. Save it as `adventure.py`.

#### The plan

A text adventure has:

- **Rooms** — places the player can be. Each one has a
  description and a list of exits to other rooms.
- **A current location** — which room the player is in right
  now.
- **A game loop** — print the room, ask the user what to do,
  update the location.
- **A win condition** — reach a specific room.

We'll use a *dictionary of rooms* — perfect application of
what we learned in Session 10.

#### Build the rooms

```python
rooms = {
    "entry": {
        "description": "You're in a dark entryway. Doors lead north and east.",
        "north": "kitchen",
        "east": "library"
    },
    "kitchen": {
        "description": "A bright kitchen. The entryway is south.",
        "south": "entry"
    },
    "library": {
        "description": "Books from floor to ceiling. The entryway is west. Stairs go up.",
        "west": "entry",
        "up": "study"
    },
    "study": {
        "description": "A quiet study. You found the treasure chest!",
        "down": "library"
    }
}
```

This is a **dictionary of dictionaries.** The outer dict has
room names as keys. Each value is *another* dict describing
that room — its `"description"` and its exits (`"north"`,
`"east"`, etc.) which point to other room names.

So if you're in `"entry"` and you go `"north"`, you end up in
`"kitchen"`.

#### Show the current room

```python
current = "entry"
room = rooms[current]
print(room["description"])
```

`rooms[current]` looks up the current room by name. Then
`room["description"]` gets its description string. Two dict
lookups in a row.

Save and run. You should see:

```
You're in a dark entryway. Doors lead north and east.
```

#### The game loop

Now the loop: print the room, ask for a command, update the
location, repeat.

```python
rooms = {
    "entry": {
        "description": "You're in a dark entryway. Doors lead north and east.",
        "north": "kitchen",
        "east": "library"
    },
    "kitchen": {
        "description": "A bright kitchen. The entryway is south.",
        "south": "entry"
    },
    "library": {
        "description": "Books from floor to ceiling. The entryway is west. Stairs go up.",
        "west": "entry",
        "up": "study"
    },
    "study": {
        "description": "A quiet study. You found the treasure chest!",
        "down": "library"
    }
}

current = "entry"

while True:
    room = rooms[current]
    print(f"\n{room['description']}")
    
    # win check
    if current == "study":
        print("You won!")
        break
    
    # get a command
    command = input("> ").lower().strip()
    
    if command == "quit":
        print("Goodbye!")
        break
    elif command in room:
        current = room[command]
    else:
        print("You can't go that way.")
```

Save. Run. Type commands like `north`, `east`, `up`, `quit`.
Try to find the study (the win room).

Walk through what's happening:

- `current = "entry"` — start in the entry room.
- `while True:` — game loops forever (until break).
- Each iteration: look up the current room, print its
  description, check for win.
- Get a command. Commands are direction names (`north`,
  `east`, etc.) or `quit`.
- `if command in room:` — check if the command is a key in
  the current room's dict (i.e., a valid exit).
- If it is, `room[command]` gives the next room name; update
  `current`.
- If not, print "you can't go that way" and loop again.

**This game uses every Phase 3 concept.** Look at what's in
those 30 lines: dicts, lookup, iteration, conditionals,
loops, input, output, the `in` operator, f-strings, string
methods. You wrote a small but complete game.

**Checkpoint:** *You have a working text adventure with at
least three rooms connected by exits, and you can navigate
from a starting room to a winning room.* **This is the natural
stop point if class is cut short.**

---

### Part B: Make it your adventure

The base game works. Now make it *yours.*

#### Base goal — your own world

Replace the rooms dictionary with your own. Build a world that
makes sense to *you* — a house you've been in, a fantasy
setting, a school, a spaceship, anywhere. Aim for at least
**six rooms** with interesting connections.

Don't make a straight line — branch the paths. Make some rooms
dead-ends. Make the path to the win room have at least one
"choice point" where the player has to pick a direction.

```python
rooms = {
    "front_yard": {
        "description": "A small front yard. The house is north. A path leads east to the garden.",
        "north": "house_door",
        "east": "garden"
    },
    # ... your rooms here ...
}
```

Test it. Walk through the entire world to make sure every
exit goes where you intended.

#### Stretch — items

Some rooms have items the player can pick up:

```python
rooms = {
    "kitchen": {
        "description": "A bright kitchen. There's a cookie on the counter.",
        "south": "entry",
        "items": ["cookie"]
    },
    # ...
}
```

The `"items"` key holds a list of items in the room.

Add an inventory variable:

```python
inventory = []
```

Add commands for `take` and `inventory`:

```python
elif command.startswith("take "):
    item = command[5:]    # remove "take " (5 chars)
    if "items" in room and item in room["items"]:
        room["items"].remove(item)
        inventory.append(item)
        print(f"You picked up the {item}.")
    else:
        print("There's no such thing here.")
elif command == "inventory" or command == "i":
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print(f"You have: {', '.join(inventory)}")
```

The `command.startswith("take ")` checks if the command begins
with "take " — that's how we recognize "take cookie" as a
take-something command. The `command[5:]` slices off "take "
and leaves just the item name.

`', '.join(inventory)` is a string method that joins a list
into one string with separators. `["cookie", "key"].join(", ")`
becomes `"cookie, key"`. (Not actually a method on the list
— it's a method on the *separator string.* Weird Python
choice, but that's the syntax.)

Update room descriptions to mention items, and add `items`
keys to the rooms that have them.

#### Stretch — a `look` command

Sometimes the player wants to re-read the current room's
description without moving:

```python
elif command == "look" or command == "l":
    # the description prints automatically next loop iteration
    pass
```

Or for a richer version, list the available exits explicitly:

```python
elif command == "look" or command == "l":
    print(f"\n{room['description']}")
    exits = []
    for key in room:
        if key not in ("description", "items"):
            exits.append(key)
    print(f"Exits: {', '.join(exits)}")
```

This iterates the room dict's keys, skipping the description
and items keys (which aren't exits), and lists the rest.

#### Extension — locked doors

Some exits require a specific item to open:

```python
"library": {
    "description": "A library. The west door is locked.",
    "west": "entry",
    "west_requires": "key"
},
```

Then in the movement code:

```python
elif command in room:
    next_room = room[command]
    
    # check for lock
    requires = command + "_requires"
    if requires in room:
        needed = room[requires]
        if needed not in inventory:
            print(f"You need a {needed} to go that way.")
            continue
    
    current = next_room
```

Now the player has to find the key (in some other room) before
they can use the locked door. Real puzzle-game logic.

#### Extension — load rooms from a file

Hard but rewarding. The room data is currently *in your code.*
Pull it into a separate file (`rooms.txt` or — fancier — a
`rooms.json`).

JSON format is what Python uses for dict-like data:

```json
{
    "entry": {
        "description": "...",
        "north": "kitchen"
    }
}
```

Loading:

```python
import json

with open("rooms.json", "r") as f:
    rooms = json.load(f)
```

Now you can edit the world without touching the Python code.
Same code-vs-data separation pattern from hangman.

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built their own world — what's it set in?
  Walk us through finding the win room.
- For the kids who added items — what items did you include?
  Did anyone build a real puzzle (need item X to get item Y to
  reach room Z)?
- Did anyone get their parent or sibling to play it?

You built **a complete game with multiple systems** today. Not
just a "play one round" game like hangman or the
number-guesser — a *world* the player can explore. With items
and locks (if you added them), this is a real puzzle game.

You also used **almost every concept from Phase 3** — Python
syntax, types, strings, lists, dicts, loops, conditionals,
functions, file I/O, error handling — all in one program.
That's the proof that you have the toolkit.

Two more sessions of Phase 3 — milestone planning and demos —
and then you move into **Phase 4: Intermediate Python and
the command line.** You're well on your way.

### If you missed this session

Open Thonny and start a new file. Save as `adventure.py`.
Then:

1. Build the rooms dictionary (Part A) — at least three rooms
   with exits.
2. Build the game loop (the full Part A code).
3. Run it. Navigate from entry to study (or wherever your
   win room is). Quit.
4. Replace the rooms with your own world — at least six rooms.

About 50-60 minutes for the base. If you want items or
locked doors (Part B), add another 30 minutes.

If you get stuck, ask your buddy at the start of next class.

### Stretch and extension ideas

- **Multiple win conditions** — find the treasure AND escape
  to the front door. Track multiple flags.
- **NPCs (characters)** — some rooms have a character who
  says something, or who you have to talk to (with a `talk`
  command).
- **Dynamic descriptions** — the description changes based on
  whether you've taken something, picked up a clue, etc.
- **Inventory limits** — only carry 3 items; have to drop one
  to pick up another.
- **A map command** — print the world's layout (advanced;
  requires thinking about how to render dict relationships
  visually).
- **Save and load** — save your current state to a file so you
  can resume later. (Use `json.dump(...)` and `json.load(...)`.)

### What's next

Next week starts your **milestone project** — *your* program,
your design. You have two sessions to plan, build, and demo.
Your milestone could be:

- A more elaborate text adventure
- A different kind of game (riddle game, trivia, puzzle)
- A useful tool (a quiz study app, a budget tracker, a daily
  journal)
- A creative program (a poem generator, a story builder)
- Anything else you can imagine that uses Python

Start thinking about what you want to build. **Bring an idea
to next week's class.**
