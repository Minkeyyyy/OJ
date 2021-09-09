# 2021.09.09
# 2309
# 일곱 난쟁이

ls = []
for _ in range(9):
    ls.append(int(input()))

target = sum(ls) - 100
for i in range(9):
    flag = False
    for j in range(i + 1, 9):
        if (ls[i] + ls[j]) == target:
            ls.pop(i)
            ls.pop(j-1)  # 하나 삭제되기 때문에 하나 줄여줘야 함
            flag = True
            break
    # 찾았으면 거기서 멈추자
    if flag:
        break

ls.sort()
for i in ls:
    print(i)
