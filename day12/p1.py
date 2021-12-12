import networkx as nx

with open("input.txt") as f:
	data = [l.split("-") for l in f.read().splitlines()]
g = nx.Graph()
for d in data:
	g.add_edge(d[0], d[1])


# Original function from https://stackoverflow.com/questions/24471136/how-to-find-all-paths-between-two-graph-nodes
def find_all_paths(graph: nx.Graph, start: str, end: str, path: list[str] = []):
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return []
	paths = []
	node: str
	for node in nx.neighbors(graph, start):
		if node not in path or node.isupper():
			newpaths = find_all_paths(graph, node, end, path)

			for newpath in newpaths:
				paths.append(newpath)
	return paths


print(len(find_all_paths(g, "start", "end")))
