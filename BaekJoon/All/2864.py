# 2021.10.11
# 2864
# 5와 6의 차이

a, b = input().split()

# 최소값을 위해 6을 5로 변환
a = a.replace('6', '5')
b = b.replace('6', '5')
print(int(a)+int(b), end=' ')
# 최대값을 위해 5을 6로 변환
a = a.replace('5', '6')
b = b.replace('5', '6')
print(int(a)+int(b))
