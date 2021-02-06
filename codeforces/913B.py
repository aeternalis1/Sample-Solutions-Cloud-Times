n = int(raw_input())

par = [0 for x in range(n+1)]
children = [[] for x in range(n+1)]
for i in range(2,n+1):
    par[i] = int(raw_input())
    children[par[i]].append(i)

spruce = 1

for i in range(n):
    leaf = 0
    for j in children[i]:
        if len(children[j]) == 0:
            leaf += 1
    if leaf < 3 and children[i] != []:
        spruce = 0

print "Yes" if spruce else "No"