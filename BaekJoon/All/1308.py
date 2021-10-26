# 2021.10.24
# 1308
# D-day

from datetime import datetime, timedelta

today = list(map(int, input().split()))
target = list(map(int, input().split()))

time1 = datetime(today[0], today[1], today[2])
time2 = datetime(target[0], target[1], target[2])

if target[0] - today[0] > 1000:
    print('gg')
elif target[0] - today[0] == 1000:
    if target[1] > today[1]:
        print('gg')
    elif target[1] == today[1]:
        if target[2] >= today[2]:
            print('gg')
        else:
            print("D-{}".format((time2-time1).days))
else:
    print("D-{}".format((time2-time1).days))
