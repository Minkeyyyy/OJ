#2021.06.23 good
#네 번째 점

x = []
y = []
for _ in range(3):
    x1 , y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
x.sort()
y.sort()
if x.count(x[0]) == 1:
    print(x[0], end =" ")
else:
    print(x[2], end =" ")

if y.count(y[0]) == 1:
    print(y[0])
else:
    print(y[2])
