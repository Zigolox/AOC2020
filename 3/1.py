with open("input.txt", "r") as karta:
	trees = 0
	for i, line in enumerate(karta):
		if line.strip()[i * 3 % (len(line) - 1)] == '#':
			trees += 1
	print(trees)