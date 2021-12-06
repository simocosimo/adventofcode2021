from copy import deepcopy

with open("../input.txt") as f_input:
    delays = list(map(int, f_input.readline().rstrip().split(',')))
    x = 0
    target_days = 256

    while x < target_days:
        to_append = []
        m = delays[-1] if delays[-1] != 0 else 1
        if x + m > target_days:
            #print("Final stop incoming")
            m = target_days - x
        #print(f"Before: {delays}")
        #print(f"Day {x} - First is {m} - len is: {len(delays)}")
        for i in range(0, len(delays)):
            delays[i] -= m
            while delays[i] < 0:
                delays.append(8 + delays[i] + 1)
                delays[i] = 6 + (delays[i] + 1)
        #print(f"After: {delays}\n")
        x += m

    print(f"Number of fishes after {target_days} days: {len(delays)}")