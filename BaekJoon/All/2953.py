# 2021.08.19
# 2953
# 나는 요리사다
maxi = 0

for i in range(5):
    now = (sum(map(int, input().split())))
    if maxi < now:
        result1 = i+1
        maxi = now
        result2 = maxi

print(result1, result2)
