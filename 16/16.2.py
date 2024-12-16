import heapq
from collections import defaultdict

WALL = '#'
START = 'S'
END = 'E'

def parse_input(file_name: str) -> list[list[str]]:
    """
    Reads the maze from the input file and returns it as a 2D list.
    """
    with open(file_name, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def get_neighbors(maze, r, c, direction):
    """
    Returns all possible neighbors (row, col, direction, cost) from the current position and direction.
    """
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    clockwise = ['N', 'E', 'S', 'W']

    neighbors = []
    rows, cols = len(maze), len(maze[0])

    # Forward move
    dr, dc = directions[direction]
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != WALL:
        neighbors.append((nr, nc, direction, 1))

    # Rotations
    for new_direction in clockwise:
        if new_direction != direction:
            cost = 1000 if new_direction != opposite[direction] else 2000
            neighbors.append((r, c, new_direction, cost))
    
    return neighbors

def dijkstra(maze, start, end):
    """
    Finds the shortest path from start to end using Dijkstra's algorithm.
    """
    rows, cols = len(maze), len(maze[0])
    directions = ['N', 'E', 'S', 'W']
    start_state = (start[0], start[1], 'E')  # Start facing East
    end_states = [(end[0], end[1], d) for d in directions]

    pq = [(0, start_state)]  # Priority queue (cost, state)
    distances = defaultdict(lambda: float('inf'))
    distances[start_state] = 0
    prev = defaultdict(list)  # Store multiple predecessors for all best paths

    while pq:
        cost, current = heapq.heappop(pq)
        r, c, direction = current

        for neighbor in get_neighbors(maze, r, c, direction):
            nr, nc, nd, move_cost = neighbor
            new_cost = cost + move_cost
            neighbor_state = (nr, nc, nd)

            if new_cost < distances[neighbor_state]:
                distances[neighbor_state] = new_cost
                prev[neighbor_state] = [current]
                heapq.heappush(pq, (new_cost, neighbor_state))
            elif new_cost == distances[neighbor_state]:
                prev[neighbor_state].append(current)

    return distances, prev

def collect_all_best_path_tiles(prev, end_states):
    """
    Collects all tiles that are part of any best path from start to any of the end states.
    """
    best_path_tiles = set()
    stack = list(end_states)

    while stack:
        state = stack.pop()
        if state[:2] not in best_path_tiles:
            best_path_tiles.add(state[:2])
        for predecessor in prev[state]:
            stack.append(predecessor)
    
    return best_path_tiles

def solution2(file_name: str):
    """
    Solution 2: Compute the number of tiles in all best paths.
    """
    maze = parse_input(file_name)
    start = next((r, c) for r, row in enumerate(maze) for c, val in enumerate(row) if val == START)
    end = next((r, c) for r, row in enumerate(maze) for c, val in enumerate(row) if val == END)

    distances, prev = dijkstra(maze, start, end)
    end_states = [(end[0], end[1], d) for d in ['N', 'E', 'S', 'W']]
    best_path_tiles = collect_all_best_path_tiles(prev, end_states)

    print(f"Solution 2: Tiles in best paths = {len(best_path_tiles)}")

if __name__ == "__main__":
    solution2("16/input.txt")