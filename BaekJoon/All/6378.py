# 2021.09.25
# 6378
# 디지털 루트

while True:
    n = input()
    if n == '0':
        break
    digital = 0

    while digital != 1:
        result = 0
        for i in n:
            result += int(i)
        digital = len(str(result))
        n = str(result)

    print(result)
