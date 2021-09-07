# 2021.09.07
# 5217
# 쌍의 합

n = int(input())

for _ in range(n):
    num = int(input())
    print("Pairs for {}:".format(num), end=' ')
    flag = True
    for i in range(1, (num//2)+1):
        if i == (num-i):
            pass
        else:
            if flag:
                print(i, num-i, end='')
                flag = False
            else:
                print(',', i, num-i, end='')

    print()
