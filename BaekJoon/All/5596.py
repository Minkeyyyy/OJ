# 2021.07.25
# 시험 점수

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = sum(A)
sum_B = sum(B)

if sum_A >= sum_B:
    print(sum_A)
else:
    print(sum_B)
