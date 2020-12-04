with open("input.txt", "r") as passports:
	data = passports.read().split('\n\n')
	valid = 0
	for p in data:
		nf = p.count(' ') + p.count('\n')
		if (nf == 7 or (nf == 6 and "cid" not in p)):
			#Dirty but works
			l = p.replace('\n',' ').replace(':',' ').split()
			kv = dict(zip(l[::2], l[1::2]))
			if len(kv['pid']) == 9:
				print(sorted(kv))
				if 1920 <= int(kv['byr']) <= 2002:
					if 2010 <= int(kv['iyr']) <= 2020:
						if 2020 <= int(kv['eyr']) <= 2030:
							if kv['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:	
								if ('in' in kv['hgt'] and (59 <= int(kv['hgt'][:kv['hgt'].find('i')]) <= 76)) or \
									('cm' in kv['hgt'] and 150 <= int(kv['hgt'][:kv['hgt'].find('cm')]) <= 193):
									if kv['hcl'][0] == '#':
										try:
											int(kv['hcl'][1:],16)
											valid += 1
										except ValueError:
											pass

	print(valid)