# 2021.09.26
# 2711
# 오타맨 고창영

n = int(input())

for _ in range(n):
    a, b = input().split()
    a = int(a)

    b = b[:a-1] + b[a:]
    print(b)
