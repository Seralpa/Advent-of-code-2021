import statistics as st

with open("input.txt") as f:
	lines = [l for l in f.read().splitlines()]

pairs = {"(": ")", "[": "]", "<": ">", "{": "}"}
complete_values = {")": 1, "]": 2, "}": 3, ">": 4}
scores = []
for l in lines:
	invalid = False
	open_chars = []
	for i, c in enumerate(l):
		if c in ("(", "[", "<", "{"):
			open_chars.append(c)
		elif c in (")", "]", ">", "}"):
			if pairs[open_chars[-1]] == c:
				open_chars.pop()
			else:
				invalid = True
				break
		else:
			raise ValueError
	if invalid:
		continue
	completion = [pairs[c] for c in reversed(open_chars)]
	score = 0
	for c in completion:
		score *= 5
		score += complete_values[c]
	scores.append(score)

print(st.median(scores))