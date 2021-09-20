# 2021.09.20
# 2592
# 대표값

ls = []
total = 0
max_idx = maxi = -1


for _ in range(10):
    n = int(input())
    ls.append(n)
    total += n

for i in range(10):
    if maxi < ls.count(ls[i]):
        max_idx = i
        maxi = ls.count(ls[i])

print(total//10)
print(ls[max_idx])
