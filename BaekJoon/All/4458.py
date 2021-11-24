# 2021.11.24
# 4458
# 첫 글자를 대문자로
n = int(input())

for i in range(n):
    s = input()
    print(s[0].upper() + s[1:])
