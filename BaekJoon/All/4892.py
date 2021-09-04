# 2021.09.04
# 4892
# 숫자 맞추기 게임

i = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3*n0
    if n1 % 2 == 0:
        n2 = n1//2
        n4 = (3*n2)//9
        print("{}. even {}".format(i, n4))
        i += 1
    else:
        n2 = (n1+1)//2
        n4 = (3*n2)//9
        print("{}. odd {}".format(i, n4))
        i += 1
