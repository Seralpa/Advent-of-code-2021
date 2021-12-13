from collections import defaultdict
from typing import DefaultDict


def fold(dots: DefaultDict, orientation: str, coord: int) -> DefaultDict:
	new_dots = []
	to_remove = []
	if orientation == "x":
		for d, v in dots.items():
			if d[0] < coord or v == 0:
				continue
			distance = d[0] - coord
			new_dots.append((coord - distance, d[1]))
			to_remove.append(d)

	elif orientation == "y":
		for d, v in dots.items():
			if d[1] < coord or v == 0:
				continue
			distance = d[1] - coord
			new_dots.append((d[0], coord - distance))
			to_remove.append(d)
	for d in to_remove:
		dots[d] = 0
	for d in new_dots:
		dots[d] = 1


with open("input.txt") as f:
	dots, folds = f.read().split("\n\n")
dots_dict = defaultdict(int)

for d in dots.split("\n"):
	d1, d2 = d.split(",")
	d1 = int(d1)
	d2 = int(d2)
	dots_dict[(d1, d2)] = 1
f = folds.split("\n")[0].split(" ")[-1].split("=")
fold(dots_dict, f[0], int(f[1]))
print(len([v for v in dots_dict.values() if v == 1]))
