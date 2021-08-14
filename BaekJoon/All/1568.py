# 2021.08.12
# 1568
# 새

remain = int(input())
song = 1 #불러야 하는 노래
result = 0 #부르고 날라가는 초

while remain > 0:
    if song <= remain:
        remain -= song
        song += 1
        result += 1
    else:
        song = 1

print(result)
