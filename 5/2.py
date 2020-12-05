with open("input.txt", "r") as boardingpass:
	max = 0
	plane = [ [0]*8 for _ in range(128) ]
	for boarding in boardingpass:
		bin = boarding.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
		plane[int(bin[:7],2)][int(bin[7:],2)] = 1
	for i, row in enumerate(plane):
		if 1 in plane[i - 1 % 128] and 1 in plane[(i + 1) % 128] and 0 in row:
			print(i*8 + row.index(0))
			break
