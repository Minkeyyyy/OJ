# 2021.11.01
# 9295
# 주사위

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(f"Case {i+1}: {a+b}")
