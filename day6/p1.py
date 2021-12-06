with open("input.txt") as f:
	fishes = [int(l) for l in f.read().split(",")]

for d in range(80):
	new_fishes = 0
	for i, fish in enumerate(fishes):
		if fish == 0:
			new_fishes += 1
			fishes[i] = 6
		else:
			fishes[i] -= 1
	fishes.extend([8 for _ in range(new_fishes)])
print(len(fishes))