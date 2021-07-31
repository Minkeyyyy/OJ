# 2021.07.31
# 시그마
import sys

a, b = map(int, sys.stdin.readline().split())
if a < b:
    result = (a+b)*(b-a+1)//2
else:
    result = (a+b)*(a-b+1)//2
print(result)
