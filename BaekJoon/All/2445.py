# 2021.08.04
# 2445
# 별 찍기 - 8

n = int(input())

for i in range(1, 2*n):
    if i < n:
        print('*'*i+' '*(n-i) + ' '*(n-i) + '*' * i)
    elif i > n:
        i = i - n
        print('*'*(n-i) + ' ' * i + ' '*i + '*' * (n-i))
    else:
        print('*' * (2*i))
