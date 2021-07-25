# 2021.07.25
# 꼬리를 무는 숫자 나열
a, b = map(int, input().split())

a -= 1
b -= 1

print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))
