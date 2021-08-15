# 2021.08.14
# 15921
# 수찬은 마린보이야!!

n = int(input())
if n == 0:
    print('divide by zero')
else:
    ls = list(map(int, input().split()))

    mean = sum(ls) / n
    result = 0
    for i in ls:
        result += (i/n)

    if result == 0:
        print('divide by zero')
    else:
        print("{:.2f}".format(mean/result))
