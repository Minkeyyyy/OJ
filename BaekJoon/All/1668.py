# 2021.08.21
# 1668
# 트로피 진열

n = int(input())
height = []  # 트로피 높이들
for _ in range(n):
    height.append(int(input()))
    
# 왼쪽 보이는 트로피 조사
flag = 0
cnt1 = 0
for now in height:
    if flag < now:
        cnt1 += 1
        flag = now
# 오른쪽 보이는 트로피 조사
flag = 0
cnt2 = 0
for now in height[::-1]:
    if flag < now:
        cnt2 += 1
        flag = now

print(cnt1)
print(cnt2)
