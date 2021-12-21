def die():
	n = 0
	while True:
		yield n + 1
		n = (n + 1) % 100


# -1 to make the modulo easier
p1 = 2 - 1
p2 = 5 - 1
# test
# p1 = 4 - 1
# p2 = 8 - 1

p1_score = 0
p2_score = 0
MAX_SCORE = 1000
d = die()
n_rolls = 0
while True:
	d1, d2, d3 = next(d), next(d), next(d)
	p1 = (p1 + d1 + d2 + d3) % 10
	# +1 because p1 starts at 0 instead of 1
	p1_score += p1 + 1
	n_rolls += 3
	if p1_score >= MAX_SCORE:
		looser = p2_score
		break
	d4, d5, d6 = next(d), next(d), next(d)
	p2 = (p2 + d4 + d5 + d6) % 10
	# +1 because p2 starts at 0 instead of 1
	p2_score += p2 + 1
	n_rolls += 3
	if p2_score >= MAX_SCORE:
		looser = p1_score
		break
print(f"{looser*n_rolls}")