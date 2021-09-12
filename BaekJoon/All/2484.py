# 2021.09.12
# 2484
# 주사위 네개

def reward(ls):
    ls.sort()
    set_ls = set(ls)
    len_set = len(set_ls)
    if len_set == 1:   # 4개가 같을 때
        result.append(50000 + ls[0] * 5000)
        return
    elif len_set == 2:
        if ls[1] != ls[2]:  # 2개, 2개씩 같을 때
            result.append(2000+(ls[1]+ls[2])*500)
            return
        else:  # 3개, 1개씩 같을 때
            result.append(10000 + ls[1]*1000)
            return
    for i in range(3):  # 2개, 1개, 1개
        if ls[i] == ls[i+1]:
            result.append(1000 + ls[i]*100)
            return
    result.append(max(ls) * 100)  # 4개 모두 각각 다를 때
    return


n = int(input())
result = []
for _ in range(n):
    ls = list(map(int, input().split()))
    reward(ls)

print(max(result))
