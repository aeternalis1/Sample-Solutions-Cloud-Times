n = 8
dist = [[0 for x in range(8)] for x in range(8)]
sx, sy = map(int,raw_input().split())
dx, dy = map(int,raw_input().split())
sx -= 1
sy -= 1
dx -= 1
dy -= 1

moves = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]

q = [[sx,sy]]
dist[sx][sy] = 1
while q:
    x, y = q.pop(0)
    for i in moves:
        nx, ny = x + i[0], y + i[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if dist[nx][ny] != 0:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append([nx,ny])

print dist[dx][dy]-1