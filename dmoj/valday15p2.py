N, W = map(int,raw_input().split())

items = []

for i in range(N):
    items.append(map(int,raw_input().split())[::-1])

dp = [[0 for x in range(W+1)] for x in range(N)]    # dp[i][j] stores max value if you take some items with indices <= i with total weight j

if items[0][0] <= W:
    dp[0][items[0][0]] = items[0][1]

for i in range(1,N):
    for j in range(W+1):
        if j >= items[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]] + items[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print max(dp[N-1])