N,Q = map(int,raw_input().split())
arr = [0 for x in range(N)] + [0]

for i in range(Q):
    l,r = map(int,raw_input().split())
    arr[l] += 1
    arr[r] -= 1

for i in range(1,N):
    arr[i] += arr[i-1]

cnt = 0

for i in range(N):
    if arr[i] != 0:
        cnt += 1 

print N-cnt, cnt
