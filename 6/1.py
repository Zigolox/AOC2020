with open("input.txt", "r") as form:
    groups = form.read().split('\n\n')
    counts = 0
    for g in groups:
        d = {}
        for letter in g.strip():
            if letter != '\n':
                d[letter] = 1
        print(g,d,len(d))
        counts += len(d)

    print(counts)
