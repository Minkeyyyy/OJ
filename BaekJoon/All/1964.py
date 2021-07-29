# 2021.07.29
# 오각형, 오각형, 오각형...

n = int(input())
result = 5

if n == 1:
    print(5)
else:
    for i in range(2, n+1):
        result += 5*i
        result -= (2*i - 1)

    print(result % 45678)
