# 2021.11.17
# 4435
# 중간계 전쟁

g = [1, 2, 3, 3, 4, 10]
s = [1, 2, 2, 2, 3, 5, 10]

n = int(input())
for j in range(n):
    ls1 = list(map(int, input().split()))
    result1 = 0
    ls2 = list(map(int, input().split()))
    result2 = 0
    for i in range(6):
        result1 += ls1[i]*g[i]
    for i in range(7):
        result2 += ls2[i]*s[i]

    if result1 < result2:
        print(f"Battle {j+1}: Evil eradicates all trace of Good")
    elif result1 > result2:
        print(f"Battle {j+1}: Good triumphs over Evil")
    else:
        print(f"Battle {j+1}: No victor on this battle field")
