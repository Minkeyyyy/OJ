# 2021.09.10
# 2386
# 도비의 영어 공부

while True:
    inp = input()
    if inp == '#':
        break
    a = inp[0]
    b = inp[2:]
    b = b.lower()
    cnt = 0

    for i in b:
        if i == a:
            cnt += 1

    print(a, cnt)
