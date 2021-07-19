#2021.06.22
#베르트랑 공준
import math

def sosu(num):
    if num == 1:
        return False
    new = int(math.sqrt(num))
    for i in range(2,new+1):
        if num % i == 0:
            return False
    return True

def check(num):
    result = 0
    for i in range(num + 1, num*2 + 1):
        if sosu(i):
            result += 1
        
    return result

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(check(n))