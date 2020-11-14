from __future__ import division
import sys

N,S = map(int,raw_input().split())
arr = []

tot = 0
for i in range(N):
    x,y,p = map(int,raw_input().split())
    arr.append([x*x + y*y, p])
    tot += p

if tot + S < 1000000:
    print -1
    sys.exit()

lo = 0
hi = 100000
for i in range(100):
    mid = (lo+hi)/2
    cur = 0
    for j in range(N):
        if mid*mid >= arr[j][0]:
            cur += arr[j][1]
    if cur + S >= 1000000:
        hi = mid
    else:
        lo = mid
print lo
