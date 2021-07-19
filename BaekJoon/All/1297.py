# 2021.07.16
# TV 크기
import math

a, b, c = map(int, input().split())
x = math.sqrt((a*a) / (b*b + c*c))

print(int(b*x), int(c*x))
