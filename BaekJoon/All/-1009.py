# 2021.07.18
# 분산처리
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    na = []
    a, b = map(int, sys.stdin.readline().split())
    if b == 1:
        na.append(a)
    else:
        for i in range(1, b+1):
            if ((a**i) % 10) not in na:
                na.append((a**i) % 10)
            else:
                break
    if len(na) == 1:
        print(na[0])
    else:
        print(na[b % (len(na))-1])
