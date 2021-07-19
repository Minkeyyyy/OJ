#2021.06.12
#벌집

#찾고자 하는 숫자
n = int(input())
room = 1
now = 1
while True:
    if n == 1:
        print(1)
        break
    else:
        now = now + 6*room
        if now >= n:
            print(room+1)
            break
        else:
            room += 1
