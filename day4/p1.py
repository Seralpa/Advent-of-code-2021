from Bingo_board import Bingo_board

with open("input.txt") as f:
	sequence = [int(n) for n in f.readline().split(",")]
	f.readline()
	txt_boards = [l.replace("  ", " ") for l in f.read().split("\n\n")]

boards: list[Bingo_board] = []
for b in txt_boards:
	boards.append(Bingo_board([[int(n.strip()) for n in l.strip().split(" ")] for l in b.split("\n")]))

winner: Bingo_board = None
last_num: int = None
for n in sequence:
	for b in boards:
		b.mark(n)

	end = False
	for i, b in enumerate(boards):
		if b.is_won():
			winner = b
			last_num = n
			end = True
			break
	if end:
		break

print(f"{winner.sum_remain() * last_num}")