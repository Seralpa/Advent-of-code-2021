with open("input.txt") as f:
	data = [l.split(" ") for l in f.read().splitlines()]

depth = 0
x = 0
for ins in data:
	if ins[0] == "up":
		depth -= int(ins[1])
	elif ins[0] == "down":
		depth += int(ins[1])
	elif ins[0] == "forward":
		x += int(ins[1])
	else:
		raise ValueError("Unknown instruction!")
print(x * depth)
