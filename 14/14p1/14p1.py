from collections import Counter

with open("../input.txt") as f_input:
    string = f_input.readline().rstrip()
    f_input.readline()
    rules = {}

    for l in f_input:
        k, v = l.rstrip().split(' -> ')
        rules[k] = k[0] + v + k[1]

    for _ in range(0, 10):
        i = 0
        while i != len(string) - 1:
            oldv = ''.join(string[i:i+2])
            string = string.replace(oldv, rules[oldv], 1)
            i += 2

    print(string)
    maxocc = max(Counter(list(string)).values())
    minocc = min(Counter(list(string)).values())
    print(maxocc - minocc)