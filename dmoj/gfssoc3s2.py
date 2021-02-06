import sys

R, C = map(int,raw_input().split())

grid = []

dy = -1
dx = -1
sby = -1
sbx = -1
spy = -1
spx = -1

for i in range(R):
    grid.append(list(raw_input()))
    for j in range(C):
        if grid[i][j] == 'B':
            sby = i
            sbx = j
        elif grid[i][j] == 'P':
            spy = i
            spx = j
        elif grid[i][j] == 'X':
            dy = i
            dx = j

if spy == -1 or spx == -1 or sby == -1 or sbx == -1:
    print -1
    sys.exit()

q = [[spy, spx, sby, sbx]]
chk = [[[[-1 for x in range(C)] for x in range(R)] for x in range(C)] for x in range(R)]    # chk[i][j][k][l] stores min moves to get player to [i,j] and box to [k,l]
chk[spy][spx][sby][sbx] = 0

moves = [[-1,0], [1,0], [0,-1], [0,1]]

while q:
    py, px, by, bx = q.pop(0)
    for i in moves:
        npy, npx = py + i[0], px + i[1]
        if npy < 0 or npy >= R or npx < 0 or npx >= C or grid[npy][npx] == '#':
            continue
        nby, nbx = by, bx
        if npy == by and npx == bx:
            nby, nbx = by + i[0], bx + i[1]
            if nby < 0 or nby >= R or nbx < 0 or nbx >= C or grid[nby][nbx] == '#':
                continue
        if chk[npy][npx][nby][nbx] != -1:
            continue
        chk[npy][npx][nby][nbx] = chk[py][px][by][bx] + 1
        q.append([npy, npx, nby, nbx])

ans = float('inf')
for i in range(R):
    for j in range(C):
        if chk[i][j][dy][dx] == -1:
            continue
        ans = min(ans, chk[i][j][dy][dx])

if ans == float('inf') or dy == dx == -1:
    print -1
else:
    print ans