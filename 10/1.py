with open("input.txt", "r") as n:
        adapter = [0] + sorted([int(i) for i in n])
        difference = [adapter[i + 1] - adapter[i] for i in range(len(adapter) - 1)] + [3]
        start = stop = 0
        ones = []
        print(difference.count(1)*(difference.count(3)))
        while start < len(difference):
                if difference[start] == 3:
                        ones += [difference[stop:start - 1].count(1)]
                        stop = start + 1
                start += 1
        print((2**ones.count(1))*(4**ones.count(2))*(7**ones.count(3)))
