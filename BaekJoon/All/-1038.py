#2021.07.08
#감소하는 수
'''import sys
n = int(sys.stdin.readline())

def gamso(num):
    str_num = str(num)
    if len(str_num) == 1:
        return True
    for index, i in enumerate(str_num[:-1]):
        if int(i) <= int(str_num[index+1]):
            return False
        else:
            continue
    return True

count = 0
i = 0
while count != n :
    if gamso(i):
        count += 1
        i += 1
    else:
        i += 1

print(i)
'''

#이게 시간 초과가 나오네