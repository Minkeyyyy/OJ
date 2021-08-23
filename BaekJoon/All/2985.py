# 2021.08.21
# 2985
# 세 수

a, b, c = map(int, input().split())

if (a+b) == c:
    print(str(a)+'+'+str(b)+'='+str(c))
if (a-b) == c:
    print(str(a)+'-'+str(b)+'='+str(c))
if (a*b) == c:
    print(str(a)+'*'+str(b)+'='+str(c))
if (a//b) == c:
    print(str(a)+'/'+str(b)+'='+str(c))
if (b+c) == a:
    print(str(a)+'='+str(b)+'+'+str(c))
if (b-c) == a:
    print(str(a)+'='+str(b)+'-'+str(c))
if (b*c) == a:
    print(str(a)+'='+str(b)+'*'+str(c))
if (b//c) == a:
    print(str(a)+'='+str(b)+'/'+str(c))
