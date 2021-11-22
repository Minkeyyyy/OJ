# 2021.11.22
# 1075
# 나누기

n = input()
f = int(input())
mini = int(n[:-2]+'00')

for i in range(mini, mini+100):
    if i % f == 0:
        print(str(i)[-2:])
        break
