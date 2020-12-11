import copy

def place_people(l,n, x, y):
    if l[y][x] != '.':
        a = 0
        for i, j in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            if 0 <= y + i < len(l) and 0 <= x + j < len(l[y]) and l[y + i][x + j] == '#':
                a += 1
            if a == 4 and l[y][x] == '#':
                n[y][x] = 'L'
                return
        if a == 0 and l[y][x] == 'L':
            n[y][x] = '#'

with open('verify.txt', 'r') as f:
    n = [[char for char in line.strip() ] for line in f]
    l = []
    while(hash(str(l)) != hash(str(n))):
        l = copy.deepcopy(n)
        for y in range(len(l)):
            for x in range(len(l[y])):
                place_people(l, n, x, y)
    print(sum(i.count('#') for i in l))
