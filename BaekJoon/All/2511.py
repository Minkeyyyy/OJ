# 2021.08.09
# 2511
# 카드 놀이

a = list(map(int, input().split()))
b = list(map(int, input().split()))
asc = 0
bsc = 0
last = -1
for i in range(10):
    if a[i] > b[i]:
        asc += 3
        last = 0
    elif a[i] < b[i]:
        bsc += 3
        last = 1
    else:
        asc += 1
        bsc += 1

if asc > bsc:
    print(asc, bsc)
    print('A')
elif asc < bsc:
    print(asc, bsc)
    print('B')
else:
    if last == 0:
        print(asc, bsc)
        print('A')
    elif last == 1:
        print(asc, bsc)
        print('B')
    else:
        print(asc, bsc)
        print('D')
