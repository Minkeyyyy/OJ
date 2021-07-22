#2021.07.22
#집주소
def space(n):
    str_n = str(n)
    result = 0
    for i in str_n:
        if i == '0':
            result += 4
        elif i == '1':
            result += 2
        else: 
            result += 3
    return len(str_n) + result + 1

while True:
    n = int(input())
    if n == 0 :
        break
    else: 
        print(space(n))