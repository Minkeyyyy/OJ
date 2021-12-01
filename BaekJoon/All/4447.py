# 2021.12.02
# 4447
#좋은놈, 나쁜놈

n = int(input())

for i in range(n):
    s = input()
    b = s.lower().count('b')
    g = s.lower().count('g')

    if b > g:
        print(f"{s} is A BADDY")
    elif b < g:
        print(f"{s} is GOOD")
    else:
        print(f"{s} is NEUTRAL")
