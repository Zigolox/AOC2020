from collections import defaultdict

def before(graph, seen, key):
    if key not in seen:
        seen[key] = 1
        return 1 + sum(before(graph, seen, i[1]) for i in graph[key])
    return 0

with open("input.txt", "r") as bags:
    graph = defaultdict(list)
    for line in bags:
        b = line.replace(',','').replace('.','').split(" ")
        a = b[4:]
        for i in range(len(a)//4):
            if a[i] != "no":
                graph[a[i*4 + 1] + a[i*4 + 2]] += [(a[i*4], b[0] + b[1])]
    seen = {}
    print(before(graph, seen, "shinygold") - 1)
