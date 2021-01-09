from copy import deepcopy
s = list(raw_input())
N = len(s)

dp = [[0 for x in range(4)] for x in range(N+1)]    # dp[i][j] stores # of subsequences of prefix of "love" of length j+1 up to (not including) index i

for i in range(N):
    dp[i+1] = deepcopy(dp[i])

    if s[i] == 'l':
        dp[i+1][0] += 1
    if s[i] == 'o':
        dp[i+1][1] += dp[i][0]
    if s[i] == 'v':
        dp[i+1][2] += dp[i][1]
    if s[i] == 'e':
        dp[i+1][3] += dp[i][2]

print dp[N][3]

