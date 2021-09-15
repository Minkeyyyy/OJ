# 2021.09.15
# 5613
# 계산기 프로그램

i = 0
a = input()

while True:
    n = input()
    if i % 2 == 0:
        if n == '=':
            break
        elif n == '/':
            oper = '//'
        else:
            oper = n
    else:
        a = eval(a+oper+n)
    i += 1

print(a)
