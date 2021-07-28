# 2021.07.28
# 문어 숫자

moon = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4,
        '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    n = input()
    result = 0
    if n == '#':
        break
    else:
        jari = len(n) - 1
        for i in n:
            result += moon[i] * (8 ** jari)
            jari -= 1
        print(result)
