# 2021.07.15
# a부터 b까지 출력하기

a, b = map(int, input().split())
if a > b:
    a, b = b, a
for i in range(a, b+1):
    print(i, end=" ")
