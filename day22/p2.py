import os, re

regex = re.compile(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)")


def check_lights_overlaps(ins: list[int], light_blocks: list[list[int]]) -> list[list[int]]:
	""" returns portions of ins that dont overlap with any light blocks """
	final_partition = []
	for i, block in enumerate(light_blocks):
		ov = overlap(ins, block)
		if not ov:
			continue
		new_blocks = partition(ins, ov)
		for b in new_blocks:
			final_partition += check_lights_overlaps(b, light_blocks[i + 1:])
		return final_partition
	return [ins]


def test_cube(cube: list[int]) -> bool:
	for i in range(3):
		index = i * 2 + 1
		if cube[index] > cube[index + 1]:
			return False
	return True


def size(cube: list[int]) -> int:
	return (cube[2] + 1 - cube[1]) * (cube[4] + 1 - cube[3]) * (cube[6] + 1 - cube[5])


def overlap(c1: list[int], c2: list[int]) -> None | list[int]:
	if c1[1] > c2[2] or c2[1] > c1[2] or c1[3] > c2[4] or c2[3] > c1[4] or c1[5] > c2[6] or c2[5] > c1[6]:
		# no overlap
		return None
	ov = [c1[0]]
	ov.append(max(c1[1], c2[1]))
	ov.append(min(c1[2], c2[2]))
	ov.append(max(c1[3], c2[3]))
	ov.append(min(c1[4], c2[4]))
	ov.append(max(c1[5], c2[5]))
	ov.append(min(c1[6], c2[6]))
	return ov


def partition(cube: list[int], subcube: list[int]) -> None | list[list[int]]:
	""" subcube is always inside cube, output does not include subcube """
	new_cubes = []
	if cube[1:] == subcube[1:]:
		None
	new_cubes.append([cube[0], cube[1], subcube[1] - 1, cube[3], cube[4], cube[5], cube[6]])
	new_cubes.append([cube[0], subcube[2] + 1, cube[2], cube[3], cube[4], cube[5], cube[6]])

	new_cubes.append([cube[0], subcube[1], subcube[2], cube[3], subcube[3] - 1, cube[5], cube[6]])
	new_cubes.append([cube[0], subcube[1], subcube[2], subcube[4] + 1, cube[4], cube[5], cube[6]])

	new_cubes.append([cube[0], subcube[1], subcube[2], subcube[3], subcube[4], cube[5], subcube[5] - 1])
	new_cubes.append([cube[0], subcube[1], subcube[2], subcube[3], subcube[4], subcube[6] + 1, cube[6]])
	return [n for n in new_cubes if test_cube(n)]


cwd = os.path.dirname(os.path.abspath(__file__))
instructions = []
with open(f"{cwd}/input.txt") as f:
	for l in f.read().strip().splitlines():
		m = regex.match(l)
		instructions.append([
		    0 if m.group(1) == "off" else 1,
		    int(m.group(2)),
		    int(m.group(3)),
		    int(m.group(4)),
		    int(m.group(5)),
		    int(m.group(6)),
		    int(m.group(7))
		])

# each block: on/off, xrange, yrange, zrange
light_blocks: list[list[int]] = []
for ins in instructions:
	if ins[0] == 1:
		new_blocks = check_lights_overlaps(ins, light_blocks)
		light_blocks += new_blocks
	else:
		new_light_blocks = []
		for block in light_blocks:
			ov = overlap(ins, block)
			if not ov:
				new_light_blocks.append(block)
			else:
				new_light_blocks += partition(block, ov)
		light_blocks = new_light_blocks

print(sum([size(b) for b in light_blocks]))