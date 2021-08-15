# 2021.08.14
# 2783
# 삼각 김밥

money, g = map(int, input().split())
n = int(input())
result = []
result.append(money*(1000/g))

for _ in range(n):
    money1, g1 = map(int, input().split())
    result.append(money1*(1000/g1))

print("{:.2f}".format(min(result)))
