# 2021.09.24
# 2622
# 삼각형 만들기

n = int(input())
count = 0

for i in range(1, n):
    for j in range(i, n):
        k = n-i-j
        if j > k:
            break
        if i+j > k:
            count += 1

print(count)
