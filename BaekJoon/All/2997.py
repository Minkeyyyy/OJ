# 2021.08.23
# 2997
# 네 번째 수

ls = list(map(int, input().split()))
ls.sort()

dif1 = ls[1] - ls[0]
dif2 = ls[2] - ls[1]

if dif1 == dif2:
    print(ls[-1] + dif1)
elif dif1 == 2*dif2:
    print(ls[0] + dif2)
else:
    print(ls[-1] - dif1)
