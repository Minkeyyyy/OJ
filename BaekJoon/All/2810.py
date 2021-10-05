# 2021.10.05
# 2810
# 컵홀더

num = int(input())
seat = input()
holder = 1
idx = 0

while idx < len(seat):
    if seat[idx] == 'S':
        holder += 1
        idx += 1
    else:
        holder += 1
        idx += 2

print(min(holder, num))
