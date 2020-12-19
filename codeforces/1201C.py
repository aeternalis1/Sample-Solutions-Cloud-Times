n,k = map(int,raw_input().split())
arr = map(int,raw_input().split())

arr = sorted(arr)
lo = arr[n/2]
hi = arr[len(arr)-1] + k + 1

while lo < hi:
    mid = (lo+hi)/2     # desired median
    cnt = 0
    for i in range(n/2, n):
        if arr[i] >= mid:
            continue
        else:
            cnt += mid - arr[i]
    if cnt <= k:
        lo = mid + 1
    else:
        hi = mid

print lo - 1