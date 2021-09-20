# 2021.09.20
# 5692
# 팩토리얼 진법
import sys

fac = [1]
for i in range(1, 5+1):
    fac.append(fac[i-1] * i)

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    result = 0
    length = len(n)

    for i in range(length):
        result += int(n[i]) * fac[(length - i)]
    print(result)
