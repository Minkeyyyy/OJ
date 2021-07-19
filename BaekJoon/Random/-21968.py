#2021.06.29
#선린의 터를

n = int(input())
list3 = []
for _ in range(n):
    x = int(input())
    count = 0 
    while x % 3 != 0:
        x -= 1
        count += 1
    