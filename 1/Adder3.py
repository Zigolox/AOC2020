#Itertools had been a cleaner solution

def add(number1, number2, number3):
	if number1 + number2 + number3 == 2020:
			print(number1*number2*number3)

with open("input.txt", "r") as numbers:
	nl = [int(line) for line in numbers]
	for i, number1 in enumerate(nl):
		for j, number2 in enumerate(nl[i:]):
			for number3 in nl[i + j:]:
				add(number1, number2, number3)