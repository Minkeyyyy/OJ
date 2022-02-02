# 2021.10.12
# 2909
# 캔디 구매

c, k = map(int, input().split())
if len(str(c)) <= k:
    print(10**k)
else:
    print(round(c, -k))
