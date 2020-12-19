r,c = map(int,raw_input().split())
m = int(raw_input())

dp = [[0 for x in range(c)] for x in range(r)]
cat = [[0 for x in range(c)] for x in range(r)]
for i in range(m):
    a,b = map(int,raw_input().split())
    cat[a-1][b-1] = 1

dp[0][0] = cat[0][0] ^ 1
for i in range(r):
    for j in range(c):
        if not i and not j or cat[i][j]:
            continue
        if not i:
            dp[i][j] += dp[i][j-1]
        elif not j:
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += dp[i-1][j] + dp[i][j-1]

print dp[r-1][c-1]