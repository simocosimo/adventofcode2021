with open("../input.txt") as f_input:
    mat = [[int(i) for i in x] for x in [list(l.rstrip()) for l in f_input.readlines()]]
    res = 0

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
            res += (mat[i][x] + 1)
            print(f"Added {mat[i][x]} at row {i + 1}, col {x + 1} ")
        print("============")

    print(res)