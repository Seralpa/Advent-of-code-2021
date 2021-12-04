from Bingo_board import Bingo_board

with open("input.txt") as f:
	sequence = [int(n) for n in f.readline().split(",")]
	f.readline()
	txt_boards = [l.replace("  ", " ") for l in f.read().split("\n\n")]

boards: list[Bingo_board] = []
for b in txt_boards:
	boards.append(Bingo_board([[int(n.strip()) for n in l.strip().split(" ")] for l in b.split("\n")]))

looser: Bingo_board = None
last_num = None
for n in sequence:
	for b in boards:
		b.mark(n)

	end = False
	to_remove = []
	for i, b in enumerate(boards):
		if b.is_won():
			to_remove.append(b)
	if len(to_remove) < len(boards):
		boards = [b for b in boards if b not in to_remove]
	else:
		looser = boards[0]
		last_num = n
		break
print(f"{looser.sum_remain()*last_num}")