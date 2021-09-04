# 2021.09.04
# 5043
# 정말 좋은 압축

n, b = map(int, input().split())
maxi = 0

for i in range(b+1):
    maxi += 2**i

if maxi >= n:
    print("yes")
else:
    print("no")
