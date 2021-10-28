# 2021.10.28
# 3449
# 해밍 거리

n = int(input())

for _ in range(n):
    a = input()
    b = input()
    count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

    print(f"Hamming distance is {count}.")
