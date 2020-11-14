a, b = map(int,raw_input().split())

def solve(n):
    lo = 1
    hi = pow(10,9)
    while lo < hi:
        mid = (lo+hi)/2
        cur = 5
        cnt = 0
        while cur <= mid:
            cnt += mid/cur
            cur *= 5
        if cnt >= n:
            hi = mid
        else:
            lo = mid+1
    return lo

print solve(b+1)-solve(a)
