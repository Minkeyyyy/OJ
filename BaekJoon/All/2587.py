# 2021.09.16
# 2587
# 대표값2

ls = []
for _ in range(5):
    ls.append(int(input()))

ls.sort()
print(sum(ls)//5)
print(ls[2])
