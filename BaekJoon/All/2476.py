# 2021.08.07
# 2476
# 주사위 게임

n = int(input())
prizes = []

for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        prizes.append(10000+(a*1000))
    elif a == b or c == a:
        prizes.append(1000+(a*100))
    elif b == c:
        prizes.append(1000+(c*100))
    else:
        prizes.append(max(a, b, c)*100)

print(max(prizes))
