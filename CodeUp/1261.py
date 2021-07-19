# 2021.07.14
# First Special Judge(Test)

list1 = list(map(int, input().split()))
list1 = list1[:10]

for index, i in enumerate(list1):
    if i % 5 == 0:
        print(i)
        break
    else:
        if index == (len(list1) - 1):
            print(0)
        else:
            continue
