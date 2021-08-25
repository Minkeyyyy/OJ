# 2021.08.25
# 3034
# 앵그리 창영

n, w, h = map(int, input().split())
flag = w**2 + h**2

for _ in range(n):
    num = int(input())
    if num**2 <= flag:
        print('DA')
    else:
        print('NE')
