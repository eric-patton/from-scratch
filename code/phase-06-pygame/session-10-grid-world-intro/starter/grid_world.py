"""
grid_world.py — From Scratch Programming Class.

A code-controlled puzzle game. The character at the top of the
grid moves only when you write code that calls move_right(),
move_left(), move_up(), or move_down() inside solve(). Press
SPACE to run your solve(), 1-5 to switch puzzles, R to reset.

The student-facing API (the four movement functions) is
deliberately tiny. Everything else lives in this file:

  * Puzzles are data — dicts in the `PUZZLES` list. Add a new
    one to add a new puzzle.
  * The movement functions append to a `moves` list. They do
    NOT move the character immediately.
  * The main loop pops one move per ANIM_STEP_MS milliseconds
    and animates the character cell-to-cell smoothly.
  * Walls are checked on the *attempted* move; the character
    "bumps" without passing through.

Designed for ~9-15 year olds who've finished Phase 6 Sessions 1-9.
"""

import pygame
import sys

# ---------------------------------------------------------------
# Setup
# ---------------------------------------------------------------

GRID_SIZE = 8
CELL_PX = 64
GRID_PX = GRID_SIZE * CELL_PX
HUD_HEIGHT = 80
WIDTH = GRID_PX
HEIGHT = GRID_PX + HUD_HEIGHT

FPS = 60
ANIM_STEP_MS = 220   # how long each move takes to animate

# Colors
BG = (24, 28, 38)
GRID_LINE = (52, 58, 72)
CELL_LIGHT = (40, 46, 60)
CELL_DARK = (32, 38, 52)
WALL = (110, 90, 70)
GOAL = (255, 210, 60)
GOAL_RING = (255, 235, 130)
CHAR_BODY = (90, 170, 255)
CHAR_OUTLINE = (220, 240, 255)
HUD_BG = (16, 18, 28)
HUD_TEXT = (220, 230, 245)
HUD_DIM = (120, 130, 150)
SOLVED_TEXT = (120, 240, 150)
BUMP_FLASH = (255, 90, 90)


# ---------------------------------------------------------------
# Puzzles
# Each puzzle is a dict. Add more to PUZZLES; press number keys
# (1, 2, 3, ...) to switch between them at runtime.
# Coordinates are (x, y) where (0, 0) is the top-left cell.
# ---------------------------------------------------------------

PUZZLES = [
    {
        "name": "Straight line",
        "start": (0, 0),
        "goal": (3, 0),
        "walls": [],
    },
    {
        "name": "Turn the corner",
        "start": (0, 0),
        "goal": (4, 4),
        "walls": [],
    },
    {
        "name": "Long path",
        "start": (0, 4),
        "goal": (7, 4),
        "walls": [],
    },
    {
        # Two staircase walls force the path to bend twice. The
        # gap at (4, 7) means the only way through the bottom
        # wall is along the bottom row.
        "name": "Walls!",
        "start": (0, 0),
        "goal": (7, 7),
        "walls": [
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 4), (4, 5), (4, 6),
        ],
    },
    {
        # The path snakes: across to the right, blocked by a wall
        # row, back to the left through the passage at the far
        # column, then down, etc. Forces real path planning.
        "name": "Snaking path",
        "start": (0, 0),
        "goal": (7, 7),
        "walls": [
            # y=2: blocks columns 0-6, passage at column 7
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
            # y=4: blocks columns 1-7, passage at column 0
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
            # y=6: blocks columns 0-6, passage at column 7
            (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
        ],
    },
]


# ---------------------------------------------------------------
# Game state
# ---------------------------------------------------------------

current_puzzle_index = 0
current_puzzle = PUZZLES[0]

char_cell_x = 0       # current logical cell
char_cell_y = 0
char_pixel_x = 0.0    # current draw position (pixels), animated
char_pixel_y = 0.0
start_pixel_x = 0.0   # where the in-flight animation started
start_pixel_y = 0.0
target_pixel_x = 0.0
target_pixel_y = 0.0
move_progress_ms = 0  # how far through the current animation
animating = False
bump_flash_ms = 0     # >0 while showing a "bumped a wall" flash

moves = []            # queue of "right" / "left" / "up" / "down"
running_solve = False
solved = False


