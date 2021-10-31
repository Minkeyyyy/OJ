# 2021.10.31
# 1834
# 나머지와 몫이 같은 수

n = int(input())
result = 0

for i in range(1, n):
    result += (n*i + i)

print(result)
