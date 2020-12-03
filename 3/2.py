with open("input.txt", "r") as karta:
	x = trees = 0
	for line in karta:
		if line.strip()[x] == '#':
			trees += 1
		x = (x + 3) % len(line.strip())
	print(trees)