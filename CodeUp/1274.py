# 2021.07.15
# 소수 판별

n = int(input())
count = 2
for i in range(2, n):
    if n % i == 0:
        count += 1
        print("not prime")
        break

if count == 2:
    print("prime")
