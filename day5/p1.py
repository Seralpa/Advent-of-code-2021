from collections import defaultdict
from operator import add
from math import gcd


def normalize_vector(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
	vector = [x2 - x1 for x1, x2 in zip(p1, p2)]
	div = gcd(*vector)
	return tuple(map(lambda x: int(x / div), vector))


with open("input.txt") as f:
	data = [l.split(" -> ") for l in f.read().splitlines()]

lines: list[tuple[tuple, tuple]] = []
for d in data:
	p1 = tuple(map(int, d[0].split(",")))
	p2 = tuple(map(int, d[1].split(",")))
	if p1[0] == p2[0] or p1[1] == p2[1]:
		lines.append((p1, p2))

points = defaultdict(int)
for l in lines:
	p1, p2 = l
	vector = normalize_vector(p1, p2)
	done = False
	while not done:
		done = p1 == p2
		points[p1] += 1
		p1 = tuple(map(add, p1, vector))

print(len([p for p in points.values() if p >= 2]))
