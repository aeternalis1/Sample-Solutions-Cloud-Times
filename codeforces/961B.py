N,K = map(int,raw_input().split())

arr = list(map(int,raw_input().split()))
awake = list(map(int,raw_input().split()))

pre1 = [0]
pre2 = [0]

for i in range(N):
    pre1.append(pre1[-1] + arr[i])
    pre2.append(pre2[-1] + arr[i] * awake[i])

ans = 0

for i in range(N-K+1):
    tot = pre2[i] + pre1[i+K] - pre1[i] + pre2[N] - pre2[i+K]
    ans = max(ans, tot)

print ans