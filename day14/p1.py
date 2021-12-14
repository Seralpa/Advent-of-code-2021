from Node import Node

with open("input_test.txt") as f:
	starting = list(f.readline().strip())
	f.readline()
	rules = dict()
	for l in f.read().splitlines():
		line = l.split(" -> ")
		rules[line[0]] = line[1]

polymer = Node.from_list(starting)

for iter in range(10):
	insertions: list[tuple[Node, str]] = []
	for n in polymer:
		if not n.next:
			break
		pair = "".join([n.data, n.next.data])
		if pair in rules.keys():
			insertions.append((n, rules[pair]))
	for n, v in insertions:
		n.insert_after(Node(v))

counter = dict()
for n in polymer:
	if n.data in counter.keys():
		counter[n.data] += 1
	else:
		counter[n.data] = 1
print(max(counter.values()) - min(counter.values()))
