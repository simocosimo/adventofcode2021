with open("../input.txt") as f_input:

    res = 0
    for l in f_input:
        l = l.rstrip().split('|')[1].split()
        lens = list(map(lambda n: 1 if len(n) == 2 or len(n) == 4 or len(n) == 3 or len(n) == 7 else 0, l))
        res += sum(lens)
    
    print(res)
        