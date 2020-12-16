import re

def address(bitmap, number, i):
    if i < 0:
        return [number]

    if bitmap[i] == 'X':
        return address(bitmap, number | (1 << (35 - i)), i - 1) + \
        address(bitmap, number & ~(1 << (35 - i)), i - 1)

    elif bitmap[i] == '0':
        return address(bitmap, number | (0 << (35 - i)), i - 1)
    else:
        return address(bitmap, number | (1 << (35 - i)), i - 1)

with open("input.txt", "r") as config:
    a = {}
    for i in config:
        t = i.split(' ')
        if t[0][1] == 'a':
            bitmap = t[2].strip()
        else:
            p = address(bitmap,int(t[0][4:-1]),len(bitmap) - 1)
            for i in p:
                a[i] = int(t[2])
    print(sum(a[i] for i in a))
