import copy

def next_chair(l, x, y, i, j):
    if (len(l) <= y or y < 0) or (len(l[y]) <= x or x < 0) or l[y][x] == 'L':
        return 0
    elif l[y][x] == '#':
        return 1
    return next_chair(l, x + j, y + i, i, j)



def place_people(l, n, x, y):
    if l[y][x] != '.':
        a = 0
        for i, j in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            a += next_chair(l, x + j, y + i, i, j)
            if a == 5 and l[y][x] == '#':
                n[y][x] = 'L'
                return
        if a == 0 and l[y][x] == 'L':
            n[y][x] = '#'

with open('input.txt', 'r') as f:
    n = [[char for char in line.strip() ] for line in f]
    l = []
    while(hash(str(l)) != hash(str(n))):
        l = copy.deepcopy(n)
        for y in range(len(l)):
            for x in range(len(l[y])):
                place_people(l, n, x, y)
    print(sum(i.count('#') for i in l))
