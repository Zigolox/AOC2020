import re

def address(bitmap, number, i):
    if i + number.bit_length() <= 35:
        return [number]

    print(bin(number)[::-1], 35 - i, bitmap[i])

    if bitmap[i] == 'X':
        return address(bitmap, number | (1 << (35 - i)), i - 1) + \
        address(bitmap, number & ~(1 << (35 - i)), i - 1)

    elif bitmap[i] == '0':
        return address(bitmap, number, i - 1)
    else:
        return address(bitmap, number | (1 << (35 - i)), i - 1)

with open("verify2.txt", "r") as config:
    a = {}
    for i in config:
        t = i.split(' ')
        if t[0][1] == 'a':
            bitmap = t[2].strip()
        else:
            print(bitmap[::-1])
            p = address(bitmap,int(t[0][4:-1]),len(bitmap) - 1)
            print(2**bitmap[36 - int(t[0][4:-1]).bit_length():].count('X'),len(p))
            for i in p:
                a[i] = int(t[2])
    print(a)
    print(sum(a[i] for i in a))
