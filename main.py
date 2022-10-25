n, m = map(int, input().split())
w = [[1] * m for i in range(n)]
for i in range(1, n):
    for j in range(1, m):
        w[i][j] = w[i][j - 1]
print(w[-1][-1])
