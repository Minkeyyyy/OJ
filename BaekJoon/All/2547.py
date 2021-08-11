# 2021.08.10
# 2547
# 사탕 선생 고창영
import sys

t = int(sys.stdin.readline())
sys.stdin.readline()

for i in range(t):
    result = 0
    n = int(sys.stdin.readline())
    for _ in range(n):
        result += int(sys.stdin.readline())
    if (i + 1) != t:
        sys.stdin.readline()

    if result % n == 0:
        print("YES")
    else:
        print("NO")
