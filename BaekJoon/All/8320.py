# 2021.10.08
# 8320
# 직사각형을 만드는 방법

n = int(input())
result = n

for i in range(2, int(n**0.5) + 1):
    for j in range(i, n):
        if i*j <= n:
            result += 1
        else:
            break

print(result)
