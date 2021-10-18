# 2021.10.18
# 9085
# 더하기

n = int(input())

for _ in range(n):
    size = int(input())
    ls = list(map(int, input().split()))[:size]
    print(sum(ls))
