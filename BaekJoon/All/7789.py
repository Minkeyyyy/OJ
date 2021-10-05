# 2021.10.05
# 7789
# 텔레프라임

a, b = input().split()
int_a = int(a)
result = 0

for i in range(2, int_a):
    if int_a % i == 0:
        result += 1
        break
new = int(b+a)

for i in range(2, new):
    if new % i == 0:
        result += 1
        break

if result == 0:
    print("Yes")
else:
    print("No")
