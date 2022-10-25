x, y = map(int, input().split())
x1, y1 = map(int, input().split())
if x != x1 and y != y1:
    s = abs(x - x1) + abs(y -y1)
else:
    s = 1
print(s)
