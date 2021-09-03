# 2021.09.03
# 1268
# 임시 반장 정하기

n = int(input())
lss = []
results = []

for _ in range(n):
    lss.append(list(map(int, input().split()))[:n])

for ls in lss:
    # 이제 찾아야지 하나하나
    result = [0]*n
    for i in range(n):
        for j in range(n):
            if ls[i] == lss[j][i]:
                result[j] = 1

    results.append(sum(result))

print(results.index(max(results))+1)
