with open("../input.txt", "r") as f_input:
    mat = [[int(f) for f in l.rstrip()] for l in f_input.readlines()]
    inf = 100000000

    H = len(mat)
    W = len(mat[0])
    dp = [[inf for _ in range(W)] for _ in range(H)]

    for row in range(H):
        for col in range(W):
            if row == 0 and col == 0:
                dp[row][col] = 0
            else:
                dp[row][col] = mat[row][col] + min((inf if row == 0 else dp[row-1][col]), (inf if col == 0 else dp[row][col-1]))

    print(dp[H-1][W-1])
    