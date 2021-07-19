#2021.06.12
#손익분기점

a,b,c = map(int,input().split())

profit = c-b
if profit > 0:
    result = a//profit + 1
    print(result)
else:
    print(-1)

