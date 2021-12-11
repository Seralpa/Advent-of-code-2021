with open("input.txt") as f:
	octopi = [[int(x) for x in list(l)] for l in f.read().splitlines()]

total_flashes = 0
for _ in range(100):
	flashed = set()
	new_flashed = set()
	for i, l in enumerate(octopi):
		for j, o in enumerate(l):
			octopi[i][j] += 1
			if octopi[i][j] > 9:
				flashed.add((i, j))
				new_flashed.add((i, j))
				octopi[i][j] = -999  # so no octopus flashes twice

	while len(new_flashed) > 0:
		# increment neighbors
		for f in new_flashed:
			for i1 in range(f[0] - 1, f[0] + 2):
				for j1 in range(f[1] - 1, f[1] + 2):
					if i1 >= 0 and i1 < len(octopi) and j1 >= 0 and j1 < len(l):
						octopi[i1][j1] += 1
		new_flashed = set()

		# check for new flashes
		for i, l in enumerate(octopi):
			for j, o in enumerate(l):
				if o > 9:
					new_flashed.add((i, j))
					flashed.add((i, j))
					octopi[i][j] = -9

	# reset flashed octopi
	for f in flashed:
		octopi[f[0]][f[1]] = 0
	total_flashes += len(flashed)

print(total_flashes)