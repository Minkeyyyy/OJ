# 2021.07.28
# 하얀 칸
status = True
count = 0

for _ in range(8):
    n = input()
    if status:
        for i in range(0, 8, 2):
            if n[i] != '.':
                count += 1
        status = False
    else:
        for i in range(1, 8, 2):
            if n[i] != '.':
                count += 1
        status = True

print(count)
