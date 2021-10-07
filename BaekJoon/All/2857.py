# 2021.10.07
# 2857
# FBI
result = []
for i in range(1, 6):
    n = input()
    if 'FBI' in n:
        result.append(i)

if result:
    for i in result:
        print(i, end=' ')
else:
    print('HE GOT AWAY!')
