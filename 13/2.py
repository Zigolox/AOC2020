from math import prod
from time import sleep
with open("input.txt", "r") as buses:
        time_id = [i.strip().split(',') for i in buses]
        id = [(int(i), j) for j, i in enumerate(time_id[1]) if i != 'x']
        print(id)
        number = id[0][0]
        t = [0]
        while not min(t):
                number += prod(id[k][0] for k, i in enumerate(t) if i == True)
                t = [(i - number) % i == j % i for i,j in id]
        print(number)
