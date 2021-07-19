#2021.06.11
#그룹 단어 체커

num = int(input())
result = 0

for j in range(num):
    n = input()
    now = 0
    for i in n:
        index2 = n[now+1:].find(i)
        if index2 >= 1:
            result += 1
            break
        now = now + 1 


print(num - result)

