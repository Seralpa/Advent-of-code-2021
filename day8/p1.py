# with open("day8/input_test.txt") as f:
# with open("input_test.txt") as f:
with open("input.txt") as f:
	data = [l.split(" | ") for l in f.read().splitlines()]
for d in data:
	d[0] = d[0].split(" ")
	d[1] = d[1].split(" ")
print(sum([len(["a" for i in d[1] if len(i) in (2, 3, 4, 7)]) for d in data]))
