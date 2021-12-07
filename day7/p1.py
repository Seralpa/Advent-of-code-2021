import statistics as st

with open("input_test.txt") as f:
	data = [int(l) for l in f.read().split(",")]

target = int(round(st.mean(data)))
print(sum([abs(x - target) for x in data]))
