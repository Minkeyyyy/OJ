# 2021.09.21
# 2605
# 줄세우기

n = int(input())
move = list(map(int, input().split()))
ls = [k+1 for k in range(n)]

# for i in range(n):
#     if move[i] == 0:
#         continue
#     want_idx = i - move[i]
#     if i == (n-1):
#         new = ls[:want_idx] + [ls[i]] + ls[want_idx:i]
#     else:
#         new = ls[:want_idx] + [ls[i]] + ls[want_idx:i] + ls[i+1:]
#     ls = new
#     print(new)

for i in range(n):
    if move[i] != 0:
        ls.insert(i-move[i], ls[i])
        del ls[i+1]

print(" ".join(map(str, ls)))
