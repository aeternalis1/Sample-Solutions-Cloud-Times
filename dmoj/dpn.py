N = int(raw_input())
arr = list(map(int,raw_input().split()))

dp = [[float('inf') for x in range(N)] for x in range(N)]
for i in range(N):
    dp[i][i] = 0

psum = [0 for x in range(N+1)]
for i in range(N):
    psum[i+1] = psum[i] + arr[i]

def size(l, r):     # returns total size of slimes in [l, r]
    return psum[r+1] - psum[l]

def solve(l, r):        # assume solve(l,r) returns min cost to merge [l, r]
    if dp[l][r] != float('inf'):
        return dp[l][r]
    
    for i in range(l, r):       # [l,i] is left subarray, [i+1, r] is right subarray
        dp[l][r] = min(dp[l][r], solve(l,i) + solve(i+1,r) + size(l,r))

    return dp[l][r]

print solve(0,N-1)