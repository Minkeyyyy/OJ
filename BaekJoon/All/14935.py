# 2021.08.15
# 14935
# FA

def f(x):
    a = int(x[0])
    b = len(x)
    result = a*b
    x = int(x)
    if result == x:
        return 'FA'
    else:
        return str(result)


n = input()
res = n
while True:
    res = f(res)
    if res == 'FA':
        print(res)
        break
