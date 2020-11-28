N = int(raw_input())
arr = list(map(int,raw_input().split()))

arr = sorted(arr)

Q = int(raw_input())
for i in range(Q):
    a = int(raw_input())
    lo = 0
    hi = N
    while lo < hi:
        mid = (lo+hi)/2
        if arr[mid] > a:
            hi = mid
        else:
            lo = mid+1
    print lo