from collections import deque

def parse_input():
    INPUT = "12/input.txt"
    grid: list[list[str]] = []
    with open(INPUT) as file:
        lines = file.read().splitlines()
        for line in lines:
            grid.append([c for c in line])
    return grid

groups: list[list[tuple[int, int]]] = []
visited: list[list[bool]] = []

def is_valid(grid, x, y):
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])

def get_adjacent_coords(x: int, y: int) -> list[tuple[int, int]]:
    return [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

def bfs(grid: list[list[str]], x: int, y: int) -> None:
    global groups
    global visited

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    group: list[tuple[int, int]] = [(x, y)]

    while len(q):
        x, y = q.popleft()
        for z, a in get_adjacent_coords(x, y):
            if is_valid(grid, z, a) and not visited[z][a] and grid[z][a] == grid[x][y]:
                q.append((z, a))
                visited[z][a] = True
                group.append((z, a))

    groups.append(group)

def perimeter(group: list[tuple[int, int]]) -> int:
    p = 0
    for x, y in group:
        for a in get_adjacent_coords(x, y):
            if a not in group:
                p += 1
    return p

def solution1():
    global groups
    global visited
    grid = parse_input()
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not visited[x][y]:
                bfs(grid, x, y)

    sum_prices = 0
    for group in groups:
        sum_prices += len(group) * perimeter(group)
    print(sum_prices)

if __name__ == "__main__":
    solution1()