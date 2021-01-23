N,M,T = map(int,raw_input().split())

edges = [[] for x in range(N+1)]

for i in range(M):
    a,b = map(int,raw_input().split())
    edges[a].append(b)

dist = [[float('inf') for x in range(N+1)] for x in range(N+1)]

for i in range(1,N+1):
    q = [i]
    dist[i][i] = 0
    while q:
        cur = q.pop(0)
        for j in edges[cur]:
            if dist[i][j] == float('inf'):
                dist[i][j] = dist[i][cur] + 1
                q.append(j)

Q = int(raw_input())
for i in range(Q):
    a,b = map(int,raw_input().split())
    if dist[a][b] == float('inf'):
        print "Not enough hallways!"
    else:
        print dist[a][b] * T