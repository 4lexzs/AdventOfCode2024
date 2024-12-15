from pathlib import Path

DIRECTIONS: list[tuple[int, int]] = [
    (-1, 0),  # Up
    (0, 1),  # Right
    (1, 0),  # Down
    (0, -1),  # Left
]
NUMBER_OF_DIRECTIONS: int = len(DIRECTIONS)
STARTING_DIRECTION: tuple[int, int] = DIRECTIONS[0]

ROWS: int
COLS: int

def read_input() -> list[str]:
    # Read the input data
    input_data: str = Path("06/input6.txt").resolve().read_text().strip()

    # Parse the input data
    return input_data.split("\n")

def find_guard_start(input_data: list[str]) -> tuple[int, int]:
    """Finds the guard's starting position marked by '^'."""
    for i, row in enumerate(input_data):
        if "^" in row:
            return i, row.index("^")
    return -1, -1  # Default if not found

def move_guard(
    input_data: list[str],
    direction: tuple[int, int],
    current_pos: tuple[int, int],
) -> tuple[tuple[int, int], tuple[int, int]]:
    # Get the target position after moving in the current direction
    new_x, new_y = current_pos[0] + direction[0], current_pos[1] + direction[1]

    # If the new position is out of bounds, stop
    if new_x < 0 or new_x >= ROWS or new_y < 0 or new_y >= COLS:
        return (-1, -1), direction

    if input_data[new_x][new_y] == "#":
        # There is an obstacle in the way, turn right
        direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % NUMBER_OF_DIRECTIONS]
        # Don't move the guard, just change the direction
        return current_pos, direction

    # Update the current position
    return (new_x, new_y), direction

def find_path(input_data: list[str], starting_position: tuple[int, int]) -> set[tuple[int, int]]:
    direction: tuple[int, int] = STARTING_DIRECTION
    visited: set[tuple[int, int]] = set()
    current_pos: tuple[int, int] = starting_position

    while True:
        # Add the current position to the visited set
        visited.add(current_pos)

        # Move the guard in the current direction
        current_pos, direction = move_guard(
            input_data,
            direction,
            current_pos,
        )

        if current_pos == (-1, -1):
            break

    return visited

def solution1() -> None:
    global ROWS, COLS

    # Read the input data
    input_data: list[str] = read_input()
    ROWS, COLS = len(input_data), len(input_data[0])

    # Find the guard starting position (^)
    start_pos: tuple[int, int] = find_guard_start(input_data)
    # Find the path the guard takes to patrol the area
    path: set[tuple[int, int]] = find_path(input_data, start_pos)

    print(len(path))

if __name__ == "__main__":
    solution1()
