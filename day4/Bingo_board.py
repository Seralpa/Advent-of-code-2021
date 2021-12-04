class Bingo_board:

	def __init__(self, board: list[list[int]]) -> None:
		self.board = board
		self.checked: list[tuple[int, int]] = []

	def mark(self, n: int) -> None:
		for i, l in enumerate(self.board):
			for j, c in enumerate(l):
				if c == n:
					self.checked.append((i, j))

	def is_won(self) -> bool:
		for i in range(len(self.board)):
			row_found = True
			for j in range(len(self.board)):
				if (i, j) not in self.checked:
					row_found = False
					break
			if row_found:
				return True
		for j in range(len(self.board)):
			col_found = True
			for i in range(len(self.board)):
				if (i, j) not in self.checked:
					col_found = False
					break
			if col_found:
				return True
		return False

	def sum_remain(self) -> int:
		remain = 0
		for i, l in enumerate(self.board):
			for j, c in enumerate(l):
				if (i, j) not in self.checked:
					remain += c
		return remain
