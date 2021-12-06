from collections import Counter

with open("../input.txt") as f_input:
    delays = list(map(int, f_input.readline().rstrip().split(',')))
    f = [Counter(delays)[x] for x in range(0, 9)]
    target_days = 256
    tot = 0

    for i in range(0, target_days):
        f.append(f.pop(0))
        f[6] += f[8]
    
    i = 0
    while i < len(f) - 1:
        tot += f[i] + f[i+1]
        i += 2
    tot += f[-1]

    print(f"Number of fishes after {target_days} days: {tot}")