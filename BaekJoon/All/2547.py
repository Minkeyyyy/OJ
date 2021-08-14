# 2021.08.10
# 2547
# 사탕 선생 고창영
import sys

t = int(sys.stdin.readline())
#빈 줄을 삽입
sys.stdin.readline()

for i in range(t):
    result = 0
    n = int(sys.stdin.readline())
    for _ in range(n):
        result += int(sys.stdin.readline())
    #마지막 케이스 빼고는 모두 빈 줄을 삽입
    if (i + 1) != t:
        sys.stdin.readline()

    if result % n == 0:
        print("YES")
    else:
        print("NO")
