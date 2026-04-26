## Session 4 — Teacher Notes

*Phase 4, Intermediate Python · Session 4 of 9 · Title: A
light intro to classes*

### Purpose of this session

Classes are the central organizing idea in modern Python.
"Light intro" per CURRICULUM-DECISIONS.md — just `class`,
`__init__`, methods. No inheritance. Five jobs, in priority
order:

1. **Land "data + functions in one package."** The mental
   shift from "separate variables and functions" to "objects
   that have state and behavior" is the lesson.
2. **Land the `self` parameter.** Counterintuitive at first.
   Make it concrete: "self is the specific instance this
   method is being called on."
3. **Land instantiation.** `pet = Pet("Rex")` creates a new
   instance. Each instance is independent.
4. **Land the connection to stdlib classes.** `Path`,
   `datetime` — they've been using classes all along. Today
   is the producer side of what they've been consuming.
5. **Set up Phase 5 (customtkinter) and Phase 6 (Pygame).**
   Both are class-heavy. Today's foundation makes them
   accessible.

### Before class

**Bring:** nothing physical.

**Set up:**

- Demo machine with Thonny + terminal.
- Optional: pre-built two-class Pet+Treat for destination
  preview.

**Prep time:** ~15 minutes.

### Timing and flow

Total: ~90 min, two halves with a hard checkpoint.

- **Welcome and recap** (~5 min) — last week was stdlib.
  Anyone build a CLI tool at home?
- **Part A: first class** (~45 min) — motivation ~5 min,
  define Pet ~15 min, walk through pieces (class, __init__,
  self, methods) ~15 min, instantiate and use ~5 min,
  multiple pets ~5 min.
- **Break** (~5 min).
- **Part B: use for real** (~30 min) — multi-pet base ~15
  min, menu stretch ~10 min, two-class extension ~5 min.
- **Wrap-up** (~5 min).

If running short, **the two-class extension can be cut.**
The multi-pet base + menu is the goal.

### Teaching Part A

#### The motivation

Open with the awkwardness of separate variables:

```python
pet_name = "Rex"
pet_hungry = True
def feed(name, hungry):
    ...
```

> "This works but is awkward. The data and the functions are
> separate. We have to keep them in sync in our heads. With
> two pets it's worse. There's a better way."

This sets up "classes" as the answer.

#### Define the class

Walk through `class Pet:` at the projector. Then `__init__`:

> "`__init__` is special. It runs when you create a new pet.
> The double-underscore name — Python developers call it
> 'dunder init' — means 'this is a special method Python
> calls for you.' You don't call `__init__` directly; it
> happens when you create an instance."

The `self` parameter is the conceptually trickiest piece.
Frame it explicitly:

> "`self` always comes first in a method's parameter list.
> It refers to *the specific pet this method is being called
> on.* When you call `rex.feed()`, Python passes `rex` as
> `self` automatically. So inside `feed`, `self.name` is
> Rex's name, `self.hungry` is Rex's hungry status."

This will need re-explaining a few times. That's normal. The
`self` concept doesn't fully click until they've used it
several times.

The `self.name = name` line — assigning the parameter to
an instance attribute — is also new and worth pausing on:

> "This stores the name *on this specific pet.* Other pets
> have their own `self.name`. They don't share."

#### Methods

`feed`, `play`, `status` — all standard methods. Each takes
`self` and uses `self.something` to read/modify the pet's
state.

Worth pointing out: methods are just functions defined inside
a class:

> "Methods are basically functions that belong to a class.
> They take `self` as the first parameter; otherwise they're
> regular functions."

#### Instantiate and use

`pet = Pet("Rex")` is the new mechanic. Walk through:

> "`Pet(...)` looks like a function call. What it actually
> does: create a new pet object, run `__init__` on it
> (passing 'Rex' as the name parameter), and return the
> new pet. We save it in `pet`."

The "you don't pass self when you call" thing is the
counterpart to "self is always the first parameter." Address
it:

> "When you call `rex.feed()`, you don't pass `self` — Python
> does that for you. The `rex` before the dot tells Python
> which pet to pass as `self`."

This will be confusing for some kids. Show explicitly:

```python
rex = Pet("Rex")  # __init__(self=new_pet, name="Rex")
rex.feed()        # feed(self=rex)
```

The "there's an invisible argument being passed" is one of
the OO concepts that takes time.

#### Multiple pets

The power of classes is many independent instances:

```python
rex = Pet("Rex")
whiskers = Pet("Whiskers")
rex.feed()
# whiskers is unaffected
```

> "Each pet has its own data. They don't interfere. That's
> the power of classes — instances are independent."

This is the lesson landing. The "each pet has its own state"
moment.

### Teaching Part B

#### Multi-pet base

Mechanical. A list of Pet instances, looped through.
Worth pointing out:

> "You can have a list of objects, just like a list of
> numbers or strings. The objects have richer behavior
> (methods, state) but lists work the same way."

