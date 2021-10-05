# 2021.10.04
# 2804
# 크로스워드 만들기

a, b = input().split()

for i in range(len(a)):
    index = b.find(a[i])
    if 0 <= index:
        r = index
        c = i
        break

for i in range(len(b)):
    if r != i:
        for j in range(len(a)):
            if j == c:
                print(b[i], end='')
            else:
                print('.', end='')
    else:
        print(a, end='')
    print()
