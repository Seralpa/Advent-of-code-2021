import os
from collections import defaultdict


def pretty_print(img_dict: dict):
	mini = min(img_dict.keys(), key=lambda x: x[0])[0]
	maxi = max(img_dict.keys(), key=lambda x: x[0])[0]
	minj = min(img_dict.keys(), key=lambda x: x[1])[1]
	maxj = max(img_dict.keys(), key=lambda x: x[1])[1]
	for i in range(mini, maxi + 1):
		for j in range(minj, maxj + 1):
			print(f"{'#' if img_dict[(i,j)]==1 else '.'}", end='')
		print()


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	enhance_str = f.readline().strip()
	enhance = [1 if c == '#' else 0 for c in enhance_str]
	img_str = [l for l in f.read().strip().splitlines()]
img_dict = defaultdict(int)
img_dict_odd = defaultdict(lambda: 1)
for i, l in enumerate(img_str):
	for j, c in enumerate(l):
		if c == '#':
			img_dict[(i, j)] = 1
			img_dict_odd[(i, j)] = 1
		else:
			img_dict[(i, j)] = 0
			img_dict_odd[(i, j)] = 0

for n in range(50):
	if n == 2:
		print(f"p1: {sum(img_dict.values())}")
	mini = min(img_dict.keys(), key=lambda x: x[0])[0]
	maxi = max(img_dict.keys(), key=lambda x: x[0])[0]
	minj = min(img_dict.keys(), key=lambda x: x[1])[1]
	maxj = max(img_dict.keys(), key=lambda x: x[1])[1]
	updates = dict()
	for i in range(mini - 1, maxi + 2):
		for j in range(minj - 1, maxj + 2):
			binary_str = []
			for i2 in range(-1, 2):
				for j2 in range(-1, 2):
					if enhance[0] == 1 and n % 2 != 0:
						binary_str.append(str(img_dict_odd[(i + i2, j + j2)]))
					else:
						binary_str.append(str(img_dict[(i + i2, j + j2)]))
			binary = int(''.join(binary_str), 2)
			updates[(i, j)] = enhance[binary]
	for k, v in updates.items():
		img_dict[k] = v
		img_dict_odd[k] = v

print(f"p2: {sum(img_dict.values())}")