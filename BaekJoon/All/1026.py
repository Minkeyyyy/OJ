#2021.07.08
#보물

'''


n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a[:n])
b = sorted(b[:n], reverse= True)
result = 0

for i in range(n):
    result += a[i] * b[i]

print(result)

#맞음
'''
n = int(input())
a = list(map(int,input().split()))[:n]
b = list(map(int,input().split()))[:n]
new_a = sorted(a)
new_b = sorted(b, reverse= True)