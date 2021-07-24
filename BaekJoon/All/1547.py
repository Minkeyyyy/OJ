# 2021.07.24
# 공

list1 = [1, 2, 3]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    new_a = list1.index(a)
    new_b = list1.index(b)
    list1[new_a], list1[new_b] = list1[new_b], list1[new_a]

print(list1[0])

# swap에서 왜 index를 사용해서는 변수를 사용해야만 하는 것이지?...
# index를 이용하려면 변수로 써야함..
