def next_instruction(ins, acc, vi, i, split):
    if i < len(ins):
        if i not in visited:
            visited.add(i)
            if ins[i][0] == "acc":
                next_instruction(ins, int(ins[i][1]) + acc, vi, i + 1, split)
            else:
                if ins[i][0] == "jmp":
                    next_instruction(ins, acc, vi.copy(), i + int(ins[i][1]) ,split)
                    if split > 0:
                        next_instruction(ins, acc, vi.copy(), i + 1, split - 1)
                else:
                    next_instruction(ins, acc, vi.copy(), i + 1, split)
                    if split > 0:
                        next_instruction(ins, acc, vi.copy(), i + int(ins[i][1]), split - 1)
        return
    print(acc)


with open("input.txt", "r") as inst:
    instruction = [i.strip().split(' ') for i in inst]
    visited = set()
    next_instruction(instruction,0,visited,0,1)
