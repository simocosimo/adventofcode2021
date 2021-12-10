with open("../input.txt") as f_input:
    lines = [list(l.rstrip()) for l in f_input.readlines()]
    res = 0

    for i in range(0, len(lines)):
        tmp = []
        r = 0
        incomplete = True
        for x in lines[i]:
            if x == '(' or x == '[' or x == '{' or x == '<': tmp.append(x)
            if x == ')':
                if tmp[-1] != '(': 
                    r += 3
                    incomplete = False
                    break
                else: tmp.pop()
            elif x == ']':
                if tmp[-1] != '[': 
                    r += 57
                    incomplete = False
                    break
                else: tmp.pop()
            elif x == '}':
                if tmp[-1] != '{': 
                    r += 1197
                    incomplete = False
                    break
                else: tmp.pop()
            elif x == '>':
                if tmp[-1] != '<': 
                    r += 25137
                    incomplete = False
                    break
                else: tmp.pop()
        if not incomplete: res += r

    print(res)