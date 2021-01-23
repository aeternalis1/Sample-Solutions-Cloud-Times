N,M,A,B = map(int,raw_input().split())

edges = [[] for x in range(N+1)]
for i in range(M):
    a,b = map(int,raw_input().split())
    edges[a].append(b)
    edges[b].append(a)

q = [A]
chk = [0 for x in range(N+1)]
chk[A] = 1

while q:
    cur = q.pop(0)
    for i in edges[cur]:
        if not chk[i]:
            q.append(i)
            chk[i] = 1

print "GO SHAHIR!" if chk[B] else "NO SHAHIR!"