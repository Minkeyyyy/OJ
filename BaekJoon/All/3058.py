# 2021.08.24
# 3058
# 짝수를 찾아라

n = int(input())

for _ in range(n):
    ls = list(map(int, input().split()))
    ls.sort()
    ls2 = []

    for i in ls:
        if i % 2 == 0:
            ls2.append(i)

    print(sum(ls2), ls2[0])
