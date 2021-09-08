# 2021.09.08
# 2161
# 카드1

n = int(input())
ls = [i for i in range(1, n+1)]

while True:
    if len(ls) == 1:
        print(ls[0])
        break
    print(ls[0], end=' ')
    ls.pop(0)
    last = ls.pop(0)
    ls = ls + [last]
