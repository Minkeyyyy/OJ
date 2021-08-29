# 2021.08.29
# 1731
# 추론

n = int(input())
ls = []

for _ in range(n):
    ls.append(int(input()))

cha1 = ls[1] - ls[0]
if (ls[1] % ls[0]) == 0:
    bi1 = ls[1]//ls[0]
    if (ls[2] // ls[1]) == bi1:
        print(ls[-1]*bi1)
else:
    print(ls[-1] + cha1)
