# 2021.10.17
# 2966
# 찍기

a = ['A', 'B', 'C']
b = ['B', 'A', 'B', 'C']
c = ['C', 'C', 'A', 'A', 'B', 'B']
names = ['Adrian', 'Bruno', 'Goran']
results = [0, 0, 0]

n = int(input())
ans = input()
for i in range(n):
    if a[i % 3] == ans[i]:
        results[0] += 1
    if b[i % 4] == ans[i]:
        results[1] += 1
    if c[i % 6] == ans[i]:
        results[2] += 1

maxi = max(results)
print(maxi)
for i in range(3):
    if maxi == results[i]:
        print(names[i])