def _cell_to_pixels(cx, cy):
    """Top-left pixel of a cell."""
    return cx * CELL_PX, cy * CELL_PX


def load_puzzle(index):
    """Switch to puzzle `index`. Resets character and any queued moves."""
    global current_puzzle_index, current_puzzle
    global char_cell_x, char_cell_y
    global char_pixel_x, char_pixel_y
    global start_pixel_x, start_pixel_y, target_pixel_x, target_pixel_y
    global moves, running_solve, solved, animating, move_progress_ms, bump_flash_ms

    if index < 0 or index >= len(PUZZLES):
        return
    current_puzzle_index = index
    current_puzzle = PUZZLES[index]

    char_cell_x, char_cell_y = current_puzzle["start"]
    char_pixel_x, char_pixel_y = _cell_to_pixels(char_cell_x, char_cell_y)
    start_pixel_x, start_pixel_y = char_pixel_x, char_pixel_y
    target_pixel_x, target_pixel_y = char_pixel_x, char_pixel_y

    moves = []
    running_solve = False
    solved = False
    animating = False
    move_progress_ms = 0
    bump_flash_ms = 0


def reset_character():
    """Reset character to the current puzzle's start. Clears queued moves."""
    load_puzzle(current_puzzle_index)


# ---------------------------------------------------------------
# Student-facing API
# Calling these inside solve() does NOT move the character
# immediately; it appends to the queue. The main loop animates
# the queue one step at a time.
# ---------------------------------------------------------------

def move_right():
    moves.append("right")


def move_left():
    moves.append("left")


def move_up():
    moves.append("up")


def move_down():
    moves.append("down")


# ---------------------------------------------------------------
# === YOUR CODE GOES HERE ===
# Edit solve() to write code that gets the character to the
# goal. Press SPACE in the running game to run this function.
# ---------------------------------------------------------------

def solve():
    pass


# ---------------------------------------------------------------
# Movement playback (engine internals — students read these in
# Session 10 Part B and modify them in Session 11)
# ---------------------------------------------------------------

def _start_next_move():
    """Pop the next move from the queue and start animating it.

    If the next move would go off the grid or into a wall, the
    character "bumps" — we keep them in place but flash red
    briefly so it's obvious nothing went through.
    """
    global char_cell_x, char_cell_y
    global start_pixel_x, start_pixel_y, target_pixel_x, target_pixel_y
    global animating, move_progress_ms, bump_flash_ms

    if not moves:
        animating = False
        return

    direction = moves.pop(0)
    dx, dy = 0, 0
    if direction == "right":
        dx = 1
    elif direction == "left":
        dx = -1
    elif direction == "up":
        dy = -1
    elif direction == "down":
        dy = 1

    next_x = char_cell_x + dx
    next_y = char_cell_y + dy

    in_bounds = 0 <= next_x < GRID_SIZE and 0 <= next_y < GRID_SIZE
    is_wall = (next_x, next_y) in current_puzzle["walls"]

    start_pixel_x, start_pixel_y = char_pixel_x, char_pixel_y
    move_progress_ms = 0
    animating = True

    if not in_bounds or is_wall:
        # Bump — character stays put, animation just plays a flash.
        bump_flash_ms = ANIM_STEP_MS
        target_pixel_x, target_pixel_y = char_pixel_x, char_pixel_y
        return

    char_cell_x = next_x
    char_cell_y = next_y
    target_pixel_x, target_pixel_y = _cell_to_pixels(char_cell_x, char_cell_y)


def _update_animation(dt_ms):
    """Advance the in-flight animation; if it just finished, look
    at the queue and either start the next move or stop."""
    global char_pixel_x, char_pixel_y
    global animating, move_progress_ms, bump_flash_ms
    global running_solve, solved

    if bump_flash_ms > 0:
        bump_flash_ms = max(0, bump_flash_ms - dt_ms)

    if not animating:
        return

    move_progress_ms += dt_ms
    t = min(1.0, move_progress_ms / ANIM_STEP_MS)
    char_pixel_x = start_pixel_x + (target_pixel_x - start_pixel_x) * t
    char_pixel_y = start_pixel_y + (target_pixel_y - start_pixel_y) * t

    if t >= 1.0:
        char_pixel_x = target_pixel_x
        char_pixel_y = target_pixel_y
        animating = False
        # Check the goal as soon as we land.
        if (char_cell_x, char_cell_y) == current_puzzle["goal"]:
            solved = True
            running_solve = False
            moves.clear()
            return
        # If solve() is mid-playback and there are more moves, kick the
        # next one off automatically.
        if running_solve and moves:
            _start_next_move()
        elif running_solve and not moves:
            running_solve = False


