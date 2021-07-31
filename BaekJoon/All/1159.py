# 2021.08.01
# 농구 경기

num = int(input())
dic = {}
flag = False
for _ in range(num):
    name = input()
    if name[0] in dic:
        dic[name[0]] += 1
    else:
        dic[name[0]] = 1

dic = sorted(dic.items())
for i in dic:
    if int(i[1]) >= 5:
        flag = True
        print(i[0], end="")

if not flag:
    print("PREDAJA")
