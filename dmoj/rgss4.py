N = int(raw_input())
arr = [int(raw_input()) for x in range(N)]

dp = [[0 for x in range(1001)] for x in range(N+1)] # dp[i][j] holds maximal sum of stictly increasing subsequence with elements up to index i and final element j

dp[0][arr[0]] = arr[0]

for i in range(1,N):      # consider the element at index i with value arr[i]
    for j in range(1,arr[i]):
        dp[i][arr[i]] = max(dp[i-1][j] + arr[i], dp[i][arr[i]])
    for j in range(1001):
        dp[i][j] = max(dp[i][j], dp[i-1][j])

print max(dp[N-1])

# we already have by previous computation all values dp[i-1][j]
# each dp[i-1][j] represents the max value of an increasing subsequence terminating before i with final value j
