t = int(raw_input())

moves = [[1,0],[-1,0],[0,1],[0,-1]]

for _ in range(t):
    m,n = map(int,raw_input().split())
    grid = []

    for i in range(n):
        grid.append(list(raw_input()))
        for j in range(m):
            if grid[i][j] == 'C':
                sx = j
                sy = i
            elif grid[i][j] == 'W':
                dx = j
                dy = i

    dist = [[-1 for x in range(m)] for x in range(n)]
    dist[sy][sx] = 0
    q = [[sx,sy]]
    while q:
        x,y = q.pop(0)
        for [i,j] in moves:
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[ny][nx] == 'X' or dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            q.append([nx,ny])
    print dist[dy][dx] if dist[dy][dx] < 60 else "#notworth"