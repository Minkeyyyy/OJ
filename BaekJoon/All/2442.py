# 2021.08.02
#별찍기 - 5

n = int(input())

for i in range(1, n+1):
    print(' '*(n-i) + '*'*(i-1) + '*' + '*'*(i-1))

# 별을 찍는 위치를 생각해서 처음부터 개수를 잡고 푸는 것이 더 좋겠다.