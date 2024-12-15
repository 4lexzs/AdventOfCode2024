import numpy as np

def parse(part2=False):
    with open("15/input.txt") as f:
        grid = []
        movements = ""
        moves = False
        y = 0
        start = ()
        for line in f:
            line = line.strip()
            if moves:
                movements += line
                continue
            if "@" in line:
                start = line.index("@"), y
                if part2:
                    line = line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
                    grid.append(list(line))
                    start = line.index("@"), y
                    y += 1
                    continue
            if line == "":
                moves = True
            else:
                if part2:
                    line = line.replace("#", "##").replace("O", "[]").replace(".", "..")
                grid.append(list(line))
                y += 1
    grid = np.array(grid)
    return grid, start, movements


def move(left, right, y, direction, mod_grid):
    next_l = mod_grid[y + direction][left]
    next_r = mod_grid[y + direction][right]
    if next_l == "#" or next_r == '#':
        return False
    elif next_l == "." and next_r == ".":
        mod_grid[y + direction][left] = "["
        mod_grid[y + direction][right] = "]"
        mod_grid[y][left] = "."
        mod_grid[y][right] = "."
        return True
    else:
        movable_r = movable_l = True
        if next_l == "[":
            movable_l = move(left, right, y + direction, direction, mod_grid)
        if next_r == "[":
            movable_r = move(right, right+1, y + direction, direction, mod_grid)
        if next_l == "]":
            movable_l = move(left-1, left, y + direction, direction, mod_grid)
        movement_possible = movable_l and movable_r
        if movement_possible:
            mod_grid[y+direction][left] = "["
            mod_grid[y+direction][right] = "]"
            mod_grid[y][left] = "."
            mod_grid[y][right] = "."
        return movement_possible


def solution2():
    grid, start, movements = parse(part2=True)
    x, y = start
    count = 0
    for mov in movements:
        match mov:
            case "<":
                if grid[y][x-1] == "#":
                    continue
                elif grid[y][x-1] in ["[", "]"]:
                    temp = x-1
                    while grid[y][temp] in ["[", "]"]:
                        temp -= 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][temp:x-1] = grid[y][temp+1:x]
                        grid[y][x-1] = "@"
                        grid[y][x] = "."
                        x -= 1
                else:
                    grid[y][x - 1] = "@"
                    grid[y][x] = "."
                    x -= 1
            case ">":
                if grid[y][x + 1] == "#":
                    continue
                elif grid[y][x + 1] in ["[", "]"]:
                    temp = x + 1
                    while grid[y][temp] in ["[", "]"]:
                        temp += 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][x+2:temp+1] = grid[y][x+1:temp]
                        grid[y][x + 1] = "@"
                        grid[y][x] = "."
                        x += 1
                else:
                    grid[y][x + 1] = "@"
                    grid[y][x] = "."
                    x += 1
            case "^":
                current = grid[y-1][x]
                if current == "#":
                    continue
                elif current in ["[", "]"]:
                    if current == "[":
                        left, right = x, x + 1
                    else:
                        left, right = x - 1, x
                    mod_grid = grid.copy()
                    check_move = move(left, right, y - 1, -1, mod_grid)
                    if not check_move:
                        continue
                    else:
                        grid = mod_grid
                        grid[y-1][x] = "@"
                        grid[y][x] = "."
                        y -= 1
                else:
                    grid[y - 1][x] = "@"
                    grid[y][x] = "."
                    y -= 1
            case "v":
                current = grid[y+1][x]
                if current == "#":
                    continue
                elif current in ["[", "]"]:
                    if current == "[":
                        left, right = x, x + 1
                    else:
                        left, right = x - 1, x
                    mod_grid = grid.copy()
                    check_move = move(left, right, y + 1, 1, mod_grid)
                    if not check_move:
                        continue
                    else:
                        grid = mod_grid
                        grid[y + 1][x] = "@"
                        grid[y][x] = "."
                        y += 1
                else:
                    grid[y + 1][x] = "@"
                    grid[y][x] = "."
                    y += 1
        count += 1
    boxes = np.where(grid == "[")
    boxes = list(zip(boxes[0], boxes[1]))
    result = 0
    for i, j in boxes:
        result += 100 * i + j
    print(result)

solution2()