# 2021.09.05
# 2037
# 문자 메세지

lss = [' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
p, w = map(int, input().split())
st = input()
flag = -1  # 전에 누른 숫자 위치
cho = 0

for i in st:
    for ls in lss:
        if i in ls:
            n_flag = lss.index(ls) + 1  # 어느 숫자를 눌러야 하는지 결정
            if n_flag == 1 and flag == 1:  # 공백이 연속으로 나오면
                pass
            elif n_flag == flag:  # 이전 숫자와 같은 숫자면
                cho += w
            flag = n_flag  # flag를 최신화
            cho += p*(ls.index(i)+1)  # 문자의 위치에 따라서 누르는 횟수를 결정
            break  # 나온 것이면 거기서 끝내면 됨

print(cho)
