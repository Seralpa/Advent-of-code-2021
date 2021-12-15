import os
import networkx as nx


def add_n_mat(mat, n):
	new_mat = []
	for l in mat:
		new_mat.append(list(map(lambda x: ((x + n - 1) % 9) + 1, l)))
	return new_mat


def add_n_list(l, n):
	return list(map(lambda x: ((x + n - 1) % 9) + 1, l))


cwd = os.getcwd()
with open(f"{cwd}/input.txt") as f:
	data = [[int(c) for c in l] for l in f.read().splitlines()]

orig_data = data[:]
for i in range(4):
	data += add_n_mat(orig_data, i + 1)
aux = []
for l in data:
	aux.append(l[:])
for i in range(4):
	for j, l in enumerate(data):
		l.extend(add_n_list(aux[j], i + 1))

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
