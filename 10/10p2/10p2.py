import math

with open("../input.txt") as f_input:
    lines = [list(l.rstrip()) for l in f_input.readlines()]
    scores = []
    incompletes = []
    points = {'(': 1, '[': 2, '{': 3, '<': 4}

    for i in range(0, len(lines)):
        tmp = []
        r = 0
        incomplete = True
        for x in lines[i]:
            if x == '(' or x == '[' or x == '{' or x == '<': tmp.append(x)
            if x == ')':
                if tmp[-1] != '(': 
                    incomplete = False
                    break
                else: tmp.pop()
            elif x == ']':
                if tmp[-1] != '[': 
                    incomplete = False
                    break
                else: tmp.pop()
            elif x == '}':
                if tmp[-1] != '{': 
                    incomplete = False
                    break
                else: tmp.pop()
            elif x == '>':
                if tmp[-1] != '<': 
                    incomplete = False
                    break
                else: tmp.pop()
        if incomplete: incompletes.append(tmp)

    for i in incompletes:
        res = 0
        for c in reversed(i):
            res *= 5
            res += points[c]
        scores.append(res)
    scores.sort()

    print(scores[math.floor(len(scores)/2)])
