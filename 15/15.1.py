import numpy as np

def parse():
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
            if line == "":
                moves = True
            else:
                grid.append(list(line))
                y += 1
    grid = np.array(grid)
    return grid, start, movements


def solution1():
    grid, start, movements = parse()
    x, y = start
    for mov in movements:
        match mov:
            case "<":
                if grid[y][x-1] == "#":
                    continue
                elif grid[y][x-1] == "O":
                    temp = x-1
                    while grid[y][temp] == "O":
                        temp -= 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][temp:x-1] = "O"
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
                elif grid[y][x + 1] == "O":
                    temp = x + 1
                    while grid[y][temp] == "O":
                        temp += 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][x+2:temp+1] = "O"
                        grid[y][x + 1] = "@"
                        grid[y][x] = "."
                        x += 1
                else:
                    grid[y][x + 1] = "@"
                    grid[y][x] = "."
                    x += 1
            case "^":
                if grid[y-1][x] == "#":
                    continue
                elif grid[y-1][x] == "O":
                    temp = y - 1
                    while grid[temp][x] == "O":
                        temp -= 1
                    if grid[temp][x] == "#":
                        continue
                    else:
                        grid[temp:y-1,x] = "O"
                        grid[y-1][x] = "@"
                        grid[y][x] = "."
                        y -= 1
                else:
                    grid[y - 1][x] = "@"
                    grid[y][x] = "."
                    y -= 1
            case "v":
                if grid[y + 1][x] == "#":
                    continue
                elif grid[y+1][x] == "O":
                    temp = y + 1
                    while grid[temp][x] == "O":
                        temp += 1
                    if grid[temp][x] == "#":
                        continue
                    else:
                        grid[y+2:temp+1,x] = "O"
                        grid[y + 1][x] = "@"
                        grid[y][x] = "."
                        y += 1
                else:
                    grid[y + 1][x] = "@"
                    grid[y][x] = "."
                    y += 1
    boxes = np.where(grid == "O")
    boxes = list(zip(boxes[0], boxes[1]))
    result = 0
    for i, j in boxes:
        result += 100 * i + j
    print(result)

solution1()