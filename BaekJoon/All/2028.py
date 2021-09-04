# 2021.09.04
# 2028
# 자기복제수

n = int(input())

for _ in range(n):
    num = input()
    num2 = str(int(num)**2)
    num_l = len(num)
    if num2[-num_l:] == num:
        print("YES")
    else:
        print("NO")
