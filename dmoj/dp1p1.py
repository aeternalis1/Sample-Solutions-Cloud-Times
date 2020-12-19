N = int(raw_input())
arr = [int(raw_input()) for x in xrange(N)]

a = 0
b = arr[0]

for i in xrange(1,N):
    a, b = max(a, b), a + arr[i]

print max(a,b)