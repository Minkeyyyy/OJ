# 2021.10.04
# 7510
# 고급 수학

n = int(input())
i = 1

for _ in range(n):
    ls = list(map(int, input().split()))
    ls.sort()
    if (ls[0]*ls[0] + ls[1]*ls[1]) == ls[2]*ls[2]:
        print("Scenario #{}:".format(i))
        print("yes")
    else:
        print("Scenario #{}:".format(i))
        print("no")
    if i != n:
        print()
    i += 1
