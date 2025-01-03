from pathlib import Path
from typing import Callable

def read_input() -> list[str]:
    # Read the input data
    input_data: str = Path("08/input.txt").resolve().read_text().strip()

    # Parse the input data
    return input_data.split("\n")

def find_antennas_coordinates(
    input_data: list[str],
) -> dict[str, list[tuple[int, int]]]:
    antennas: dict[str, list[tuple[int, int]]] = {}

    for y, row in enumerate(input_data):
        for x, char in enumerate(row):
            if char != ".":
                antennas.setdefault(char, []).append((x, y))

    return antennas

def calculate_antinode_projections_updated_model(
    coords: list[tuple[int, int]],
    rows: int,
    cols: int,
) -> set[tuple[int, int]]:
    """
    Given the vector and the coordinates of the antennas, calculate the
    coordinates that have a projection of the vector of the antenna only from
    one point to the other.

    Y' <--- X ---- Y ---> X'

    This means, we need to calculate:
    - the projection of X over Y = X * vector * 2 = X'
    - the projection of Y over X = Y * (-vector) * 2 = Y'

    The coordinates that have the same projection are the ones that
    are in the same line as the vector.
    """
    projections: set[tuple[int, int]] = set()

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            # Calculate the vector (difference in coordinates)
            dx, dy = x2 - x1, y2 - y1

            # Extend projections in both forward (k > 0) and backward (k < 0) directions
            for k in range(
                -cols, cols
            ):  # Reasonable range for k to avoid infinite loop
                x_proj, y_proj = x1 + k * dx, y1 + k * dy
                if 0 <= x_proj < cols and 0 <= y_proj < rows:
                    projections.add((x_proj, y_proj))

    return projections

def find_antinodes(
    projections_function: Callable[
        [list[tuple[int, int]], int, int], set[tuple[int, int]]
    ]
) -> None:
    # Read the input data
    input_data: list[str] = read_input()
    rows, cols = len(input_data), len(input_data[0])

    # Step 1: Find the antennas coordinates
    antennas: dict[str, list[tuple[int, int]]] = find_antennas_coordinates(input_data)

    # Step 2: Calculate antinode projections for each frequency
    all_projections = set()
    for antenna, coordinates in antennas.items():
        if antenna == "#" or len(coordinates) < 2:
            continue

        # Calculate the projection of the vector
        projections: set[tuple[int, int]] = projections_function(
            coordinates, rows, cols
        )

        all_projections.update(projections)

    print(len(all_projections))

def solution2() -> None:
    find_antinodes(calculate_antinode_projections_updated_model)

if __name__ == "__main__":
    solution2()
