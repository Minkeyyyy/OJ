# 2021.07.15
# 몇 번째 데이터 출력하기

n = int(input())
if n % 2 == 1:
    list1 = list(map(int, input().split()))
    mid_index = len(list1) // 2

    print(f"{list1[0]} {list1[mid_index]} {list1[-1]}")
