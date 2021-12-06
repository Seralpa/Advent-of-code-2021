from collections import defaultdict

fishes = defaultdict(int)
with open("input.txt") as f:
	for n in f.read().split(","):
		fishes[int(n)] += 1

for _ in range(256):
	aux = fishes[0]
	for i in range(1, 9):
		fishes[i - 1] = fishes[i]
	fishes[6] += aux
	fishes[8] = aux
print(sum(fishes.values()))
