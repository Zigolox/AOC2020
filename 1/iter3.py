import itertools

def add(number1, number2, number3):
	if number1 + number2 + number3 == 2020:
			print(number1*number2*number3)

with open("input.txt", "r") as numbers:
	nl = [int(line) for line in numbers]
	for c in itertools.combinations(nl, 3):
		add(c[0], c[1], c[2])
