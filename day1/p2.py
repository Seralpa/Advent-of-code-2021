with open("input.txt") as f:
	depths: list[int] = [int(l.strip()) for l in f.readlines()]

increases = 0
prev_window = 9999999  # first window must not be an increase
for i in range(len(depths) - 2):
	window = depths[i] + depths[i + 1] + depths[i + 2]
	if window > prev_window:
		increases += 1
	prev_window = window
print(increases)