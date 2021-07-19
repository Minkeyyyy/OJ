#2021.07.01
#세워라 반석 위에

n = int(input())
list1 = list(map(int,input().split()))
list1 = list1[:n]
ban = 1

for index, i in enumerate(list1):
    for j in range(index + 1 + ban, n+1):
        new = list1[index:j]
        print(new)
        if max(new) - min(new) <= 2 :
            if ban <= len(new):
                ban = len(new)
        else:
            break

print(ban)

#map은 map객체 -> list로 만들어줘야함.
#시간초과.. 더 단축시켜야 함. 
#다른 알고리즘을 선택해야 할 수도 있음.
