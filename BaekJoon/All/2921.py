# 2021.08.16
# 2921
# 도미노

n = int(input())
result = 0

for i in range(n+1):
    result += i*((n-i) + 1)
    result += sum(range(i, n+1))

print(result)
