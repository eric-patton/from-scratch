## Session 4: A light intro to classes

*Phase 4 — Intermediate Python · Session 4 of 9*

### What we're learning today

Until now, your programs have been organized as **functions**
operating on **separate variables**. Today you'll learn how
to bundle data and functions together into a single thing
called a **class**. Classes let you say "this is a Pet, and
here's how to feed it, play with it, check on it" — all in
one organized package. By the end of class, you'll have built
a Pet class with several methods, plus tested it with
multiple pets.

### You'll need to remember from last time

- **Functions with parameters and return values.**
- **The `def` keyword** for defining functions.
- **Indentation** for grouping code.
- **Standard library classes** like `Path` and `datetime` —
  yes, those are classes. Today we learn how to make our own.

---

### Part A: Your first class

Open Thonny and start a new file. Save it as `pet.py`.

#### The motivation

Suppose you wanted to track a pet — its name, whether it's
hungry, whether it's happy. With what you know, you'd use
separate variables:

```python
pet_name = "Rex"
pet_hungry = True
pet_happy = True

def feed(name, hungry):
    if hungry:
        return False    # not hungry anymore
    return hungry

pet_hungry = feed(pet_name, pet_hungry)
```

This works but is awkward. The data (name, hungry, happy)
and the functions that work on it (feed, play) are *separate*
— you have to keep them organized in your head.

It gets worse with multiple pets:

```python
pet1_name = "Rex"
pet1_hungry = True
pet2_name = "Whiskers"
pet2_hungry = True
# ... ugh
```

There's a better way: **classes.**

#### Define a class

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hungry = True
        self.happy = True
    
    def feed(self):
        if self.hungry:
            self.hungry = False
            print(f"{self.name} eats happily.")
        else:
            print(f"{self.name} is not hungry right now.")
    
    def play(self):
        if self.hungry:
            print(f"{self.name} is too hungry to play.")
        else:
            self.hungry = True   # playing makes them hungry
            print(f"{self.name} loves playing!")
    
    def status(self):
        h = "hungry" if self.hungry else "full"
        m = "happy" if self.happy else "sad"
        print(f"{self.name} is {h} and {m}.")
```

A lot of new pieces. Let's break it down.

#### `class Pet:`

`class` starts a class definition. `Pet` is the class name.
The convention in Python is **CapitalCase** for class names
(unlike functions and variables which are lowercase). Just
like `Path`, `datetime`, etc. — those are classes too.

#### `def __init__(self, name):`

`__init__` is a special method that runs when a new pet is
*created*. It's called the **constructor.** The double
underscores around the name (called "dunder") are a Python
convention for "this is a special method the language calls
for you."

`self` is the first parameter, always. It refers to **the
specific pet being created.** Don't worry about understanding
this fully yet — just know that `self` is always the first
parameter, and you don't pass it when you call methods.

`name` is a normal parameter — the pet's name when you create
it.

Inside `__init__`:

- `self.name = name` — set this pet's name to the value
  passed in.
- `self.hungry = True` — every new pet starts hungry.
- `self.happy = True` — every new pet starts happy.

The `self.something = value` syntax stores values **on the
pet itself** — they live with that specific pet, not with
the class as a whole.

#### `def feed(self):`

A regular method (function inside a class). `self` is again
the first parameter — it refers to the specific pet being
fed. We use `self.hungry` to check the pet's hungry status,
and `self.hungry = False` to change it.

`self.name` reads the pet's name. `self.hungry` reads the
pet's hungry status. **Methods on a class always take `self`
as the first parameter** so they know which specific
instance to work with.

#### Use the class

Add this at the bottom of `pet.py`:

```python
my_pet = Pet("Rex")
my_pet.status()
my_pet.feed()
my_pet.status()
my_pet.play()
my_pet.status()
my_pet.feed()
my_pet.status()
```

Save and run.

```
Rex is hungry and happy.
Rex eats happily.
Rex is full and happy.
Rex loves playing!
Rex is hungry and happy.
Rex eats happily.
Rex is full and happy.
```

Walk through:

- `Pet("Rex")` — *instantiates* the class. Creates a new pet
  named Rex. Returns the new pet object, which we save in
  `my_pet`.
- `my_pet.status()` — call the `status` method on `my_pet`.
  Notice we don't pass `self` — Python passes it
  automatically. The `self` inside the method refers to
  `my_pet`.
- The pet's state changes over time as we feed and play
  with it.

#### Multiple pets

The power of classes: you can have many independent pets:

```python
rex = Pet("Rex")
whiskers = Pet("Whiskers")

rex.feed()
whiskers.status()
rex.status()
```

Two separate pets, each with their own name, their own
hungry status, their own happy status. Calling `rex.feed()`
doesn't affect `whiskers` at all.

Each pet is an **instance** of the Pet class. The class is
the blueprint; the instances are the actual pets you create
from it.

**Checkpoint:** *You've defined a class with `__init__` and
at least one other method, created at least one instance of
it, and called methods on that instance.* **This is the
natural stop point if class is cut short.**

---

### Part B: Use it for real

Time to do something more substantial with classes.

#### Base goal — multiple pets

Build a small program where the user takes care of three
different pets:

```python
class Pet:
    # ... (the class from Part A)

