#2021.06.16
#분수 찾기

num = int(input()) 
index = 1 #분수의 군집에 있는 숫자의 합
now = 0 #현재 숫자
while True:
    if now < num:
        now += index
        index += 1
    else:
        break

if index%2 == 0:
    in_index = now - num + 1
    up = in_index 
    down = index - in_index
    print('{}/{}'.format(up,down))
else:
    in_index = now - num + 1
    down = in_index 
    up = index - in_index
    print('{}/{}'.format(up,down))
# print( num , index , now)

