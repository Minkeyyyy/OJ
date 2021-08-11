# 2021.08.11
# 2576
# 홀수
import sys

odd_sum = 0  # 합계
odd_min = 100  # 최소값
flag = False

for _ in range(7):
    n = int(sys.stdin.readline())
    if n % 2 == 1:
        # 홀수가 나왔는지 알기 위한 구분
        flag = True
        odd_sum += n
        # 최소값 갱신
        if odd_min > n:
            odd_min = n
# 홀수가 나왔으면 출력, 아니면 -1 출력
if flag:
    print(odd_sum)
    print(odd_min)
else:
    print(-1)
