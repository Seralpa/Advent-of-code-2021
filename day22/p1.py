import os, re

regex = re.compile(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)")

cwd = os.path.dirname(os.path.abspath(__file__))
instructions = []
with open(f"{cwd}/input.txt") as f:
	for l in f.read().strip().splitlines():
		m = regex.match(l)
		instructions.append([
		    0 if m.group(1) == "off" else 1,
		    int(m.group(2)),
		    int(m.group(3)),
		    int(m.group(4)),
		    int(m.group(5)),
		    int(m.group(6)),
		    int(m.group(7))
		])

LIMIT = 50
reactor: list[list[list[int]]] = []
for x in range(LIMIT * 2 + 1):
	reactor.append([])
	for y in range(LIMIT * 2 + 1):
		reactor[x].append([])
		for z in range(LIMIT * 2 + 1):
			reactor[x][y].append(0)

for ins in instructions:
	if ins[1] > LIMIT or ins[2] < -LIMIT or ins[3] > LIMIT or ins[4] < -LIMIT or ins[5] > LIMIT or ins[6] < -LIMIT:
		continue
	for x, mat in enumerate(reactor):
		for y, l in enumerate(mat):
			for z, c in enumerate(l):
				if (x - LIMIT) >= ins[1] and (x - LIMIT) <= ins[2] and (y - LIMIT) >= ins[3] and (
				    y - LIMIT) <= ins[4] and (z - LIMIT) >= ins[5] and (z - LIMIT) <= ins[6]:
					l[z] = ins[0]

print(sum([sum([sum(l) for l in mat]) for mat in reactor]))