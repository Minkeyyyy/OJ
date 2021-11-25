# 2021.11.25
# 1384
# 메세지

group = 1   # 그룹 번호

while True:
    n = int(input())
    if n == 0:
        break
    ls = []
    ls2 = []
    flag = False  # nasty알아보기 위한 flag
    print(f"Group {group}")

    # 입력 받기
    for j in range(n):
        s = input().split()
        ls.append(s[0])  # 이름 list
        ls2.append(s)   # 전체 list

    for k in ls2:
        who = ls.index(k[0])    # nasty의 주인의 index
        for i in range(1, len(k)):
            if k[i] == 'N':
                target = ls[who-i]  # nasty 대상의 이름
                flag = True  # nasty가 있으면 flag 변경
                print(f"{target} was nasty about {ls[who]}")

    if not flag:
        print("Nobody was nasty")

    print()
    group += 1
