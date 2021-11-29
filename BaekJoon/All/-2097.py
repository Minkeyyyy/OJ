# 2021.11.29
# 2097
# 조약돌
import math

n = int(input())
ls = []
search = int(math.sqrt(n))+1

for i in range(2, search):
    b = (n // i + 1)
    result = ((i-1)+(b-1))*2
    ls.append(result)
    # print(i, b, result)

print(min(ls))
