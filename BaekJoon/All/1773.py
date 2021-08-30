# 2021.08.30
# 1773
# 폭죽쇼

n, c = map(int, input().split())
ls = [0]*(c+1)
result = 0

for _ in range(n):
    a = int(input())
    for i in range(a, c+1, a):
        if ls[i] == 0:
            ls[i] = 1
            result += 1
print(result)
