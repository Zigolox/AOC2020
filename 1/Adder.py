def add(number1, number2):
	if number1 + number2 == 2020:
			print(number1*number2)

with open("input.txt", "r") as numbers:
	nl = [int(line) for line in numbers]
	for i, number1 in enumerate(nl):
		for number2 in nl[i:]:
			add(number1, number2)