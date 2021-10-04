# 2021.09.27
# 2744
# 대소문자 바꾸기

n = input()
result = ''
for i in n:
    if 65 <= ord(i) <= 90:
        result += i.lower()
    else:
        result += i.upper()

print(result)
