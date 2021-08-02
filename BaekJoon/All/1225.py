# 2021.08.02
# 1225
# 이상한 곱셈

a, b = input().split()
result1, result2 = 0, 0
for i in a:
    result1 += int(i)
for j in b:
    result2 += int(j)

print(result1*result2)
