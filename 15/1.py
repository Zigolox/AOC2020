with open("input.txt",'r') as start:
    s = [int(i) for i in start.readlines()[0].split(',')]
    seen = {}
    for i,j in enumerate(s[:-1]):
        seen[j] = i + 1
    prev = s[-1]
    for i in range(len(s),2021):
        print(prev,i)
        p = prev
        if prev in seen:
            prev = i - seen[prev]
        else:
            prev = 0
        seen[p] = i
