# 2021.09.04
# 1952
# 달팽이2

a, b = map(int, input().split())
result = 0

while True:
    if min(a, b) == 1:
        result += 1
        break
    elif min(a, b) == 2:
        result += 3
        break
    else:
        result += 4
    a -= 2
    b -= 2

print(result)
