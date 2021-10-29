# 2021.10.29
# 1357
# 뒤집힌 덧셈

a, b = input().split()
print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))
