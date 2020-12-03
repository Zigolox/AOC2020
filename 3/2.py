with open("input.txt", "r") as karta:
	multiply = 1
	map = [line.strip() for line in karta]
	for i, j in [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2)]:	
		trees = 0
		for x, m in enumerate(map[::j]):
			if m[i*x % len(m)] == '#':
				trees += 1
		multiply *= trees
	print(multiply)