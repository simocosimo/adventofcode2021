def explore(mat, i, x, explored) -> int:
    amount = 1
    if i >= len(mat) or i < 0 or x >= len(mat[i]) or x < 0 or mat[i][x] == 9 or [i, x] in explored:
        return 0
    
    explored.append([i, x])
    amount += explore(mat, i, x + 1, explored)
    amount += explore(mat, i, x - 1, explored)
    amount += explore(mat, i + 1, x, explored)
    amount += explore(mat, i - 1, x, explored)
    return amount

with open("../input.txt") as f_input:
    mat = [[int(i) for i in x] for x in [list(l.rstrip()) for l in f_input.readlines()]]
    mins = []
    basins = []
    res = 1

    for i in range(0, len(mat)):
        for x in range(0, len(mat[i])):
            if x + 1 < len(mat[i]): 
                if mat[i][x] >= mat[i][x + 1]: continue      #check dx
            if x - 1 >= 0:
                if mat[i][x] >= mat[i][x - 1]: continue      #check sx
            if i - 1 >= 0: 
                if mat[i][x] >= mat[i - 1][x]: continue      #check up
            if i + 1 < len(mat):
                if mat[i][x] >= mat[i + 1][x]: continue      #check down
            mins.append([i, x])
        
    for m in mins: basins.append(explore(mat, m[0], m[1], []))
    basins.sort(reverse=True)
    for i in range(0, 3): res *= basins[i]
    print(res)