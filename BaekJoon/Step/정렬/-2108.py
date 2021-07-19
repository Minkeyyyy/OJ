#2021.07.07
#통계학

n = int(input())
list1 = []

if n % 2 == 0:
    print("error")
else:
    for _ in range(n):
        list1.append(int(input()))

sort_list1 = sorted(list1)

def mean(list1):
    return sum(list1) / len(list1)

def mid(list1):
    mid_index = len(list1) // 2
    return sort_list1[mid_index]

def dif(list1):
    return max(list1) - min(list1)

print(mean(list1))
print(mid(list1))
print(dif(list1))

#최빈값을 어떻게 할 것인지 고민
#소숫점 1자리에서 반올림 고민