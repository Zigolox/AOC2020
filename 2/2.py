with open("input.txt", "r") as passwords:
	pw = [line.strip() for line in passwords]
	correct = 0
	for p in pw:
		times, letter, string = p.split()
		lower, upper = times.split("-")
		#xor the letter for just one occurance
		if bool(string[int(lower) - 1] == letter[0]) !=\
		bool(string[int(upper) - 1] == letter[0]):
			correct += 1
	print(correct)