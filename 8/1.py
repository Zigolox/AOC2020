with open("input.txt", "r") as instructions:
    instruction = [i.strip().split(' ') for i in instructions]
    visited = set()
    i = 0
    accumilation = 0
    while(i not in visited):
        visited.add(i)
        print(instruction[i])
        if instruction[i][0] == "acc":
            accumilation += int(instruction[i][1])
            i += 1
        elif instruction[i][0] == "jmp":
            i += int(instruction[i][1])
        else:
            i +=1
    print(accumilation)
