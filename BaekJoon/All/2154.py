# 2021.09.07
# 2154
# 수 이어 쓰기3

num = input()
i = 1  # 숫자 덧셈용
now = ''

while True:
    now += str(i)
    if num in now:
        print(now.index(num)+1)
        break
    else:
        i += 1
