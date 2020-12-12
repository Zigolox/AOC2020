with open("input.txt", "r") as instructions:
        directions = [(1,1),(1,-1),(-1,-1),(-1,1)]
        d = w_n = w_e = 0
        for i in instructions:
                if i[0] == 'N':
                        w_n += int(i[1:])
                elif i[0] == 'S':
                        w_n -= int(i[1:])
                elif i[0] == 'W':
                        w_e -= int(i[1:])
                elif i[0] == 'E':
                        w_e += int(i[1:])
                elif i[0] == 'F':
                        w_n += directions[d][0]*int(i[1:])
                        w_e += directions[d][1]*int(i[1:])
                elif i[0] == 'L':
                        d = (d - (int(i[1:]) // 90)) % 4
                else:
                        d = (d + (int(i[1:]) // 90)) % 4
                print(i[0],d,e,n)
        print(abs(n) + abs(e))
