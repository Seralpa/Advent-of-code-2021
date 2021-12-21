from collections import defaultdict

p1 = 2 - 1
p2 = 5 - 1
# test
# p1 = 4 - 1
# p2 = 8 - 1
sum_num = defaultdict(int)
for d1 in range(1, 4):
	for d2 in range(1, 4):
		for d3 in range(1, 4):
			sum_num[d1 + d2 + d3] += 1

p1_wins = 0
p2_wins = 0
# ((pos1, score1), (pos2, score2)) -> n_universes
universes: dict[tuple[tuple[int, int], tuple[int, int]], int] = dict()
universes[((p1, 0), (p2, 0))] = 1
MAX_SCORE = 21
while True:
	aux_universes: dict[tuple[int, int], int] = dict()
	for die_sum, n_splits in sum_num.items():
		for state, n_universes in universes.items():
			p1_pos = (state[0][0] + die_sum) % 10
			p1_score = state[0][1] + p1_pos + 1
			if p1_score >= MAX_SCORE:
				p1_wins += n_universes * n_splits
				continue

			if ((p1_pos, p1_score), state[1]) in aux_universes:
				aux_universes[((p1_pos, p1_score), state[1])] += n_universes * n_splits
			else:
				aux_universes[((p1_pos, p1_score), state[1])] = n_universes * n_splits
	universes = aux_universes

	aux_universes: dict[tuple[int, int], int] = dict()
	for die_sum, n_splits in sum_num.items():
		for state, n_universes in universes.items():
			p2_pos = (state[1][0] + die_sum) % 10
			p2_score = state[1][1] + p2_pos + 1
			if p2_score >= MAX_SCORE:
				p2_wins += n_universes * n_splits
				continue
			if (state[0], (p2_pos, p2_score)) in aux_universes:
				aux_universes[(state[0], (p2_pos, p2_score))] += n_universes * n_splits
			else:
				aux_universes[(state[0], (p2_pos, p2_score))] = n_universes * n_splits
	universes = aux_universes

	if len(universes) == 0:
		break

print(max((p1_wins, p2_wins)))