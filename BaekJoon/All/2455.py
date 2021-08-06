# 2021.08.06
# 2455
# 지능형 기차

now = 0
max1 = 0
for _ in range(4):
    a, b = map(int, input().split())
    now1 = now - a
    now2 = now1 + b
    if max1 < max(now1, now2):
        max1 = max(now1, now2)
    now = now2

print(max1)
