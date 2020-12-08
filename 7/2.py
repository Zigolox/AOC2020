from collections import defaultdict
# DAG that we can solve with DP of traversal
def after(graph, seen, amount, key):
    if key in seen:
        return seen[key]
    if len(graph[key]) != 0:
        seen[key] = amount + amount * sum(after(graph, seen, i[0], i[1]) for i in graph[key])
        return seen[key]
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
