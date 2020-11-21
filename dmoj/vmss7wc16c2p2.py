s = raw_input()
N = len(s)

psa = [0]
for i in range(N):
    psa.append(psa[-1] + (s[i] == 'G'))

Q = int(raw_input())
for i in range(Q):
    l,r = map(int,raw_input().split())
    print psa[r+1] - psa[l]
