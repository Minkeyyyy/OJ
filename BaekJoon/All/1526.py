# 2021.10.31
# 1526
# 가장 큰 김민수

n = int(input())

for i in range(n, 3, -1):
    str_i = str(i)
    if len(str_i) == str_i.count('4') + str_i.count('7'):
        print(i)
        break
