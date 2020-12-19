n,m,k = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))
ops = []
qs = []
for i in range(m):
    l,r,d = map(int,raw_input().split())
    ops.append([l,r,d])

for i in range(k):
    x,y = map(int,raw_input().split())
    qs.append([x,y])

freq = [0 for x in range(m+1)]
for i in range(k):
    freq[qs[i][0]-1] += 1
    freq[qs[i][1]] -= 1

for i in range(m):
    freq[i+1] += freq[i]

diff = [0 for x in range(n+1)]
for i in range(m):
    diff[ops[i][0]-1] += freq[i] * ops[i][2]
    diff[ops[i][1]] -= freq[i] * ops[i][2]

for i in range(n):
    diff[i+1] += diff[i]

for i in range(n):
    arr[i] += diff[i]

print " ".join(str(x) for x in arr)