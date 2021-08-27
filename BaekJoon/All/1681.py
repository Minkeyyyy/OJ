# 2021.08.27
# 1681
# 줄 세우기

n, l = input().split()
result = int(n)
i = 1

while result != 0:
    if l in str(i):
        i += 1
    else:
        result -= 1
        i += 1

print(i-1)
