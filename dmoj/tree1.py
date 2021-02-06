n = 4
adj = []
tot = 0
for i in range(n):
    adj.append(list(map(int,raw_input().split())))
    tot += sum(adj[i])

q = [0]
chk = [0 for x in range(4)]
chk[0] = 1
while q:
    c = q.pop(0)
    for i in range(4):
        if adj[c][i] and not chk[i]:
            q.append(i)
            chk[i] = 1

if sum(chk) == 4 and tot == 6:
    print "Yes"
else:
    print "No"