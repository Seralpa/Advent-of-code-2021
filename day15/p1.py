import os
import networkx as nx

cwd = os.getcwd()
with open(f"{cwd}/input.txt") as f:
	data = [[int(c) for c in l] for l in f.read().splitlines()]

g = nx.DiGraph()
for i, l in enumerate(data):
	for j, n in enumerate(l):
		if i < len(data) - 1:
			g.add_edge((i + 1, j), (i, j), weight=n)
		if i > 0:
			g.add_edge((i - 1, j), (i, j), weight=n)
		if j < len(l) - 1:
			g.add_edge((i, j + 1), (i, j), weight=n)
		if j > 0:
			g.add_edge((i, j - 1), (i, j), weight=n)

print(nx.shortest_path_length(g, (0, 0), (len(data) - 1, len(data[0]) - 1), "weight"))
