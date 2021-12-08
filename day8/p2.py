def get_inputs_of_len(signal: list[set[str]], n: int) -> list[set[str]]:
	return [s for s in signal if len(s) == n]


def find_five(signal: list[set[str]], bd_signal: set[str]) -> set[str]:
	for s in get_inputs_of_len(signal, 5):
		if bd_signal.issubset(s):
			return s


def find_three(signal: list[set[str]], seven: set[str]) -> set[str]:
	# print(bacf_signal)
	for s in get_inputs_of_len(signal, 5):
		if seven.issubset(s):
			return s


# with open("day8/input_test.txt") as f:
# with open("input_test.txt") as f:
with open("input.txt") as f:
	data = [l.split(" | ") for l in f.read().splitlines()]
for d in data:
	d[0] = [set(a) for a in d[0].split(" ")]
	d[1] = d[1].split(" ")

rules = {
    2: {"c", "f"},
    3: {"a", "c", "f"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "c", "d", "e", "f", "g"},
    6: {"a", "b", "c", "d", "e", "f", "g"},
    7: {"a", "b", "c", "d", "e", "f", "g"},
}

sig_dig = {
    frozenset("abcefg"): 0,
    frozenset("cf"): 1,
    frozenset("acdeg"): 2,
    frozenset("acdfg"): 3,
    frozenset("bcdf"): 4,
    frozenset("abdfg"): 5,
    frozenset("abdefg"): 6,
    frozenset("acf"): 7,
    frozenset("abcdefg"): 8,
    frozenset("abcdfg"): 9,
}
total = 0
for signal, output in data:
	# signal -> light
	avail_options = {
	    "a": {"a", "b", "c", "d", "e", "f", "g"},
	    "b": {"a", "b", "c", "d", "e", "f", "g"},
	    "c": {"a", "b", "c", "d", "e", "f", "g"},
	    "d": {"a", "b", "c", "d", "e", "f", "g"},
	    "e": {"a", "b", "c", "d", "e", "f", "g"},
	    "f": {"a", "b", "c", "d", "e", "f", "g"},
	    "g": {"a", "b", "c", "d", "e", "f", "g"},
	}
	seven = get_inputs_of_len(signal, 3)[0]
	four = get_inputs_of_len(signal, 4)[0]
	one = get_inputs_of_len(signal, 2)[0]
	eight = get_inputs_of_len(signal, 7)[0]
	# print(f"{seven=} {four=} {seven-four=}")
	a_signal = list(seven - four)[0]
	bd_signal = four - seven
	five = find_five(signal, bd_signal)
	c_signal = one - five
	avail_options[a_signal] = set("a")
	for k, v in avail_options.items():
		if k == a_signal:
			continue
		v.remove("a")
	# print(f"step 1 {avail_options}\n\n")

	# print(f"{seven=} {four=} {seven-four=}")
	for option in bd_signal:
		avail_options[option].intersection_update({"b", "d"})
	for k, v in avail_options.items():
		if k in bd_signal:
			continue
		v -= {"b", "d"}
	# print(f"step 2 {avail_options}\n\n")

	for s in signal:
		options = rules[len(s)]
		for c in s:
			avail_options[c] = {o for o in avail_options[c] if o in options}
	# print(avail_options)

	# remove pairs
	for k1, v1 in avail_options.items():
		for k2, v2 in avail_options.items():
			if k1 != k2 and v1 == v2 and len(v1) <= 2:
				for k3, v3 in avail_options.items():
					if k3 in (k1, k2):
						continue
					v3 -= v1

	avail_options[list(c_signal)[0]] = {"c"}
	for k, v in avail_options.items():
		if k in c_signal:
			continue
		v -= {"c"}
	# print(f"step 3 {avail_options}\n\n")

	e_signal = eight - five - c_signal
	avail_options[list(e_signal)[0]] = {"e"}
	for k, v in avail_options.items():
		if k in e_signal:
			continue
		v -= {"e"}
	# print(f"step 4 {avail_options}\n\n")
	# print(seven)
	three = find_three(signal, seven)
	b_signal = (eight - three).intersection(bd_signal)
	# print(three)
	# print(b_signal)
	avail_options[list(b_signal)[0]] = {"b"}
	for k, v in avail_options.items():
		if k in b_signal:
			continue
		v -= {"b"}
	# print(f"step 5 {avail_options}\n\n")

	val = 0
	for o in output:
		# print(o)
		final_signal = set()
		for c in o:
			final_signal.add(list(avail_options[c])[0])
		# 	print(f"{c} {final_signal}")
		# print(final_signal)
		val *= 10
		val += sig_dig[frozenset(final_signal)]
	# print(val)
	total += val
print(total)