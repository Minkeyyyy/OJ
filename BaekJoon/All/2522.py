# 2021.08.09
# 2522
# 별 찍기 - 12

n = int(input())

for i in range(1, 2*n):
    if i <= n:
        print(' '*(n-i) + '*'*(i))
    else:
        print(' '*(i-n) + '*'*(2*n-i))
