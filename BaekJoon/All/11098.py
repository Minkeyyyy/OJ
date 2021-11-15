# 2021.11.15
# 11098
# 첼시를 도와줘!

n = int(input())

for _ in range(n):
    num = int(input())
    players = []
    for i in range(num):
        mon, name = input().split()
        mon = int(mon)
        players.append((mon, name))
    players.sort()
    print(players[-1][1])
