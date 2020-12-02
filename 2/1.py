with open("input.txt", "r") as passwords:
	pw = [line.strip() for line in passwords]
	correct = 0
	for p in pw:
		times, letter, string = p.split()
		lower, upper = times.split("-")
		count = string.count(letter[0])
		if  int(lower) <= count <= int(upper):
			correct += 1
	print(correct)