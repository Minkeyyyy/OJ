# 2021.07.28
# 쿠폰

n = int(input())

for _ in range(n):
    raw = float(input())
    new = raw*0.8
    print("${:0.2f}".format(new))
