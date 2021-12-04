# 2021.12.04
# 2740
# 행렬 곱셈

"""
   1 2     -1 -2 0
   3 4      0  0 3
   5 6     
"""

mat1 = []
mat2 = []
n, m = map(int, input().split())
for _ in range(n):
    mat1.append(list(map(int, input().split())))

m, k = map(int, input().split())

for i in range(m):
    if i == 0:
        ls = list(map(int, input().split()))
        for i in ls:
            mat2.append([i])
    else:
        ls = list(map(int, input().split()))
        for j in range(len(ls)):
            mat2[j].append(ls[j])

# print(mat1)
# print(mat2)

for t in range(k):
    for j in range(n):
        result = 0
        for i in range(m):
            result += mat1[t][i] * mat2[j][i]

        print(result, end=" ")
    print()
