file_path = '23/input.txt'
with open(file_path, 'r') as f:
    connections = [line.strip() for line in f.readlines()]

from collections import defaultdict
from itertools import combinations

def build_graph(connections):
    graph = defaultdict(set)
    for connection in connections:
        a, b = connection.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def bron_kerbosch(graph, r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
        return
    for node in list(p):
        new_r = r.union({node})
        new_p = p.intersection(graph[node])
        new_x = x.intersection(graph[node])
        bron_kerbosch(graph, new_r, new_p, new_x, cliques)
        p.remove(node)
        x.add(node)

def find_largest_clique(graph):
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    largest_clique = max(cliques, key=len)
    return sorted(largest_clique)

graph = build_graph(connections)
largest_clique = find_largest_clique(graph)
password = ",".join(largest_clique)
print(f"Password to the LAN party: {password}")