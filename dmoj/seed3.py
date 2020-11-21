I = int(raw_input())
N = int(raw_input())
J = int(raw_input())
arr = [0 for x in range(I+1)]

for i in range(J):
    l,r,x = map(int,raw_input().split())
    l -= 1
    r -= 1
    arr[l] += x
    arr[r+1] -= x

for i in range(1,I):
    arr[i] = arr[i-1] + arr[i]

cnt = 0
for i in range(I):
    if arr[i] < N:
        cnt += 1

print cnt
