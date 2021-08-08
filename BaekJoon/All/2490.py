# 2021.08.08
# 2490
# 윷놀이

for _ in range(3):
    yoot = list(map(int, input().split()))
    bae = yoot.count(0)
    if bae == 1:
        print('A')
    elif bae == 2:
        print('B')
    elif bae == 3:
        print('C')
    elif bae == 4:
        print('D')
    else:
        print('E')
