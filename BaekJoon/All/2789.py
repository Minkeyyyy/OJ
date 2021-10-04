# 2021.09.28
# 2789
# 유학 금지

uni = 'CAMBRIDGE'
n = input()

for i in uni:
    if i in n:
        n = n.replace(i, '')

print(n)
