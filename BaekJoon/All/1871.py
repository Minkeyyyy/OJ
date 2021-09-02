# 2021.09.02
# 1871
# 좋은 자동차 번호판

n = int(input())
for _ in range(n):
    al, num = input().split('-')
    result1 = 0
    result2 = int(num)
    for idx, val in enumerate(al):
        result1 += (ord(val) - ord('A')) * (26**(2-idx))
    if -100 <= result2 - result1 <= 100:
        print('nice')
    else:
        print('not nice')
