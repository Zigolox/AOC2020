with open("input.txt", "r") as boardingpass:
	max = 0
	for boarding in boardingpass:
		bin = boarding.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
		if (n := int(bin[:7],2) * 8 + int(bin[7:],2)) > max:
			max = n
	print(max)