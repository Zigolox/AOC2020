with open("input.txt", "r") as form:
    groups = form.read().split('\n\n')
    counts = 0
    for g in groups:
        d = {}
        for letter in g.strip():
            if letter != '\n':
                if letter in d:
                    d[letter] += 1
                else:
                    d[letter] = 1
        np = g.strip().count('\n') + 1
        print(np, g.split('\n'))
        for letter in d:
            if d[letter] == np:
                counts += 1

    print(counts)
