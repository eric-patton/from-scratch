"""
solutions.py — reference solutions for the five built-in puzzles.

Drop the body of any of these into the `solve()` function in
grid_world.py to test that the puzzle works as expected. Useful
when verifying changes to grid_world.py haven't broken anything.

Each solve() below produces a winning move sequence for the
matching built-in puzzle. They are NOT the only solutions and
not necessarily the shortest possible — they are designed to
read clearly and match the techniques each puzzle is meant to
teach (straight calls, then nested moves, then loops, then
loops with planning, then a real snake).
"""


# Puzzle 1 — straight line, three to the right.
def solve_puzzle_1():
    move_right()
    move_right()
    move_right()


# Puzzle 2 — turn the corner. Right four, then down four.
def solve_puzzle_2():
    move_right()
    move_right()
    move_right()
    move_right()
    move_down()
    move_down()
    move_down()
    move_down()


# Puzzle 3 — long path. Loops are the win here.
def solve_puzzle_3():
    for _ in range(7):
        move_right()


# Puzzle 4 — walls staircase. Down 4, right 3 (to (3, 4) — col 4
# is wall), down 3 (to (3, 7)), right 4 (along the bottom row).
def solve_puzzle_4():
    for _ in range(4):
        move_down()
    for _ in range(3):
        move_right()
    for _ in range(3):
        move_down()
    for _ in range(4):
        move_right()


# Puzzle 5 — snaking path. Three sweeps across the grid, each
# one funnels through the single open cell in the wall row.
def solve_puzzle_5():
    # row 0 → right edge
    for _ in range(7):
        move_right()
    # down through the col-7 passage in row 2, then to row 3
    for _ in range(3):
        move_down()
    # back across row 3 to the left edge
    for _ in range(7):
        move_left()
    # down through the col-0 passage in row 4, then to row 5
    for _ in range(2):
        move_down()
    # back across row 5 to the right edge
    for _ in range(7):
        move_right()
    # down through the col-7 passage in row 6 to the goal at row 7
    for _ in range(2):
        move_down()
