# 2021.09.05
# 2037
# 문자 메세지

lss = [' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
p, w = map(int, input().split())
st = input()
flag = -1
cho = 0

for i in st:
    for ls in lss:
        if i in ls:
            n_flag = lss.index(ls) + 1
            if n_flag == flag:
                cho += w
            flag = n_flag
            cho += p*(ls.index(i)+1)
            print(i, cho)
            break

print(cho)
