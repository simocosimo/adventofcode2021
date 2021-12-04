from copy import deepcopy

def checkVittoria(map) -> bool:
    x = ['x'] * 5
    for i in range(0, 5):
        if [a[i] for a in map] == x: return True
        if map[i] == x: 
            #print(map[i])
            return True
    return False

def getWinningValue(map, last_val) -> int:
    rem = [int(x) for l in map for x in l if x != 'x' ]
    print(rem)
    return (sum(rem) * last_val)

with open("../input.txt", "r") as f_input:
    extraction = f_input.readline().rstrip().split(',')
    #print(extraction)
    f_input.readline()
    i = 0
    cur = f_input.tell()
    len_f = sum(1 for _ in f_input)
    f_input.seek(cur)
    best_turn = -100000000
    winning_value = 0
    victory = False
    winning_mat = []

    while True:
        victory = False
        turn = 0
        x_placed = 0
        mat = [f_input.readline().rstrip().split() for _ in range(0, 5)]
        print(f"Actual: {mat}")
        if not victory:
            for ex in extraction:
                for l in mat:
                    if checkVittoria(mat): break    #WTF
                    try:
                        l[l.index(ex)] = 'x'
                        x_placed += 1
                        victory = checkVittoria(mat)
                        if x_placed >= 5 and victory and turn > best_turn: 
                            best_turn = turn
                            winning_mat = deepcopy(mat)
                            winning_value = int(ex)
                            print("BINGO!")
                            print(f"local winner in {turn}: {mat}")
                            break
                        if victory: victory = False
                        continue
                    except ValueError as ve:
                        continue
                turn += 1
                if victory: break

        print("=========")
        i += 5
        if i < len_f - 1: 
            f_input.readline()
            i += 1
        else: break

print(f"Winning mat is\n{winning_mat}")
print(f"Winning value is: {getWinningValue(winning_mat, winning_value)}")