N,Q = map(int,raw_input().split())

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

for i in range(Q):
    q,x,y = raw_input().split()
    x = int(x) - 1
    y = int(y) - 1
    if q == 'A':
        rootx = findRoot(x)
        rooty = findRoot(y)
        if rootx == rooty:
            continue
        merge(rootx, rooty)
    else:
        rootx = findRoot(x)
        rooty = findRoot(y)
        if rootx == rooty:
            print "Y"
        else:
            print "N"