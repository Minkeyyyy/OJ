#2021.06.22
#소인수분해

n = int(input())

for i in range(2,n+1):
    if n == 1:
        break
    else:
        while n % i == 0:
            n = n // i
            print(i) 