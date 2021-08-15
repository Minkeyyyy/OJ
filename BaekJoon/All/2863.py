# 2021.08.15
# 2863
# 이게 분수?

a, b = map(int, input().split())
c, d = map(int, input().split())
result = []

result.append(a/c+b/d)
result.append(c/d+a/b)
result.append(d/b+c/a)
result.append(b/a+d/c)

max1 = max(result)
index = result.index(max1)

print(index)
