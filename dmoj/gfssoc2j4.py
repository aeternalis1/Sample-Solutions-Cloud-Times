N,Q = map(int,raw_input().split())
arr = list(map(int,raw_input().split()))

psa = [0]
for i in range(N):
    psa.append(psa[-1] + arr[i])

for i in range(Q):
    a,b = map(int,raw_input().split())
    skipped = psa[b] - psa[a-1]
    total = psa[N]
    print total - skipped
