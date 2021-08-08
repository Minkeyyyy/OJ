# 2021.08.08
# 2501
# 약수 구하기

n, k = map(int, input().split())
result = 0

for i in range(1, n+1):
    if n % i == 0:
        result += 1
    if result == k:
        print(i)
        break

if result < k:
    print(0)
