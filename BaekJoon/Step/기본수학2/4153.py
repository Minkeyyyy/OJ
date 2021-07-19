#2021.06.23
#직각삼각형

while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        list1 = [a,b,c]
        list1.sort()
        if (list1[2]*list1[2]) == (list1[0]*list1[0] + list1[1]*list1[1]):
            print("right")
        else:
            print("wrong")