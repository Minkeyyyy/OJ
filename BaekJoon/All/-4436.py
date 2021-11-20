# 2021.11.20
# 4436
# 엘프의 검

def check(s):
    flag = True
    for i in range(10):
        if str(i) not in s:
            flag = False

    return flag


for i in range(4):
    s = input()
    i = 1
    int_s = int(s)
    new_s = s
    while True:
        if check(new_s):
            print(i)
            break
        else:
            i = i + 1
            new_s = new_s + str(int_s * i)
