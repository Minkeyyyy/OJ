# 2021.10.05
# 2810
# 컵홀더

num = int(input())
seat = input() #좌석
holder = 1 #홀더의 갯수
idx = 0 #홀더의 갯수를 세기 위한 

while idx < len(seat):
    if seat[idx] == 'S':
        holder += 1 #사람의 오른쪽에 1추가
        idx += 1
    else:
        holder += 1
        idx += 2    #커플석이기 때문에 2추가

print(min(holder, num))
