# 2021.11.18
# 2033
# 반올림

n = input()
n = n[::-1]
now = int(n[0])
result = ''

# if len(n)>= 2:
for i in range(len(n)-1):
    if now >= 5:
        result = result + '0'
        now = int(n[i+1])+1
    else:
        result = result + '0'
        now = int(n[i+1])

result += str(now)

print(int(result[::-1]))
