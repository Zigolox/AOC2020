with open("input.txt", "r") as passports:
	data = passports.read().split('\n\n')
	valid = 0
	for p in data:
		nf = p.count(' ') + p.count('\n')
		if (nf == 7 or (nf == 6 and "cid" not in p)):
			valid += 1
		
	print(valid)