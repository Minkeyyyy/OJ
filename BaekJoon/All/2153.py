# 2021.09.06
# 2153
# 소수 단어
# A = 65 , a = 97

st = input()
result = 0
for i in st:
    asc = ord(i)
    if 97 <= asc <= (97+25):
        result += (asc - ord('a'))
    else:
        result += (asc-38)

flag = True
for i in range(2, result):
    if result % i == 0:
        flag = False
        print(result, "It is not a prime word.")
        break

if flag:
    print(result, "It is a prime word.")
