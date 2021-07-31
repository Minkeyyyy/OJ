# 2021.07.30
# 지수 연산
import sys

n = int(sys.stdin.readline())
result = "{:.300f}".format(1/2**n)
end = len(result)
i = 4
while True:
    if result[end-i] != '0':
        not_0 = end-i
        break
    else:
        i += 1
print(result[:not_0+1])
