#2021.06.11
#다이얼

tel = ['','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WYZX']
spel = input()
sum = 0

for i in spel:
    for j in tel:
        if i in j:
            sum += tel.index(j)+2

print(sum)

