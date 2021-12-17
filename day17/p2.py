# test
target_x = (20, 30)
target_y = (-10, -5)
# input
target_x = (236, 262)
target_y = (-78, -58)


def test_path(vel: list[int, int]) -> int:
	pos = [0, 0]
	while pos[1] >= target_y[0]:
		if pos[0] >= target_x[0] and pos[0] <= target_x[1] and pos[1] >= target_y[0] and pos[1] <= target_y[1]:
			return True
		pos[0] += vel[0]
		pos[1] += vel[1]
		if vel[0] < 0:
			vel[0] += 1
		elif vel[0] > 0:
			vel[0] -= 1
		vel[1] -= 1
	return 0


valid_x = []
for i in range(target_x[1] + 1):
	final_x = 0
	vel = i
	while final_x < target_x[0] and vel > 0:
		final_x += vel
		vel -= 1
		if final_x >= target_x[0] and final_x <= target_x[1]:
			valid_x.append(i)

valid_y = []
for i in range(target_y[0], 1000):  # just guessing this is enough lol
	final_y = 0
	vel = i
	while final_y >= target_y[0]:
		final_y += vel
		vel -= 1
		if final_y >= target_y[0] and final_y <= target_y[1]:
			valid_y.append(i)

valid = set()
for x in valid_x:
	for y in valid_y:
		if test_path([x, y]):
			valid.add((x, y))
print(len(valid))
