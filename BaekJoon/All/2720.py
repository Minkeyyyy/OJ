# 2021.08.12
# 2720
# 세탁소 사장 동혁

n = int(input())
coins = [25, 10, 5, 1]

for _ in range(n):
    case = int(input())
    result = []
    for coin in coins:
        # 몫이 0이상이면 그 coin에 해당하는 개수가 나옴
        if (case // coin) > 0:
            result.append(case//coin)
            case %= coin
        else:
            #해당 화폐가 없어도 일단 0을 넣어야 함
            result.append(0)
            continue

    print(result[0], result[1], result[2], result[3])
