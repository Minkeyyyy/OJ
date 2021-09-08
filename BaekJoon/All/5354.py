# 2021.09.08
# 5354
# J박스

n = int(input())

for _ in range(n):
    num = int(input())
    for i in range(1, num+1):
        if i == 1 or i == num:
            print('#'*num)
        else:
            print('#'+'J'*(num-2) + '#')

    print()
