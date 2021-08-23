# 2021.08.23
# 2991
# 사나운 개

a, b, c, d = map(int, input().split())
ls = list(map(int, input().split()))

for i in ls:
    result = 0
    if 0 < (i % (a+b)) <= a:
        result += 1
    if 0 < (i % (c+d)) <= c:
        result += 1
    print(result)
