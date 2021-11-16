# 2021.11.16
# 9094
# 수학적 호기심

n = int(input())

for _ in range(n):
    result = 0
    n, m = map(int, input().split())
    for i in range(1, n):
        for j in range(i+1, n):
            if ((i*i+j*j + m)//(i*j)) == ((i*i+j*j + m)/(i*j)):
                result += 1

    print(result)
