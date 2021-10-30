# 2021.10.30
# 1453
# 피시방 알바

n = int(input())
seats = [False]*101
ls = list(map(int, input().split()))
count = 0

for i in ls:
    if not seats[i]:
        seats[i] = True
    else:
        count += 1

print(count)
