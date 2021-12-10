with open("input.txt") as f:
	lines = [l for l in f.read().splitlines()]

pairs = {"(": ")", "[": "]", "<": ">", "{": "}"}
err_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
error = 0
for l in lines:
	open_chars = []
	for i, c in enumerate(l):
		if c in ("(", "[", "<", "{"):
			open_chars.append(c)
		elif c in (")", "]", ">", "}"):
			if pairs[open_chars[-1]] == c:
				open_chars.pop()
			else:
				error += err_values[c]
				break
		else:
			raise ValueError
print(error)