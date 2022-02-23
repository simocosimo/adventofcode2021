# SOLUTION WITH DYNAMIC PROGRAMMING
# this solution is ok for the first part but not sufficient for the second
# thi algo suppose you can only go down and right, but proper pathfinding is needed

with open("../input.txt", "r") as f_input:
    mat = [[int(f) for f in l.rstrip()] for l in f_input.readlines()]
    inf = 100000000
    W = len(mat[0])
    H = len(mat)

    print(f"Before - H: {H}, W: {W}")
    for i in range(len(mat)):
        for c in range(W * 4):
            mat[i].append((mat[i][c] + 1) if mat[i][c] != 9 else 1)
    
    for i in range(H, H * 5):
        tmp = mat[i - H].copy()
        for t in range(len(tmp)): 
            if tmp[t] != 9: tmp[t] += 1
            else: tmp[t] = 1
        mat.append(tmp)

    W = len(mat[0])
    H = len(mat)
    print(mat[0][0:100])
    print(mat[0][100:200])
    print(f"After - H: {H}, W: {W}")
    dp = [[0 for _ in range(W)] for _ in range(H)]

    for row in range(H):
        for col in range(W):
            if row == 0 and col == 0: dp[row][col] = 0
            else: dp[row][col] = mat[row][col] + min((inf if row == 0 else dp[row-1][col]), (inf if col == 0 else dp[row][col-1]))

    print(dp[H-1][W-1])