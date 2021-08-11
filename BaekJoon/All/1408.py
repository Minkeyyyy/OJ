# 2021.08.10
# 1408
# 24

now = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))

now_sec = now[0]*3600 + now[1]*60 + now[2]
start_sec = start[0]*3600 + start[1]*60 + start[2]

if now_sec < start_sec:
    new_sec = start_sec - now_sec
    hour = new_sec//3600
    minu = (new_sec % 3600)//60
    sec = (new_sec % 3600) % 60
    print("{:02d}:{:02d}:{:02d}".format(hour, minu, sec))
else:
    new_sec = start_sec + 86400 - now_sec
    hour = new_sec//3600
    minu = (new_sec % 3600)//60
    sec = (new_sec % 3600) % 60
    print("{:02d}:{:02d}:{:02d}".format(hour, minu, sec))
