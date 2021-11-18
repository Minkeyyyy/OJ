# 2021.11.18
# 2083
# 럭비 클럽

while True:
    s = input()
    if s == '# 0 0':
        break
    a, b, c = s.split()
    b = int(b)
    c = int(c)

    if b > 17 or c >= 80:
        flag = True
    else:
        flag = False

    if flag:
        print(f"{a} Senior")
    else:
        print(f"{a} Junior")
