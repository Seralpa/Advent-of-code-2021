with open("input.txt") as f:
	polymer = list(f.readline().strip())
	f.readline()
	rules = dict()
	for l in f.read().splitlines():
		line = l.split(" -> ")
		rules[line[0]] = line[1]

pairs = dict()

for i in range(len(polymer) - 1):
	p = "".join(polymer[i:i + 2])
	if p in pairs.keys():
		pairs[p] += 1
	else:
		pairs[p] = 1

for iter in range(40):
	new_pairs = dict()
	for k, v in pairs.items():
		if k not in rules.keys():
			continue
		new1 = k[0] + rules[k]
		new2 = rules[k] + k[1]
		if new1 in new_pairs.keys():
			new_pairs[new1] += v
		else:
			new_pairs[new1] = v
		if new2 in new_pairs.keys():
			new_pairs[new2] += v
		else:
			new_pairs[new2] = v
	pairs = new_pairs

count = dict()
for k, v in pairs.items():
	if k[0] in count.keys():
		count[k[0]] += v
	else:
		count[k[0]] = v
	if k[1] in count.keys():
		count[k[1]] += v
	else:
		count[k[1]] = v

# all values are counted twice (pairs overlap) except first and last element those
# don't change during the simulation
count[polymer[0]] += 1
count[polymer[-1]] += 1
print(max(count.values()) / 2 - min(count.values()) / 2)