# 2021.08.04
# 1145
# 적어도 대부분의 배수

numl = list(map(int, input().split()))
numl.sort()
i = numl[-1]

while True:
    cnt = 0
    for j in numl:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break
    i += 1
