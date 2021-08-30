# 2021.08.30
# 4504
# 배수찾기

n = int(input())

while True:
    a = int(input())
    if a == 0:
        break
    if a % n == 0:
        print("{} is a multiple of {}.".format(a, n))
    else:
        print("{} is NOT a multiple of {}.".format(a, n))
