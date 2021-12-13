from collections import defaultdict
from typing import DefaultDict


def pretty_print(dots: DefaultDict):
	minx = min([k for k, v in dots_dict.items() if v == 1], key=lambda x: x[0])[0]
	miny = min([k for k, v in dots_dict.items() if v == 1], key=lambda x: x[1])[1]
	maxx = max([k for k, v in dots_dict.items() if v == 1], key=lambda x: x[0])[0]
	maxy = max([k for k, v in dots_dict.items() if v == 1], key=lambda x: x[1])[1]

	for y in range(miny, maxy + 1):
		for x in range(minx, maxx + 1):
			print("#" if dots[(x, y)] == 1 else ".", end=" ")
		print()


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

for f in folds.split("\n"):
	f = f.split(" ")[-1].split("=")
	fold(dots_dict, f[0], int(f[1]))
pretty_print(dots_dict)