def run_solve():
    """Called when the user presses SPACE. Resets state, then calls
    the student's solve() to fill the moves queue, then starts
    animating."""
    global running_solve, solved
    reset_character()
    running_solve = True
    solved = False
    solve()
    if moves:
        _start_next_move()
    else:
        # solve() didn't queue any moves — nothing to play.
        running_solve = False


# ---------------------------------------------------------------
# Drawing
# ---------------------------------------------------------------

def draw(screen, font_big, font_small):
    screen.fill(BG)
    _draw_grid(screen)
    _draw_walls(screen)
    _draw_goal(screen)
    _draw_character(screen)
    _draw_hud(screen, font_big, font_small)


def _draw_grid(screen):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = CELL_LIGHT if (x + y) % 2 == 0 else CELL_DARK
            pygame.draw.rect(
                screen, color,
                (x * CELL_PX, y * CELL_PX, CELL_PX, CELL_PX),
            )
    # subtle grid lines
    for i in range(GRID_SIZE + 1):
        pygame.draw.line(screen, GRID_LINE,
                         (i * CELL_PX, 0), (i * CELL_PX, GRID_PX), 1)
        pygame.draw.line(screen, GRID_LINE,
                         (0, i * CELL_PX), (GRID_PX, i * CELL_PX), 1)


def _draw_walls(screen):
    for (wx, wy) in current_puzzle["walls"]:
        rect = pygame.Rect(wx * CELL_PX, wy * CELL_PX, CELL_PX, CELL_PX)
        pygame.draw.rect(screen, WALL, rect)
        # darker inner border to make wall feel solid
        pygame.draw.rect(screen, BG, rect, 3)


def _draw_goal(screen):
    gx, gy = current_puzzle["goal"]
    cx = gx * CELL_PX + CELL_PX // 2
    cy = gy * CELL_PX + CELL_PX // 2
    pygame.draw.circle(screen, GOAL_RING, (cx, cy), CELL_PX // 2 - 6)
    pygame.draw.circle(screen, GOAL, (cx, cy), CELL_PX // 2 - 12)


def _draw_character(screen):
    # Body
    rect = pygame.Rect(
        int(char_pixel_x) + 8,
        int(char_pixel_y) + 8,
        CELL_PX - 16, CELL_PX - 16,
    )
    body_color = BUMP_FLASH if bump_flash_ms > 0 else CHAR_BODY
    pygame.draw.rect(screen, body_color, rect, border_radius=10)
    pygame.draw.rect(screen, CHAR_OUTLINE, rect, width=2, border_radius=10)


def _draw_hud(screen, font_big, font_small):
    hud_rect = pygame.Rect(0, GRID_PX, WIDTH, HUD_HEIGHT)
    pygame.draw.rect(screen, HUD_BG, hud_rect)

    title = f"Puzzle {current_puzzle_index + 1}: {current_puzzle['name']}"
    surf = font_big.render(title, True, HUD_TEXT)
    screen.blit(surf, (12, GRID_PX + 8))

    if solved:
        msg = font_big.render("Solved!", True, SOLVED_TEXT)
        screen.blit(msg, (WIDTH - msg.get_width() - 12, GRID_PX + 8))

    instructions = "1-5: switch puzzle   SPACE: run solve()   R: reset"
    surf2 = font_small.render(instructions, True, HUD_DIM)
    screen.blit(surf2, (12, GRID_PX + 44))


# ---------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("grid-world")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    font_big = pygame.font.SysFont(None, 28)
    font_small = pygame.font.SysFont(None, 20)

    load_puzzle(0)

    while True:
        dt_ms = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    reset_character()
                if event.key == pygame.K_SPACE:
                    run_solve()
                # 1-9 puzzle switching
                if pygame.K_1 <= event.key <= pygame.K_9:
                    load_puzzle(event.key - pygame.K_1)

        _update_animation(dt_ms)
        draw(screen, font_big, font_small)
        pygame.display.flip()


if __name__ == "__main__":
    main()
