# 2021.09.24
# 6131
# 완전제곱수

n = int(input())
count = 0

for a in range(1, 500+1):
    for b in range(1, a):
        if (a*a) - (b*b) == n:
            count += 1
            print(a, b, (a*a) - (b*b))
        elif (a*a) - (b*b) > n:
            print(a, b, (a*a) - (b*b))
            break

print(count)
