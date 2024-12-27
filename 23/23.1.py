file_path = '23/input.txt'
with open(file_path, 'r') as f:
    connections = [line.strip() for line in f.readlines()]

from collections import defaultdict
from itertools import combinations

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

triangles = set()
for node in graph:
    neighbors = graph[node]
    for n1, n2 in combinations(neighbors, 2):
        if n2 in graph[n1]:
            triangles.add(tuple(sorted([node, n1, n2])))

filtered_triangles = [triangle for triangle in triangles if any(comp[0] == 't' for comp in triangle)]

num_triangles = len(filtered_triangles)
print(f"Number of triangles with at least one 't'-starting computer: {num_triangles}")