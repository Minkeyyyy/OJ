# 2021.08.10
# 2523
# 별 찍기 - 13

n = int(input())

for i in range(1, 2*n):
    if i <= n:
        print('*'*i)
    else:
        print('*'*(2*n-i))
