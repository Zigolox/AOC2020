with open("input.txt", "r") as instructions:
        directions = [(0,1),(-1,0),(0,-1),(1,0)]
        d = n = e = 0
        for i in instructions:
                if i[0] == 'N':
                        n += int(i[1:])
                elif i[0] == 'S':
                        n -= int(i[1:])
                elif i[0] == 'W':
                        e -= int(i[1:])
                elif i[0] == 'E':
                        e += int(i[1:])
                elif i[0] == 'F':
                        n += directions[d][0]*int(i[1:])
                        e += directions[d][1]*int(i[1:])
                elif i[0] == 'L':
                        d = (d - (int(i[1:]) // 90)) % 4
                else:
                        d = (d + (int(i[1:]) // 90)) % 4
                print(i[0],d,e,n)
        print(abs(n) + abs(e))
