# 2021.07.14
# 수열의 값 구하기

a, b, c, n = map(int, input().split())


def sy(before):
    return before*b + c


for i in range(1, n):
    a = sy(a)

print(a)
