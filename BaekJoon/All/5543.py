# 2021.07.24
# 상근날드
list1 = []

for _ in range(5):
    list1.append(int(input()))

hamb = min(list1[:3])
soda = min(list1[3:])
print(hamb + soda - 50)
