# 2021.10.08
# 2858
# 기숙사 바닥

r, b = map(int, input().split())

for i in range(1, b+1):  # 갈색 타일의 가로
    if b % i == 0:
        j = b//i  # 갈색 타일의 세로
        if (2*(i+j)+4) == r:  # 빨강 타일의 갯수와 맞을 때
            print(j+2, i+2)
            break
