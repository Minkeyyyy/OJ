# 2021.10.18
# 2979
# 트럭 주차

cost = list(map(int, input().split()))
result = 0
ls = [0]*101

for i in range(3):
    s, e = map(int, input().split())
    for j in range(s, e):
        ls[j] += 1

for i in ls:
    if i == 1:
        result += cost[0]*1
    elif i == 2:
        result += cost[1]*2
    elif i == 3:
        result += cost[2]*3

print(result)
