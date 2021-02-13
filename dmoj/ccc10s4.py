N = int(raw_input())
pens = []

for i in range(N):
    pen = map(int,raw_input().split())
    pens.append(pen)

edges = []
isEdge = {}
for i in range(N):
    for j in range(i+1,N):
        for k in range(1,pens[i][0]+1):
            a = pens[i][k]
            b = pens[i][k%pens[i][0] + 1]
            for l in range(1,pens[j][0]+1):
                c = pens[j][l]
                d = pens[j][l%pens[j][0] + 1]
                if a == c and b == d or a == d and b == c:
                    edges.append([pens[i][k+pens[i][0]], i, j])
                    isEdge[(a,b)] = 1

for i in range(N):
    for k in range(1,pens[i][0]+1):
        a = pens[i][k]
        b = pens[i][k%pens[i][0] + 1]
        if (a,b) in isEdge or (b,a) in isEdge:
            continue
        edges.append([pens[i][k+pens[i][0]], i, N])

edges = sorted(edges)


par = [x for x in range(N+1)]
rank = [0 for x in range(N+1)]

def root(node):
    if par[node] == node:
        return node
    return root(par[node])

def join(a, b):
    if rank[a] < rank[b]:
        par[a] = b
    elif rank[a] > rank[b]:
        par[b] = a
    else:
        par[b] = a
        rank[a] += 1

def mst(outside, N):
    for x in range(N+1):
        par[x] = x
        rank[x] = 0
    
    cnt = 0
    ans = 0
    for i in range(len(edges)):
        if edges[i][2] == N and not outside:
            continue
        a, b = root(edges[i][1]), root(edges[i][2])
        if a == b:
            continue
        join(a,b)
        ans += edges[i][0]
        cnt += 1
        if cnt == N-1+outside:
            break
    return ans

print min(mst(0, N), mst(1, N))