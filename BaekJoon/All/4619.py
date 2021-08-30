# 2021.08.30
# 4619
# 루트

while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break
    new1 = int(b**(1/n))
    new2 = new1 + 1
    result1 = b-(new1**n)
    result2 = (new2**n)-b
    if result1 > result2:
        print(new2)
    else:
        print(new1)
