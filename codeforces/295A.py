N,M,K = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))

ops = []
for i in range(M):
    ops.append(list(map(int,raw_input().split())))

diff = [0 for x in range(M+1)]
for i in range(K):
    a,b = map(int,raw_input().split())
    diff[a-1] += 1
    diff[b] -= 1

for i in range(M):
    diff[i+1] += diff[i]

diff2 = [0 for x in range(N+1)]

for i in range(M):
    diff2[ops[i][0]-1] += ops[i][2] * diff[i]
    diff2[ops[i][1]] -= ops[i][2] * diff[i]

for i in range(N):
    diff2[i+1] += diff2[i]
    arr[i] += diff2[i]

print " ".join(str(x) for x in arr)