#2021.06.18
#설탕배달

total = int(input())
bongzi = 0
bong3 = 0

while total > 0 :
    if total%5 != 0:
        total -= 3
        bongzi += 1
        continue
    else:
        bongzi += (total//5)
        break


if total < 0:
    print(-1)
else:
    print(bongzi)