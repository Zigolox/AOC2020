with open("input.txt", "r") as boardingpass:
	plane = [0 for _ in range(1024)]
	for boarding in boardingpass:
		bin = boarding.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
		plane[int(bin[:7],2)* 8+int(bin[7:],2)] = 1
	for i in range(1024):
		if plane[i] == 0 and plane[i - 1 % 128] == 1 and plane[(i + 1) % 128] == 1:
			print(i)
			break
