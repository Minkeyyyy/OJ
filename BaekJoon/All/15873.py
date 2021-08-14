# 2021.08.13
# 15873
# 공백 없는 A+B

n = input()
result = 0

for i in n:
    if i == '0':
        result += 9
    else:
        result += int(i)

print(result)
