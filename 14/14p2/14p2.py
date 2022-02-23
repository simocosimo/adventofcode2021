import math

def ccount(s, i):
    if s in mem and i == 0:
        for k in mem[s].keys(): 
            if k in local: local[k] += mem[s][k]
            else: local[k] = mem[s][k]
        return
    if i == 20: 
        if s not in local: local[s] = 1
        else: local[s] += 1
        return
    ccount(s[0]+rules[s], i+1)      #this goes from beginning
    ccount(rules[s]+s[1], i+1)      #this goes from the insert

with open("../input.txt") as f_input:
    string = f_input.readline().rstrip()
    f_input.readline()
    rules = {}
    pairs = {}
    pairsOfString = []
    local = {}
    mem = {}

    for l in f_input:
        k, v = l.rstrip().split(' -> ')
        rules[k] = v
        pairs[k] = 0
        pairs[k[0] + v] = 0
        pairs[v + k[1]] = 0

    for i in range(len(string)): pairsOfString.append(string[i:i+2])
    if len(string) % 2 == 0: del pairsOfString[-1]

    for i in range(2):
        for k in pairsOfString:
            ccount(k, 0)
            mem[k] = local
            local = {}
            for x in mem[k].keys(): pairs[x] += mem[k][x]
            
        if i != 1:
            pairsOfString = []
            for k in pairs.keys():
                for v in range(pairs[k]): pairsOfString.append(k)
            for k in pairs.keys(): pairs[k] = 0
    
    letters = {}
    for k in pairs.keys():
        if k[0] in letters.keys(): letters[k[0]] += pairs[k]
        else: letters[k[0]] = pairs[k]
        if k[1] in letters.keys(): letters[k[1]] += pairs[k]
        else: letters[k[1]] = pairs[k]

    res = math.ceil((max(letters.values()) - min(letters.values())) / 2)
    print(res)