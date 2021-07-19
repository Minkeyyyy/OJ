#2021.07.09
#괄호 문자열

n, k = map(int,input().split())

k2 = bin(k)[2:].zfill(n)

print(k2)
def a(str):
    result = ''
    for i in str:
        if i == '0':
            result = result + '('
        else:
            result = result + ')'
    return result

if (2**n)-1 < k :
    print(-1)
else:
    print(a(k2)) 

#문제 잘못 이해함.