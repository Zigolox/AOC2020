with open("input.txt", "r") as instructions:
        directions = [(1,1),(-1,1),(-1,-1),(1,-1)]
        w = [1, 10]
        d = 0
        s = [0, 0]
        for i in instructions:
                if i[0] == 'N':
                        w[0] += int(i[1:])
                elif i[0] == 'S':
                        w[0] -= int(i[1:])
                elif i[0] == 'W':
                        w[1] -= int(i[1:])
                elif i[0] == 'E':
                        w[1] += int(i[1:])
                elif i[0] == 'F':
                        s[0] += w[0]*int(i[1:])
                        s[1] += w[1]*int(i[1:])
                elif i[0] == 'L':
                        d = (-int(i[1:]) // 90) % 4
                        p = w[:]
                        w[0] = p[d % 2]*directions[d][0]
                        w[1] = p[(d + 1)% 2]*directions[d][1]
                else:
                        d = ((int(i[1:])) // 90) % 4
                        p = w[:]
                        w[0] = p[d % 2]*directions[d][0]
                        w[1] = p[(d + 1)% 2]*directions[d][1]

        print(abs(s[0]) + abs(s[1]))
