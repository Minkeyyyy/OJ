# 2021.11.11
# 4328
# 기초 나머지 계산

def jinbub(b, n):
    result = ''
    while n >= b:
        result += str(n % b)
        n //= b

    result += str(n)
    return result[::-1]


while True:
    s = input()
    if s == '0':
        break
    b, p, m = s.split()
    p = int(p, int(b))
    m = int(m, int(b))
    result = p % m
    print(jinbub(int(b), result))
