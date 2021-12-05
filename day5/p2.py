with open("input.txt") as f:
	data = [l.split(" -> ") for l in f.read().splitlines()]

lines: list[tuple[tuple, tuple]] = []
for d in data:
	point1, point2 = d[0].split(","), d[1].split(",")
	point1 = (int(point1[0]), int(point1[1]))
	point2 = (int(point2[0]), int(point2[1]))
	lines.append((point1, point2))

points = dict()
for l in lines:
	if l[0][0] == l[1][0]:  # horizontal
		for p in range(min(l[0][1], l[1][1]), max(l[0][1], l[1][1]) + 1):
			if (p, l[0][0]) not in points.keys():
				points[(p, l[0][0])] = 1
			else:
				points[(p, l[0][0])] += 1
	elif l[0][1] == l[1][1]:  #vertical
		for p in range(min(l[0][0], l[1][0]), max(l[0][0], l[1][0]) + 1):
			if (l[0][1], p) not in points.keys():
				points[(l[0][1], p)] = 1
			else:
				points[(l[0][1], p)] += 1
	else:  #diagonal
		x_points = range(min(l[0][1], l[1][1]), max(l[0][1], l[1][1]) + 1)
		y_points = range(min(l[0][0], l[1][0]), max(l[0][0], l[1][0]) + 1)
		if l[0][0] > l[1][0]:
			x_points = reversed(x_points)
		if l[0][1] > l[1][1]:
			y_points = reversed(y_points)

		diag_points = list(zip(x_points, y_points))
		for p in diag_points:
			if p not in points.keys():
				points[p] = 1
			else:
				points[p] += 1

print(len([p for p in points.values() if p >= 2]))
