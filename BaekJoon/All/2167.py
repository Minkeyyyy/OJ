# 2021.12.03
# 2167
# 2차원 배열의 합

n, m = map(int, input().split())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

num = int(input())

for _ in range(num):
    i, j, x, y = map(int, input().split())
    result = 0
    for k in range(i-1, x):
        for t in range(j-1, y):
            result += ls[k][t]
    print(result)