This connects classes back to the rest of Python they know.

#### Menu stretch

Mostly mechanical too — the menu pattern from Phase 3 with
class-based actions. The interesting bit:

```python
i = int(input("Which pet? ")) - 1
pets[i].feed()
```

Index into the list of pets, then call a method on the
selected one.

> "We're combining lists and classes — `pets[i]` gets a
> specific pet object; `.feed()` calls the method on it."

#### Two-class extension

The Pet-and-Treat example shows class interaction:

```python
class Treat:
    def __init__(self, name, food_value):
        ...

class Pet:
    def eat(self, treat):
        # treat is a Treat instance
        self.hunger -= treat.food_value
```

Worth pointing out:

> "The `eat` method takes a `Treat` as a parameter. So one
> class's method *uses* another class's instance. This is
> how big OO programs work — many classes, each with one
> job, calling each other's methods."

Don't go deeper into OO design today. Just show the pattern.

### Common stumbles

- **Forgot `self` in method definition.** `def feed(self):`
  vs `def feed():`. The latter errors when you call
  `pet.feed()`.
- **Forgot `self.` when accessing instance variables.**
  `name` (refers to no variable) vs `self.name` (the pet's
  name). Common confusion.
- **Tried to call `self.name = name` outside `__init__`.**
  Works, but unusual. Initialization belongs in `__init__`.
- **Created class but never instantiated.** Defined `Pet`
  but never did `Pet("Rex")`. The class definition just
  exists; you have to make instances.
- **`Pet("Rex").feed()`** without saving the instance.
  Works once but you can't use it again. Save in a variable:
  `rex = Pet("Rex"); rex.feed()`.
- **Two pets accidentally sharing state.** Usually a class
  attribute (defined at class level, outside `__init__`)
  instead of instance attribute (set with `self.x = ...`).
  Less common but trips up advanced kids.
- **Using `=` instead of `:` after class name.** `class Pet:`
  not `class Pet =`. SyntaxError.
- **CapitalCase vs lowercase.** Convention only — lowercase
  works syntactically. Use CapitalCase for classes per Python
  convention.

### Differentiation

- **Younger kids (9-10):** May find `self` and instances
  confusing. Lean on the visual: when you do `Pet("Rex")`,
  draw it on the whiteboard as a "new pet box" with name,
  hungry, happy filled in. When you do `Pet("Whiskers")`,
  draw a SECOND box. Make the independence concrete.
- **Older kids (12+):** Will pick up the syntax fast. Push
  through the menu and two-class extension. If they finish:
  ask them to add a `__str__` method to Pet so `print(pet)`
  shows nice output.
- **Advanced (any age):** Suggest:
  - Inheritance: `class Dog(Pet):`
  - Class methods (`@classmethod`)
  - Static methods (`@staticmethod`)
  - `__str__` and `__repr__` magic methods
  - Properties (`@property`)
  Don't formally teach; let them explore.
- **Struggling:** A kid who can't get a basic Pet class
  working is the kid you focus on. Most common cause: forgot
  `self` in method definition, or didn't save the instance
  in a variable. Walk through line by line.

### What to watch for

- **The "wait, Path is a class?" insight.** When kids
  realize they've been using classes all along (Path,
  datetime, even the int() and str() functions are classes),
  affirm. The continuity is the lesson.
- **Buddies trading class ideas.** "What other things could
  be classes?" — encourage. Cars, books, players in a game,
  characters in a story. Brainstorming class shapes is real
  software design.
- **The "I can have many independent pets" reaction.** Lands
  the instances concept.
- **Frustration with `self`.** Common. Reassure that it
  takes a few sessions to feel natural.

### After class

*(Leave this section blank until after the session. Fill in
then.)*

- What worked:
- What didn't:
- Timing surprises:
- Specific kids to follow up with:
- Adjustments for next year:

### Connections forward

- **Sessions 5-6 (Git).** Less about classes; more about
  workflow. But the "each commit is an independent state"
  framing is a class-like mental model.
- **Session 7 (testing).** Test functions test class
  behavior. Today's Pet is a great target for tests
  ("after `pet.feed()`, `pet.hungry` should be False").
- **Phase 5 (customtkinter).** EVERY widget is a class. The
  whole library is class-based. Today is the foundation.
- **Phase 6 (Pygame).** Sprites are classes. Game state
  classes. Heavy OO. Today is the foundation.
- **Phase 8 (Flask).** Models in Flask are classes. Forms
  are classes. Decorators are functions but the patterns are
  class-friendly.
- **Peanut butter callback opportunity:** the "forgot self
  in method" bug is a precision moment. The computer can't
  guess that you meant the instance variable; you have to
  say `self.name`, not just `name`.

### Materials checklist

- [ ] Demo machine with Thonny
- [ ] Optional: pre-built Pet+Treat example
- [ ] Whiteboard or projector for "two pets, two boxes"
      visualization
- [ ] Class roster
