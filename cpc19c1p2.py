N,K = map(int,raw_input().split())
arr = sorted(map(int,raw_input().split()))

ans = 1

for i in range(N):
    small = arr[i]
    lo = i+1
    hi = N
    while lo < hi:
        mid = (lo+hi)/2
        if arr[mid] - small > K:
            hi = mid
        else:
            lo = mid + 1
    ans = max(ans, lo-i)

print ans
