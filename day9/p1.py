with open("input.txt") as f:
	data = [[int(n) for n in list(l)] for l in f.read().splitlines()]

risk = 0
for i, l in enumerate(data):
	for j, n in enumerate(l):
		if i != 0:
			if n >= data[i - 1][j]:
				continue
		if i != len(data) - 1:
			if n >= data[i + 1][j]:
				continue
		if j != 0:
			if n >= data[i][j - 1]:
				continue
		if j != len(l) - 1:
			if n >= data[i][j + 1]:
				continue
		risk += n + 1
print(risk)