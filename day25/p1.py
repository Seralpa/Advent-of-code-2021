import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	sea_floor = [list(l) for l in f.read().splitlines()]

movement = True
step = 0
while movement:
	movement = False
	to_move = set()
	for i, l in enumerate(sea_floor):
		for j, c in enumerate(l):
			if c == ">" and sea_floor[i][(j + 1) % len(sea_floor[i])] == '.':
				to_move.add((i, j))
	for c in to_move:
		sea_floor[c[0]][c[1]] = '.'
		sea_floor[c[0]][(c[1] + 1) % len(sea_floor[i])] = '>'
	if len(to_move) > 0:
		movement = True
	to_move = set()
	for i, l in enumerate(sea_floor):
		for j, c in enumerate(l):
			if c == "v" and sea_floor[(i + 1) % len(sea_floor)][j] == '.':
				to_move.add((i, j))
	for c in to_move:
		sea_floor[c[0]][c[1]] = '.'
		sea_floor[(c[0] + 1) % len(sea_floor)][c[1]] = 'v'
	if len(to_move) > 0:
		movement = True
	step += 1
print(step)