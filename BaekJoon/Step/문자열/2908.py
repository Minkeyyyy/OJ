#상수
#2021.06.09

a,b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
