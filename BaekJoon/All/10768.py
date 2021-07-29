# 2021.07.29
# 특별한 날

month = int(input())
day = int(input())

if month > 2:
    print('After')
elif month < 2:
    print('Before')
else:
    if day == 18:
        print('Special')
    elif day < 18:
        print('Before')
    else:
        print('After')
