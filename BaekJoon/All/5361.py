# 2021.09.09
# 5361
# 전투 드로이드 가격

n = int(input())
ls = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(n):
    need = list(map(int, input().split()))
    result = 0
    for i in range(5):
        result += ls[i]*need[i]

    print("${:.2f}".format(result))
