N, M = map(int,raw_input().split())

ones = []
twos = []

for i in range(N):
    a,b = map(int,raw_input().split())
    if b == 1:
        ones.append(a)
    else:
        twos.append(a)

ones = sorted(ones)
twos = sorted(twos)

psa = [0]

for i in range(len(twos)):
    psa.append(psa[-1] + twos[i])

ans = 0
bad = 0
for i in range(len(ones) + 1):
    if i:
        bad += ones[i-1]
    if bad > M:
        break
    good = M - bad
    lo = 0
    hi = len(twos) + 1
    while lo < hi:
        mid = (lo+hi)/2
        if psa[mid] > good:
            hi = mid
        else:
            lo = mid+1
    total = (lo-1) * 2 + i
    ans = max(ans, total)

print ans


'''

5 11
1 1
6 2
3 1
5 2
4 2


bad gunmen:

0: (1, 1)
1: (3, 1)
2: (2, 1)
3: (5, 1)

x = 2

we take: (1,1) and (2,1) = 3 units of space

y units of space to take good gunmen

good gunmen:

0: (4, 2)
1: (5, 2)
2: (6, 2)

--> psa = [0, 4, 9, 15]

psa[i] = sum of space values for all gunmen with index < i


'''