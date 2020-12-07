from collections import defaultdict

def after(graph, seen, amount, key):
    print(amount,graph[key])
    if len(graph[key]) != 0:
        return amount + amount * sum(after(graph, seen, i[0], i[1]) for i in graph[key])
    return amount

with open("input.txt", "r") as bags:
    graph = defaultdict(list)
    for line in bags:
        b = line.replace(',','').replace('.','').split(" ")
        a = b[4:]
        for i in range(len(a)//4):
            if a[i] != "no":
                graph[b[0] + b[1]] += [(int(a[i*4]), a[i*4 + 1] + a[i*4 + 2])]
    seen = {}
    print(after(graph, seen, 1, "shinygold")-1)
