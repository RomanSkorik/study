n, m = map(int, input().split())
a = [list(map(str, input().split())) for i in range(n)]
need = int(input()) * "0"
counter = 0
counteri = 0
truth = 0

a = "".join(a[2])
print(a)
print(need)
print(a.find(need))