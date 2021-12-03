from collections import Counter

with open("input.txt") as f:
	data: list[list] = [list(l) for l in f.read().splitlines()]

# find oxygen
data_aux = data[:]
for i in range(len(data[0])):
	if len(data_aux) <= 1:
		break
	digit_count = Counter([d[i] for d in data_aux]).most_common(2)
	target_digit = "1" if (digit_count[0][1] == digit_count[1][1]) else digit_count[0][0]
	data_aux = [d for d in data_aux if d[i] == target_digit]

oxygen = "".join(data_aux[0])

# co2 scrubing
data_aux = data[:]
for i in range(len(data[0])):
	if len(data_aux) <= 1:
		break
	digit_count = Counter([d[i] for d in data_aux]).most_common(2)
	target_digit = "0" if (digit_count[0][1] == digit_count[1][1]) else digit_count[1][0]
	data_aux = [d for d in data_aux if d[i] == target_digit]

co2 = "".join(data_aux[0])

print(f"{int(oxygen,2)*int(co2,2)}")