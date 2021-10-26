# 2021.10.26
# 1356
# 유진수

n = input()
flag = False

# 어디서 자를지 결정 i
for i in range(1, len(n)):
    # i에 따라서 앞과 뒤의 곱을 계산
    for j in range(i):
        result1 = 1  # 앞의 곱 계산값
        result2 = 1  # 뒤의 곱 계산값
        for k in n[:j+1]:
            result1 *= int(k)
        for k in n[j+1:]:
            result2 *= int(k)
    if result1 == result2:
        print('YES')
        flag = True
        break

# 같은 것이 없었으면 NO출력
if not flag:
    print('NO')
