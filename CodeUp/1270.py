# 2021.07.15
# 1의 개수는? 1

n = int(input())
count = 0

for i in range(n+1):
    str_n = str(i)
    if str_n[-1] == '1':
        count += 1

print(count)
