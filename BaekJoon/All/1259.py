# 2021.08.20
# 1259
# 팰린드롬수

while True:
    n = input()
    if n == '0':
        break
    else:
        reverse_n = n[::-1]
        if n == reverse_n:
            print('yes')
        else:
            print('no')
