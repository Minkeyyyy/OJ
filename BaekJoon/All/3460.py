# 2021.08.26
# 3460
# 이진수

n = int(input())
for _ in range(n):
    # 이진수로 변환
    num = bin(int(input()))[2:]
    # 이진수를 역순으로 바꿈
    num = num[::-1]
    for i in range(len(num)):
        if num[i] == '1':
            print(i, end=' ')
