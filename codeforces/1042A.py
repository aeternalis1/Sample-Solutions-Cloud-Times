n = int(raw_input())
m = int(raw_input())
arr = [int(raw_input()) for x in range(n)]

lo = max(arr)
hi = max(arr) + m
while lo < hi:
    mid = (lo+hi)/2
    cur = 0
    for i in range(n):
        cur += mid - arr[i]
    if cur >= m:
        hi = mid
    else:
        lo = mid+1
print lo, max(arr) + m
