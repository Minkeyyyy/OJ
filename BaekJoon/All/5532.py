# 2021.07.26
# 방학 숙제

list1 = []
for _ in range(5):
    list1.append(int(input()))

if list1[1] % list1[3] == 0:
    math = list1[1]//list1[3]
else:
    math = list1[1]//list1[3] + 1

if list1[2] % list1[4] == 0:
    korean = list1[2]//list1[4]
else:
    korean = list1[2]//list1[4] + 1
done = max(math, korean)

print(list1[0] - done)
