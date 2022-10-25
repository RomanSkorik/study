import math
n = int(input())
sum1 = 0
A = []
Bdown = []
Bup = []
Symbol = []
Final = []
for i in range(n):
    a = list(map(str, input().split()))
    A.append(a)
    Symbol.append(a[0])
    sum1 += int(a[1])
unit = 100 / sum1
for i in range(len(A)):
    if A[i][0] == "-":
        Bdown.append(math.floor(unit * int(A[i][1])))
    elif A[i][0] == "+":
        Bup.append(math.ceil(unit * int(A[i][1])))
dif = 100 - (sum(Bdown) + sum(Bup))
if Bup == []:
    Bdown[0] += dif
if Bdown == []:
    Bup[0] += dif
if dif > 0 and Bup != []:
    Bup[0] += dif
if dif < 0 and Bdown != []:
    Bdown[0] += dif
pos1 = 0
pos2 = 0
for i in range(len(Symbol)):
    if Symbol[i] == "+":
        Final.append(Bup[pos1])
        pos1 += 1
    elif Symbol[i] == "-":
        Final.append(Bdown[pos2])
        pos2 += 1
for i in range(len(Final)):
    print(str(Final[i]))
