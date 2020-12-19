N,M = map(int,raw_input().split())
arr = []
for i in range(N):
	arr.append(list(map(int,raw_input().split())))
ans = [[pow(10,18) for x in range(M)] for x in range(N)]
ans[0][0] = arr[0][0]
for i in range(N):
	for j in range(M):
		if i > 0:
			ans[i][j] = min(ans[i][j],ans[i-1][j]+arr[i][j])
		if j > 0:
			ans[i][j] = min(ans[i][j],ans[i][j-1]+arr[i][j])
print ans[N-1][M-1]