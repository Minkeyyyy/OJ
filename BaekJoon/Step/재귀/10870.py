#2021.07.01
#피보나치 수5

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

inp = int(input())

print(fibo(inp))

#점화식에서 2번째부터 성립한다고 해도 직접 눈으로 확인