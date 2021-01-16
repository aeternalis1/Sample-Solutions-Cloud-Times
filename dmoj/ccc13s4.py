N,M = map(int,raw_input().split())

edges = [[] for x in range(N+1)]  # edges[i] is a list storing vertices that are neighbours of i

for i in range(M):
    x,y = map(int,raw_input().split())
    edges[x].append(y)

def bfs(p, q, N):
    queue = [p]
    visited = [0 for x in range(N+1)]
    visited[p] = 1
    while queue != []:
        cur = queue.pop(0)
        for neighbour in edges[cur]:
            if not visited[neighbour]:
                visited[neighbour] = 1
                queue.append(neighbour)
    return visited[q]

p,q = map(int,raw_input().split())

if bfs(p,q,N):
    print "yes"
elif bfs(q,p,N):
    print "no"
else:
    print "unknown"