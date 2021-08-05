# 2021.08.05
# 1264
# 모음의 개수
mo = ['A', 'E', 'I', 'O', 'U']

while True:
    n = input()
    cnt = 0
    if n == '#':
        break
    else:
        n = n.upper()
        for i in n:
            if i in mo:
                cnt += 1
        print(cnt)
