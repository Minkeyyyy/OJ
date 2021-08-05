# 2021.08.05
# 2446
# 별 찍기 - 9

n = int(input())

for i in range(1, (2*n)):
    if i < n:
        print(' '*(i-1) + '*'*(n-i) + '*' + '*'*(n-i))
    elif n == i:
        print(' '*(i-1) + '*')
    else:
        i = i - n
        print(' '*(n-i-1) + '*' * i + '*' + '*' * i)
