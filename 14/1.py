with open("input.txt", "r") as config:
    a = {}
    for i in config:
        t = i.split(' ')
        if t[0][1] == 'a':
            ob = int(t[2].replace('X','0'),2)
            ab = int(t[2].replace('X','1'),2)
        else:
            a[t[0]] = int(t[2]) & ab | ob
            print(a)
    print(sum([a[i] for i in a]))
