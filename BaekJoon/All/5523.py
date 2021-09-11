# 2021.09.10
# 5523
# 경기 결과
import sys

n = int(sys.stdin.readline())
cnt_a = 0
cnt_b = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        cnt_a += 1
    elif a == b:
        pass
    else:
        cnt_b += 1

print(cnt_a, cnt_b)
