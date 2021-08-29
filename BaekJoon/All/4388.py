# 2021.08.29
# 4388
# 받아올림

while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break

    flag = 0
    dif = len(a) - len(b)
    if dif > 0:
        b = '0' * dif + b
    else:
        a = '0' * (-dif) + a
    result = 0

    for i in reversed(range(len(a))):
        if (int(a[i]) + int(b[i])) + flag > 9:
            flag = 1
            result += 1
        else:
            flag = 0

    print(result)
