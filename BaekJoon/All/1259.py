# 2021.08.20
# 1259
# 팰린드롬수

while True:
    n = input()
    if n == '0':
        break
    else:
        #문자열을 뒤집은 것 reverse_n에 저장
        reverse_n = n[::-1]
        if n == reverse_n:
            print('yes')
        else:
            print('no')
