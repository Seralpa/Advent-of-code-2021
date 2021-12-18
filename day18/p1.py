import os
from math import floor, ceil


def reduce(final_sum: list) -> list:
	while True:
		# explode
		level = -1
		last_num_pos = 0
		explodes_done = False
		for i, c in enumerate(final_sum):
			if c == '[':
				level += 1
				if level >= 4:
					if last_num_pos != 0:
						final_sum[last_num_pos] += final_sum[i + 1]
					for j in range(i + 4, len(final_sum)):
						if final_sum[j] not in ('[', ']', ','):
							final_sum[j] += final_sum[i + 3]
							break
					del final_sum[i:i + 5]
					final_sum.insert(i, 0)
					explodes_done = True
					break

			elif c == ']':
				level -= 1
			elif c == ',':
				pass
			else:
				last_num_pos = i
		if explodes_done:
			continue
		# split
		splits_done = False
		for i, c in enumerate(final_sum):
			if c not in ('[', ']', ','):
				if c >= 10:
					left = floor(c / 2)
					right = ceil(c / 2)
					del final_sum[i]
					final_sum.insert(i, ']')
					final_sum.insert(i, right)
					final_sum.insert(i, ',')
					final_sum.insert(i, left)
					final_sum.insert(i, '[')
					splits_done = True
					break
		if not splits_done:
			break
	return final_sum


def magnitude(final_sum: list) -> int:
	while len(final_sum) > 1:
		for i, c in enumerate(final_sum):
			if c not in ('[', ']', ','):
				if final_sum[i + 2] not in ('[', ']', ','):
					res = 3 * c + 2 * final_sum[i + 2]
					del final_sum[i - 1:i + 4]
					final_sum.insert(i - 1, res)
					break
	return final_sum[0]


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input_test.txt") as f:
	nums = [list(l) for l in f.read().strip().splitlines()]

for n in nums:
	for i in range(len(n)):
		if n[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
			n[i] = int(n[i])

final_sum = nums[0]
for n in nums[1:]:
	final_sum.insert(0, '[')
	final_sum.append(',')
	final_sum += n
	final_sum.append(']')
	final_sum = reduce(final_sum)

while len(final_sum) > 1:
	for i, c in enumerate(final_sum):
		if c not in ('[', ']', ','):
			if final_sum[i + 2] not in ('[', ']', ','):
				res = 3 * c + 2 * final_sum[i + 2]
				del final_sum[i - 1:i + 4]
				final_sum.insert(i - 1, res)
				break
print(final_sum[0])