# create three pets
pets = [Pet("Rex"), Pet("Whiskers"), Pet("Spot")]

# show all
print("Your pets:")
for pet in pets:
    pet.status()

# feed each one
print("\nFeeding everyone...")
for pet in pets:
    pet.feed()

# show again
print("\nAfter feeding:")
for pet in pets:
    pet.status()
```

Save. Run. The program walks through three pets, doing the
same thing to each.

The interesting move: **you have a list of objects**, and you
loop through it calling methods on each. Same pattern as
looping through a list of strings or numbers — except the
items are richer (they have data AND methods).

#### Stretch — interactive pet care

Add a menu-driven version:

```python
class Pet:
    # ... (same as before)

pets = [Pet("Rex"), Pet("Whiskers"), Pet("Spot")]

while True:
    print("\nYour pets:")
    for i, pet in enumerate(pets):
        print(f"  {i + 1}. {pet.name}")
    
    print("\n1. Status all\n2. Feed one\n3. Play with one\n4. Quit")
    choice = input("> ")
    
    if choice == "1":
        for pet in pets:
            pet.status()
    elif choice == "2":
        i = int(input("Which pet (number)? ")) - 1
        if 0 <= i < len(pets):
            pets[i].feed()
    elif choice == "3":
        i = int(input("Which pet (number)? ")) - 1
        if 0 <= i < len(pets):
            pets[i].play()
    elif choice == "4":
        break
```

Now the user picks which pet to interact with from a menu.
Real game-like feel, with a list of class instances under
the hood.

#### Extension — a second class

Add a `Treat` class that pets can be fed:

```python
class Treat:
    def __init__(self, name, food_value):
        self.name = name
        self.food_value = food_value
    
    def describe(self):
        return f"a {self.name} (worth {self.food_value} hunger points)"

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5    # 0 = full, 10 = starving
        self.happy = True
    
    def eat(self, treat):
        print(f"{self.name} eats {treat.describe()}.")
        self.hunger -= treat.food_value
        if self.hunger < 0:
            self.hunger = 0
    
    def status(self):
        print(f"{self.name}: hunger {self.hunger}/10, "
              f"{'happy' if self.happy else 'sad'}.")

# usage
rex = Pet("Rex")
cookie = Treat("cookie", 3)
steak = Treat("steak", 8)

rex.status()
rex.eat(cookie)
rex.status()
rex.eat(steak)
rex.status()
```

Two classes interacting:

- `Treat` has a name and a food value (how much hunger it
  removes).
- `Pet` has a numeric hunger (instead of just True/False).
- `Pet.eat()` takes a `Treat` and reduces hunger by the
  treat's food value.

**Two classes, one program, working together.** That's how
real OOP code is structured — many classes, each
representing a thing in the program's world, calling each
other's methods.

(This is a hint of where Phase 5's customtkinter goes —
Buttons, Frames, Labels, all classes that interact.)

---

### Wrap-up

Before we leave, share with the room:

- For the kids who built the Pet class — what behavior did
  you add beyond feed/play? Anything custom?
- For the menu version — does having a list of pet objects
  feel cleaner than tracking each pet's variables
  separately?
- For the two-class extension — was it natural for two
  classes to interact?

You learned today the foundational idea of **object-oriented
programming** — bundling data and functions into named
units. Real Python (and most other modern languages) is
mostly classes. `Path` is a class. `datetime` is a class.
The customtkinter widgets you'll meet in Phase 5 are
classes. The Pygame sprites in Phase 6 are classes.

You're not done with classes — Phase 5 and beyond build on
them constantly. Today is the foundation: define a class,
make instances of it, call methods on them. That's enough to
read and understand most class-based code you'll see.

### If you missed this session

Open Thonny. Then:

1. Type out the basic Pet class from Part A. Create one pet
   with `Pet("Rex")`. Call `.status()`, `.feed()`,
   `.play()`. Watch the state change.

2. Try creating two pets. Feed one. Verify the other isn't
   affected.

3. Build the multi-pet base from Part B (a list of pets, a
   loop calling methods on each).

About 35-40 minutes. If you get stuck, ask your buddy at the
start of next class.

### Stretch and extension ideas

- **Class attributes** (vs instance attributes). `class
  Pet: max_hunger = 10` is shared by all pets. `self.hunger`
  is per-instance. Try both.
- **More methods.** `Pet.celebrate_birthday()`,
  `Pet.rename(new_name)`, `Pet.adopt_friend(other_pet)`.
  Get creative.
- **A `__str__` method** — special method that defines what
  `print(pet)` shows. Makes your class friendlier to print.
- **`__repr__`** — like `__str__` but for the developer.
- **Multiple classes interacting** — pets and treats,
  players and enemies, books and authors. Whatever you can
  imagine.
- **Inheritance** — make a `Dog` class that's a special
  kind of `Pet`. We're not formally covering this but if
  you're curious: `class Dog(Pet):`.

### What's next

Next week we start **Git** — the most important tool in
modern programming for *saving your code's history.* You'll
finally have a way to undo mistakes, track changes over
time, and (eventually, in Phase 6) share your code with the
world.
