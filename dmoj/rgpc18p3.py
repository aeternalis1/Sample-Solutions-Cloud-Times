N,T = map(int,raw_input().split())
arr = [0 for x in range(N+1)]

for i in range(T):
    a,b,c = map(int,raw_input().split())
    arr[a-1] += c
    arr[b] -= c

for i in range(N):
    arr[i+1] += arr[i]

arr.pop(-1)

psa = [0]
for i in range(N):
    psa.append(psa[-1] + arr[i])

ans = 0

L = int(raw_input())

for i in range(N):
    lo = i
    hi = N + 1
    while lo < hi:
        mid = (lo+hi)/2
        if psa[mid] - psa[i] > L:
            hi = mid
        else:
            lo = mid + 1
    taken = lo-1-i
    ans = max(ans, taken)

print ans


'''
arr = [6, 7, 7, 8, 4, 1]

-->

psa = [0, 6, 13, 20, 28, 32, 33]

l = 1
L = ???

how to find r?

'''