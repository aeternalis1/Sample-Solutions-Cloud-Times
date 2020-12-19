N = int(raw_input())
arr = list(map(int,raw_input().split()))
dp = [float('inf') for x in range(N)]

dp[0] = 0
dp[1] = abs(arr[0] - arr[1])
for i in range(2,N):
    dp[i] = min(dp[i-2] + abs(arr[i-2] - arr[i]), dp[i-1] + abs(arr[i-1] - arr[i]))

print dp[N-1]