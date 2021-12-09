import networkx as nx

with open("input.txt") as f:
	data = [[int(n) for n in list(l)] for l in f.read().splitlines()]

g = nx.DiGraph()
for i, l in enumerate(data):
	for j, n in enumerate(l):
		if i != 0:
			if 9 != data[i - 1][j] and n < data[i - 1][j]:
				g.add_edge((i, j), (i - 1, j))
		if i != len(data) - 1:
			if 9 != data[i + 1][j] and n < data[i + 1][j]:
				g.add_edge((i, j), (i + 1, j))
		if j != 0:
			if 9 != data[i][j - 1] and n < data[i][j - 1]:
				g.add_edge((i, j), (i, j - 1))
		if j != len(l) - 1:
			if 9 != data[i][j + 1] and n < data[i][j + 1]:
				g.add_edge((i, j), (i, j + 1))

low_points = []
for i, l in enumerate(data):
	for j, n in enumerate(l):
		if i != 0:
			if n >= data[i - 1][j]:
				continue
		if i != len(data) - 1:
			if n >= data[i + 1][j]:
				continue
		if j != 0:
			if n >= data[i][j - 1]:
				continue
		if j != len(l) - 1:
			if n >= data[i][j + 1]:
				continue
		low_points.append((i, j))

basins_lens = []
for r in low_points:
	basins_lens.append(len(nx.algorithms.dag.descendants(g, r)) + 1)
basins_lens.sort(reverse=True)
print(basins_lens[0] * basins_lens[1] * basins_lens[2])
