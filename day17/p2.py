# test
target_x = (20, 30)
target_y = (-10, -5)
# input
target_x = (236, 262)
target_y = (-78, -58)

valid_x: dict[int, set] = dict()
valid_y: dict[int, set] = dict()
for i in range(target_x[1] + 1):
	x = 0
	vel = i
	steps = 0
	while x <= target_x[1] and vel >= 0:
		steps += 1
		x += vel
		vel -= 1
		if x >= target_x[0] and x <= target_x[1]:
			valid_x.setdefault(i, {steps}).add(steps)
			if vel == 0:
				from_steps_to_inf = set(range(steps, 1000))  # guessing no valid path takes more than 1000 steps
				valid_x.setdefault(i, from_steps_to_inf).update(from_steps_to_inf)

for i in range(target_y[0], 1000):  # just guessing this is enough lol
	y = 0
	vel = i
	steps = 0
	while y >= target_y[0]:
		steps += 1
		y += vel
		vel -= 1
		if y >= target_y[0] and y <= target_y[1]:
			valid_y.setdefault(i, {steps}).add(steps)

valid = set()
for x, xv in valid_x.items():
	for y, yv in valid_y.items():
		if xv & yv:
			valid.add((x, y))
print(len(valid))
