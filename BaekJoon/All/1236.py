# 2021.07.31
# 성 지키기
import sys

n, m = map(int, sys.stdin.readline().split())
status = []

for _ in range(n):
    status.append(input())

count1, count2 = 0, 0

for i in status:
    if 'X' not in i:
        count1 += 1

for i in range(m):
    if 'X' not in [status[j][i]for j in range(n)]:
        count2 += 1

print(max(count1, count2))
