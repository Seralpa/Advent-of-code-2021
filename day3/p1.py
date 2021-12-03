from collections import Counter

with open("input.txt") as f:
	data: list[list] = [list(l) for l in f.read().splitlines()]

gamma = list()
epsilon = list()
for i in range(len(data[0])):
	digit_count = Counter([d[i] for d in data]).most_common(2)
	gamma.append(digit_count[0][0])
	epsilon.append(digit_count[1][0])

gamma = ''.join(gamma)
epsilon = ''.join(epsilon)
print(f"{int(gamma, 2)*int(epsilon, 2)}")
