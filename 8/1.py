def next_instruction(ins, acc, vi, i):
        if i not in visited:
            visited.add(i)
            if ins[i][0] == "acc":
                next_instruction(ins, int(ins[i][1]) + acc, vi, i + 1)
            elif ins[i][0] == "jmp":
                next_instruction(ins, acc, vi.copy(), i + int(ins[i][1]))
            else:
                next_instruction(ins, acc, vi.copy(), i + 1)
        else:
            print(acc)


with open("input.txt", "r") as inst:
    instruction = [i.strip().split(' ') for i in inst]
    visited = set()
    next_instruction(instruction,0,visited,0)
