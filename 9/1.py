with open("input.txt", "r") as n:
        number = [int(i) for i in n]
        d = 25
        error = contiguous = start = stop = 0
        for i in range(len(number) - (d + 1)):
                seen = set(number[i:i + d + 1])
                for j in seen:
                        if number[i + d] - j in seen:
                                break
                else:
                        print(number[i + d])
                        error = number[i + d]
                        break
        while contiguous != error:
                if contiguous > error:
                        contiguous -= number[stop]
                        stop += 1
                else:
                        contiguous += number[start]
                        start += 1
        print(min(number[stop:start]) + max(number[stop:start]))
