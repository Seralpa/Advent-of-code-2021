with open("input.txt") as f:
	depths: list[int] = [int(l.strip()) for l in f.readlines()]

increases = 0
for i in range(len(depths) - 1):
	if depths[i] < depths[i + 1]:
		increases += 1
print(increases)
