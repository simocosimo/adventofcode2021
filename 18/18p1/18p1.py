import math

def simpleAddition(a, b): return '[' + a + ',' + b + ']'

def magnitude(a, b): return 3*a + 2*b

def explode():
    global int_number
    global depths
    l = -1
    while True:
        l += -1
        try: 
            x = depths.index(5)
            y = x + 1
            if x != 0: int_number[x-1] += int_number[x]
            if y != len(int_number) - 1: int_number[y+1] += int_number[y]
            int_number[x] = int_number[y] = 0
            if x == 0: 
                int_number = [0] + int_number[2:]
                depths = [4] + depths[2:]
            elif x == len(int_number) - 2: 
                int_number = int_number[:x] + [0]
                depths = depths[:x] + [4]
            else: 
                int_number = int_number[:x] + [0] + int_number[y+1:]
                depths = depths[:x] + [4] + depths[y+1:]
        except ValueError:
            break
    return l

def splitNumber():
    global int_number
    global depths
    l = 0
    for n in range(len(int_number)):
        if int_number[n] >= 10: 
            l += 1
            int_number = int_number[:n] + [math.floor(int_number[n]/2)] + [math.ceil(int_number[n]/2)] + int_number[n+1:]
            depths = depths[:n] + [(depths[n] + 1), (depths[n] + 1)] + depths[n+1:]
    return l

def parse(a, numbers, depths):
    d = 0
    for c in a:
        if c == '[':
            d += 1
            continue
        if c == ']':
            d -= 1
            continue
        if c == ',': continue
        numbers.append(int(c))
        depths.append(d)

def execute(a, b):
    global int_number
    global depths
    parse(simpleAddition(a, b), int_number, depths)
    checkExplode = checkSplit = True
    while checkExplode and checkSplit:
        checkExplode = explode()
        checkSplit = splitNumber()

# TODO: write function to recompose string format number from arrays

with open("../test.txt", "r") as f_input:
    numbers = [s.rstrip() for s in f_input.readlines()]
    int_number = []
    depths = []

    #parse(simpleAddition(numbers[0], numbers[1]), int_number, depths)
    parse("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", int_number, depths)
    #print(simpleAddition(numbers[0], numbers[1]), int_number, depths)
    print(depths)
    print(int_number)
    print('=============')

    #parse(simpleAddition(numbers[i], numbers[i+1]), int_number, depths)

    checkExplode = checkSplit = True
    while checkExplode and checkSplit:
        checkExplode = explode()
        checkSplit = splitNumber()

    print(depths)
    print(int_number)
