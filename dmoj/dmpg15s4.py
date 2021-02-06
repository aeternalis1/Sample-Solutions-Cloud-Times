B, Q = map(int,raw_input().split())
beacons = []
for i in range(B):
    beacons.append(list(map(int,raw_input().split())))

edges = [[] for x in range(B)]
for i in range(B):
    for j in range(i+1, B):
        dist = pow(beacons[j][0] - beacons[i][0], 2) + pow(beacons[j][1] - beacons[i][1], 2)
        if dist <= pow(beacons[i][2], 2):
            edges[i].append(j)
        if dist <= pow(beacons[j][2], 2):
            edges[j].append(i)

for i in range(Q):
    a,b = map(int,raw_input().split())
    a -= 1
    b -= 1
    q = [a]
    chk = [0 for x in range(B)]
    chk[a] = 1
    while q:
        c = q.pop(0)
        for j in edges[c]:
            if not chk[j]:
                chk[j] = 1
                q.append(j)
    print "YES" if chk[b] else "NO"