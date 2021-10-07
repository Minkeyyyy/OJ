# 2021.10.07
# 2846
# 오르막 길

n = int(input())
hi = list(map(int, input().split()))
dif = []  # 높이의 차이
result = []  # 오르막길의 길이를 구하기 위한
now = 0  # 현재 오르막이 얼마나 되었는지

for i in range(1, len(hi)):
    dif.append(hi[i]-hi[i-1])

flag = False
for i in dif:
    if i > 0:  # 오르막길이면
        now += i  # 그 길이만큼 더해줌
    else:  # 내리막길이거나 높이가 같으면
        result.append(now)  # 현재까지 길이를 append해주고
        now = 0  # 길이를 초기화

result.append(now)  # 마지막이 오르막길로 끝나면 그것을 넣어줘야 함.
print(max(result))
