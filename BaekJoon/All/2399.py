# 2021.09.11
# 2399
# 거리의 합

n = int(input())
ls = list(map(int, input().split()))
ls.sort()  # 정렬을 해줘서 나머지를 신경쓰지 않도록 함
result = 0

for i in range(n):
    for j in range(i, n):
        result += ls[j] - ls[i]  # 각각의 차를 구함
print(result * 2)
