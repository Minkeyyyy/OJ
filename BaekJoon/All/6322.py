# 2021.09.25
# 6322
# 직각 삼각형의 두 변

import math
i = 1
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a == -1:
        if c <= b:
            print("Triangle #{}".format(i))
            print("Impossible.\n")
        else:
            a = math.sqrt(c*c - b*b)
            print("Triangle #{}".format(i))
            print("{:.3f}\n".format(a))
    elif b == -1:
        if c <= a:
            print("Triangle #{}".format(i))
            print("Impossible.\n")
        else:
            b = math.sqrt(c*c - a*a)
            print("Triangle #{}".format(i))
            print("{:.3f}\n".format(b))
    else:
        c = math.sqrt(a*a+b*b)
        print("Triangle #{}".format(i))
        print("{:.3f}\n".format(c))
    i += 1
