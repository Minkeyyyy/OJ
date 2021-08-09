# 2021.07.26
# 암호 제작

p, k = map(int, input().split())
result = []
flag = True
i = 2
while True:
    if p % i == 0:
        result.append(i)
        p = p // i
        result.append(p)
        break
    else:
        i += 1

for i in result:
    if i < k:
        flag = False

if flag:
    print("GOOD")
else:
    print("BAD", result[0])
