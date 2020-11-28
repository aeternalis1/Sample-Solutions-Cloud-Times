N,K = map(int,raw_input().split())
arr = sorted(list(map(int,raw_input().split())), reverse=True)

lo = arr[N/2]
hi = arr[0] + K + 1

while lo < hi:
    mid = (lo+hi)/2
    need = 0
    for i in range(N/2+1):
        need += max(0, mid-arr[i])
    if need <= K:
        lo = mid + 1
    else:
        hi = mid

print lo - 1