from pathlib import Path

def read_input() -> list[str]:
    # Read the input data
    input_data: str = Path("04/input4.txt").resolve().read_text().strip()

    # Parse the input data
    return [line for line in input_data.split("\n")]

def is_valid_x_mas(
    data: list[str], i: int, j: int, diagonals: list[tuple[int, int]]
) -> bool:
    """
    Check if the cell (i, j) forms the center of a valid X-MAS pattern.
    """
    # Extract characters at diagonal positions
    diag_chars: list[str] = [data[i + di][j + dj] for di, dj in diagonals]

    # Ensure all diagonals are either 'S' or 'M'
    if any(char not in "SM" for char in diag_chars):
        return False

    # Ensure opposite diagonals match ('S' <-> 'M')
    return (
        diag_chars[0] != diag_chars[3]  # Top-left and Bottom-right
        and diag_chars[1] != diag_chars[2]  # Top-right and Bottom-left
    )

def solution2() -> None:
    data: list[str] = read_input()
    repetitions = 0
    rows, cols = len(data), len(data[0])

    # Coordinates of the diagonals
    diagonals: list[tuple[int, int]] = [
        (-1, -1),  # Top-left
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
        (1, 1),  # Bottom-right
    ]

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if data[i][j] == "A" and is_valid_x_mas(data, i, j, diagonals):
                repetitions += 1

    print(repetitions)

if __name__ == "__main__":
    solution2()
