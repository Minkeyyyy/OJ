# 2021.08.19
# 2959
# 거북이

ls = list(map(int, input().split()))
ls.sort()

print(ls[0] * ls[-2])
