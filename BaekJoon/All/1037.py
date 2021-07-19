#2021.07.08
#약수

n = int(input())
list1 = list(map(int,input().split()))
list1 = list1[:n]
list1.sort()

print(list1[0] * list1[-1])

#여기서 n을 사용하지도 않았는데 맞음.