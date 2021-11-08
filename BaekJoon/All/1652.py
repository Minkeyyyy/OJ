# 2021.11.08
# 1652
# 누울 자리를 찾아라

n = int(input())
ls = []
row, col = 0, 0


def check(s):
    flag = 0  # 빈자리 체크 variable
    result = 0  # 누울 수 있는 자리

    for i in s:
        if i == '.':
            flag += 1
            if flag == 2:  # 빈자리 2개 일때 1증가
                result += 1

        if i != '.':  # 빈자리가 아니면 체크 변수 0초기화
            flag = 0
    return result


for _ in range(n):
    inp = input()
    ls.append(inp)
    cc = check(inp)
    row += cc

for i in range(n):
    new = ''
    for j in range(n):
        new += ls[j][i]
    cc = check(new)
    col += cc

print(row, col)
