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
edges = []

for i in range(M):
    a,b,c,d = map(int,raw_input().split())
    a -= 1
    b -= 1
    edges.append([d,c,a,b])

edges = sorted(edges)
danger = 0
cost = 0
cnt = 0 

for i in range(M):
    d,c,a,b = edges[i]
    roota = findRoot(a)
    rootb = findRoot(b)
    if roota == rootb:
        continue
    merge(roota, rootb)
    cnt += 1
    danger += d
    cost += c
    if cnt == N-1:
        break

print danger, cost