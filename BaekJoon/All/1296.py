# 2021.09.16
# 1296
# 데이트

man = input()
n = int(input())
women = [input() for i in range(n)]
maxi = max_idx = 0
women.sort()

for j in range(n):
    L = man.count('L') + women[j].count('L')
    O = man.count('O') + women[j].count('O')
    V = man.count('V') + women[j].count('V')
    E = man.count('E') + women[j].count('E')
    pos = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if maxi < pos:
        maxi = pos
        max_idx = j

print(women[max_idx])
