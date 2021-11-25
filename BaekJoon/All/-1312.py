# 2021.11.25
# 1312
# 소수

a, b, n = map(int, input().split())

r = a/b
print(r)
str_r = str(r).split('.')[1]

if len(str_r) >= n:
    print(str_r[n-1])
else:
    print(0)

# failed
