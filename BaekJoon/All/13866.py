# 2021.08.03
# 13866
# 팀 나누기

skills = list(map(int, input().split()))
sum1 = skills[0] + skills[3]
sum2 = skills[1] + skills[2]

if sum1 >= sum2:
    print(sum1 - sum2)
else:
    print(sum2 - sum1)
