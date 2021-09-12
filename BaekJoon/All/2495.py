# 2021.09.12
# 2495
# 연속구간


for _ in range(3):
    n = input()
    flag = 0
    result = 0
    for i in range(8):
        if i == 0:
            flag = 1
            result = 1
            continue
        if n[i] == n[i-1]:
            flag += 1
            result = max(flag, result)
        else:
            result = max(flag, result)
            flag = 1
    print(result)
