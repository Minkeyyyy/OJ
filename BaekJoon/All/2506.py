# 2021.08.08
# 2506
# 점수계산

n = int(input())
inp = list(map(int, input().split()[:n]))

result = 0
sc = 1
for i in inp:
    if i == 1:
        result += sc
        sc += 1
    else:
        sc = 1
print(result)
