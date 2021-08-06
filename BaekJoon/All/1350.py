# 2021.08.06
# 1350
# 진짜 공간

n = int(input())
sizes = list(map(int, input().split()))[:n]
limit = int(input())
result = 0

for size in sizes:
    if size % limit == 0:
        result += size//limit
    else:
        result += size//limit + 1


print(limit * result)
