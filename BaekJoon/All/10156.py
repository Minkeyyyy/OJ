# 2021.07.27
# 과자

k, n, m = map(int, input().split())
need = k * n

if m >= need:
    print(0)
else:
    print(need - m)
