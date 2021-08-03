# 2021.08.03
# 2444
# 별 찍기 - 7

n = int(input())

for i in range(1, n+1):
    print(' '*(n-i) + '*'*(i-1) + '*' + '*'*(i-1))
for i in range(1, n):
    print(' '*i+'*'*(n-i-1) + '*' + '*'*(n-i-1))
