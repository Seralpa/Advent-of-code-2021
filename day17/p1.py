# test
target_x = (20, 30)
target_y = (-10, -5)
# input
target_x = (236, 262)
target_y = (-78, -58)

# assume X is 0 when it reaches the target (if it goes high, it takes some time to fall down?)
total_max_y = 0
for i in range(target_y[0], 1000):  # just guessing this is enough lol
	y = 0
	max_y = 0
	vel = i
	while y >= target_y[0]:
		y += vel
		vel -= 1
		if y > max_y:
			max_y = y
		if y >= target_y[0] and y <= target_y[1]:
			if max_y > total_max_y:
				total_max_y = max_y
print(total_max_y)
