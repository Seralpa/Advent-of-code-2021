import os


def prod(l: list[int]) -> int:
	res = 1
	for e in l:
		res *= e
	return res


def gt(l: list[int]) -> int:
	return int(l[0] > l[1])


def lt(l: list[int]) -> int:
	return int(l[0] < l[1])


def eq(l: list[int]) -> int:
	return int(l[0] == l[1])


def read_n_packets(binary: list[str], n: int, op) -> tuple[int, int]:
	""" Returns value of n packets with op and total size of those packets """
	values = []
	current = 0  # current bit in parsing
	for _ in range(n):
		result = read_packet(binary[current:])
		values.append(result[0])
		current += result[1]
	return (op(values), current)


def read_packets(binary: list[str], op) -> int:
	""" Returns value of packets with op until binary is exhasuted (no padding) """
	values = []
	current = 0  # current bit in parsing
	while current < len(binary):
		result = read_packet(binary[current:])
		values.append(result[0])
		current += result[1]
	return op(values)


def read_packet(binary: list[str]) -> tuple[int, int]:
	""" Returns total version of 1 packet """
	current = 0
	# total_version = int(''.join(binary[current:current + 3]), 2)
	tid = int(''.join(binary[current + 3:current + 6]), 2)
	current += 6
	if tid == 4:  # literal
		gid = current
		number = ''
		while True:
			if binary[gid] == '0':  # last group
				number += ''.join(binary[gid + 1:gid + 5])
				value = int(number, 2)
				current = gid + 5
				break
			number += ''.join(binary[gid + 1:gid + 5])
			gid += 5
	else:  # operator
		ops = {
		    0: sum,
		    1: prod,
		    2: min,
		    3: max,
		    5: gt,
		    6: lt,
		    7: eq,
		}
		mode = binary[current]
		current += 1
		if mode == '0':
			packet_size = int(''.join(binary[current:current + 15]), 2)
			current += 15
			value = read_packets(binary[current:current + packet_size], ops[tid])
			current += packet_size
		else:
			n_packets = int(''.join(binary[current:current + 11]), 2)
			current += 11
			result = read_n_packets(binary[current:], n_packets, ops[tid])
			value = result[0]
			current += result[1]
	return (value, current)


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	hexadecimal = f.readline()

binary = list(bin(int(hexadecimal, 16))[2:].zfill(len(hexadecimal) * 4))
print(read_packet(binary)[0])