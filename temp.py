N = int(raw_input())
arr = map(int,raw_input().split())

dp = [0 for x in range(N)] # dp[i] stores minimum cost to jump to i'th rock from 0'th rock

dp[0] = 0
dp[1] = abs(arr[1] - arr[0])

for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(arr[i-1] - arr[i]), dp[i-2] + abs(arr[i-2] - arr[i]))

print (dp[N-1])
