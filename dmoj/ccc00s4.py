N = int(raw_input())
M = int(raw_input())
arr = [int(raw_input()) for x in range(M)]

dp = [float('inf') for x in range(N+1)]
dp[0] = 0
for i in range(N+1):
    if dp[i] != float('inf'):
        for j in arr:
            if i + j <= N:
                dp[i+j] = min(dp[i+j], dp[i] + 1)

if dp[N] == float('inf'):
    print "Roberta acknowledges defeat."
else:
    print "Roberta wins in %d strokes." % dp[N]