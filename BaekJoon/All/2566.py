# 2021.08.11
# 2566
# 최댓값

mat = []
max_now = 0

for i in range(9):
    lst = list(map(int, input().split()))
    mat.append(lst)
    if max_now < max(lst):
        b = lst.index(max(lst)) + 1
        a = i + 1
        max_now = max(lst)

print(max_now)
print(a, b)
