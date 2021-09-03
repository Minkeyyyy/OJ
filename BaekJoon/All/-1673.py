# 2021.08.26
# 1673
# 치킨 쿠폰

while True:
    try:
        n, k = map(int, input().split())
        result = 0

        result = n + (n//k) + (((n % k) + (n//k)) // k)
        print(result)
    except:
        break
