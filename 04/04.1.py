from pathlib import Path

def read_input() -> list[str]:
    # Read the input data
    input_data: str = Path("04/input4.txt").resolve().read_text().strip()

    # Parse the input data
    return [line for line in input_data.split("\n")]

def is_valid_xmas(
    data: list[str],
    rows: int,
    cols: int,
    i: int,
    j: int,
    direction: tuple[int, int],
) -> bool:
    """Check if 'XMAS' can fit starting at (i, j) in the given direction."""
    row_delta, col_delta = direction
    for k in range(4):
        ni, nj = i + k * row_delta, j + k * col_delta
        if not (0 <= ni < rows and 0 <= nj < cols) or data[ni][nj] != "XMAS"[k]:
            return False
    return True

def solution1() -> None:
    data: list[str] = read_input()
    repetitions = 0
    rows, cols = len(data), len(data[0])

    # Directions: (row_delta, col_delta)
    directions: list[tuple[int, int]] = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1),  # Diagonal Up-Left
    ]

    for i in range(rows):
        for j in range(cols):
            if data[i][j] != "X":  # Start only from 'X'
                continue

            for direction in directions:
                if not is_valid_xmas(data, rows, cols, i, j, direction):
                    continue
                repetitions += 1

    print(repetitions)

if __name__ == "__main__":
    solution1()
