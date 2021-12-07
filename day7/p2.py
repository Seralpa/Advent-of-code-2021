from math import ceil
with open("input.txt") as f:
	data = [int(l) for l in f.read().split(",")]

res = set()
for target in range(min(data), max(data) + 1):
	res.add(sum([sum(range(abs(x - target) + 1)) for x in data]))
print(min(res))