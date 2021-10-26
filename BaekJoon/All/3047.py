# 2021.10.26
# 3047
# ABC

ls = list(map(int, input().split()))
orders = input()
ls.sort()
for i in orders:
    if i == 'A':
        print(ls[0], end=' ')
    elif i == 'B':
        print(ls[1], end=' ')
    else:
        print(ls[2], end=' ')
