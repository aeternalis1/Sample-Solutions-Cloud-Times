edges = [[] for x in range(10000)]

N = int(raw_input())

for i in range(N):
    a,b = map(int,raw_input().split())
    edges[a].append(b)

while True:
    a,b = map(int,raw_input().split())
    if a == b == 0:
        break
    queue = [a]
    visited = [0 for x in range(10000)]
    dist = [-1 for x in range(10000)]
    while queue:
        cur = queue.pop(0)
        for neighbour in edges[cur]:
            if not visited[neighbour]:
                visited[neighbour] = 1
                dist[neighbour] = dist[cur] + 1
                queue.append(neighbour)
    if not (visited[a] and visited[b]):
        print "No"
        continue
    print "Yes",dist[b]