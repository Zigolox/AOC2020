with open("input.txt", "r") as karta:
	multiply = 1
	map = [line.strip() for line in karta]
	for i, j in [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2)]:	
		x = y = trees = 0
		while y < len(map):
			if map[y][x] == '#':
				trees += 1
			x = (x + i) % len(map[y])
			y = (y + j)
		multiply *= trees
	print(multiply)