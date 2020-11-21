N = int(raw_input())
arr = [int(raw_input()) for x in range(N)]
psa = [0]
for i in range(N):
    psa.append(psa[-1] + arr[i])

Q = int(raw_input())
for i in range(Q):
    l,r = map(int,raw_input().split())
    print psa[r+1] - psa[l]
