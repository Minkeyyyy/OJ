# 2021.10.29
# 3595
# 맥주 냉장고

n = int(input())
min_len = [1, 1, n]
min_box = 4*n + 2

# for i in range(1, n+1):
#     if n % i == 0:
#         for j in range(1, n//i + 1):
#             if (n//i) % j == 0:
#                 k = n // (i*j)
#                 box = (i*j + j*k + i*k)*2
#                 if box <= min_box:
#                     min_box = box
#                     min_len[0], min_len[1], min_len[2] = i, j, k

# print(min_len)

for i in range(n, 0, -1):
    if n % i == 0:
        for j in range(n//i, 0, -1):
            if (n//i) % j == 0:
                k = n // (i*j)
                box = (i*j + j*k + i*k)*2
                if box < min_box:
                    min_box = box
                    min_len[0], min_len[1], min_len[2] = i, j, k

print(min_len)
