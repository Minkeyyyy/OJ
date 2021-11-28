# 2021.11.28
# 3230
# 금메달,은메달,동메달은 누가?

n, m = map(int, input().split())

ls1 = []    # 1회차
result = []

for i in range(1, n+1):
    idx = int(input())
    ls1.insert(idx-1, i)

ls1 = ls1[:m]   # 1회차의 순서에 맞춰서 거름
ls1.reverse()

for j in range(m):
    idx = int(input())
    result.insert(idx-1, ls1[j])

for i in result[:3]:
    print(i)
