# 2022.02.11
# 2798
# 블랙잭
# 내 풀이

# n, m = map(int, input().split())
# ls = list(map(int, input().split()))[:n]
# result = 0

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             sum0 = ls[i] + ls[j] + ls[k]
#             if sum0 == m:
#                 result = sum0
#             elif sum0 < m and sum0 > result:
#                 result = sum0
#     if result == m:
#         break

# print(result)

# 풀이2
n, m = map(int, input().split())
ls = list(map(int, input().split()))[:n]
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum0 = ls[i] + ls[j] + ls[k]
            if sum0 <= m:
                result = max(sum0, result)

print(result)
