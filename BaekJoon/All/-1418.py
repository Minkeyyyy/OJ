# 2021.11.15
# 1418
# k-세준수
def sol(n, k):
    check = 2
    result = []
    while check <= n:
        if n % check == 0:
            if check not in result:
                result.append(check)
            if check > k:
                return False
            n //= check
        else:
            check += 1
    result.insert(0, 1)
    return True


n = int(input())
k = int(input())
cnt = 0
for i in range(1, n+1):
    if sol(i, k):
        cnt += 1

print(cnt)
