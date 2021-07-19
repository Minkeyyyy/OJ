# 2021.07.13
# 최대공약수와 최소공배수

a, b = map(int, input().split())
if a <= b:
    min = a
else:
    min = b

for i in range(2, min + 1):
    if a % i == 0 and b % i == 0:
        g = i

print(g)
print(a*b//g)

# nameError 나온다.
