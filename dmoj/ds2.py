N,M = map(int,raw_input().split())

par = [x for x in range(N)]
size = [1 for x in range(N)]

def findRoot(i):
    if i == par[i]:
        return i
    return findRoot(par[i])

def merge(a, b):
    if size[a] > size[b]:
        size[a] += size[b]
        par[b] = a
    else:
        size[b] += size[a]
        par[a] = b

mst = []

for i in range(M):
    a,b = map(int,raw_input().split())
    a -= 1
    b -= 1
    roota = findRoot(a)
    rootb = findRoot(b)
    if roota == rootb:
        continue
    merge(roota, rootb)
    mst.append(i+1)
    if len(mst) == N-1:
        break

if len(mst) != N-1:
    print "Disconnected Graph"
else:
    for i in mst:
        print i