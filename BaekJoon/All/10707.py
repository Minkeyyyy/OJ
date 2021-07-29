# 2021.07.29
# 수도요금

list1 = []

for _ in range(5):
    list1.append(int(input()))

result1 = list1[0] * list1[-1]
if list1[2] >= list1[-1]:
    result2 = list1[1]
else:
    result2 = list1[1]
    result2 += (list1[-1] - list1[2]) * list1[3]

print(min(result1, result2))
