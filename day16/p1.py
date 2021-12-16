import os


def read_n_packets(binary: list[str], n: int) -> tuple[int, int]:
	""" Returns total version of n packets and total size of those packets """
	total_version = 0
	current = 0  # current bit in parsing
	for _ in range(n):
		result = read_packet(binary[current:])
		total_version += result[0]
		current += result[1]
	return (total_version, current)


def read_packets(binary: list[str]) -> int:
	""" Returns total version until binary is exhasuted (no padding) """
	total_version = 0
	current = 0  # current bit in parsing
	while current < len(binary):
		result = read_packet(binary[current:])
		total_version += result[0]
		current += result[1]
	return total_version


def read_packet(binary: list[str]) -> tuple[int, int]:
	""" Returns total version of 1 packet """
	current = 0
	total_version = int(''.join(binary[current:current + 3]), 2)
	tid = int(''.join(binary[current + 3:current + 6]), 2)
	current += 6
	if tid == 4:  # literal
		gid = current
		while True:
			if binary[gid] == '0':  # last group
				current = gid + 5
				break
			gid += 5
	else:  # operator
		current = 6
		mode = binary[current]
		current += 1
		if mode == '0':
			packet_size = int(''.join(binary[current:current + 15]), 2)
			current += 15
			total_version += read_packets(binary[current:current + packet_size])
			current += packet_size
		else:
			n_packets = int(''.join(binary[current:current + 11]), 2)
			current += 11
			result = read_n_packets(binary[current:], n_packets)
			total_version += result[0]
			current += result[1]
	return total_version


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	hexadecimal = f.readline()

binary = list(bin(int(hexadecimal, 16))[2:].zfill(len(hexadecimal) * 4))
print(read_packet(binary)[0])