# 2021.08.07
# 1362
# 펫
num = 0

while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    die = False
    if a.isdigit() and b.isdigit():
        good = int(a)
        now = int(b)
    while True:
        c, d = input().split()
        if c == '#' and d == '0':
            break

        if not die:
            if c == 'F':
                now += int(d)
            elif c == 'E':
                now -= int(d)

        if now <= 0:
            die = True

    if die:
        print(num, "RIP")
    elif (good/2) < now < (good*2):
        print(num, ':-)')
    else:
        print(num, ':-(')
