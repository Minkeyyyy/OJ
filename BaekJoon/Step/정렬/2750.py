#2021.07.06
#수 정렬하기

n = int(input())
list1 = []
for _ in range(n):
    list1.append(int(input()))

list1.sort()
for i in list1:
    print(i)