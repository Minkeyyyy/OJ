# 2021.09.14
# 5612
# 터널의 입구와 출구

n = int(input())
now = int(input())
maxi = now

for _ in range(n):
    a, b = map(int, input().split())
    if (now + a - b) >= 0:
        now = (now + a - b)
        maxi = max(now, maxi)
    else:
        maxi = 0
        break

print(maxi)
