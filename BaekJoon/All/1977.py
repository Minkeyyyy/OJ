# 2021.11.01
# 1977
# 완전제곱수

import math
# 미리 100의 완전제곱수까지 구하기
pre = [i*i for i in range(0, 101)]
a = int(input())
b = int(input())

# a가 정수라면 그 index를 저장
if math.sqrt(a) == int(math.sqrt(a)):
    mini_idx = int(math.sqrt(a))
# 정수가 아니면 올림해서 index를 저장
else:
    mini_idx = int(math.sqrt(a))+1
# 마지막 수는 내림해서 index를 저장
maxi_idx = int(math.sqrt(b))

# 가장 작은 완전수가 최댓값보다 크면 -1출력
if pre[mini_idx] > b:
    print(-1)
else:
    print(sum(pre[mini_idx:maxi_idx+1]))
    print(pre[mini_idx])
