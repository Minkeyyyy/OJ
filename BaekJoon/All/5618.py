# 2021.09.15
# 5618
# 공약수

n = int(input())
if n == 2:
    a, b = map(int, input().split())
    ls = [a, b]
else:
    a, b, c = map(int, input().split())
    ls = [a, b, c]

for i in range(1, min(ls)):
    if n == 2:
        if a % i == 0 and b % i == 0:
            print(i)
    else:
        if a % i == 0 and b % i == 0 and c % i == 0:
            print(i)
