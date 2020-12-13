with open("input.txt", "r") as buses:
        time_id = [i.strip().split(',') for i in buses]
        id = [int(i) for i in time_id[1] if i != 'x']
        diff = [i - int(time_id[0][0]) % i for i in id]
        smallest = id[diff.index(min(diff))]*min(diff)
        print(smallest)
