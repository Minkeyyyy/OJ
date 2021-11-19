# 2021.11.19
# 2145
# 숫자 놀이

def solution(s):
    result = 0
    for i in s:
        result += int(i)
    return result


while True:
    n = input()
    if n == '0':
        break
    result = 0

    while int(n) >= 10:
        n = (str(solution(n)))

    print(n)
